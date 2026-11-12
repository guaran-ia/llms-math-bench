# Prompt Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_azure_v9.jsonl`
- Attempts read: 60
- Attempts evaluated for ranking: 60
- Invalid JSONL lines: 0
- Best combination: **azure / Llama-3.3-70B-Instruct / v9** (3/10)

## Ranking by Prompt

| Rank | Provider | Model | Prompt | Name | Correct answers | Accuracy | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | azure | Llama-3.3-70B-Instruct | v9 | Simple few-shot autocomplete | 3/10 | 30.0% | 0/10 | 0/10 | 0 | 0 | 0.604s |
| 2 | azure | Mistral-Large-3 | v9 | Simple few-shot autocomplete | 3/10 | 30.0% | 0/10 | 0/10 | 0 | 0 | 0.736s |
| 3 | azure | gpt-4o-mini | v9 | Simple few-shot autocomplete | 3/10 | 30.0% | 0/10 | 0/10 | 0 | 1 | 0.991s |
| 4 | azure | gpt-4.1 | v9 | Simple few-shot autocomplete | 3/10 | 30.0% | 0/10 | 0/10 | 0 | 0 | 1.219s |
| 5 | azure | gpt-5.4-mini | v9 | Simple few-shot autocomplete | 3/10 | 30.0% | 0/10 | 0/10 | 0 | 0 | 1.435s |
| 6 | azure | grok-4-1-fast-non-reasoning | v9 | Simple few-shot autocomplete | 1/10 | 10.0% | 0/10 | 0/10 | 0 | 0 | 0.637s |

## Per-Problem Details

| Prompt | Problem | Model | Expected | Predicted | Correct | Valid JSON | Line |
|---|---:|---|---:|---:|---|---|---:|
| v9 | 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | no | 6 |
| v9 | 1 | Mistral-Large-3 | 18 | 10 | no | no | 5 |
| v9 | 1 | gpt-4.1 | 18 | 6 | no | no | 2 |
| v9 | 1 | gpt-4o-mini | 18 | 6 | no | no | 3 |
| v9 | 1 | gpt-5.4-mini | 18 | 10 | no | no | 1 |
| v9 | 1 | grok-4-1-fast-non-reasoning | 18 | 12 | no | no | 4 |
| v9 | 2 | Llama-3.3-70B-Instruct | 8 | 8 | yes | no | 12 |
| v9 | 2 | Mistral-Large-3 | 8 | 8 | yes | no | 11 |
| v9 | 2 | gpt-4.1 | 8 | 8 | yes | no | 8 |
| v9 | 2 | gpt-4o-mini | 8 | 8 | yes | no | 9 |
| v9 | 2 | gpt-5.4-mini | 8 | 8 | yes | no | 7 |
| v9 | 2 | grok-4-1-fast-non-reasoning | 8 | 8 | yes | no | 10 |
| v9 | 3 | Llama-3.3-70B-Instruct | 140 | 140 | yes | no | 18 |
| v9 | 3 | Mistral-Large-3 | 140 | 140 | yes | no | 17 |
| v9 | 3 | gpt-4.1 | 140 | 140 | yes | no | 14 |
| v9 | 3 | gpt-4o-mini | 140 | 140 | yes | no | 15 |
| v9 | 3 | gpt-5.4-mini | 140 | 140 | yes | no | 13 |
| v9 | 3 | grok-4-1-fast-non-reasoning | 140 | 28 | no | no | 16 |
| v9 | 4 | Llama-3.3-70B-Instruct | 600 | 600 | yes | no | 24 |
| v9 | 4 | Mistral-Large-3 | 600 | 600 | yes | no | 23 |
| v9 | 4 | gpt-4.1 | 600 | 600 | yes | no | 20 |
| v9 | 4 | gpt-4o-mini | 600 | 17 | no | no | 21 |
| v9 | 4 | gpt-5.4-mini | 600 | 600 | yes | no | 19 |
| v9 | 4 | grok-4-1-fast-non-reasoning | 600 | 64 | no | no | 22 |
| v9 | 5 | Llama-3.3-70B-Instruct | 3 | 2 | no | no | 30 |
| v9 | 5 | Mistral-Large-3 | 3 | 10 | no | no | 29 |
| v9 | 5 | gpt-4.1 | 3 | 5 | no | no | 26 |
| v9 | 5 | gpt-4o-mini | 3 | 7 | no | no | 27 |
| v9 | 5 | gpt-5.4-mini | 3 | 7 | no | no | 25 |
| v9 | 5 | grok-4-1-fast-non-reasoning | 3 | 7 | no | no | 28 |
| v9 | 6 | Llama-3.3-70B-Instruct | 60 | 120 | no | no | 36 |
| v9 | 6 | Mistral-Large-3 | 60 | 3 | no | no | 35 |
| v9 | 6 | gpt-4.1 | 60 | 80 | no | no | 32 |
| v9 | 6 | gpt-4o-mini | 60 | 6 | no | no | 33 |
| v9 | 6 | gpt-5.4-mini | 60 | 40 | no | no | 31 |
| v9 | 6 | grok-4-1-fast-non-reasoning | 60 | 29 | no | no | 34 |
| v9 | 7 | Llama-3.3-70B-Instruct | 91 | 71 | no | no | 42 |
| v9 | 7 | Mistral-Large-3 | 91 | 25 | no | no | 41 |
| v9 | 7 | gpt-4.1 | 91 | 42 | no | no | 38 |
| v9 | 7 | gpt-4o-mini | 91 | 10 | no | no | 39 |
| v9 | 7 | gpt-5.4-mini | 91 | 7 | no | no | 37 |
| v9 | 7 | grok-4-1-fast-non-reasoning | 91 | 70 | no | no | 40 |
| v9 | 8 | Llama-3.3-70B-Instruct | 360 | 8 | no | no | 48 |
| v9 | 8 | Mistral-Large-3 | 360 | 180 | no | no | 47 |
| v9 | 8 | gpt-4.1 | 360 | 120 | no | no | 44 |
| v9 | 8 | gpt-4o-mini | 360 | 180 | no | no | 45 |
| v9 | 8 | gpt-5.4-mini | 360 | 120 | no | no | 43 |
| v9 | 8 | grok-4-1-fast-non-reasoning | 360 | 52 | no | no | 46 |
| v9 | 9 | Llama-3.3-70B-Instruct | 8 | 7 | no | no | 54 |
| v9 | 9 | Mistral-Large-3 | 8 | 5 | no | no | 53 |
| v9 | 9 | gpt-4.1 | 8 | 7 | no | no | 50 |
| v9 | 9 | gpt-4o-mini | 8 | 2 | no | no | 51 |
| v9 | 9 | gpt-5.4-mini | 8 | 2 | no | no | 49 |
| v9 | 9 | grok-4-1-fast-non-reasoning | 8 | 29 | no | no | 52 |
| v9 | 10 | Llama-3.3-70B-Instruct | 34 | 32 | no | no | 60 |
| v9 | 10 | Mistral-Large-3 | 34 | 29.5 | no | no | 59 |
| v9 | 10 | gpt-4.1 | 34 | 35 | no | no | 56 |
| v9 | 10 | gpt-4o-mini | 34 | 34 | yes | no | 57 |
| v9 | 10 | gpt-5.4-mini | 34 | 32 | no | no | 55 |
| v9 | 10 | grok-4-1-fast-non-reasoning | 34 | 17 | no | no | 58 |
