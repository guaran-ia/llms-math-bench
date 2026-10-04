import json
from collections import defaultdict
from pathlib import Path

from evaluate_prompt_results import average, evaluate_row, percentage


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "reports" / "azure" / "azure_v4_v9_team_comparison.md"

PROMPT_FILES = {
    "v4": BASE_DIR / "results" / "azure" / "model_test_results_guarani_prompt_v4.jsonl",
    "v5": BASE_DIR / "results" / "azure" / "model_test_results_azure_v5.jsonl",
    "v6": BASE_DIR / "results" / "azure" / "model_test_results_azure_v6.jsonl",
    "v7": BASE_DIR / "results" / "azure" / "model_test_results_azure_v7.jsonl",
    "v8": BASE_DIR / "results" / "azure" / "model_test_results_azure_v8.jsonl",
    "v9": BASE_DIR / "results" / "azure" / "model_test_results_azure_v9.jsonl",
}


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
            "latencies": [],
            "correct_problem_ids": set(),
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
        if isinstance(row.get("latency_seconds"), (int, float)):
            item["latencies"].append(row["latency_seconds"])
        if evaluation["strict_correct"]:
            item["correct_problem_ids"].add(row.get("problem_id"))
        else:
            item["wrong"].append(
                {
                    "problem_id": row.get("problem_id"),
                    "expected": evaluation["expected"],
                    "predicted": evaluation["predicted"],
                    "json_valid": evaluation["json_valid"],
                }
            )
    return stats


def load_all_stats():
    return {prompt_id: summarize(load_rows(path)) for prompt_id, path in PROMPT_FILES.items()}


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


def delta(a, b):
    value = b["correct"] - a["correct"]
    return f"+{value}" if value > 0 else str(value)


def render_problem_list(problem_ids):
    if not problem_ids:
        return "-"
    return ", ".join(f"P{problem_id}" for problem_id in sorted(problem_ids))


def render_wrong(wrong):
    if not wrong:
        return "ninguno"
    return ", ".join(
        f"P{item['problem_id']} ({item['expected']} -> {item['predicted']})"
        for item in wrong
    )


def models_in(stats_by_prompt):
    models = set()
    for stats in stats_by_prompt.values():
        models.update(stats.keys())
    return sorted(models)


def best_for_model(stats_by_prompt, model):
    candidates = []
    for prompt_id, stats in stats_by_prompt.items():
        item = stats.get(model)
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


def ranked_prompt(stats):
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


