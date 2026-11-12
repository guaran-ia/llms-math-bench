import argparse
import json
import math
import re
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from src.math_evaluation import evaluate as evaluate_math_row


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "results" / "educacion_media" / "model_test_results_em.jsonl"
DEFAULT_OUTPUT = BASE_DIR / "reports" / "educacion_media" / "education_media_accuracy_report.md"


def load_jsonl(path):
    rows = []
    invalid_lines = []
    with Path(path).open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as error:
                invalid_lines.append((line_number, str(error)))
                continue
            row["_line_number"] = line_number
            rows.append(row)
    return rows, invalid_lines


def to_decimal(value):
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float, Decimal)):
        return Decimal(str(value))
    if isinstance(value, str):
        cleaned = re.sub(r"[^0-9.\-]", "", value.strip().replace(",", "."))
        if not cleaned:
            return None
        try:
            return Decimal(cleaned)
        except InvalidOperation:
            return None
    return None


def numeric_match(expected, actual, tolerance=Decimal("0.0001")):
    expected_decimal = to_decimal(expected)
    actual_decimal = to_decimal(actual)
    if expected_decimal is None or actual_decimal is None:
        return False
    return abs(expected_decimal - actual_decimal) <= tolerance


def normalize_string(value):
    text = str(value).lower().strip()
    replacements = {
        "²": "^2",
        "−": "-",
        "–": "-",
        "—": "-",
        " ": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def parse_point_string(value):
    if not isinstance(value, str):
        return None
    numbers = re.findall(r"-?\d+(?:[\.,]\d+)?", value)
    if len(numbers) != 2:
        return None
    return numbers


def dict_alias_value(actual, aliases):
    if not isinstance(actual, dict):
        return None
    normalized = {normalize_string(key): value for key, value in actual.items()}
    for alias in aliases:
        key = normalize_string(alias)
        if key in normalized:
            return normalized[key]
    return None


def final_answer_value(response):
    if not isinstance(response, dict):
        return response
    final_answer = response.get("final_answer")
    if isinstance(final_answer, dict):
        return final_answer.get("value")
    return final_answer


def extract_json_from_raw(raw_response):
    if not raw_response:
        return None
    text = raw_response.strip()
    fenced = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        text = fenced.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    try:
        return json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return None


def extract_numeric_from_raw(raw_response):
    if not raw_response:
        return None
    match = re.search(r"-?\d+(?:[\.,]\d+)?", raw_response)
    if not match:
        return None
    return match.group(0)


def compare_lists(expected, actual):
    if isinstance(actual, str):
        point = parse_point_string(actual)
        if point is not None:
            actual = point
    if not isinstance(actual, list) or len(expected) != len(actual):
        return False
    for expected_item, actual_item in zip(expected, actual):
        if not values_match(expected_item, actual_item):
            return False
    return True


def compare_dicts(expected, actual):
    if not isinstance(actual, dict):
        return False
    for key, expected_value in expected.items():
        actual_value = actual.get(key)
        if actual_value is None and key == "center":
            actual_value = dict_alias_value(actual, ["center", "centro", "isentro", "iséntro"])
        if actual_value is None and key == "radius":
            actual_value = dict_alias_value(actual, ["radius", "radio", "irradio", "irádio"])
        if actual_value is None or not values_match(expected_value, actual_value):
            return False
    return True


def values_match(expected, actual):
    if isinstance(expected, (int, float, Decimal)):
        return numeric_match(expected, actual)
    if isinstance(expected, list):
        return compare_lists(expected, actual)
    if isinstance(expected, dict):
        return compare_dicts(expected, actual)
    if isinstance(expected, str):
        if isinstance(actual, list):
            point = parse_point_string(expected)
            if point is not None:
                return compare_lists(point, actual)
        if isinstance(actual, dict):
            for key in ("equation", "ecuacion", "ecuación", "ecuacion_estandar", "ecuacion_general"):
                value = dict_alias_value(actual, [key])
                if value is not None and values_match(expected, value):
                    return True
        if normalize_string(expected) == normalize_string(actual):
            return True
        expected_number = to_decimal(expected)
        if expected_number is not None:
            return numeric_match(expected, actual)
        return False
    return expected == actual


def evaluate_row(row):
    result = evaluate_math_row(row)
    return {
        "correct": result["correct"],
        "json_valid": result["json_valid"],
        "expected": row.get("expected_answer"),
        "predicted": result["predicted"],
    }


def summarize(rows):
    stats = defaultdict(
        lambda: {
            "total": 0,
            "correct": 0,
            "json_valid": 0,
            "errors": 0,
            "json_parse_errors": 0,
            "latencies": [],
            "wrong": [],
            "reasoning_types": defaultdict(lambda: {"total": 0, "correct": 0}),
        }
    )
    details = []
    for row in rows:
        key = (row.get("provider", "unknown"), row.get("model", "unknown"), row.get("prompt_id", "unknown"))
        evaluation = evaluate_row(row)
        item = stats[key]
        item["total"] += 1
        item["correct"] += int(evaluation["correct"])
        item["json_valid"] += int(evaluation["json_valid"])
        item["errors"] += int(bool(row.get("error")))
        item["json_parse_errors"] += int(bool(row.get("json_parse_error")))
        if isinstance(row.get("latency_seconds"), (int, float)):
            item["latencies"].append(row["latency_seconds"])
        reasoning_type = row.get("reasoning_type") or "unknown"
        item["reasoning_types"][reasoning_type]["total"] += 1
        item["reasoning_types"][reasoning_type]["correct"] += int(evaluation["correct"])
        if not evaluation["correct"]:
            item["wrong"].append(
                {
                    "problem_id": row.get("problem_id"),
                    "reasoning_type": reasoning_type,
                    "expected": evaluation["expected"],
                    "predicted": evaluation["predicted"],
                    "json_valid": evaluation["json_valid"],
                }
            )
        details.append({"key": key, "row": row, "evaluation": evaluation})
    return stats, details


def percentage(value, total):
    if not total:
        return "0.0%"
    return f"{(value / total) * 100:.1f}%"


def average(values):
    if not values:
        return None
    return sum(values) / len(values)


def render_value(value):
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def rank_stats(stats):
    return sorted(
        stats.items(),
        key=lambda pair: (
            pair[1]["correct"] / pair[1]["total"] if pair[1]["total"] else 0,
            pair[1]["correct"],
            pair[1]["json_valid"] / pair[1]["total"] if pair[1]["total"] else 0,
            -(average(pair[1]["latencies"]) or 0),
        ),
        reverse=True,
    )


def render_report(input_path, rows, invalid_lines, stats):
    ranked = rank_stats(stats)
    lines = [
        "# Reporte De Evaluación Matemática Guaraní",
        "",
        "## Resumen",
        "",
        f"- Archivo evaluado: `{Path(input_path).name}`",
        f"- Intentos leídos: {len(rows)}",
        f"- Líneas JSONL inválidas: {len(invalid_lines)}",
    ]
    if ranked:
        (provider, model, prompt_id), best = ranked[0]
        lines.append(f"- Mejor combinación: **{provider} / {model} / {prompt_id}** ({best['correct']}/{best['total']})")

    lines.extend(
        [
            "",
            "## Ranking Por Modelo Y Prompt",
            "",
            "| Posición | Proveedor | Modelo | Prompt | Aciertos | Exactitud | JSON válido | Errores API | Errores JSON | Latencia media |",
            "|---:|---|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for position, ((provider, model, prompt_id), item) in enumerate(ranked, start=1):
        total = item["total"]
        avg_latency = average(item["latencies"])
        latency = f"{avg_latency:.3f}s" if avg_latency is not None else "-"
        lines.append(
            f"| {position} | {provider} | {model} | {prompt_id} | {item['correct']}/{total} | "
            f"{percentage(item['correct'], total)} | {item['json_valid']}/{total} | "
            f"{item['errors']} | {item['json_parse_errors']} | {latency} |"
        )

    prompt_ids = sorted({prompt for _provider, _model, prompt in stats})
    lines.extend(
        [
            "",
            "## Comparación Final",
            "",
            f"| Modelo | {' | '.join(prompt_ids)} | Mejor prompt | Mejor resultado |",
            f"|---|{'|'.join(['---:'] * len(prompt_ids))}|---|---:|",
        ]
    )
    models = sorted({model for _provider, model, _prompt in stats})
    for model in models:
        by_prompt = {
            prompt: item
            for (_provider, m, prompt), item in stats.items()
            if m == model
        }
        candidates = [(prompt, by_prompt.get(prompt)) for prompt in prompt_ids]
        candidates = [(prompt, item) for prompt, item in candidates if item]
        if not candidates:
            continue
        candidates.sort(
            key=lambda pair: (
                pair[1]["correct"] / pair[1]["total"] if pair[1]["total"] else 0,
                pair[1]["correct"],
                pair[1]["json_valid"] / pair[1]["total"] if pair[1]["total"] else 0,
                -(average(pair[1]["latencies"]) or 0),
            ),
            reverse=True,
        )
        best_prompt, best_item = candidates[0]
        scores = [
            f"{by_prompt[prompt]['correct']}/{by_prompt[prompt]['total']}" if prompt in by_prompt else "-"
            for prompt in prompt_ids
        ]
        lines.append(
            f"| `{model}` | {' | '.join(scores)} | `{best_prompt}` | "
            f"{best_item['correct']}/{best_item['total']} |"
        )

    lines.extend(
        [
            "",
            "## Detalle De Errores",
            "",
            "| Modelo | Prompt | Problema | Tipo | Esperado | Predicho | JSON válido |",
            "|---|---|---:|---|---|---|---|",
        ]
    )
    for (provider, model, prompt_id), item in ranked:
        for wrong in item["wrong"]:
            json_valid = "sí" if wrong["json_valid"] else "no"
            lines.append(
                f"| `{model}` | `{prompt_id}` | {wrong['problem_id']} | {wrong['reasoning_type']} | "
                f"{render_value(wrong['expected'])} | {render_value(wrong['predicted'])} | {json_valid} |"
            )

    return "\n".join(lines) + "\n"


def parse_args():
    parser = argparse.ArgumentParser(description="Evalúa resultados de Educación Media.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    return parser.parse_args()


def main():
    args = parse_args()
    rows, invalid_lines = load_jsonl(args.input)
    stats, _details = summarize(rows)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_report(args.input, rows, invalid_lines, stats), encoding="utf-8")
    print(f"Reporte generado: {output_path}")
    ranked = rank_stats(stats)
    if ranked:
        (provider, model, prompt_id), best = ranked[0]
        print(f"Mejor combinación: {provider} / {model} / {prompt_id} ({best['correct']}/{best['total']})")


if __name__ == "__main__":
    main()
