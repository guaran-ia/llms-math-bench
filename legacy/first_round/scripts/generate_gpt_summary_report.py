import json
import re
from pathlib import Path

from src.evaluate_prompt_results import evaluate_row, percentage


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results" / "gpt"
REPORTS_DIR = BASE_DIR / "reports" / "gpt"
OUTPUT_FILE = REPORTS_DIR / "resumen_gpt_v5.md"


def display_name(path):
    name = path.stem
    name = re.sub(r"^model_test_results_", "", name)
    name = re.sub(r"_evaluable$", "", name)
    return name


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


def summarize_file(path):
    rows = load_rows(path)
    evaluations = [(row, evaluate_row(row)) for row in rows]
    total = len(evaluations)
    correct = sum(int(evaluation["strict_correct"]) for _row, evaluation in evaluations)
    json_valid = sum(int(evaluation["json_valid"]) for _row, evaluation in evaluations)
    option_consistent = sum(
        int(evaluation["option_consistent"]) for _row, evaluation in evaluations
    )
    errors = [
        {
            "problem_id": row.get("problem_id"),
            "expected": evaluation["expected"],
            "predicted": evaluation["predicted"],
        }
        for row, evaluation in evaluations
        if not evaluation["strict_correct"]
    ]
    prompt_ids = sorted({row.get("prompt_id", "-") for row in rows})
    model_names = sorted({row.get("model", "-") for row in rows})
    return {
        "name": display_name(path),
        "path": path,
        "total": total,
        "correct": correct,
        "json_valid": json_valid,
        "option_consistent": option_consistent,
        "errors": errors,
        "prompt_ids": prompt_ids,
        "model_names": model_names,
    }


def render_error_summary(errors):
    if not errors:
        return "ninguno"
    return ", ".join(
        f"P{error['problem_id']} ({error['expected']} -> {error['predicted']})"
        for error in errors
    )


def render_report(summaries):
    ranked = sorted(
        summaries,
        key=lambda item: (
            item["correct"] / item["total"] if item["total"] else 0,
            item["correct"],
            item["json_valid"] / item["total"] if item["total"] else 0,
        ),
        reverse=True,
    )

    lines = [
        "# Resumen GPT v5",
        "",
        "Todas las corridas fueron evaluadas con el prompt `v5` (`Guaraní estricto con JSON reforzado`).",
        "",
        "La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.",
        "",
        "## Comparación de modelos",
        "",
        "| Modelo/Corrida | Prompt | Aciertos | Exactitud | JSON válido | Opción consistente | Errores |",
        "|---|---|---:|---:|---:|---:|---|",
    ]

    for item in ranked:
        prompt = ", ".join(item["prompt_ids"])
        total = item["total"]
        lines.append(
            f"| `{item['name']}` | `{prompt}` | {item['correct']}/{total} | "
            f"{percentage(item['correct'], total)} | {item['json_valid']}/{total} | "
            f"{item['option_consistent']}/{total} | {render_error_summary(item['errors'])} |"
        )

    lines.extend(
        [
            "",
            "## Ranking global",
            "",
            "| Posición | Modelo/Corrida | Aciertos estrictos | Exactitud estricta | JSON válido | Errores |",
            "|---:|---|---:|---:|---:|---|",
        ]
    )

    for position, item in enumerate(ranked, start=1):
        total = item["total"]
        lines.append(
            f"| {position} | `{item['name']}` | {item['correct']}/{total} | "
            f"{percentage(item['correct'], total)} | {item['json_valid']}/{total} | "
            f"{render_error_summary(item['errors'])} |"
        )

    lines.extend(
        [
            "",
            "## Detalle de errores",
            "",
            "| Modelo/Corrida | Problema | Esperado | Predicho |",
            "|---|---:|---:|---:|",
        ]
    )

    has_errors = False
    for item in ranked:
        for error in item["errors"]:
            has_errors = True
            lines.append(
                f"| `{item['name']}` | {error['problem_id']} | "
                f"{error['expected']} | {error['predicted']} |"
            )
    if not has_errors:
        lines.append("| - | - | - | - |")

    best = ranked[0] if ranked else None
    if best:
        lines.extend(
            [
                "",
                "## Conclusión",
                "",
                f"El mejor resultado fue `{best['name']}` con {best['correct']}/{best['total']}.",
            ]
        )

    return "\n".join(lines) + "\n"


def main():
    files = sorted(RESULTS_DIR.glob("*_evaluable.jsonl"))
    summaries = [summarize_file(path) for path in files]
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(render_report(summaries), encoding="utf-8")
    print(f"Reporte generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
