# Prompt Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_azure_v6.jsonl`
- Attempts read: 60
- Attempts evaluated for ranking: 60
- Invalid JSONL lines: 0
- Best combination: **azure / Llama-3.3-70B-Instruct / v6** (5/10)

## Ranking by Prompt

| Rank | Provider | Model | Prompt | Name | Correct answers | Accuracy | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | azure | Llama-3.3-70B-Instruct | v6 | Strict Guaraní with reinforced JSON rules and warmup | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 3.345s |
| 2 | azure | gpt-5.4-mini | v6 | Strict Guaraní with reinforced JSON rules and warmup | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 3.577s |
| 3 | azure | gpt-4.1 | v6 | Strict Guaraní with reinforced JSON rules and warmup | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 2.694s |
| 4 | azure | grok-4-1-fast-non-reasoning | v6 | Strict Guaraní with reinforced JSON rules and warmup | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 3.954s |
| 5 | azure | gpt-4o-mini | v6 | Strict Guaraní with reinforced JSON rules and warmup | 2/10 | 20.0% | 10/10 | 10/10 | 0 | 0 | 3.238s |
| 6 | azure | Mistral-Large-3 | v6 | Strict Guaraní with reinforced JSON rules and warmup | 0/10 | 0.0% | 0/10 | 10/10 | 0 | 10 | 4.606s |

## Per-Problem Details

| Prompt | Problem | Model | Expected | Predicted | Correct | Valid JSON | Line |
|---|---:|---|---:|---:|---|---|---:|
| v6 | 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | yes | 6 |
| v6 | 1 | Mistral-Large-3 | 18 | 10 | no | no | 5 |
| v6 | 1 | gpt-4.1 | 18 | 10 | no | yes | 2 |
| v6 | 1 | gpt-4o-mini | 18 | 6 | no | yes | 3 |
| v6 | 1 | gpt-5.4-mini | 18 | 6 | no | yes | 1 |
| v6 | 1 | grok-4-1-fast-non-reasoning | 18 | 6 | no | yes | 4 |
| v6 | 2 | Llama-3.3-70B-Instruct | 8 | 8 | yes | yes | 12 |
| v6 | 2 | Mistral-Large-3 | 8 | 8 | no | no | 11 |
| v6 | 2 | gpt-4.1 | 8 | 8 | yes | yes | 8 |
| v6 | 2 | gpt-4o-mini | 8 | 11 | no | yes | 9 |
| v6 | 2 | gpt-5.4-mini | 8 | 8 | yes | yes | 7 |
| v6 | 2 | grok-4-1-fast-non-reasoning | 8 | 8 | yes | yes | 10 |
| v6 | 3 | Llama-3.3-70B-Instruct | 140 | 140 | yes | yes | 18 |
| v6 | 3 | Mistral-Large-3 | 140 | 140 | no | no | 17 |
| v6 | 3 | gpt-4.1 | 140 | 140 | yes | yes | 14 |
| v6 | 3 | gpt-4o-mini | 140 | 140 | yes | yes | 15 |
| v6 | 3 | gpt-5.4-mini | 140 | 140 | yes | yes | 13 |
| v6 | 3 | grok-4-1-fast-non-reasoning | 140 | 140 | yes | yes | 16 |
| v6 | 4 | Llama-3.3-70B-Instruct | 600 | 600 | yes | yes | 24 |
| v6 | 4 | Mistral-Large-3 | 600 | 600 | no | no | 23 |
| v6 | 4 | gpt-4.1 | 600 | 600 | yes | yes | 20 |
| v6 | 4 | gpt-4o-mini | 600 | 67 | no | yes | 21 |
| v6 | 4 | gpt-5.4-mini | 600 | 24 | no | yes | 19 |
| v6 | 4 | grok-4-1-fast-non-reasoning | 600 | 600 | yes | yes | 22 |
| v6 | 5 | Llama-3.3-70B-Instruct | 3 | 1 | no | yes | 30 |
| v6 | 5 | Mistral-Large-3 | 3 | 33 | no | no | 29 |
| v6 | 5 | gpt-4.1 | 3 | 10 | no | yes | 26 |
| v6 | 5 | gpt-4o-mini | 3 | 5 | no | yes | 27 |
| v6 | 5 | gpt-5.4-mini | 3 | 5 | no | yes | 25 |
| v6 | 5 | grok-4-1-fast-non-reasoning | 3 | 210 | no | yes | 28 |
| v6 | 6 | Llama-3.3-70B-Instruct | 60 | 3 | no | yes | 36 |
| v6 | 6 | Mistral-Large-3 | 60 | 4 | no | no | 35 |
| v6 | 6 | gpt-4.1 | 60 | 28 | no | yes | 32 |
| v6 | 6 | gpt-4o-mini | 60 | 4 | no | yes | 33 |
| v6 | 6 | gpt-5.4-mini | 60 | 60 | yes | yes | 31 |
| v6 | 6 | grok-4-1-fast-non-reasoning | 60 | 2 | no | yes | 34 |
| v6 | 7 | Llama-3.3-70B-Instruct | 91 | 45 | no | yes | 42 |
| v6 | 7 | Mistral-Large-3 | 91 | 45 | no | no | 41 |
| v6 | 7 | gpt-4.1 | 91 | 28 | no | yes | 38 |
| v6 | 7 | gpt-4o-mini | 91 | 7 | no | yes | 39 |
| v6 | 7 | gpt-5.4-mini | 91 | 28 | no | yes | 37 |
| v6 | 7 | grok-4-1-fast-non-reasoning | 91 | 25 | no | yes | 40 |
| v6 | 8 | Llama-3.3-70B-Instruct | 360 | 30 | no | yes | 48 |
| v6 | 8 | Mistral-Large-3 | 360 | 120 | no | no | 47 |
| v6 | 8 | gpt-4.1 | 360 | 120 | no | yes | 44 |
| v6 | 8 | gpt-4o-mini | 360 | 180 | no | yes | 45 |
| v6 | 8 | gpt-5.4-mini | 360 | 120 | no | yes | 43 |
| v6 | 8 | grok-4-1-fast-non-reasoning | 360 | 180 | no | yes | 46 |
| v6 | 9 | Llama-3.3-70B-Instruct | 8 | 8 | yes | yes | 54 |
| v6 | 9 | Mistral-Large-3 | 8 | 7 | no | no | 53 |
| v6 | 9 | gpt-4.1 | 8 | 7 | no | yes | 50 |
| v6 | 9 | gpt-4o-mini | 8 | 3 | no | yes | 51 |
| v6 | 9 | gpt-5.4-mini | 8 | 8 | yes | yes | 49 |
| v6 | 9 | grok-4-1-fast-non-reasoning | 8 | 1 | no | yes | 52 |
| v6 | 10 | Llama-3.3-70B-Instruct | 34 | 34 | yes | yes | 60 |
| v6 | 10 | Mistral-Large-3 | 34 | 34 | no | no | 59 |
| v6 | 10 | gpt-4.1 | 34 | 34 | yes | yes | 56 |
| v6 | 10 | gpt-4o-mini | 34 | 34 | yes | yes | 57 |
| v6 | 10 | gpt-5.4-mini | 34 | 34 | yes | yes | 55 |
| v6 | 10 | grok-4-1-fast-non-reasoning | 34 | 34 | yes | yes | 58 |
