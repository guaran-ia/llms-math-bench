# Prompt Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_azure_v7.jsonl`
- Attempts read: 60
- Attempts evaluated for ranking: 60
- Invalid JSONL lines: 0
- Best combination: **azure / gpt-5.4-mini / v7** (5/10)

## Ranking by Prompt

| Rank | Provider | Model | Prompt | Name | Correct answers | Accuracy | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | azure | gpt-5.4-mini | v7 | Bilingual teacher with glossary and warmup | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 3.780s |
| 2 | azure | Mistral-Large-3 | v7 | Bilingual teacher with glossary and warmup | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 13.063s |
| 3 | azure | Llama-3.3-70B-Instruct | v7 | Bilingual teacher with glossary and warmup | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 3.722s |
| 4 | azure | gpt-4o-mini | v7 | Bilingual teacher with glossary and warmup | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 4.678s |
| 5 | azure | grok-4-1-fast-non-reasoning | v7 | Bilingual teacher with glossary and warmup | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 4.945s |
| 6 | azure | gpt-4.1 | v7 | Bilingual teacher with glossary and warmup | 4/10 | 40.0% | 9/10 | 9/10 | 0 | 1 | 3.698s |

## Per-Problem Details

| Prompt | Problem | Model | Expected | Predicted | Correct | Valid JSON | Line |
|---|---:|---|---:|---:|---|---|---:|
| v7 | 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | yes | 6 |
| v7 | 1 | Mistral-Large-3 | 18 | 10 | no | yes | 5 |
| v7 | 1 | gpt-4.1 | 18 | 10 | no | yes | 2 |
| v7 | 1 | gpt-4o-mini | 18 | 10 | no | yes | 3 |
| v7 | 1 | gpt-5.4-mini | 18 | 10 | no | yes | 1 |
| v7 | 1 | grok-4-1-fast-non-reasoning | 18 | 10 | no | yes | 4 |
| v7 | 2 | Llama-3.3-70B-Instruct | 8 | 8 | yes | yes | 12 |
| v7 | 2 | Mistral-Large-3 | 8 | 8 | yes | yes | 11 |
| v7 | 2 | gpt-4.1 | 8 | 8 | yes | yes | 8 |
| v7 | 2 | gpt-4o-mini | 8 | 8 | yes | yes | 9 |
| v7 | 2 | gpt-5.4-mini | 8 | 8 | yes | yes | 7 |
| v7 | 2 | grok-4-1-fast-non-reasoning | 8 | 8 | yes | yes | 10 |
| v7 | 3 | Llama-3.3-70B-Instruct | 140 | 140 | yes | yes | 18 |
| v7 | 3 | Mistral-Large-3 | 140 | 140 | yes | yes | 17 |
| v7 | 3 | gpt-4.1 | 140 | 140 | yes | yes | 14 |
| v7 | 3 | gpt-4o-mini | 140 | 140 | yes | yes | 15 |
| v7 | 3 | gpt-5.4-mini | 140 | 140 | yes | yes | 13 |
| v7 | 3 | grok-4-1-fast-non-reasoning | 140 | 140 | yes | yes | 16 |
| v7 | 4 | Llama-3.3-70B-Instruct | 600 | 600 | yes | yes | 24 |
| v7 | 4 | Mistral-Large-3 | 600 | 600 | yes | yes | 23 |
| v7 | 4 | gpt-4.1 | 600 | 600 | yes | yes | 20 |
| v7 | 4 | gpt-4o-mini | 600 | 67 | no | yes | 21 |
| v7 | 4 | gpt-5.4-mini | 600 | 600 | yes | yes | 19 |
| v7 | 4 | grok-4-1-fast-non-reasoning | 600 | 600 | yes | yes | 22 |
| v7 | 5 | Llama-3.3-70B-Instruct | 3 | 1 | no | yes | 30 |
| v7 | 5 | Mistral-Large-3 | 3 | 11 | no | yes | 29 |
| v7 | 5 | gpt-4.1 | 3 | 10 | no | yes | 26 |
| v7 | 5 | gpt-4o-mini | 3 | 3 | yes | yes | 27 |
| v7 | 5 | gpt-5.4-mini | 3 | 5 | no | yes | 25 |
| v7 | 5 | grok-4-1-fast-non-reasoning | 3 | 217 | no | yes | 28 |
| v7 | 6 | Llama-3.3-70B-Instruct | 60 | 21 | no | yes | 36 |
| v7 | 6 | Mistral-Large-3 | 60 | 8 | no | yes | 35 |
| v7 | 6 | gpt-4.1 | 60 | 21 | no | yes | 32 |
| v7 | 6 | gpt-4o-mini | 60 | 6 | no | yes | 33 |
| v7 | 6 | gpt-5.4-mini | 60 | 420 | no | yes | 31 |
| v7 | 6 | grok-4-1-fast-non-reasoning | 60 | 32 | no | yes | 34 |
| v7 | 7 | Llama-3.3-70B-Instruct | 91 | 49 | no | yes | 42 |
| v7 | 7 | Mistral-Large-3 | 91 | 35 | no | yes | 41 |
| v7 | 7 | gpt-4.1 | 91 | 91 | yes | yes | 38 |
| v7 | 7 | gpt-4o-mini | 91 | 35 | no | yes | 39 |
| v7 | 7 | gpt-5.4-mini | 91 | 49 | no | yes | 37 |
| v7 | 7 | grok-4-1-fast-non-reasoning | 91 | 15 | no | yes | 40 |
| v7 | 8 | Llama-3.3-70B-Instruct | 360 | 66 | no | yes | 48 |
| v7 | 8 | Mistral-Large-3 | 360 | 120 | no | yes | 47 |
| v7 | 8 | gpt-4.1 | 360 | 120 | no | yes | 44 |
| v7 | 8 | gpt-4o-mini | 360 | 120 | no | yes | 45 |
| v7 | 8 | gpt-5.4-mini | 360 | 120 | no | yes | 43 |
| v7 | 8 | grok-4-1-fast-non-reasoning | 360 | 180 | no | yes | 46 |
| v7 | 9 | Llama-3.3-70B-Instruct | 8 | 5 | no | yes | 54 |
| v7 | 9 | Mistral-Large-3 | 8 | 8 | yes | yes | 53 |
| v7 | 9 | gpt-4.1 | 8 | 4 | no | yes | 50 |
| v7 | 9 | gpt-4o-mini | 8 | 3 | no | yes | 51 |
| v7 | 9 | gpt-5.4-mini | 8 | 8 | yes | yes | 49 |
| v7 | 9 | grok-4-1-fast-non-reasoning | 8 | 5 | no | yes | 52 |
| v7 | 10 | Llama-3.3-70B-Instruct | 34 | 34 | yes | yes | 60 |
| v7 | 10 | Mistral-Large-3 | 34 | 34 | yes | yes | 59 |
| v7 | 10 | gpt-4.1 | 34 | None | no | no | 56 |
| v7 | 10 | gpt-4o-mini | 34 | 34 | yes | yes | 57 |
| v7 | 10 | gpt-5.4-mini | 34 | 34 | yes | yes | 55 |
| v7 | 10 | grok-4-1-fast-non-reasoning | 34 | 34 | yes | yes | 58 |
