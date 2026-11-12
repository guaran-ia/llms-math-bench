import argparse
import json
import re
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from src.math_evaluation import evaluate as evaluate_math_row, equivalent as math_equivalent


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "results" / "gemini" / "model_test_results_gemini_2_5_pro.jsonl"
DEFAULT_OUTPUT = BASE_DIR / "reports" / "gemini" / "gemini_prompt_accuracy_report.md"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Evalúa resultados JSONL agrupando por proveedor, modelo y prompt."
    )
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    return parser.parse_args()


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


def values_match(expected, actual):
    expected_decimal = to_decimal(expected)
    actual_decimal = to_decimal(actual)
    if expected_decimal is None or actual_decimal is None:
        return False
    return expected_decimal == actual_decimal


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

    text = raw_response.strip()
    fenced = re.match(r"^```(?:text|json)?\s*(.*?)\s*```$", text, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        text = fenced.group(1).strip()

    match = re.search(r"-?\d+(?:[\.,]\d+)?", text)
    if not match:
        return None
    return match.group(0)


def final_answer_value(response):
    if response is not None and not isinstance(response, dict):
        return response
    if not isinstance(response, dict):
        return None
    final_answer = response.get("final_answer")
    if not isinstance(final_answer, dict):
        return None
    return final_answer.get("value")


def correct_option_value(response):
    if not isinstance(response, dict):
        return None
    correct_option_id = response.get("correct_option_id")
    options = response.get("options")
    if not correct_option_id or not isinstance(options, list):
        return None
    for option in options:
        if isinstance(option, dict) and option.get("id") == correct_option_id:
            return option.get("value")
    return None


def evaluate_row(row):
    result = evaluate_math_row(row)
    parsed_response = row.get("response")
    recovered_response = parsed_response if parsed_response is not None else extract_json_from_raw(row.get("raw_response"))
    parsed_predicted = final_answer_value(parsed_response)
    option_value = correct_option_value(recovered_response)

    return {
        "strict_correct": row.get("error") is None and math_equivalent(row.get("expected_answer"), parsed_predicted),
        "recovered_correct": result["correct"],
        "json_valid": result["json_valid"],
        "option_consistent": math_equivalent(result["predicted"], option_value),
        "expected": row.get("expected_answer"),
        "predicted": result["predicted"],
    }


def latest_by_prompt_model_problem(rows):
    latest = {}
    for row in rows:
        key = (
            row.get("provider", "unknown"),
            row.get("model", "unknown"),
            row.get("prompt_id", "unknown"),
            row.get("problem_id"),
        )
        latest[key] = row
    return list(latest.values())


def summarize(rows):
    stats = defaultdict(
        lambda: {
            "prompt_name": None,
            "total": 0,
            "strict_correct": 0,
            "recovered_correct": 0,
            "json_valid": 0,
            "option_consistent": 0,
            "errors": 0,
            "json_parse_errors": 0,
            "latencies": [],
        }
    )
    details = []

    for row in rows:
        key = (
            row.get("provider", "unknown"),
            row.get("model", "unknown"),
            row.get("prompt_id", "unknown"),
        )
        evaluation = evaluate_row(row)
        item = stats[key]
        item["prompt_name"] = row.get("prompt_name")
        item["total"] += 1
        item["strict_correct"] += int(evaluation["strict_correct"])
        item["recovered_correct"] += int(evaluation["recovered_correct"])
        item["json_valid"] += int(evaluation["json_valid"])
        item["option_consistent"] += int(evaluation["option_consistent"])
        item["errors"] += int(bool(row.get("error")))
        item["json_parse_errors"] += int(bool(row.get("json_parse_error")))
        if isinstance(row.get("latency_seconds"), (int, float)):
            item["latencies"].append(row["latency_seconds"])

        details.append(
            {
                "provider": key[0],
                "model": key[1],
                "prompt_id": key[2],
                "problem_id": row.get("problem_id"),
                "expected": evaluation["expected"],
                "predicted": evaluation["predicted"],
                "strict_correct": evaluation["strict_correct"],
                "json_valid": evaluation["json_valid"],
                "line_number": row.get("_line_number"),
            }
        )

    return stats, details


def percentage(value, total):
    if not total:
        return "0.0%"
    return f"{(value / total) * 100:.1f}%"


def average(values):
    if not values:
        return None
    return sum(values) / len(values)


def rank_stats(stats):
    return sorted(
        stats.items(),
        key=lambda item: (
            item[1]["strict_correct"] / item[1]["total"] if item[1]["total"] else 0,
            item[1]["strict_correct"],
            item[1]["json_valid"] / item[1]["total"] if item[1]["total"] else 0,
            -(average(item[1]["latencies"]) or 0),
        ),
        reverse=True,
    )


def yes_no(value):
    return "sí" if value else "no"


def render_report(input_path, all_rows, evaluated_rows, invalid_lines, stats, details):
    ranked = rank_stats(stats)
    winner = ranked[0] if ranked else None
    lines = [
        "# Reporte de prompts por modelo",
        "",
        "## Resumen",
        "",
        f"- Archivo evaluado: `{Path(input_path).name}`",
        f"- Intentos leídos: {len(all_rows)}",
        f"- Intentos evaluados para ranking: {len(evaluated_rows)}",
        f"- Líneas JSONL inválidas: {len(invalid_lines)}",
    ]
    if winner:
        (provider, model, prompt_id), winner_stats = winner
        lines.append(
            f"- Mejor combinación: **{provider} / {model} / {prompt_id}** "
            f"({winner_stats['strict_correct']}/{winner_stats['total']})"
        )

    lines.extend(
        [
            "",
            "## Ranking Por Prompt",
            "",
            "| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |",
            "|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for position, ((provider, model, prompt_id), item) in enumerate(ranked, start=1):
        total = item["total"]
        avg_latency = average(item["latencies"])
        latency = f"{avg_latency:.3f}s" if avg_latency is not None else "-"
        lines.append(
            f"| {position} | {provider} | {model} | {prompt_id} | {item['prompt_name'] or '-'} | "
            f"{item['strict_correct']}/{total} | {percentage(item['strict_correct'], total)} | "
            f"{item['json_valid']}/{total} | {item['option_consistent']}/{total} | "
            f"{item['errors']} | {item['json_parse_errors']} | {latency} |"
        )

    lines.extend(
        [
            "",
            "## Detalle Por Problema",
            "",
            "| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |",
            "|---|---:|---|---:|---:|---|---|---:|",
        ]
    )
    for row in sorted(details, key=lambda item: (item["prompt_id"], item["problem_id"], item["model"])):
        lines.append(
            f"| {row['prompt_id']} | {row['problem_id']} | {row['model']} | "
            f"{row['expected']} | {row['predicted']} | {yes_no(row['strict_correct'])} | "
            f"{yes_no(row['json_valid'])} | {row['line_number']} |"
        )

    if invalid_lines:
        lines.extend(["", "## Líneas Inválidas", ""])
        for line_number, error in invalid_lines:
            lines.append(f"- Línea {line_number}: {error}")

    lines.append("")
    return "\n".join(lines)


def main():
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    rows, invalid_lines = load_jsonl(input_path)
    evaluated_rows = latest_by_prompt_model_problem(rows)
    stats, details = summarize(evaluated_rows)
    report = render_report(input_path, rows, evaluated_rows, invalid_lines, stats, details)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Reporte generado: {output_path}")
    ranked = rank_stats(stats)
    if ranked:
        (provider, model, prompt_id), item = ranked[0]
        print(f"Mejor combinación: {provider} / {model} / {prompt_id} ({item['strict_correct']}/{item['total']})")


if __name__ == "__main__":
    main()
