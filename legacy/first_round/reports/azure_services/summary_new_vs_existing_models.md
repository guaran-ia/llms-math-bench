# New Azure Services Models Summary

Summary comparison of the new models `gpt-5.6-terra` and `gpt-5.5` against previously evaluated Azure/GuaranIA models.

The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

## Global Ranking by Best Prompt

| Rank | Model | Best prompt | Correct answers | Accuracy | Valid JSON | Mean latency |
|---:|---|---|---:|---:|---:|---:|
| 1 | `gpt-5.5` | `v7` | 10/10 | 100.0% | 10/10 | 7.150s |
| 2 | `gpt-5.6-terra` | `v9` | 9/10 | 90.0% | 0/10 | 3.285s |
| 3 | `gpt-5.4-mini` | `v4` | 6/10 | 60.0% | 10/10 | 2.934s |
| 4 | `Llama-3.3-70B-Instruct` | `v6` | 5/10 | 50.0% | 10/10 | 3.345s |
| 5 | `Mistral-Large-3` | `v7` | 5/10 | 50.0% | 10/10 | 13.063s |
| 6 | `gpt-4.1` | `v5` | 5/10 | 50.0% | 10/10 | 2.717s |
| 7 | `gpt-4o-mini` | `v7` | 4/10 | 40.0% | 10/10 | 4.678s |
| 8 | `grok-4-1-fast-non-reasoning` | `v6` | 4/10 | 40.0% | 10/10 | 3.954s |

## New Models: Results by Prompt

| Model | v1 | v2 | v3 | v4 | v5 | v6 | v7 | v8 | v9 | Best prompt | Best result |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| `gpt-5.5` | 9/10 | 10/10 | 10/10 | 10/10 | 9/10 | 9/10 | 10/10 | 10/10 | 10/10 | `v7` | 10/10 |
| `gpt-5.6-terra` | 7/10 | 8/10 | 8/10 | 8/10 | 7/10 | 7/10 | 8/10 | 7/10 | 9/10 | `v9` | 9/10 |

## Summary Comparison with Existing Models

| Model | v1 | v2 | v3 | v4 | v5 | v6 | v7 | v8 | v9 | Best prompt | Best result |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| `gpt-5.5` | 9/10 | 10/10 | 10/10 | 10/10 | 9/10 | 9/10 | 10/10 | 10/10 | 10/10 | `v7` | 10/10 |
| `gpt-5.6-terra` | 7/10 | 8/10 | 8/10 | 8/10 | 7/10 | 7/10 | 8/10 | 7/10 | 9/10 | `v9` | 9/10 |
| `gpt-5.4-mini` | - | - | - | 6/10 | 5/10 | 5/10 | 5/10 | 3/10 | 3/10 | `v4` | 6/10 |
| `Llama-3.3-70B-Instruct` | - | - | - | 4/10 | 4/10 | 5/10 | 4/10 | 2/10 | 3/10 | `v6` | 5/10 |
| `Mistral-Large-3` | - | - | - | 4/10 | 0/10 | 0/10 | 5/10 | 1/10 | 3/10 | `v7` | 5/10 |
| `gpt-4.1` | - | - | - | 5/10 | 5/10 | 4/10 | 4/10 | 4/10 | 3/10 | `v5` | 5/10 |
| `gpt-4o-mini` | - | - | - | 3/10 | 2/10 | 2/10 | 4/10 | 2/10 | 3/10 | `v7` | 4/10 |
| `grok-4-1-fast-non-reasoning` | - | - | - | 0/10 | 2/10 | 4/10 | 4/10 | 1/10 | 1/10 | `v6` | 4/10 |

## Errors with the Best Prompt for Each New Model

| Model | Best prompt | Errors |
|---|---|---|
| `gpt-5.5` | `v7` | none |
| `gpt-5.6-terra` | `v9` | P1 (18 -> 10) |

## Conclusion

The best overall result is now `gpt-5.5` with `v7`: 10/10.
