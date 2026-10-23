# Azure Summary v7

All runs were evaluated with prompt `v7` (`Bilingual teacher with glossary and warmup`).

The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

## Model Comparison

| Model | Correct answers | Accuracy | Valid JSON | Consistent option | Mean latency | Errors |
|---|---:|---:|---:|---:|---:|---|
| `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 10/10 | 3.780s | P1 (18 -> 10), P5 (3 -> 5), P6 (60 -> 420), P7 (91 -> 49), P8 (360 -> 120) |
| `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 10/10 | 13.063s | P1 (18 -> 10), P5 (3 -> 11), P6 (60 -> 8), P7 (91 -> 35), P8 (360 -> 120) |
| `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 10/10 | 3.722s | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 21), P7 (91 -> 49), P8 (360 -> 66), P9 (8 -> 5) |
| `gpt-4o-mini` | 4/10 | 40.0% | 10/10 | 10/10 | 4.678s | P1 (18 -> 10), P4 (600 -> 67), P6 (60 -> 6), P7 (91 -> 35), P8 (360 -> 120), P9 (8 -> 3) |
| `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 10/10 | 4.945s | P1 (18 -> 10), P5 (3 -> 217), P6 (60 -> 32), P7 (91 -> 15), P8 (360 -> 180), P9 (8 -> 5) |
| `gpt-4.1` | 4/10 | 40.0% | 9/10 | 9/10 | 3.698s | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 21), P8 (360 -> 120), P9 (8 -> 4), P10 (34 -> None) |

## Global Ranking

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.780s |
| 2 | `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 13.063s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 3.722s |
| 4 | `gpt-4o-mini` | 4/10 | 40.0% | 10/10 | 4.678s |
| 5 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 4.945s |
| 6 | `gpt-4.1` | 4/10 | 40.0% | 9/10 | 3.698s |

## Error Details

| Model | Problem | Expected | Predicted | Valid JSON |
|---|---:|---:|---:|---|
| `gpt-5.4-mini` | 1 | 18 | 10 | yes |
| `gpt-5.4-mini` | 5 | 3 | 5 | yes |
| `gpt-5.4-mini` | 6 | 60 | 420 | yes |
| `gpt-5.4-mini` | 7 | 91 | 49 | yes |
| `gpt-5.4-mini` | 8 | 360 | 120 | yes |
| `Mistral-Large-3` | 1 | 18 | 10 | yes |
| `Mistral-Large-3` | 5 | 3 | 11 | yes |
| `Mistral-Large-3` | 6 | 60 | 8 | yes |
| `Mistral-Large-3` | 7 | 91 | 35 | yes |
| `Mistral-Large-3` | 8 | 360 | 120 | yes |
| `Llama-3.3-70B-Instruct` | 1 | 18 | 10 | yes |
| `Llama-3.3-70B-Instruct` | 5 | 3 | 1 | yes |
| `Llama-3.3-70B-Instruct` | 6 | 60 | 21 | yes |
| `Llama-3.3-70B-Instruct` | 7 | 91 | 49 | yes |
| `Llama-3.3-70B-Instruct` | 8 | 360 | 66 | yes |
| `Llama-3.3-70B-Instruct` | 9 | 8 | 5 | yes |
| `gpt-4o-mini` | 1 | 18 | 10 | yes |
| `gpt-4o-mini` | 4 | 600 | 67 | yes |
| `gpt-4o-mini` | 6 | 60 | 6 | yes |
| `gpt-4o-mini` | 7 | 91 | 35 | yes |
| `gpt-4o-mini` | 8 | 360 | 120 | yes |
| `gpt-4o-mini` | 9 | 8 | 3 | yes |
| `grok-4-1-fast-non-reasoning` | 1 | 18 | 10 | yes |
| `grok-4-1-fast-non-reasoning` | 5 | 3 | 217 | yes |
| `grok-4-1-fast-non-reasoning` | 6 | 60 | 32 | yes |
| `grok-4-1-fast-non-reasoning` | 7 | 91 | 15 | yes |
| `grok-4-1-fast-non-reasoning` | 8 | 360 | 180 | yes |
| `grok-4-1-fast-non-reasoning` | 9 | 8 | 5 | yes |
| `gpt-4.1` | 1 | 18 | 10 | yes |
| `gpt-4.1` | 5 | 3 | 10 | yes |
| `gpt-4.1` | 6 | 60 | 21 | yes |
| `gpt-4.1` | 8 | 360 | 120 | yes |
| `gpt-4.1` | 9 | 8 | 4 | yes |
| `gpt-4.1` | 10 | 34 | None | no |

## Conclusion

The best result was `gpt-5.4-mini` at 5/10.
