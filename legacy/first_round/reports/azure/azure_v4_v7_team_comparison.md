# Azure v4 to v7 Comparison

Team comparison of prompts `v4`, `v5`, `v6`, and `v7` on Azure/GuaranIA models.

The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

## Summary

- `v4` retains the highest individual score: `gpt-5.4-mini` reached 6/10.
- `v7` improves the robustness of weaker models, especially `grok`, `Mistral`, and `gpt-4o-mini`, but lowers the highest score to 5/10.
- `v5` and `v6` do not exceed the highest score achieved with `v4`; both peak at 5/10.
- Warmup/few-shot examples help some models but do not fix recurring problems P1, P5, P6, P7, and P8.

## Matrix v4-v7

| Model | v4 | v5 | v6 | v7 | Best prompt | Best result |
|---|---:|---:|---:|---:|---|---:|
| `gpt-5.4-mini` | 6/10 | 5/10 | 5/10 | 5/10 | `v4` | 6/10 |
| `Llama-3.3-70B-Instruct` | 4/10 | 4/10 | 5/10 | 4/10 | `v6` | 5/10 |
| `Mistral-Large-3` | 4/10 | 0/10 | 0/10 | 5/10 | `v7` | 5/10 |
| `gpt-4.1` | 5/10 | 5/10 | 4/10 | 4/10 | `v5` | 5/10 |
| `gpt-4o-mini` | 3/10 | 2/10 | 2/10 | 4/10 | `v7` | 4/10 |
| `grok-4-1-fast-non-reasoning` | 0/10 | 2/10 | 4/10 | 4/10 | `v6` | 4/10 |

## Ranking by Prompt

### v4

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 6/10 | 60.0% | 10/10 | 2.934s |
| 2 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 4.031s |
| 3 | `Mistral-Large-3` | 4/10 | 40.0% | 10/10 | 5.636s |
| 4 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 9/10 | 2.687s |
| 5 | `gpt-4o-mini` | 3/10 | 30.0% | 10/10 | 2.932s |
| 6 | `grok-4-1-fast-non-reasoning` | 0/10 | 0.0% | 6/10 | 31.346s |

### v5

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 2.717s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.729s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 2.500s |
| 4 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 2.751s |
| 5 | `grok-4-1-fast-non-reasoning` | 2/10 | 20.0% | 9/10 | 4.815s |
| 6 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 7.514s |

### v6

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 10/10 | 3.345s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.577s |
| 3 | `gpt-4.1` | 4/10 | 40.0% | 10/10 | 2.694s |
| 4 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 3.954s |
| 5 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.238s |
| 6 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 4.606s |

### v7

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.780s |
| 2 | `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 13.063s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 3.722s |
| 4 | `gpt-4o-mini` | 4/10 | 40.0% | 10/10 | 4.678s |
| 5 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 4.945s |
| 6 | `gpt-4.1` | 4/10 | 40.0% | 9/10 | 3.698s |

## Comparison v5 vs v6

| Model | v5 | v6 | Delta | JSON v5 | JSON v6 | Latency v5 | Latency v6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grok-4-1-fast-non-reasoning` | 2/10 | 4/10 | +2 | 9/10 | 10/10 | 4.815s | 3.954s |
| `Llama-3.3-70B-Instruct` | 4/10 | 5/10 | +1 | 10/10 | 10/10 | 2.500s | 3.345s |
| `gpt-5.4-mini` | 5/10 | 5/10 | 0 | 10/10 | 10/10 | 3.729s | 3.577s |
| `gpt-4o-mini` | 2/10 | 2/10 | 0 | 10/10 | 10/10 | 2.751s | 3.238s |
| `Mistral-Large-3` | 0/10 | 0/10 | 0 | 0/10 | 0/10 | 7.514s | 4.606s |
| `gpt-4.1` | 5/10 | 4/10 | -1 | 10/10 | 10/10 | 2.717s | 2.694s |

### Per-Problem Changes v5 vs v6

