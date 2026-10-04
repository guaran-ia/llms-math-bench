import argparse
import json
from collections import defaultdict
from pathlib import Path

from evaluate_prompt_results import average, evaluate_row, percentage


def load_rows(path):
    rows = []
    with Path(path).open(encoding="utf-8") as file:
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
            "correct_problem_ids": set(),
        }
    )
    for row in rows:
        model = row.get("model", "unknown")
        evaluation = evaluate_row(row)
        item = stats[model]
        item["total"] += 1
        item["correct"] += int(evaluation["strict_correct"])
        item["json_valid"] += int(evaluation["json_valid"])
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


def format_delta(delta):
    if delta > 0:
        return f"+{delta}"
    return str(delta)


def render_problem_list(values):
    if not values:
        return "-"
    return ", ".join(f"P{value}" for value in sorted(values))


def render_wrong(wrong):
    if not wrong:
        return "ninguno"
    return ", ".join(
        f"P{item['problem_id']} ({item['expected']} -> {item['predicted']})"
        for item in wrong
    )


def render_report(stats_a, stats_b, label_a, label_b):
    models = sorted(set(stats_a) | set(stats_b))
    ranked = sorted(
        models,
        key=lambda model: (
            stats_b.get(model, {}).get("correct", 0) - stats_a.get(model, {}).get("correct", 0),
            stats_b.get(model, {}).get("correct", 0),
        ),
        reverse=True,
    )

    lines = [
        f"# Comparación Azure {label_a} vs {label_b}",
        "",
        "La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.",
        "",
        "## Resumen por modelo",
        "",
        f"| Modelo | {label_a} | {label_b} | Delta | JSON {label_a} | JSON {label_b} | Latencia {label_a} | Latencia {label_b} |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for model in ranked:
        a = stats_a.get(model, {"total": 0, "correct": 0, "json_valid": 0, "latencies": [], "correct_problem_ids": set(), "wrong": []})
        b = stats_b.get(model, {"total": 0, "correct": 0, "json_valid": 0, "latencies": [], "correct_problem_ids": set(), "wrong": []})
        latency_a = f"{average(a['latencies']):.3f}s" if a["latencies"] else "-"
        latency_b = f"{average(b['latencies']):.3f}s" if b["latencies"] else "-"
        lines.append(
            f"| `{model}` | {a['correct']}/{a['total']} | {b['correct']}/{b['total']} | "
            f"{format_delta(b['correct'] - a['correct'])} | {a['json_valid']}/{a['total']} | "
            f"{b['json_valid']}/{b['total']} | {latency_a} | {latency_b} |"
        )

    lines.extend(
        [
            "",
            f"## Ranking {label_b}",
            "",
            "| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |",
            "|---:|---|---:|---:|---:|---:|",
        ]
    )

    ranked_b = sorted(
        stats_b.items(),
        key=lambda pair: (
            pair[1]["correct"] / pair[1]["total"] if pair[1]["total"] else 0,
            pair[1]["correct"],
            pair[1]["json_valid"] / pair[1]["total"] if pair[1]["total"] else 0,
            -(average(pair[1]["latencies"]) or 0),
        ),
        reverse=True,
    )
    for position, (model, item) in enumerate(ranked_b, start=1):
        total = item["total"]
        latency = f"{average(item['latencies']):.3f}s" if item["latencies"] else "-"
        lines.append(
            f"| {position} | `{model}` | {item['correct']}/{total} | "
            f"{percentage(item['correct'], total)} | {item['json_valid']}/{total} | {latency} |"
        )

    lines.extend(
        [
            "",
            "## Cambios por problema",
            "",
            f"| Modelo | Mejoró en {label_b} | Empeoró en {label_b} | Errores {label_b} |",
            "|---|---|---|---|",
        ]
    )
    for model in ranked:
        a = stats_a.get(model, {"correct_problem_ids": set(), "wrong": []})
        b = stats_b.get(model, {"correct_problem_ids": set(), "wrong": []})
        improved = b["correct_problem_ids"] - a["correct_problem_ids"]
        regressed = a["correct_problem_ids"] - b["correct_problem_ids"]
        lines.append(
            f"| `{model}` | {render_problem_list(improved)} | {render_problem_list(regressed)} | "
            f"{render_wrong(b['wrong'])} |"
        )

    if ranked_b:
        best_model, best_item = ranked_b[0]
        lines.extend(
            [
                "",
                "## Conclusión",
                "",
                f"El mejor resultado en `{label_b}` fue `{best_model}` con {best_item['correct']}/{best_item['total']}.",
            ]
        )

    return "\n".join(lines) + "\n"


def parse_args():
    parser = argparse.ArgumentParser(description="Compara dos corridas Azure por prompt.")
    parser.add_argument("--a", required=True)
    parser.add_argument("--b", required=True)
    parser.add_argument("--label-a", default="v5")
    parser.add_argument("--label-b", default="v6")
    parser.add_argument("--output", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    stats_a = summarize(load_rows(args.a))
    stats_b = summarize(load_rows(args.b))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(stats_a, stats_b, args.label_a, args.label_b), encoding="utf-8")
    print(f"Reporte generado: {output}")


if __name__ == "__main__":
    main()