def comparison_table(stats_by_prompt, a_id, b_id):
    stats_a = stats_by_prompt[a_id]
    stats_b = stats_by_prompt[b_id]
    models = sorted(
        set(stats_a) | set(stats_b),
        key=lambda model: (
            stats_b.get(model, {"correct": 0})["correct"] - stats_a.get(model, {"correct": 0})["correct"],
            stats_b.get(model, {"correct": 0})["correct"],
        ),
        reverse=True,
    )

    lines = [
        f"| Modelo | {a_id} | {b_id} | Delta | JSON {a_id} | JSON {b_id} | Latencia {a_id} | Latencia {b_id} |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for model in models:
        a = stats_a[model]
        b = stats_b[model]
        lines.append(
            f"| `{model}` | {score(a)} | {score(b)} | {delta(a, b)} | "
            f"{json_score(a)} | {json_score(b)} | {latency(a)} | {latency(b)} |"
        )
    return lines


def changes_table(stats_by_prompt, a_id, b_id):
    stats_a = stats_by_prompt[a_id]
    stats_b = stats_by_prompt[b_id]
    models = sorted(set(stats_a) | set(stats_b))
    lines = [
        f"| Modelo | Mejoró en {b_id} | Empeoró en {b_id} | Errores {b_id} |",
        "|---|---|---|---|",
    ]
    for model in models:
        a = stats_a[model]
        b = stats_b[model]
        improved = b["correct_problem_ids"] - a["correct_problem_ids"]
        regressed = a["correct_problem_ids"] - b["correct_problem_ids"]
        lines.append(
            f"| `{model}` | {render_problem_list(improved)} | {render_problem_list(regressed)} | {render_wrong(b['wrong'])} |"
        )
    return lines


def render_report(stats_by_prompt):
    models = models_in(stats_by_prompt)
    lines = [
        "# Comparación Azure v4 a v9",
        "",
        "Comparación para el equipo sobre los prompts `v4`, `v5`, `v6`, `v7`, `v8` y `v9` en los modelos Azure/GuaranIA.",
        "",
        "La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.",
        "",
        "## Resumen Ejecutivo",
        "",
        "- `v4` conserva el mejor techo individual: `gpt-5.4-mini` llegó a 6/10.",
        "- `v7` mejora la robustez de modelos débiles, especialmente `grok`, `Mistral` y `gpt-4o-mini`, pero baja el techo máximo a 5/10.",
        "- `v5` y `v6` no superan a `v4` en techo máximo; ambos quedan con máximo 5/10.",
        "- `v8` y `v9` prueban el modo autocomplete simple; no superan a los prompts estructurados.",
        "- El warmup/few-shot ayuda a algunos modelos, pero no corrige los problemas recurrentes P1, P5, P6, P7 y P8.",
        "",
        "## Matriz v4-v9",
        "",
        "| Modelo | v4 | v5 | v6 | v7 | v8 | v9 | Mejor prompt | Mejor resultado |",
        "|---|---:|---:|---:|---:|---:|---:|---|---:|",
    ]

    models_sorted = sorted(
        models,
        key=lambda model: best_for_model(stats_by_prompt, model)[1]["correct"],
        reverse=True,
    )
    for model in models_sorted:
        best_prompt, best_item = best_for_model(stats_by_prompt, model)
        lines.append(
            f"| `{model}` | {score(stats_by_prompt['v4'].get(model))} | {score(stats_by_prompt['v5'].get(model))} | "
            f"{score(stats_by_prompt['v6'].get(model))} | {score(stats_by_prompt['v7'].get(model))} | "
            f"{score(stats_by_prompt['v8'].get(model))} | {score(stats_by_prompt['v9'].get(model))} | "
            f"`{best_prompt}` | {score(best_item)} |"
        )

    lines.extend(["", "## Ranking Por Prompt", ""])
    for prompt_id in ("v4", "v5", "v6", "v7", "v8", "v9"):
        lines.extend([f"### {prompt_id}", ""])
        lines.extend(
            [
                "| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |",
                "|---:|---|---:|---:|---:|---:|",
            ]
        )
        for position, (model, item) in enumerate(ranked_prompt(stats_by_prompt[prompt_id]), start=1):
            total = item["total"]
            lines.append(
                f"| {position} | `{model}` | {item['correct']}/{total} | {percentage(item['correct'], total)} | "
                f"{item['json_valid']}/{total} | {latency(item)} |"
            )
        lines.append("")

    lines.extend(["## Comparación v5 vs v6", ""])
    lines.extend(comparison_table(stats_by_prompt, "v5", "v6"))
    lines.extend(["", "### Cambios por problema v5 vs v6", ""])
    lines.extend(changes_table(stats_by_prompt, "v5", "v6"))

    lines.extend(["", "## Comparación v4 vs v7", ""])
    lines.extend(comparison_table(stats_by_prompt, "v4", "v7"))
    lines.extend(["", "### Cambios por problema v4 vs v7", ""])
    lines.extend(changes_table(stats_by_prompt, "v4", "v7"))

    lines.extend(["", "## Comparación v8 vs v9", ""])
    lines.extend(comparison_table(stats_by_prompt, "v8", "v9"))
    lines.extend(["", "### Cambios por problema v8 vs v9", ""])
    lines.extend(changes_table(stats_by_prompt, "v8", "v9"))

    lines.extend(
        [
            "",
            "## Conclusión",
            "",
            "Para maximizar el mejor resultado individual en Azure, `v4` sigue siendo el mejor baseline porque alcanza 6/10 con `gpt-5.4-mini`.",
            "",
            "Para una comparación de robustez entre modelos, `v7` es interesante porque mejora varios modelos que rendían mal con `v4`, pero no mejora el mejor resultado absoluto.",
            "",
            "Los prompts autocomplete simples (`v8` zero-shot y `v9` few-shot) rindieron peor que los prompts estructurados, por lo que no son buenos candidatos como baseline principal.",
        ]
    )
    return "\n".join(lines) + "\n"


def main():
    stats_by_prompt = load_all_stats()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(render_report(stats_by_prompt), encoding="utf-8")
    print(f"Reporte generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
