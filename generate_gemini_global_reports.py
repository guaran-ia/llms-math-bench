import json
from collections import defaultdict
from pathlib import Path

from evaluate_prompt_results import average, evaluate_row, percentage, rank_stats


BASE_DIR = Path(__file__).resolve().parent
PROMPTS_FILE = BASE_DIR / "prompts" / "guarani_math_prompts.json"
REPORTS_DIR = BASE_DIR / "reports" / "gemini"

INPUT_FILES = [
    BASE_DIR / "results" / "gemini" / "model_test_results_gemini_3_1_pro.jsonl",
    BASE_DIR / "results" / "gemini" / "model_test_results_gemini_v5.jsonl",
    BASE_DIR / "results" / "gemini" / "model_test_results_gemini_3_5_flash.jsonl",
    BASE_DIR / "results" / "gemini" / "model_test_results_gemini_3_flash_preview.jsonl",
    BASE_DIR / "results" / "gemini" / "model_test_results_gemini_3.5_live_translate_preview.jsonl",
    BASE_DIR / "results" / "gemini" / "model_test_results_gemini_3.1_flash_lite.jsonl",
]

GLOBAL_REPORT = REPORTS_DIR / "prompts_y_resultados_gemini_v1_v5.md"
SUMMARY_REPORT = REPORTS_DIR / "resumen_gemini_v1_v5.md"
PROMPT_IDS = ["v1", "v2", "v3", "v4", "v5"]


def load_prompts():
    prompts = json.loads(PROMPTS_FILE.read_text(encoding="utf-8"))
    return {prompt["id"]: prompt for prompt in prompts}


