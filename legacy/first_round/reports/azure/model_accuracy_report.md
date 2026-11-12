# Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_guarani.jsonl`
- Attempts read: 126
- Attempts evaluated for ranking: 60
- Unique problems evaluated: 10
- Invalid JSONL lines: 0
- Most accurate model: **gpt-4.1**

The main ranking uses the latest available attempt for each `(model, problem_id)` pair to avoid counting repeated problems twice.

## Main Ranking

| Rank | Model | Strict correct answers | Strict accuracy | Recovered correct answers | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | gpt-4.1 | 6/10 | 60.0% | 6/10 | 10/10 | 10/10 | 0 | 0 | 2.340s |
| 2 | Mistral-Large-3 | 5/10 | 50.0% | 5/10 | 10/10 | 10/10 | 0 | 0 | 4.443s |
| 3 | Llama-3.3-70B-Instruct | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 2.684s |
| 4 | gpt-5.4-mini | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 2.898s |
| 5 | grok-4-1-fast-non-reasoning | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 4.117s |
| 6 | gpt-4o-mini | 2/10 | 20.0% | 2/10 | 10/10 | 10/10 | 0 | 0 | 2.829s |

## Per-Problem Details

| Problem | Model | Expected | Predicted | Strict | Recovered | Valid JSON | Line |
|---:|---|---:|---:|---|---|---|---:|
| 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | no | yes | 72 |
| 1 | Mistral-Large-3 | 18 | 10 | no | no | yes | 71 |
| 1 | gpt-4.1 | 18 | 10 | no | no | yes | 68 |
| 1 | gpt-4o-mini | 18 | 10 | no | no | yes | 69 |
| 1 | gpt-5.4-mini | 18 | 10 | no | no | yes | 67 |
| 1 | grok-4-1-fast-non-reasoning | 18 | 6 | no | no | yes | 70 |
| 2 | Llama-3.3-70B-Instruct | 8 | 20 | no | no | yes | 78 |
| 2 | Mistral-Large-3 | 8 | 20 | no | no | yes | 77 |
| 2 | gpt-4.1 | 8 | 8 | yes | yes | yes | 74 |
| 2 | gpt-4o-mini | 8 | 7 | no | no | yes | 75 |
| 2 | gpt-5.4-mini | 8 | 14 | no | no | yes | 73 |
| 2 | grok-4-1-fast-non-reasoning | 8 | 7 | no | no | yes | 76 |
| 3 | Llama-3.3-70B-Instruct | 140 | 140 | yes | yes | yes | 84 |
| 3 | Mistral-Large-3 | 140 | 140 | yes | yes | yes | 83 |
| 3 | gpt-4.1 | 140 | 140 | yes | yes | yes | 80 |
| 3 | gpt-4o-mini | 140 | 140 | yes | yes | yes | 81 |
| 3 | gpt-5.4-mini | 140 | 140 | yes | yes | yes | 79 |
| 3 | grok-4-1-fast-non-reasoning | 140 | 140 | yes | yes | yes | 82 |
| 4 | Llama-3.3-70B-Instruct | 600 | 600 | yes | yes | yes | 90 |
| 4 | Mistral-Large-3 | 600 | 600 | yes | yes | yes | 89 |
| 4 | gpt-4.1 | 600 | 600 | yes | yes | yes | 86 |
| 4 | gpt-4o-mini | 600 | 9 | no | no | yes | 87 |
| 4 | gpt-5.4-mini | 600 | 600 | yes | yes | yes | 85 |
| 4 | grok-4-1-fast-non-reasoning | 600 | 600 | yes | yes | yes | 88 |
| 5 | Llama-3.3-70B-Instruct | 3 | 2 | no | no | yes | 96 |
| 5 | Mistral-Large-3 | 3 | 60 | no | no | yes | 95 |
| 5 | gpt-4.1 | 3 | 1 | no | no | yes | 92 |
| 5 | gpt-4o-mini | 3 | 5 | no | no | yes | 93 |
| 5 | gpt-5.4-mini | 3 | 1 | no | no | yes | 91 |
| 5 | grok-4-1-fast-non-reasoning | 3 | 7 | no | no | yes | 94 |
| 6 | Llama-3.3-70B-Instruct | 60 | 5 | no | no | yes | 102 |
| 6 | Mistral-Large-3 | 60 | 4 | no | no | yes | 101 |
| 6 | gpt-4.1 | 60 | 40 | no | no | yes | 98 |
| 6 | gpt-4o-mini | 60 | 4 | no | no | yes | 99 |
| 6 | gpt-5.4-mini | 60 | 40 | no | no | yes | 97 |
| 6 | grok-4-1-fast-non-reasoning | 60 | 4 | no | no | yes | 100 |
| 7 | Llama-3.3-70B-Instruct | 91 | 30 | no | no | yes | 108 |
| 7 | Mistral-Large-3 | 91 | 43 | no | no | yes | 107 |
| 7 | gpt-4.1 | 91 | 91 | yes | yes | yes | 104 |
| 7 | gpt-4o-mini | 91 | 7 | no | no | yes | 105 |
| 7 | gpt-5.4-mini | 91 | 35 | no | no | yes | 103 |
| 7 | grok-4-1-fast-non-reasoning | 91 | 28 | no | no | yes | 106 |
| 8 | Llama-3.3-70B-Instruct | 360 | 20 | no | no | yes | 114 |
| 8 | Mistral-Large-3 | 360 | 360 | yes | yes | yes | 113 |
| 8 | gpt-4.1 | 360 | 120 | no | no | yes | 110 |
| 8 | gpt-4o-mini | 360 | 120 | no | no | yes | 111 |
| 8 | gpt-5.4-mini | 360 | 120 | no | no | yes | 109 |
| 8 | grok-4-1-fast-non-reasoning | 360 | 360 | yes | yes | yes | 112 |
| 9 | Llama-3.3-70B-Instruct | 8 | 8 | yes | yes | yes | 120 |
| 9 | Mistral-Large-3 | 8 | 8 | yes | yes | yes | 119 |
| 9 | gpt-4.1 | 8 | 8 | yes | yes | yes | 116 |
| 9 | gpt-4o-mini | 8 | 4 | no | no | yes | 117 |
| 9 | gpt-5.4-mini | 8 | 8 | yes | yes | yes | 115 |
| 9 | grok-4-1-fast-non-reasoning | 8 | 2 | no | no | yes | 118 |
| 10 | Llama-3.3-70B-Instruct | 34 | 34 | yes | yes | yes | 126 |
| 10 | Mistral-Large-3 | 34 | 34 | yes | yes | yes | 125 |
| 10 | gpt-4.1 | 34 | 34 | yes | yes | yes | 122 |
| 10 | gpt-4o-mini | 34 | 34 | yes | yes | yes | 123 |
| 10 | gpt-5.4-mini | 34 | 34 | yes | yes | yes | 121 |
| 10 | grok-4-1-fast-non-reasoning | 34 | 34 | yes | yes | yes | 124 |
