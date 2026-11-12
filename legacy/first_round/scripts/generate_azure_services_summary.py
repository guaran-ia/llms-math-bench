import json
from collections import defaultdict
from pathlib import Path

from src.evaluate_prompt_results import average, evaluate_row, percentage


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "reports" / "azure_services" / "summary_new_vs_existing_models.md"

EXISTING_FILES = {
    "v4": BASE_DIR / "results" / "azure" / "model_test_results_guarani_prompt_v4.jsonl",
    "v5": BASE_DIR / "results" / "azure" / "model_test_results_azure_v5.jsonl",
    "v6": BASE_DIR / "results" / "azure" / "model_test_results_azure_v6.jsonl",
    "v7": BASE_DIR / "results" / "azure" / "model_test_results_azure_v7.jsonl",
    "v8": BASE_DIR / "results" / "azure" / "model_test_results_azure_v8.jsonl",
    "v9": BASE_DIR / "results" / "azure" / "model_test_results_azure_v9.jsonl",
}
NEW_FILE = BASE_DIR / "results" / "azure_services" / "model_test_results_new_models_all_prompts.jsonl"
PROMPTS = ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9"]


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


def summarize(rows):
    stats = defaultdict(
        lambda: {
            "total": 0,
            "correct": 0,
            "json_valid": 0,
            "latencies": [],
            "wrong": [],
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
        if not evaluation["strict_correct"]:
            item["wrong"].append(
                {
                    "problem_id": row.get("problem_id"),
                    "expected": evaluation["expected"],
                    "predicted": evaluation["predicted"],
                }
            )
    return stats


def merge_stats(*stats_list):
    merged = {}
    for stats in stats_list:
        merged.update(stats)
    return merged


def best_by_model(stats):
    best = {}
    for (model, prompt_id), item in stats.items():
        current = best.get(model)
        rank = (
            item["correct"] / item["total"] if item["total"] else 0,
            item["correct"],
            item["json_valid"] / item["total"] if item["total"] else 0,
            -(average(item["latencies"]) or 0),
        )
        if current is None or rank > current["rank"]:
            best[model] = {"prompt_id": prompt_id, "item": item, "rank": rank}
    return best


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


def wrong_summary(item):
    if not item or not item["wrong"]:
        return "ninguno"
    return ", ".join(
        f"P{wrong['problem_id']} ({wrong['expected']} -> {wrong['predicted']})"
        for wrong in item["wrong"]
    )


def render_matrix(stats, models):
    lines = [
        "| Modelo | v1 | v2 | v3 | v4 | v5 | v6 | v7 | v8 | v9 | Mejor prompt | Mejor resultado |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|",
    ]
    best = best_by_model(stats)
    for model in models:
        values = [score(stats.get((model, prompt_id))) for prompt_id in PROMPTS]
        best_data = best[model]
        lines.append(
            f"| `{model}` | {' | '.join(values)} | `{best_data['prompt_id']}` | {score(best_data['item'])} |"
        )
    return lines


def render_report(existing_stats, new_stats):
    all_stats = merge_stats(existing_stats, new_stats)
    best_all = best_by_model(all_stats)
    new_models = sorted({model for model, _prompt in new_stats})
    existing_models = sorted({model for model, _prompt in existing_stats})
    all_models = sorted(
        set(new_models) | set(existing_models),
        key=lambda model: (
            best_all[model]["item"]["correct"] / best_all[model]["item"]["total"],
            best_all[model]["item"]["correct"],
        ),
        reverse=True,
    )

    lines = [
        "# Resumen nuevos modelos Azure Services",
        "",
        "Comparación resumida entre los nuevos modelos `gpt-5.6-terra` y `gpt-5.5` contra los modelos Azure/GuaranIA evaluados anteriormente.",
        "",
        "La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.",
        "",
        "## Ranking global por mejor prompt",
        "",
        "| Posición | Modelo | Mejor prompt | Aciertos | Exactitud | JSON válido | Latencia media |",
        "|---:|---|---|---:|---:|---:|---:|",
    ]

    for position, model in enumerate(all_models, start=1):
        best_data = best_all[model]
        item = best_data["item"]
        total = item["total"]
        lines.append(
            f"| {position} | `{model}` | `{best_data['prompt_id']}` | {item['correct']}/{total} | "
            f"{percentage(item['correct'], total)} | {json_score(item)} | {latency(item)} |"
        )

    lines.extend(["", "## Nuevos modelos: resultados por prompt", ""])
    lines.extend(render_matrix(new_stats, new_models))

    lines.extend(["", "## Comparación resumida contra modelos existentes", ""])
    lines.extend(render_matrix(all_stats, all_models))

    lines.extend(
        [
            "",
            "## Errores del mejor prompt por modelo nuevo",
            "",
            "| Modelo | Mejor prompt | Errores |",
            "|---|---|---|",
        ]
    )
    for model in new_models:
        best_data = best_all[model]
        lines.append(
            f"| `{model}` | `{best_data['prompt_id']}` | {wrong_summary(best_data['item'])} |"
        )

    best_model = all_models[0]
    best_data = best_all[best_model]
    lines.extend(
        [
            "",
            "## Conclusión",
            "",
            f"El mejor resultado global ahora es `{best_model}` con `{best_data['prompt_id']}`: {score(best_data['item'])}.",
        ]
    )
    return "\n".join(lines) + "\n"


def main():
    existing_rows = []
    for prompt_id, path in EXISTING_FILES.items():
        for row in load_jsonl(path):
            row.setdefault("prompt_id", prompt_id)
            existing_rows.append(row)
    existing_stats = summarize(existing_rows)
    new_stats = summarize(load_jsonl(NEW_FILE))
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(render_report(existing_stats, new_stats), encoding="utf-8")
    print(f"Reporte generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
