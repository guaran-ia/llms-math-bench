import json
from collections import defaultdict
from pathlib import Path

from evaluate_prompt_results import average, evaluate_row, percentage


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT_FILE = BASE_DIR / "results" / "azure" / "model_test_results_azure_v5.jsonl"
DEFAULT_OUTPUT_FILE = BASE_DIR / "reports" / "azure" / "resumen_azure_v5.md"


def load_rows(path):
    rows = []
    with path.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            row["_line_number"] = line_number
            rows.append(row)
    return rows


def summarize(rows):
    stats = defaultdict(
        lambda: {
            "total": 0,
            "correct": 0,
            "json_valid": 0,
            "option_consistent": 0,
            "errors_api": 0,
            "json_parse_errors": 0,
            "latencies": [],
            "wrong": [],
        }
    )

    for row in rows:
        model = row.get("model", "unknown")
        evaluation = evaluate_row(row)
        item = stats[model]
        item["total"] += 1
        item["correct"] += int(evaluation["strict_correct"])
        item["json_valid"] += int(evaluation["json_valid"])
        item["option_consistent"] += int(evaluation["option_consistent"])
        item["errors_api"] += int(bool(row.get("error")))
        item["json_parse_errors"] += int(bool(row.get("json_parse_error")))
        if isinstance(row.get("latency_seconds"), (int, float)):
            item["latencies"].append(row["latency_seconds"])
        if not evaluation["strict_correct"]:
            item["wrong"].append(
                {
                    "problem_id": row.get("problem_id"),
                    "expected": evaluation["expected"],
                    "predicted": evaluation["predicted"],
                    "json_valid": evaluation["json_valid"],
                }
            )
    return stats


def render_wrong(wrong):
    if not wrong:
        return "ninguno"
    return ", ".join(
        f"P{item['problem_id']} ({item['expected']} -> {item['predicted']})"
        for item in wrong
    )


def prompt_id_from_rows(rows):
    prompt_ids = sorted({row.get("prompt_id", "-") for row in rows})
    return ", ".join(prompt_ids)


def prompt_name_from_rows(rows):
    prompt_names = sorted({row.get("prompt_name", "-") for row in rows})
    return ", ".join(prompt_names)


def render_report(stats, prompt_id, prompt_name):
    ranked = sorted(
        stats.items(),
        key=lambda pair: (
            pair[1]["correct"] / pair[1]["total"] if pair[1]["total"] else 0,
            pair[1]["correct"],
            pair[1]["json_valid"] / pair[1]["total"] if pair[1]["total"] else 0,
            -(average(pair[1]["latencies"]) or 0),
        ),
        reverse=True,
    )

    lines = [
        f"# Resumen Azure {prompt_id}",
        "",
        f"Todas las corridas fueron evaluadas con el prompt `{prompt_id}` (`{prompt_name}`).",
        "",
        "La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.",
        "",
        "## Comparación de modelos",
        "",
        "| Modelo | Aciertos | Exactitud | JSON válido | Opción consistente | Latencia media | Errores |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]

    for model, item in ranked:
        total = item["total"]
        avg_latency = average(item["latencies"])
        latency = f"{avg_latency:.3f}s" if avg_latency is not None else "-"
        lines.append(
            f"| `{model}` | {item['correct']}/{total} | {percentage(item['correct'], total)} | "
            f"{item['json_valid']}/{total} | {item['option_consistent']}/{total} | {latency} | "
            f"{render_wrong(item['wrong'])} |"
        )

    lines.extend(
        [
            "",
            "## Ranking global",
            "",
            "| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |",
            "|---:|---|---:|---:|---:|---:|",
        ]
    )

    for position, (model, item) in enumerate(ranked, start=1):
        total = item["total"]
        avg_latency = average(item["latencies"])
        latency = f"{avg_latency:.3f}s" if avg_latency is not None else "-"
        lines.append(
            f"| {position} | `{model}` | {item['correct']}/{total} | "
            f"{percentage(item['correct'], total)} | {item['json_valid']}/{total} | {latency} |"
        )

    lines.extend(
        [
            "",
            "## Detalle de errores",
            "",
            "| Modelo | Problema | Esperado | Predicho | JSON válido |",
            "|---|---:|---:|---:|---|",
        ]
    )

    for model, item in ranked:
        for wrong in item["wrong"]:
            json_valid = "sí" if wrong["json_valid"] else "no"
            lines.append(
                f"| `{model}` | {wrong['problem_id']} | {wrong['expected']} | "
                f"{wrong['predicted']} | {json_valid} |"
            )

    if ranked:
        best_model, best_item = ranked[0]
        lines.extend(
            [
                "",
                "## Conclusión",
                "",
                f"El mejor resultado fue `{best_model}` con {best_item['correct']}/{best_item['total']}.",
            ]
        )

    return "\n".join(lines) + "\n"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Genera un resumen de Azure para una corrida por prompt.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT_FILE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_FILE))
    args = parser.parse_args()

    rows = load_rows(Path(args.input))
    stats = summarize(rows)
    output_file = Path(args.output)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        render_report(stats, prompt_id_from_rows(rows), prompt_name_from_rows(rows)),
        encoding="utf-8",
    )
    print(f"Reporte generado: {output_file}")


if __name__ == "__main__":
    main()
