# Prompt Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_sonnet5_extra_evaluable.jsonl`
- Attempts read: 10
- Attempts evaluated for ranking: 10
- Invalid JSONL lines: 0
- Best combination: **claude / claude-sonnet-5 / v5** (9/10)

## Ranking by Prompt

| Rank | Provider | Model | Prompt | Name | Correct answers | Accuracy | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | claude | claude-sonnet-5 | v5 | Strict Guaraní with reinforced JSON rules | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | - |

## Per-Problem Details

| Prompt | Problem | Model | Expected | Predicted | Correct | Valid JSON | Line |
|---|---:|---|---:|---:|---|---|---:|
| v5 | 1 | claude-sonnet-5 | 18 | 18 | yes | yes | 1 |
| v5 | 2 | claude-sonnet-5 | 8 | 8 | yes | yes | 2 |
| v5 | 3 | claude-sonnet-5 | 140 | 140 | yes | yes | 3 |
| v5 | 4 | claude-sonnet-5 | 600 | 600 | yes | yes | 4 |
| v5 | 5 | claude-sonnet-5 | 3 | 3 | yes | yes | 5 |
| v5 | 6 | claude-sonnet-5 | 60 | 30 | no | yes | 6 |
| v5 | 7 | claude-sonnet-5 | 91 | 91 | yes | yes | 7 |
| v5 | 8 | claude-sonnet-5 | 360 | 360 | yes | yes | 8 |
| v5 | 9 | claude-sonnet-5 | 8 | 8 | yes | yes | 9 |
| v5 | 10 | claude-sonnet-5 | 34 | 34 | yes | yes | 10 |
