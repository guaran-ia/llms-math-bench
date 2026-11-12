import argparse
import json
import re
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from src.math_evaluation import evaluate as evaluate_math_row, equivalent as math_equivalent, final_value


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "results" / "azure" / "model_test_results_guarani.jsonl"
DEFAULT_OUTPUT = BASE_DIR / "reports" / "azure" / "model_accuracy_report.md"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compara respuestas esperadas contra respuestas de modelos y genera un reporte Markdown."
    )
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Archivo JSONL con resultados de modelos.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Reporte Markdown de salida.")
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
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float, Decimal)):
        return Decimal(str(value))
    if isinstance(value, str):
        cleaned = value.strip().replace(",", ".")
        cleaned = re.sub(r"[^0-9.\-]", "", cleaned)
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


def final_answer_value(response):
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
    expected = row.get("expected_answer")
    parsed_final_value = final_value(parsed_response)
    recovered_final_value = result["predicted"]
    recovered_response = parsed_response if parsed_response is not None else extract_json_from_raw(row.get("raw_response"))
    recovered_option_value = correct_option_value(recovered_response)

    strict_correct = row.get("error") is None and math_equivalent(expected, parsed_final_value)
    recovered_correct = result["correct"]
    option_consistent = math_equivalent(recovered_final_value, recovered_option_value)

    return {
        "strict_correct": strict_correct,
        "recovered_correct": recovered_correct,
        "json_valid": isinstance(parsed_response, dict) and row.get("json_parse_error") is None,
        "option_consistent": option_consistent,
        "expected": expected,
        "predicted": recovered_final_value,
        "parsed_predicted": parsed_final_value,
        "error": row.get("error"),
        "json_parse_error": row.get("json_parse_error"),
    }


def latest_by_model_problem(rows):
    latest = {}
    for row in rows:
        key = (row.get("model"), row.get("problem_id"))
        latest[key] = row
    return list(latest.values())


def summarize(rows):
    model_stats = defaultdict(
        lambda: {
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
        evaluation = evaluate_row(row)
        model = row.get("model", "modelo_desconocido")
        stats = model_stats[model]

        stats["total"] += 1
        stats["strict_correct"] += int(evaluation["strict_correct"])
        stats["recovered_correct"] += int(evaluation["recovered_correct"])
        stats["json_valid"] += int(evaluation["json_valid"])
        stats["option_consistent"] += int(evaluation["option_consistent"])
        stats["errors"] += int(bool(evaluation["error"]))
        stats["json_parse_errors"] += int(bool(evaluation["json_parse_error"]))
        if isinstance(row.get("latency_seconds"), (int, float)):
            stats["latencies"].append(row["latency_seconds"])

        details.append(
            {
                "model": model,
                "problem_id": row.get("problem_id"),
                "expected": evaluation["expected"],
                "predicted": evaluation["predicted"],
                "strict_correct": evaluation["strict_correct"],
                "recovered_correct": evaluation["recovered_correct"],
                "json_valid": evaluation["json_valid"],
                "line_number": row.get("_line_number"),
            }
        )

    return model_stats, details


def percentage(value, total):
    if total == 0:
        return "0.0%"
    return f"{(value / total) * 100:.1f}%"


def average(values):
    if not values:
        return None
    return sum(values) / len(values)


def rank_models(model_stats):
    return sorted(
        model_stats.items(),
        key=lambda item: (
            item[1]["strict_correct"] / item[1]["total"] if item[1]["total"] else 0,
            item[1]["strict_correct"],
            item[1]["json_valid"] / item[1]["total"] if item[1]["total"] else 0,
            -(average(item[1]["latencies"]) or 0),
        ),
        reverse=True,
    )


def markdown_bool(value):
    return "sí" if value else "no"


def render_report(input_path, all_rows, evaluated_rows, invalid_lines, model_stats, details):
    ranked = rank_models(model_stats)
    winner = ranked[0][0] if ranked else "N/A"
    unique_problems = sorted({row.get("problem_id") for row in evaluated_rows})

    lines = [
        "# Reporte de acierto por modelo",
        "",
        "## Resumen",
        "",
        f"- Archivo evaluado: `{Path(input_path).name}`",
        f"- Intentos leídos: {len(all_rows)}",
        f"- Intentos evaluados para ranking: {len(evaluated_rows)}",
        f"- Problemas únicos evaluados: {len(unique_problems)}",
        f"- Líneas JSONL inválidas: {len(invalid_lines)}",
        f"- Modelo más acertado: **{winner}**",
        "",
        "El ranking principal usa el último intento disponible por cada par `(modelo, problem_id)` para evitar que problemas repetidos pesen dos veces.",
        "",
        "## Ranking Principal",
        "",
        "| Posición | Modelo | Aciertos estrictos | Exactitud estricta | Aciertos recuperados | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for position, (model, stats) in enumerate(ranked, start=1):
        total = stats["total"]
        avg_latency = average(stats["latencies"])
        latency_text = f"{avg_latency:.3f}s" if avg_latency is not None else "-"
        lines.append(
            "| "
            f"{position} | {model} | {stats['strict_correct']}/{total} | "
            f"{percentage(stats['strict_correct'], total)} | "
            f"{stats['recovered_correct']}/{total} | "
            f"{stats['json_valid']}/{total} | "
            f"{stats['option_consistent']}/{total} | "
            f"{stats['errors']} | {stats['json_parse_errors']} | {latency_text} |"
        )

    lines.extend(
        [
            "",
            "## Detalle Por Problema",
            "",
            "| Problema | Modelo | Esperado | Predicho | Estricto | Recuperado | JSON válido | Línea |",
            "|---:|---|---:|---:|---|---|---|---:|",
        ]
    )

    for item in sorted(details, key=lambda row: (row["problem_id"], row["model"])):
        lines.append(
            "| "
            f"{item['problem_id']} | {item['model']} | {item['expected']} | "
            f"{item['predicted']} | {markdown_bool(item['strict_correct'])} | "
            f"{markdown_bool(item['recovered_correct'])} | {markdown_bool(item['json_valid'])} | "
            f"{item['line_number']} |"
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
    evaluated_rows = latest_by_model_problem(rows)
    model_stats, details = summarize(evaluated_rows)
    report = render_report(input_path, rows, evaluated_rows, invalid_lines, model_stats, details)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    ranked = rank_models(model_stats)
    print(f"Reporte generado: {output_path}")
    if ranked:
        winner, stats = ranked[0]
        print(
            f"Modelo más acertado: {winner} "
            f"({stats['strict_correct']}/{stats['total']} = {percentage(stats['strict_correct'], stats['total'])})"
        )


if __name__ == "__main__":
    main()