| Model | Improved in v6 | Worsened in v6 | Errors v6 |
|---|---|---|---|
| `Llama-3.3-70B-Instruct` | P2 | - | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 3), P7 (91 -> 45), P8 (360 -> 30) |
| `Mistral-Large-3` | - | - | P1 (18 -> 10), P2 (8 -> 8), P3 (140 -> 140), P4 (600 -> 600), P5 (3 -> 33), P6 (60 -> 4), P7 (91 -> 45), P8 (360 -> 120), P9 (8 -> 7), P10 (34 -> 34) |
| `gpt-4.1` | - | P9 | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 28), P7 (91 -> 28), P8 (360 -> 120), P9 (8 -> 7) |
| `gpt-4o-mini` | - | - | P1 (18 -> 6), P2 (8 -> 11), P4 (600 -> 67), P5 (3 -> 5), P6 (60 -> 4), P7 (91 -> 7), P8 (360 -> 180), P9 (8 -> 3) |
| `gpt-5.4-mini` | P6 | P4 | P1 (18 -> 6), P4 (600 -> 24), P5 (3 -> 5), P7 (91 -> 28), P8 (360 -> 120) |
| `grok-4-1-fast-non-reasoning` | P2, P3 | - | P1 (18 -> 6), P5 (3 -> 210), P6 (60 -> 2), P7 (91 -> 25), P8 (360 -> 180), P9 (8 -> 1) |

## Comparison v4 vs v7

| Model | v4 | v7 | Delta | JSON v4 | JSON v7 | Latency v4 | Latency v7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grok-4-1-fast-non-reasoning` | 0/10 | 4/10 | +4 | 6/10 | 10/10 | 31.346s | 4.945s |
| `Mistral-Large-3` | 4/10 | 5/10 | +1 | 10/10 | 10/10 | 5.636s | 13.063s |
| `gpt-4o-mini` | 3/10 | 4/10 | +1 | 10/10 | 10/10 | 2.932s | 4.678s |
| `Llama-3.3-70B-Instruct` | 4/10 | 4/10 | 0 | 9/10 | 10/10 | 2.687s | 3.722s |
| `gpt-5.4-mini` | 6/10 | 5/10 | -1 | 10/10 | 10/10 | 2.934s | 3.780s |
| `gpt-4.1` | 5/10 | 4/10 | -1 | 10/10 | 9/10 | 4.031s | 3.698s |

### Per-Problem Changes v4 vs v7

| Model | Improved in v7 | Worsened in v7 | Errors v7 |
|---|---|---|---|
| `Llama-3.3-70B-Instruct` | - | - | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 21), P7 (91 -> 49), P8 (360 -> 66), P9 (8 -> 5) |
| `Mistral-Large-3` | P2 | - | P1 (18 -> 10), P5 (3 -> 11), P6 (60 -> 8), P7 (91 -> 35), P8 (360 -> 120) |
| `gpt-4.1` | P7 | P9, P10 | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 21), P8 (360 -> 120), P9 (8 -> 4), P10 (34 -> None) |
| `gpt-4o-mini` | P5 | - | P1 (18 -> 10), P4 (600 -> 67), P6 (60 -> 6), P7 (91 -> 35), P8 (360 -> 120), P9 (8 -> 3) |
| `gpt-5.4-mini` | - | P6 | P1 (18 -> 10), P5 (3 -> 5), P6 (60 -> 420), P7 (91 -> 49), P8 (360 -> 120) |
| `grok-4-1-fast-non-reasoning` | P2, P3, P4, P10 | - | P1 (18 -> 10), P5 (3 -> 217), P6 (60 -> 32), P7 (91 -> 15), P8 (360 -> 180), P9 (8 -> 5) |

## Conclusion

To maximize the best individual result on Azure, `v4` remains the best baseline because it reaches 6/10 with `gpt-5.4-mini`.

For comparing robustness across models, `v7` is interesting because it improves several models that performed poorly with `v4`, but it does not improve the best absolute result.
