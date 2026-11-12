"""Paired Spanish/Guarani accuracy summaries with Wilson intervals and exact McNemar."""
import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

from src.math_evaluation import evaluate


def load_jsonl(path):
    rows, invalid = [], []
    with Path(path).open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                invalid.append((number, str(exc)))
                continue
            row["_line_number"] = number
            rows.append(row)
    return rows, invalid


def wilson(successes, total, z=1.959963984540054):
    if not total:
        return None, None
    p = successes / total
    den = 1 + z * z / total
    center = (p + z * z / (2 * total)) / den
    half = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / den
    lower, upper = max(0.0, center - half), min(1.0, center + half)
    if successes == 0:
        lower = 0.0
    if successes == total:
        upper = 1.0
    return lower, upper


def exact_mcnemar(gn_only, es_only):
    n = gn_only + es_only
    if not n:
        return 1.0
    tail = sum(math.comb(n, k) for k in range(min(gn_only, es_only) + 1)) / (2 ** n)
    return min(1.0, 2 * tail)


def holm_adjust(p_values):
    """Holm step-down adjusted p-values, returned in original order."""
    indexed = sorted(enumerate(p_values), key=lambda item: item[1])
    adjusted, running = [1.0] * len(p_values), 0.0
    count = len(p_values)
    for rank, (index, p_value) in enumerate(indexed):
        running = max(running, min(1.0, (count - rank) * p_value))
        adjusted[index] = running
    return adjusted


def analyze(rows):
    paired = {}
    for row in rows:
        lang = row.get("language")
        if lang not in {"gn", "es"}:
            continue
        key = (row.get("provider"), row.get("model"), row.get("prompt_pair_id", row.get("prompt_id")), str(row.get("problem_id")))
        score = evaluate(row)
        paired.setdefault(key, {})[lang] = {
            "correct": bool(score["correct"]),
            "api_error": bool(row.get("error")),
            "json_valid": bool(score["json_valid"]),
        }
    groups = defaultdict(list)
    for (provider, model, prompt_id, problem_id), outcomes in paired.items():
        if set(outcomes) == {"gn", "es"}:
            groups[(provider, model, prompt_id)].append((problem_id, outcomes["gn"], outcomes["es"]))
    output = []
    for key, values in sorted(groups.items()):
        gn = sum(x[1]["correct"] for x in values)
        es = sum(x[2]["correct"] for x in values)
        gn_only = sum(g["correct"] and not e["correct"] for _, g, e in values)
        es_only = sum(e["correct"] and not g["correct"] for _, g, e in values)
        output.append({"key": key, "n": len(values), "gn": gn, "es": es,
                       "gn_ci": wilson(gn, len(values)), "es_ci": wilson(es, len(values)),
                       "gn_errors": sum(x[1]["api_error"] for x in values),
                       "es_errors": sum(x[2]["api_error"] for x in values),
                       "gn_invalid_json": sum(not x[1]["json_valid"] for x in values),
                       "es_invalid_json": sum(not x[2]["json_valid"] for x in values),
                       "gn_only": gn_only, "es_only": es_only,
                       "mcnemar_p": exact_mcnemar(gn_only, es_only)})
    for item, adjusted in zip(output, holm_adjust([item["mcnemar_p"] for item in output])):
        item["mcnemar_p_holm"] = adjusted
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSONL with Spanish and Guarani runs")
    parser.add_argument("--output", required=True, help="Markdown report destination")
    args = parser.parse_args()
    rows, invalid = load_jsonl(args.input)
    results = analyze(rows)
    lines = ["# Spanish–Guarani paired benchmark report", "",
             f"Input: `{Path(args.input).name}` · rows: {len(rows)} · malformed lines: {len(invalid)}", "",
             "Accuracy uses an explicit parsed `final_answer.value` (or recovered JSON field);" ,
             "free text is never scored by extracting an arbitrary number. CIs are 95% Wilson intervals.",
             "The two-sided exact McNemar p-value uses discordant paired items. P-values include Holm adjustment across comparisons in this report.", "",
             "API failures and invalid JSON remain in the accuracy denominator and are reported separately.", "",
             "| Provider | Model | Prompt | Pairs | Guarani | Spanish | GN errors/invalid JSON | ES errors/invalid JSON | GN only correct | ES only correct | McNemar p | Holm p |",
             "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for item in results:
        provider, model, prompt = item["key"]
        def rate(n, ci):
            lo, hi = ci
            return f"{n}/{item['n']} ({n/item['n']:.1%}, {lo:.1%}–{hi:.1%})"
        lines.append(f"| {provider} | {model} | {prompt} | {item['n']} | {rate(item['gn'], item['gn_ci'])} | {rate(item['es'], item['es_ci'])} | {item['gn_errors']}/{item['gn_invalid_json']} | {item['es_errors']}/{item['es_invalid_json']} | {item['gn_only']} | {item['es_only']} | {item['mcnemar_p']:.4f} | {item['mcnemar_p_holm']:.4f} |")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
