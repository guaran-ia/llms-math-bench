# Azure v5 vs v6 Comparison

The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

## Summary by Model

| Model | v5 | v6 | Delta | JSON v5 | JSON v6 | Latency v5 | Latency v6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grok-4-1-fast-non-reasoning` | 2/10 | 4/10 | +2 | 9/10 | 10/10 | 4.815s | 3.954s |
| `Llama-3.3-70B-Instruct` | 4/10 | 5/10 | +1 | 10/10 | 10/10 | 2.500s | 3.345s |
| `gpt-5.4-mini` | 5/10 | 5/10 | 0 | 10/10 | 10/10 | 3.729s | 3.577s |
| `gpt-4o-mini` | 2/10 | 2/10 | 0 | 10/10 | 10/10 | 2.751s | 3.238s |
| `Mistral-Large-3` | 0/10 | 0/10 | 0 | 0/10 | 0/10 | 7.514s | 4.606s |
| `gpt-4.1` | 5/10 | 4/10 | -1 | 10/10 | 10/10 | 2.717s | 2.694s |

## Ranking v6

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 10/10 | 3.345s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.577s |
| 3 | `gpt-4.1` | 4/10 | 40.0% | 10/10 | 2.694s |
| 4 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 3.954s |
| 5 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.238s |
| 6 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 4.606s |

## Per-Problem Changes

| Model | Improved in v6 | Worsened in v6 | Errors v6 |
|---|---|---|---|
| `grok-4-1-fast-non-reasoning` | P2, P3 | - | P1 (18 -> 6), P5 (3 -> 210), P6 (60 -> 2), P7 (91 -> 25), P8 (360 -> 180), P9 (8 -> 1) |
| `Llama-3.3-70B-Instruct` | P2 | - | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 3), P7 (91 -> 45), P8 (360 -> 30) |
| `gpt-5.4-mini` | P6 | P4 | P1 (18 -> 6), P4 (600 -> 24), P5 (3 -> 5), P7 (91 -> 28), P8 (360 -> 120) |
| `gpt-4o-mini` | - | - | P1 (18 -> 6), P2 (8 -> 11), P4 (600 -> 67), P5 (3 -> 5), P6 (60 -> 4), P7 (91 -> 7), P8 (360 -> 180), P9 (8 -> 3) |
| `Mistral-Large-3` | - | - | P1 (18 -> 10), P2 (8 -> 8), P3 (140 -> 140), P4 (600 -> 600), P5 (3 -> 33), P6 (60 -> 4), P7 (91 -> 45), P8 (360 -> 120), P9 (8 -> 7), P10 (34 -> 34) |
| `gpt-4.1` | - | P9 | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 28), P7 (91 -> 28), P8 (360 -> 120), P9 (8 -> 7) |

## Conclusion

The best result with `v6` was `Llama-3.3-70B-Instruct` at 5/10.
