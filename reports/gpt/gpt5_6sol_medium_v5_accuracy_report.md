# Prompt Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_gpt5.6sol_medium_evaluable.jsonl`
- Attempts read: 10
- Attempts evaluated for ranking: 10
- Invalid JSONL lines: 0
- Best combination: **chatgpt / gpt-5 / v5** (9/10)

## Ranking by Prompt

| Rank | Provider | Model | Prompt | Name | Correct answers | Accuracy | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | chatgpt | gpt-5 | v5 | Strict Guaraní with reinforced JSON rules | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | - |

## Per-Problem Details

| Prompt | Problem | Model | Expected | Predicted | Correct | Valid JSON | Line |
|---|---:|---|---:|---:|---|---|---:|
| v5 | 1 | gpt-5 | 18 | 10 | no | yes | 1 |
| v5 | 2 | gpt-5 | 8 | 8 | yes | yes | 2 |
| v5 | 3 | gpt-5 | 140 | 140 | yes | yes | 3 |
| v5 | 4 | gpt-5 | 600 | 600 | yes | yes | 4 |
| v5 | 5 | gpt-5 | 3 | 3 | yes | yes | 5 |
| v5 | 6 | gpt-5 | 60 | 60 | yes | yes | 6 |
| v5 | 7 | gpt-5 | 91 | 91 | yes | yes | 7 |
| v5 | 8 | gpt-5 | 360 | 360 | yes | yes | 8 |
| v5 | 9 | gpt-5 | 8 | 8 | yes | yes | 9 |
| v5 | 10 | gpt-5 | 34 | 34 | yes | yes | 10 |
