# Claude Summary v5

All runs were evaluated with prompt `v5` (`Strict Guaraní with reinforced JSON rules`).

The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

## Model Comparison

| Model/Run | Reported model | Prompt | Correct answers | Accuracy | Valid JSON | Consistent option | Errors |
|---|---|---|---:|---:|---:|---:|---|
| `sonnet5_extra` | `claude-sonnet-5` | `v5` | 9/10 | 90.0% | 10/10 | 10/10 | P6 (60 -> 30) |
| `sonnet5_hard` | `gpt-5` | `v5` | 8/10 | 80.0% | 10/10 | 10/10 | P6 (60 -> 2.5), P8 (360 -> 120) |
| `sonnet5_medium` | `gpt-5` | `v5` | 7/10 | 70.0% | 10/10 | 10/10 | P1 (18 -> 10), P3 (140 -> 280), P6 (60 -> 3) |

## Global Ranking

| Rank | Model/Run | Strict correct answers | Strict accuracy | Valid JSON | Errors |
|---:|---|---:|---:|---:|---|
| 1 | `sonnet5_extra` | 9/10 | 90.0% | 10/10 | P6 (60 -> 30) |
| 2 | `sonnet5_hard` | 8/10 | 80.0% | 10/10 | P6 (60 -> 2.5), P8 (360 -> 120) |
| 3 | `sonnet5_medium` | 7/10 | 70.0% | 10/10 | P1 (18 -> 10), P3 (140 -> 280), P6 (60 -> 3) |

## Error Details

| Model/Run | Problem | Expected | Predicted |
|---|---:|---:|---:|
| `sonnet5_extra` | 6 | 60 | 30 |
| `sonnet5_hard` | 6 | 60 | 2.5 |
| `sonnet5_hard` | 8 | 360 | 120 |
| `sonnet5_medium` | 1 | 18 | 10 |
| `sonnet5_medium` | 3 | 140 | 280 |
| `sonnet5_medium` | 6 | 60 | 3 |

## Conclusion

The best result was `sonnet5_extra` at 9/10.
