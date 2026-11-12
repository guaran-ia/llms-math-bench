"""Summarize benchmark JSONL with accuracy, confidence intervals, and paired tests."""
from __future__ import annotations
import argparse, json, math
from collections import defaultdict
from pathlib import Path
from src.math_evaluation import evaluate
from src.dataset import PROJECT_ROOT


def wilson(successes: int, n: int, z: float = 1.959963984540054):
    if not n: return (None, None)
    p = successes / n
    den = 1 + z*z/n
    center = (p + z*z/(2*n))/den
    half = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/den
    return center-half, center+half


def binom_two_sided(k: int, n: int) -> float:
    if n == 0: return 1.0
    tail = sum(math.comb(n, i) for i in range(0, min(k, n-k)+1)) / (2**n)
    return min(1.0, 2*tail)


def mcnemar(a: list[bool], b: list[bool]) -> tuple[int,int,float]:
    if len(a) != len(b): raise ValueError("Paired samples must have equal length")
    a_only = sum(x and not y for x,y in zip(a,b))
    b_only = sum(y and not x for x,y in zip(a,b))
    return a_only, b_only, binom_two_sided(min(a_only,b_only), a_only+b_only)


def holm(pairs):
    """Return (raw p, Holm-adjusted p) in original order."""
    n=len(pairs); order=sorted(range(n), key=lambda i:pairs[i][1]); adjusted=[1.0]*n; running=0.0
    for rank,idx in enumerate(order):
        running=max(running, min(1.0, (n-rank)*pairs[idx][1])); adjusted[idx]=running
    return [(pairs[i][1],adjusted[i]) for i in range(n)]


def read_rows(path: Path):
    rows=[]
    for lineno,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: row=json.loads(line)
        except json.JSONDecodeError as exc: raise ValueError(f"Invalid JSONL at line {lineno}: {exc}") from exc
        row["_score"]=evaluate(row)["correct"]
        rows.append(row)
    return rows


def aggregate(rows, keys):
    groups=defaultdict(list)
    for r in rows: groups[tuple(r.get(k) for k in keys)].append(bool(r["_score"]))
    out=[]
    for key,vals in sorted(groups.items(), key=lambda item:tuple(str(x) for x in item[0])):
        s=sum(vals); lo,hi=wilson(s,len(vals))
        out.append((key,s,len(vals),lo,hi))
    return out


