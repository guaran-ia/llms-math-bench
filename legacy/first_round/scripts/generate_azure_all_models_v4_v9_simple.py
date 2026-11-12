import json
from collections import defaultdict
from pathlib import Path

from src.evaluate_prompt_results import average, evaluate_row, percentage


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "reports" / "azure_services" / "azure_all_models_v4_v9_simple.md"

PROMPT_FILES = {
    "v4": [
        BASE_DIR / "results" / "azure" / "model_test_results_guarani_prompt_v4.jsonl",
        BASE_DIR / "results" / "azure_services" / "model_test_results_new_models_all_prompts.jsonl",
    ],
    "v5": [
        BASE_DIR / "results" / "azure" / "model_test_results_azure_v5.jsonl",
        BASE_DIR / "results" / "azure_services" / "model_test_results_new_models_all_prompts.jsonl",
    ],
    "v6": [
        BASE_DIR / "results" / "azure" / "model_test_results_azure_v6.jsonl",
        BASE_DIR / "results" / "azure_services" / "model_test_results_new_models_all_prompts.jsonl",
    ],
    "v7": [
        BASE_DIR / "results" / "azure" / "model_test_results_azure_v7.jsonl",
        BASE_DIR / "results" / "azure_services" / "model_test_results_new_models_all_prompts.jsonl",
    ],
    "v8": [
        BASE_DIR / "results" / "azure" / "model_test_results_azure_v8.jsonl",
        BASE_DIR / "results" / "azure_services" / "model_test_results_new_models_all_prompts.jsonl",
    ],
    "v9": [
        BASE_DIR / "results" / "azure" / "model_test_results_azure_v9.jsonl",
        BASE_DIR / "results" / "azure_services" / "model_test_results_new_models_all_prompts.jsonl",
    ],
}

PROMPTS = ["v4", "v5", "v6", "v7", "v8", "v9"]
PROMPT_SUMMARIES = {
    "v4": "Profesor bilingüe con glosario guaraní-español.",
    "v5": "Guaraní estricto con reglas reforzadas de JSON.",
    "v6": "v5 con warmup/few-shot matemático.",
    "v7": "v4 con warmup/few-shot matemático.",
    "v8": "Autocomplete simple zero-shot; solo resultado numérico.",
    "v9": "Autocomplete simple few-shot; solo resultado numérico.",
}


def load_jsonl(path):
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


def summarize_rows(rows):
    stats = defaultdict(
        lambda: {
            "total": 0,
            "correct": 0,
            "json_valid": 0,
            "latencies": [],
        }
    )
    for row in rows:
        model = row.get("model", "unknown")
        prompt_id = row.get("prompt_id", "unknown")
        evaluation = evaluate_row(row)
        item = stats[(model, prompt_id)]
        item["total"] += 1
        item["correct"] += int(evaluation["strict_correct"])
        item["json_valid"] += int(evaluation["json_valid"])
        if isinstance(row.get("latency_seconds"), (int, float)):
            item["latencies"].append(row["latency_seconds"])
    return stats


def load_stats():
    all_rows = []
    for prompt_id, paths in PROMPT_FILES.items():
        for path in paths:
            for row in load_jsonl(path):
                if row.get("prompt_id") and row.get("prompt_id") != prompt_id:
                    continue
                row.setdefault("prompt_id", prompt_id)
                all_rows.append(row)
    return summarize_rows(all_rows)


def score(item):
    if not item or not item["total"]:
        return "-"
    return f"{item['correct']}/{item['total']}"


def json_score(item):
    if not item or not item["total"]:
        return "-"
    return f"{item['json_valid']}/{item['total']}"


def latency(item):
    if not item or not item["latencies"]:
        return "-"
    return f"{average(item['latencies']):.3f}s"


def best_for_model(stats, model):
    candidates = []
    for prompt_id in PROMPTS:
        item = stats.get((model, prompt_id))
        if not item:
            continue
        candidates.append((prompt_id, item))
    candidates.sort(
        key=lambda pair: (
            pair[1]["correct"] / pair[1]["total"] if pair[1]["total"] else 0,
            pair[1]["correct"],
            pair[1]["json_valid"] / pair[1]["total"] if pair[1]["total"] else 0,
            -(average(pair[1]["latencies"]) or 0),
        ),
        reverse=True,
    )
    return candidates[0] if candidates else ("-", None)


def render_prompt_table(stats, prompt_id, models):
    rows = []
    for model in models:
        item = stats.get((model, prompt_id))
        if item:
            rows.append((model, item))
    rows.sort(
        key=lambda pair: (
            pair[1]["correct"] / pair[1]["total"] if pair[1]["total"] else 0,
            pair[1]["correct"],
            pair[1]["json_valid"] / pair[1]["total"] if pair[1]["total"] else 0,
            -(average(pair[1]["latencies"]) or 0),
        ),
        reverse=True,
    )

    lines = [
        "| Posición | Modelo | Aciertos | Exactitud | JSON válido | Latencia |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for position, (model, item) in enumerate(rows, start=1):
        total = item["total"]
        lines.append(
            f"| {position} | `{model}` | {item['correct']}/{total} | "
            f"{percentage(item['correct'], total)} | {json_score(item)} | {latency(item)} |"
        )
    return lines


def render_report(stats):
    models = sorted({model for model, _prompt_id in stats})
    models_by_best = sorted(
        models,
        key=lambda model: (
            best_for_model(stats, model)[1]["correct"] if best_for_model(stats, model)[1] else 0,
            best_for_model(stats, model)[1]["json_valid"] if best_for_model(stats, model)[1] else 0,
        ),
        reverse=True,
    )

    lines = [
        "# Comparación Azure v4 a v9",
        "",
        "Resumen simple de modelos Azure/GuaranIA anteriores y nuevos (`gpt-5.6-terra`, `gpt-5.5`).",
        "",
        "Métrica principal: `response.final_answer.value == expected_answer`.",
        "",
        "## Resumen de prompts",
        "",
        "| Prompt | Resumen |",
        "|---|---|",
    ]

    for prompt_id in PROMPTS:
        lines.append(f"| `{prompt_id}` | {PROMPT_SUMMARIES[prompt_id]} |")

    lines.extend([
        "",
    ]
    )

    for prompt_id in PROMPTS:
        lines.extend([f"## Prompt {prompt_id}", ""])
        lines.extend(render_prompt_table(stats, prompt_id, models))
        lines.append("")

    lines.extend(
        [
            "## Comparación Final",
            "",
            "| Modelo | v4 | v5 | v6 | v7 | v8 | v9 | Mejor prompt | Mejor resultado |",
            "|---|---:|---:|---:|---:|---:|---:|---|---:|",
        ]
    )
    for model in models_by_best:
        best_prompt, best_item = best_for_model(stats, model)
        values = [score(stats.get((model, prompt_id))) for prompt_id in PROMPTS]
        lines.append(
            f"| `{model}` | {' | '.join(values)} | `{best_prompt}` | {score(best_item)} |"
        )

    lines.extend(
        [
            "",
            "## Conclusión",
            "",
            "`gpt-5.5` es el mejor modelo global: alcanza 10/10 con varios prompts. `gpt-5.6-terra` queda segundo con 9/10 usando `v9`.",
        ]
    )
    return "\n".join(lines) + "\n"


def main():
    stats = load_stats()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(render_report(stats), encoding="utf-8")
    print(f"Reporte generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