def load_rows():
    rows = []
    for path in INPUT_FILES:
        with path.open(encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                row["_source_file"] = path.name
                row["_line_number"] = line_number
                rows.append(row)
    return latest_by_model_prompt_problem(rows)


def latest_by_model_prompt_problem(rows):
    latest = {}
    for row in rows:
        key = (row.get("model"), row.get("prompt_id"), row.get("problem_id"))
        latest[key] = row
    return list(latest.values())


def summarize(rows):
    stats = defaultdict(
        lambda: {
            "provider": None,
            "prompt_name": None,
            "total": 0,
            "strict_correct": 0,
            "json_valid": 0,
            "option_consistent": 0,
            "errors": 0,
            "json_parse_errors": 0,
            "latencies": [],
        }
    )
    for row in rows:
        key = (row.get("provider", "unknown"), row.get("model", "unknown"), row.get("prompt_id", "unknown"))
        evaluation = evaluate_row(row)
        item = stats[key]
        item["provider"] = key[0]
        item["prompt_name"] = row.get("prompt_name")
        item["total"] += 1
        item["strict_correct"] += int(evaluation["strict_correct"])
        item["json_valid"] += int(evaluation["json_valid"])
        item["option_consistent"] += int(evaluation["option_consistent"])
        item["errors"] += int(bool(row.get("error")))
        item["json_parse_errors"] += int(bool(row.get("json_parse_error")))
        if isinstance(row.get("latency_seconds"), (int, float)):
            item["latencies"].append(row["latency_seconds"])
    return stats


def prompt_text(prompt):
    template = prompt["template"]
    if isinstance(template, list):
        template = "\n".join(template)
    return template.replace("{{", "{").replace("}}", "}")


def table_for_prompt(stats, prompt_id):
    rows = [((provider, model, pid), item) for (provider, model, pid), item in stats.items() if pid == prompt_id]
    rows.sort(
        key=lambda pair: (
            pair[1]["strict_correct"] / pair[1]["total"] if pair[1]["total"] else 0,
            pair[1]["strict_correct"],
            pair[1]["json_valid"] / pair[1]["total"] if pair[1]["total"] else 0,
            -(average(pair[1]["latencies"]) or 0),
        ),
        reverse=True,
    )

    lines = [
        "| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for position, ((_provider, model, _pid), item) in enumerate(rows, start=1):
        total = item["total"]
        avg_latency = average(item["latencies"])
        latency = f"{avg_latency:.3f}s" if avg_latency is not None else "-"
        lines.append(
            f"| {position} | `{model}` | {item['strict_correct']}/{total} | "
            f"{percentage(item['strict_correct'], total)} | {item['json_valid']}/{total} | {latency} |"
        )
    return lines


def best_by_model(stats):
    best = {}
    for key, item in stats.items():
        _provider, model, prompt_id = key
        current = best.get(model)
        score = (
            item["strict_correct"] / item["total"] if item["total"] else 0,
            item["strict_correct"],
            item["json_valid"] / item["total"] if item["total"] else 0,
            -(average(item["latencies"]) or 0),
        )
        if current is None or score > current["score"]:
            best[model] = {"prompt_id": prompt_id, "item": item, "score": score}
    return best


def comparison_lines(stats):
    best = best_by_model(stats)
    models = sorted(
        best,
        key=lambda model: (
            best[model]["item"]["strict_correct"] / best[model]["item"]["total"] if best[model]["item"]["total"] else 0,
            best[model]["item"]["strict_correct"],
            -(average(best[model]["item"]["latencies"]) or 0),
        ),
        reverse=True,
    )

    lines = [
        "| Modelo | v1 | v2 | v3 | v4 | v5 | Mejor resultado |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for model in models:
        values = []
        for prompt_id in PROMPT_IDS:
            item = stats.get(("gemini", model, prompt_id))
            values.append(f"{item['strict_correct']}/{item['total']}" if item else "-")
        best_item = best[model]["item"]
        lines.append(f"| `{model}` | {' | '.join(values)} | {best_item['strict_correct']}/{best_item['total']} |")
    return lines


def ranking_lines(stats):
    best = best_by_model(stats)
    ranked = sorted(
        best.items(),
        key=lambda pair: (
            pair[1]["item"]["strict_correct"] / pair[1]["item"]["total"] if pair[1]["item"]["total"] else 0,
            pair[1]["item"]["strict_correct"],
            pair[1]["item"]["json_valid"] / pair[1]["item"]["total"] if pair[1]["item"]["total"] else 0,
            -(average(pair[1]["item"]["latencies"]) or 0),
        ),
        reverse=True,
    )

    lines = [
        "| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for position, (model, best_data) in enumerate(ranked, start=1):
        item = best_data["item"]
        total = item["total"]
        avg_latency = average(item["latencies"])
        latency = f"{avg_latency:.3f}s" if avg_latency is not None else "-"
        lines.append(
            f"| {position} | `{model}` | {item['strict_correct']}/{total} | "
            f"{percentage(item['strict_correct'], total)} | {item['json_valid']}/{total} | {latency} |"
        )
    return lines


def render_global(prompts, rows, stats):
    model_count = len({row.get("model") for row in rows})
    lines = [
        "# Prompts y resultados Gemini v1 a v5",
        "",
        f"Evaluación sobre 10 problemas matemáticos en guaraní y {model_count} modelos Gemini. La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.",
    ]

    for prompt_id in PROMPT_IDS:
        prompt = prompts[prompt_id]
        lines.extend(
            [
                "",
                f"## Prueba {prompt_id}",
                "",
                "### Prompt usado",
                "",
                "```text",
                prompt_text(prompt),
                "```",
                "",
                "### Resultado de los modelos",
                "",
            ]
        )
        lines.extend(table_for_prompt(stats, prompt_id))

    lines.extend(["", "## Comparación final", ""])
    lines.extend(comparison_lines(stats))
    lines.extend(["", "## Ranking global", ""])
    lines.extend(ranking_lines(stats))

    best = rank_stats(stats)[0]
    (_provider, best_model, best_prompt), best_item = best
    lines.extend(
        [
            "",
            "## Conclusión",
            "",
            f"El mejor resultado absoluto fue {best_item['strict_correct']}/{best_item['total']}. Lo alcanzó `{best_model}` con `{best_prompt}`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_summary(stats):
    lines = ["# Resumen Gemini v1 a v5", "", "## Comparación final", ""]
    lines.extend(comparison_lines(stats))
    lines.extend(["", "## Ranking global", ""])
    lines.extend(ranking_lines(stats))
    return "\n".join(lines) + "\n"


def main():
    prompts = load_prompts()
    rows = load_rows()
    stats = summarize(rows)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    GLOBAL_REPORT.write_text(render_global(prompts, rows, stats), encoding="utf-8")
    SUMMARY_REPORT.write_text(render_summary(stats), encoding="utf-8")
    print(f"Reporte global generado: {GLOBAL_REPORT}")
    print(f"Resumen generado: {SUMMARY_REPORT}")


if __name__ == "__main__":
    main()