def make_report(rows, source):
    for row in rows:
        if "_score" not in row:
            row["_score"] = evaluate(row)["correct"]
    lines=["# Benchmark report", "", f"Input: `{source}`", "", f"Evaluable request records: **{len(rows)}**", "",
      "Accuracy is scored from the explicit `final_answer.value` using the shared evaluator. Intervals are 95% Wilson intervals.",
      "Paired tests use exact two-sided McNemar tests; Holm adjustment is applied within each family of comparisons.", "",
      "## Accuracy by dataset, language, model, and prompt", "",
      "| Dataset | Language | Model | Prompt | Correct / n | Accuracy (95% CI) |", "|---|---|---|---|---:|---:|"]
    for (ds,lang,model,prompt),s,n,lo,hi in aggregate(rows,["dataset_id","language","model_id","prompt_condition_id"]):
        interval="—" if lo is None else f"{lo:.1%}–{hi:.1%}"
        ds_name=next((r.get("dataset_name") for r in rows if r.get("dataset_id")==ds and r.get("dataset_name")),ds)
        lines.append(f"| {ds_name} | {lang} | {model} | {prompt} | {s}/{n} | {s/n:.1%} ({interval}) |")
    lines += ["", "## Paired Spanish–Guaraní comparisons", "", "Pairs are matched on dataset, problem, model, and prompt. Difference is Spanish accuracy minus Guaraní accuracy.", "",
              "| Dataset | Model | Prompt | n | ES correct | GN correct | ES−GN (pp) | ES-only / GN-only | McNemar p | Holm p |", "|---|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    pairs=defaultdict(dict)
    for r in rows:
        if r.get("language") in ("es","gn"):
            key=(r.get("dataset_id"),r.get("problem_id"),r.get("model_id"),r.get("prompt_condition_id"))
            pairs[key][r["language"]]=bool(r["_score"])
    groups=defaultdict(list)
    for (ds,pid,model,prompt),vals in pairs.items():
        if "es" in vals and "gn" in vals: groups[(ds,model,prompt)].append((pid,vals["es"],vals["gn"]))
    for group,vals in sorted(groups.items()):
        es=[x[1] for x in vals]; gn=[x[2] for x in vals]; a,b,p=mcnemar(es,gn); groups[group]=(vals,a,b,p)
    adj=holm([(g,v[3]) for g,v in groups.items()])
    for (ds,model,prompt),(vals,a,b,p),(_,hp) in zip(groups.keys(),groups.values(),adj):
        es=sum(x[1] for x in vals); gn=sum(x[2] for x in vals); n=len(vals)
        ds_name=next((r.get("dataset_name") for r in rows if r.get("dataset_id")==ds and r.get("dataset_name")),ds)
        lines.append(f"| {ds_name} | {model} | {prompt} | {n} | {es}/{n} | {gn}/{n} | {(es-gn)/n*100:+.1f} | {a}/{b} | {p:.4g} | {hp:.4g} |")
    lines += ["", "## Prompt comparisons against standard", "", "Paired by dataset, problem, model, and language. Prompt-by-dataset findings are exploratory given the small number of problems per dataset.", "",
              "| Dataset | Language | Model | Prompt vs standard | n | Prompt correct | Standard correct | Prompt−standard (pp) | Prompt-only / standard-only | McNemar p | Holm p |", "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    cells=defaultdict(dict)
    for r in rows:
        key=(r.get("dataset_id"),r.get("problem_id"),r.get("model_id"),r.get("language"))
        cells[key][r.get("prompt_condition_id")]=bool(r["_score"])
    tests=[]
    for key,vals in cells.items():
        if "standard" not in vals: continue
        for prompt,score in vals.items():
            if prompt!="standard": tests.append((key,prompt,score,vals["standard"]))
    by_group=defaultdict(list)
    for (ds,pid,model,lang),prompt,score,base in tests: by_group[(ds,lang,model,prompt)].append((score,base))
    compared=[]
    for group,vals in sorted(by_group.items()):
        a=sum(x and not y for x,y in vals); b=sum(y and not x for x,y in vals)
        compared.append((group,vals,a,b,binom_two_sided(min(a,b),a+b)))
    adjusted=holm([(g,p) for g,_,_,_,p in compared])
    for (group,vals,a,b,p),(_,hp) in zip(compared,adjusted):
        ds,lang,model,prompt=group; n=len(vals); ps=sum(x for x,_ in vals); bs=sum(y for _,y in vals)
        ds_name=next((r.get("dataset_name") for r in rows if r.get("dataset_id")==ds and r.get("dataset_name")),ds)
        lines.append(f"| {ds_name} | {lang} | {model} | {prompt} | {n} | {ps}/{n} | {bs}/{n} | {(ps-bs)/n*100:+.1f} | {a}/{b} | {p:.4g} | {hp:.4g} |")
    lines += ["", "## Run coverage", "", "Failed API requests remain in the JSONL and count as incorrect. Incomplete pairs are omitted from paired tests. Review run metadata and data/prompt hashes before interpreting pooled results.", ""]
    return "\n".join(lines)


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("--input",required=True); p.add_argument("--output")
    a=p.parse_args(argv); src=Path(a.input); src=src if src.is_absolute() else PROJECT_ROOT/src
    rows=read_rows(src); report=make_report(rows,src)
    out=Path(a.output) if a.output else PROJECT_ROOT/"reports"/(src.stem+"_report.md")
    if not out.is_absolute(): out=PROJECT_ROOT/out
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(report,encoding="utf-8"); print(out)

if __name__=="__main__": main()
