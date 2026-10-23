# Prompt Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_gemini_3.5_live_translate_preview.jsonl`
- Attempts read: 50
- Attempts evaluated for ranking: 50
- Invalid JSONL lines: 0
- Best combination: **gemini / gemini-3.5-live-translate-preview / v3** (0/10)

## Ranking by Prompt

| Rank | Provider | Model | Prompt | Name | Correct answers | Accuracy | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | gemini | gemini-3.5-live-translate-preview | v3 | Bilingual teacher with semantic interpretation | 0/10 | 0.0% | 0/10 | 0/10 | 10 | 0 | 0.417s |
| 2 | gemini | gemini-3.5-live-translate-preview | v4 | Bilingual teacher with glossary | 0/10 | 0.0% | 0/10 | 0/10 | 10 | 0 | 0.420s |
| 3 | gemini | gemini-3.5-live-translate-preview | v2 | Internal translation into Spanish | 0/10 | 0.0% | 0/10 | 0/10 | 10 | 0 | 0.423s |
| 4 | gemini | gemini-3.5-live-translate-preview | v5 | Strict Guaraní with reinforced JSON rules | 0/10 | 0.0% | 0/10 | 0/10 | 10 | 0 | 0.541s |
| 5 | gemini | gemini-3.5-live-translate-preview | v1 | Strict Guaraní | 0/10 | 0.0% | 0/10 | 0/10 | 10 | 0 | 0.920s |

## Per-Problem Details

| Prompt | Problem | Model | Expected | Predicted | Correct | Valid JSON | Line |
|---|---:|---|---:|---:|---|---|---:|
| v1 | 1 | gemini-3.5-live-translate-preview | 18 | None | no | no | 1 |
| v1 | 2 | gemini-3.5-live-translate-preview | 8 | None | no | no | 2 |
| v1 | 3 | gemini-3.5-live-translate-preview | 140 | None | no | no | 3 |
| v1 | 4 | gemini-3.5-live-translate-preview | 600 | None | no | no | 4 |
| v1 | 5 | gemini-3.5-live-translate-preview | 3 | None | no | no | 5 |
| v1 | 6 | gemini-3.5-live-translate-preview | 60 | None | no | no | 6 |
| v1 | 7 | gemini-3.5-live-translate-preview | 91 | None | no | no | 7 |
| v1 | 8 | gemini-3.5-live-translate-preview | 360 | None | no | no | 8 |
| v1 | 9 | gemini-3.5-live-translate-preview | 8 | None | no | no | 9 |
| v1 | 10 | gemini-3.5-live-translate-preview | 34 | None | no | no | 10 |
| v2 | 1 | gemini-3.5-live-translate-preview | 18 | None | no | no | 11 |
| v2 | 2 | gemini-3.5-live-translate-preview | 8 | None | no | no | 12 |
| v2 | 3 | gemini-3.5-live-translate-preview | 140 | None | no | no | 13 |
| v2 | 4 | gemini-3.5-live-translate-preview | 600 | None | no | no | 14 |
| v2 | 5 | gemini-3.5-live-translate-preview | 3 | None | no | no | 15 |
| v2 | 6 | gemini-3.5-live-translate-preview | 60 | None | no | no | 16 |
| v2 | 7 | gemini-3.5-live-translate-preview | 91 | None | no | no | 17 |
| v2 | 8 | gemini-3.5-live-translate-preview | 360 | None | no | no | 18 |
| v2 | 9 | gemini-3.5-live-translate-preview | 8 | None | no | no | 19 |
| v2 | 10 | gemini-3.5-live-translate-preview | 34 | None | no | no | 20 |
| v3 | 1 | gemini-3.5-live-translate-preview | 18 | None | no | no | 21 |
| v3 | 2 | gemini-3.5-live-translate-preview | 8 | None | no | no | 22 |
| v3 | 3 | gemini-3.5-live-translate-preview | 140 | None | no | no | 23 |
| v3 | 4 | gemini-3.5-live-translate-preview | 600 | None | no | no | 24 |
| v3 | 5 | gemini-3.5-live-translate-preview | 3 | None | no | no | 25 |
| v3 | 6 | gemini-3.5-live-translate-preview | 60 | None | no | no | 26 |
| v3 | 7 | gemini-3.5-live-translate-preview | 91 | None | no | no | 27 |
| v3 | 8 | gemini-3.5-live-translate-preview | 360 | None | no | no | 28 |
| v3 | 9 | gemini-3.5-live-translate-preview | 8 | None | no | no | 29 |
| v3 | 10 | gemini-3.5-live-translate-preview | 34 | None | no | no | 30 |
| v4 | 1 | gemini-3.5-live-translate-preview | 18 | None | no | no | 31 |
| v4 | 2 | gemini-3.5-live-translate-preview | 8 | None | no | no | 32 |
| v4 | 3 | gemini-3.5-live-translate-preview | 140 | None | no | no | 33 |
| v4 | 4 | gemini-3.5-live-translate-preview | 600 | None | no | no | 34 |
| v4 | 5 | gemini-3.5-live-translate-preview | 3 | None | no | no | 35 |
| v4 | 6 | gemini-3.5-live-translate-preview | 60 | None | no | no | 36 |
| v4 | 7 | gemini-3.5-live-translate-preview | 91 | None | no | no | 37 |
| v4 | 8 | gemini-3.5-live-translate-preview | 360 | None | no | no | 38 |
| v4 | 9 | gemini-3.5-live-translate-preview | 8 | None | no | no | 39 |
| v4 | 10 | gemini-3.5-live-translate-preview | 34 | None | no | no | 40 |
| v5 | 1 | gemini-3.5-live-translate-preview | 18 | None | no | no | 41 |
| v5 | 2 | gemini-3.5-live-translate-preview | 8 | None | no | no | 42 |
| v5 | 3 | gemini-3.5-live-translate-preview | 140 | None | no | no | 43 |
| v5 | 4 | gemini-3.5-live-translate-preview | 600 | None | no | no | 44 |
| v5 | 5 | gemini-3.5-live-translate-preview | 3 | None | no | no | 45 |
| v5 | 6 | gemini-3.5-live-translate-preview | 60 | None | no | no | 46 |
| v5 | 7 | gemini-3.5-live-translate-preview | 91 | None | no | no | 47 |
| v5 | 8 | gemini-3.5-live-translate-preview | 360 | None | no | no | 48 |
| v5 | 9 | gemini-3.5-live-translate-preview | 8 | None | no | no | 49 |
| v5 | 10 | gemini-3.5-live-translate-preview | 34 | None | no | no | 50 |
