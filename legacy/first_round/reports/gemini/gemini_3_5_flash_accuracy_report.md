# Prompt Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_gemini_3_5_flash.jsonl`
- Attempts read: 50
- Attempts evaluated for ranking: 50
- Invalid JSONL lines: 0
- Best combination: **gemini / gemini-3.5-flash / v4** (10/10)

## Ranking by Prompt

| Rank | Provider | Model | Prompt | Name | Correct answers | Accuracy | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | gemini | gemini-3.5-flash | v4 | Bilingual teacher with glossary | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 10.360s |
| 2 | gemini | gemini-3.5-flash | v3 | Bilingual teacher with semantic interpretation | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 8.295s |
| 3 | gemini | gemini-3.5-flash | v2 | Internal translation into Spanish | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 8.452s |
| 4 | gemini | gemini-3.5-flash | v1 | Strict Guaraní | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 10.139s |
| 5 | gemini | gemini-3.5-flash | v5 | Strict Guaraní with reinforced JSON rules | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 9.250s |

## Per-Problem Details

| Prompt | Problem | Model | Expected | Predicted | Correct | Valid JSON | Line |
|---|---:|---|---:|---:|---|---|---:|
| v1 | 1 | gemini-3.5-flash | 18 | 10 | no | yes | 1 |
| v1 | 2 | gemini-3.5-flash | 8 | 8 | yes | yes | 2 |
| v1 | 3 | gemini-3.5-flash | 140 | 140 | yes | yes | 3 |
| v1 | 4 | gemini-3.5-flash | 600 | 600 | yes | yes | 4 |
| v1 | 5 | gemini-3.5-flash | 3 | 3 | yes | yes | 5 |
| v1 | 6 | gemini-3.5-flash | 60 | 60 | yes | yes | 6 |
| v1 | 7 | gemini-3.5-flash | 91 | 91 | yes | yes | 7 |
| v1 | 8 | gemini-3.5-flash | 360 | 360 | yes | yes | 8 |
| v1 | 9 | gemini-3.5-flash | 8 | 8 | yes | yes | 9 |
| v1 | 10 | gemini-3.5-flash | 34 | 34 | yes | yes | 10 |
| v2 | 1 | gemini-3.5-flash | 18 | 10 | no | yes | 11 |
| v2 | 2 | gemini-3.5-flash | 8 | 8 | yes | yes | 12 |
| v2 | 3 | gemini-3.5-flash | 140 | 140 | yes | yes | 13 |
| v2 | 4 | gemini-3.5-flash | 600 | 600 | yes | yes | 14 |
| v2 | 5 | gemini-3.5-flash | 3 | 3 | yes | yes | 15 |
| v2 | 6 | gemini-3.5-flash | 60 | 60 | yes | yes | 16 |
| v2 | 7 | gemini-3.5-flash | 91 | 91 | yes | yes | 17 |
| v2 | 8 | gemini-3.5-flash | 360 | 360 | yes | yes | 18 |
| v2 | 9 | gemini-3.5-flash | 8 | 8 | yes | yes | 19 |
| v2 | 10 | gemini-3.5-flash | 34 | 34 | yes | yes | 20 |
| v3 | 1 | gemini-3.5-flash | 18 | 10 | no | yes | 21 |
| v3 | 2 | gemini-3.5-flash | 8 | 8 | yes | yes | 22 |
| v3 | 3 | gemini-3.5-flash | 140 | 140 | yes | yes | 23 |
| v3 | 4 | gemini-3.5-flash | 600 | 600 | yes | yes | 24 |
| v3 | 5 | gemini-3.5-flash | 3 | 3 | yes | yes | 25 |
| v3 | 6 | gemini-3.5-flash | 60 | 60 | yes | yes | 26 |
| v3 | 7 | gemini-3.5-flash | 91 | 91 | yes | yes | 27 |
| v3 | 8 | gemini-3.5-flash | 360 | 360 | yes | yes | 28 |
| v3 | 9 | gemini-3.5-flash | 8 | 8 | yes | yes | 29 |
| v3 | 10 | gemini-3.5-flash | 34 | 34 | yes | yes | 30 |
| v4 | 1 | gemini-3.5-flash | 18 | 18 | yes | yes | 31 |
| v4 | 2 | gemini-3.5-flash | 8 | 8 | yes | yes | 32 |
| v4 | 3 | gemini-3.5-flash | 140 | 140 | yes | yes | 33 |
| v4 | 4 | gemini-3.5-flash | 600 | 600 | yes | yes | 34 |
| v4 | 5 | gemini-3.5-flash | 3 | 3 | yes | yes | 35 |
| v4 | 6 | gemini-3.5-flash | 60 | 60 | yes | yes | 36 |
| v4 | 7 | gemini-3.5-flash | 91 | 91 | yes | yes | 37 |
| v4 | 8 | gemini-3.5-flash | 360 | 360 | yes | yes | 38 |
| v4 | 9 | gemini-3.5-flash | 8 | 8 | yes | yes | 39 |
| v4 | 10 | gemini-3.5-flash | 34 | 34 | yes | yes | 40 |
| v5 | 1 | gemini-3.5-flash | 18 | 10 | no | yes | 41 |
| v5 | 2 | gemini-3.5-flash | 8 | 8 | yes | yes | 42 |
| v5 | 3 | gemini-3.5-flash | 140 | 140 | yes | yes | 43 |
| v5 | 4 | gemini-3.5-flash | 600 | 600 | yes | yes | 44 |
| v5 | 5 | gemini-3.5-flash | 3 | 3 | yes | yes | 45 |
| v5 | 6 | gemini-3.5-flash | 60 | 60 | yes | yes | 46 |
| v5 | 7 | gemini-3.5-flash | 91 | 91 | yes | yes | 47 |
| v5 | 8 | gemini-3.5-flash | 360 | 120 | no | yes | 48 |
| v5 | 9 | gemini-3.5-flash | 8 | 8 | yes | yes | 49 |
| v5 | 10 | gemini-3.5-flash | 34 | 34 | yes | yes | 50 |
