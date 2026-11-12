# Azure Summary v8

All runs were evaluated with prompt `v8` (`Simple zero-shot autocomplete`).

The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

## Model Comparison

| Model | Correct answers | Accuracy | Valid JSON | Consistent option | Mean latency | Errors |
|---|---:|---:|---:|---:|---:|---|
| `gpt-4.1` | 4/10 | 40.0% | 0/10 | 0/10 | 2.146s | P1 (18 -> 10), P5 (3 -> 8), P6 (60 -> 90), P7 (91 -> 37), P8 (360 -> 120), P9 (8 -> 5) |
| `gpt-5.4-mini` | 3/10 | 30.0% | 0/10 | 0/10 | 2.205s | P1 (18 -> 10), P2 (8 -> 14), P5 (3 -> 14), P6 (60 -> 20300), P7 (91 -> 49), P8 (360 -> 30), P9 (8 -> 4) |
| `Llama-3.3-70B-Instruct` | 2/10 | 20.0% | 0/10 | 0/10 | 0.809s | P1 (18 -> 10), P2 (8 -> 7), P5 (3 -> 8), P6 (60 -> 7), P7 (91 -> 50), P8 (360 -> 30), P9 (8 -> 12), P10 (34 -> 4) |
| `gpt-4o-mini` | 2/10 | 20.0% | 0/10 | 0/10 | 1.094s | P1 (18 -> 6), P2 (8 -> 7), P4 (600 -> 12), P5 (3 -> 12), P6 (60 -> 6), P7 (91 -> 7), P8 (360 -> 180), P9 (8 -> 3) |
| `Mistral-Large-3` | 1/10 | 10.0% | 0/10 | 0/10 | 0.621s | P1 (18 -> 10), P2 (8 -> 7), P3 (140 -> 420), P5 (3 -> 120), P6 (60 -> 5), P7 (91 -> 4), P8 (360 -> 120), P9 (8 -> 3), P10 (34 -> 38) |
| `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 0/10 | 0/10 | 0.900s | P1 (18 -> 6), P2 (8 -> 20), P3 (140 -> 8), P5 (3 -> 70), P6 (60 -> 5), P7 (91 -> 80), P8 (360 -> 60), P9 (8 -> 2), P10 (34 -> 36) |

## Global Ranking

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 4/10 | 40.0% | 0/10 | 2.146s |
| 2 | `gpt-5.4-mini` | 3/10 | 30.0% | 0/10 | 2.205s |
| 3 | `Llama-3.3-70B-Instruct` | 2/10 | 20.0% | 0/10 | 0.809s |
| 4 | `gpt-4o-mini` | 2/10 | 20.0% | 0/10 | 1.094s |
| 5 | `Mistral-Large-3` | 1/10 | 10.0% | 0/10 | 0.621s |
| 6 | `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 0/10 | 0.900s |

## Error Details

| Model | Problem | Expected | Predicted | Valid JSON |
|---|---:|---:|---:|---|
| `gpt-4.1` | 1 | 18 | 10 | no |
| `gpt-4.1` | 5 | 3 | 8 | no |
| `gpt-4.1` | 6 | 60 | 90 | no |
| `gpt-4.1` | 7 | 91 | 37 | no |
| `gpt-4.1` | 8 | 360 | 120 | no |
| `gpt-4.1` | 9 | 8 | 5 | no |
| `gpt-5.4-mini` | 1 | 18 | 10 | no |
| `gpt-5.4-mini` | 2 | 8 | 14 | no |
| `gpt-5.4-mini` | 5 | 3 | 14 | no |
| `gpt-5.4-mini` | 6 | 60 | 20300 | no |
| `gpt-5.4-mini` | 7 | 91 | 49 | no |
| `gpt-5.4-mini` | 8 | 360 | 30 | no |
| `gpt-5.4-mini` | 9 | 8 | 4 | no |
| `Llama-3.3-70B-Instruct` | 1 | 18 | 10 | no |
| `Llama-3.3-70B-Instruct` | 2 | 8 | 7 | no |
| `Llama-3.3-70B-Instruct` | 5 | 3 | 8 | no |
| `Llama-3.3-70B-Instruct` | 6 | 60 | 7 | no |
| `Llama-3.3-70B-Instruct` | 7 | 91 | 50 | no |
| `Llama-3.3-70B-Instruct` | 8 | 360 | 30 | no |
| `Llama-3.3-70B-Instruct` | 9 | 8 | 12 | no |
| `Llama-3.3-70B-Instruct` | 10 | 34 | 4 | no |
| `gpt-4o-mini` | 1 | 18 | 6 | no |
| `gpt-4o-mini` | 2 | 8 | 7 | no |
| `gpt-4o-mini` | 4 | 600 | 12 | no |
| `gpt-4o-mini` | 5 | 3 | 12 | no |
| `gpt-4o-mini` | 6 | 60 | 6 | no |
| `gpt-4o-mini` | 7 | 91 | 7 | no |
| `gpt-4o-mini` | 8 | 360 | 180 | no |
| `gpt-4o-mini` | 9 | 8 | 3 | no |
| `Mistral-Large-3` | 1 | 18 | 10 | no |
| `Mistral-Large-3` | 2 | 8 | 7 | no |
| `Mistral-Large-3` | 3 | 140 | 420 | no |
| `Mistral-Large-3` | 5 | 3 | 120 | no |
| `Mistral-Large-3` | 6 | 60 | 5 | no |
| `Mistral-Large-3` | 7 | 91 | 4 | no |
| `Mistral-Large-3` | 8 | 360 | 120 | no |
| `Mistral-Large-3` | 9 | 8 | 3 | no |
| `Mistral-Large-3` | 10 | 34 | 38 | no |
| `grok-4-1-fast-non-reasoning` | 1 | 18 | 6 | no |
| `grok-4-1-fast-non-reasoning` | 2 | 8 | 20 | no |
| `grok-4-1-fast-non-reasoning` | 3 | 140 | 8 | no |
| `grok-4-1-fast-non-reasoning` | 5 | 3 | 70 | no |
| `grok-4-1-fast-non-reasoning` | 6 | 60 | 5 | no |
| `grok-4-1-fast-non-reasoning` | 7 | 91 | 80 | no |
| `grok-4-1-fast-non-reasoning` | 8 | 360 | 60 | no |
| `grok-4-1-fast-non-reasoning` | 9 | 8 | 2 | no |
| `grok-4-1-fast-non-reasoning` | 10 | 34 | 36 | no |

## Conclusion

The best result was `gpt-4.1` at 4/10.
