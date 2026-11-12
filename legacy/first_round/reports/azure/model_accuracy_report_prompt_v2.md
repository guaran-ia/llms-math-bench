# Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_guarani_prompt_v2.jsonl`
- Attempts read: 60
- Attempts evaluated for ranking: 60
- Unique problems evaluated: 10
- Invalid JSONL lines: 0
- Most accurate model: **gpt-4.1**

The main ranking uses the latest available attempt for each `(model, problem_id)` pair to avoid counting repeated problems twice.

## Main Ranking

| Rank | Model | Strict correct answers | Strict accuracy | Recovered correct answers | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | gpt-4.1 | 5/10 | 50.0% | 5/10 | 10/10 | 10/10 | 0 | 0 | 2.791s |
| 2 | Mistral-Large-3 | 5/10 | 50.0% | 5/10 | 10/10 | 10/10 | 0 | 0 | 5.099s |
| 3 | Llama-3.3-70B-Instruct | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 2.557s |
| 4 | gpt-5.4-mini | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 2.788s |
| 5 | gpt-4o-mini | 2/10 | 20.0% | 2/10 | 10/10 | 10/10 | 0 | 0 | 3.025s |
| 6 | grok-4-1-fast-non-reasoning | 2/10 | 20.0% | 2/10 | 9/10 | 9/10 | 0 | 1 | 13.146s |

## Per-Problem Details

| Problem | Model | Expected | Predicted | Strict | Recovered | Valid JSON | Line |
|---:|---|---:|---:|---|---|---|---:|
| 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | no | yes | 6 |
| 1 | Mistral-Large-3 | 18 | 10 | no | no | yes | 5 |
| 1 | gpt-4.1 | 18 | 10 | no | no | yes | 2 |
| 1 | gpt-4o-mini | 18 | 10 | no | no | yes | 3 |
| 1 | gpt-5.4-mini | 18 | 10 | no | no | yes | 1 |
| 1 | grok-4-1-fast-non-reasoning | 18 | 6 | no | no | yes | 4 |
| 2 | Llama-3.3-70B-Instruct | 8 | 7 | no | no | yes | 12 |
| 2 | Mistral-Large-3 | 8 | 20 | no | no | yes | 11 |
| 2 | gpt-4.1 | 8 | 8 | yes | yes | yes | 8 |
| 2 | gpt-4o-mini | 8 | 7 | no | no | yes | 9 |
| 2 | gpt-5.4-mini | 8 | 14 | no | no | yes | 7 |
| 2 | grok-4-1-fast-non-reasoning | 8 | 7 | no | no | yes | 10 |
| 3 | Llama-3.3-70B-Instruct | 140 | 140 | yes | yes | yes | 18 |
| 3 | Mistral-Large-3 | 140 | 140 | yes | yes | yes | 17 |
| 3 | gpt-4.1 | 140 | 140 | yes | yes | yes | 14 |
| 3 | gpt-4o-mini | 140 | 140 | yes | yes | yes | 15 |
| 3 | gpt-5.4-mini | 140 | 140 | yes | yes | yes | 13 |
| 3 | grok-4-1-fast-non-reasoning | 140 | 2 | no | no | yes | 16 |
| 4 | Llama-3.3-70B-Instruct | 600 | 600 | yes | yes | yes | 24 |
| 4 | Mistral-Large-3 | 600 | 600 | yes | yes | yes | 23 |
| 4 | gpt-4.1 | 600 | 600 | yes | yes | yes | 20 |
| 4 | gpt-4o-mini | 600 | 67 | no | no | yes | 21 |
| 4 | gpt-5.4-mini | 600 | 600 | yes | yes | yes | 19 |
| 4 | grok-4-1-fast-non-reasoning | 600 | 600 | yes | yes | yes | 22 |
| 5 | Llama-3.3-70B-Instruct | 3 | 2 | no | no | yes | 30 |
| 5 | Mistral-Large-3 | 3 | 90 | no | no | yes | 29 |
| 5 | gpt-4.1 | 3 | 1 | no | no | yes | 26 |
| 5 | gpt-4o-mini | 3 | 9 | no | no | yes | 27 |
| 5 | gpt-5.4-mini | 3 | 5 | no | no | yes | 25 |
| 5 | grok-4-1-fast-non-reasoning | 3 | 175 | no | no | yes | 28 |
| 6 | Llama-3.3-70B-Instruct | 60 | 3 | no | no | yes | 36 |
| 6 | Mistral-Large-3 | 60 | 5 | no | no | yes | 35 |
| 6 | gpt-4.1 | 60 | 28 | no | no | yes | 32 |
| 6 | gpt-4o-mini | 60 | 5 | no | no | yes | 33 |
| 6 | gpt-5.4-mini | 60 | 40 | no | no | yes | 31 |
| 6 | grok-4-1-fast-non-reasoning | 60 | None | no | no | no | 34 |
| 7 | Llama-3.3-70B-Instruct | 91 | 35 | no | no | yes | 42 |
| 7 | Mistral-Large-3 | 91 | 27 | no | no | yes | 41 |
| 7 | gpt-4.1 | 91 | 70 | no | no | yes | 38 |
| 7 | gpt-4o-mini | 91 | 7 | no | no | yes | 39 |
| 7 | gpt-5.4-mini | 91 | 35 | no | no | yes | 37 |
| 7 | grok-4-1-fast-non-reasoning | 91 | 10 | no | no | yes | 40 |
| 8 | Llama-3.3-70B-Instruct | 360 | 30 | no | no | yes | 48 |
| 8 | Mistral-Large-3 | 360 | 360 | yes | yes | yes | 47 |
| 8 | gpt-4.1 | 360 | 120 | no | no | yes | 44 |
| 8 | gpt-4o-mini | 360 | 30 | no | no | yes | 45 |
| 8 | gpt-5.4-mini | 360 | 120 | no | no | yes | 43 |
| 8 | grok-4-1-fast-non-reasoning | 360 | 120 | no | no | yes | 46 |
| 9 | Llama-3.3-70B-Instruct | 8 | 8 | yes | yes | yes | 54 |
| 9 | Mistral-Large-3 | 8 | 8 | yes | yes | yes | 53 |
| 9 | gpt-4.1 | 8 | 8 | yes | yes | yes | 50 |
| 9 | gpt-4o-mini | 8 | 6 | no | no | yes | 51 |
| 9 | gpt-5.4-mini | 8 | 8 | yes | yes | yes | 49 |
| 9 | grok-4-1-fast-non-reasoning | 8 | 4 | no | no | yes | 52 |
| 10 | Llama-3.3-70B-Instruct | 34 | 34 | yes | yes | yes | 60 |
| 10 | Mistral-Large-3 | 34 | 34 | yes | yes | yes | 59 |
| 10 | gpt-4.1 | 34 | 34 | yes | yes | yes | 56 |
| 10 | gpt-4o-mini | 34 | 34 | yes | yes | yes | 57 |
| 10 | gpt-5.4-mini | 34 | 34 | yes | yes | yes | 55 |
| 10 | grok-4-1-fast-non-reasoning | 34 | 34 | yes | yes | yes | 58 |
