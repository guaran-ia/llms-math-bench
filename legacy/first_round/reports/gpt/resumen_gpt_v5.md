# GPT Summary v5

All runs were evaluated with prompt `v5` (`Strict Guaraní with reinforced JSON rules`).

The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

## Model Comparison

| Model/Run | Prompt | Correct answers | Accuracy | Valid JSON | Consistent option | Errors |
|---|---|---:|---:|---:|---:|---|
| `gpt6_lite` | `v5` | 10/10 | 100.0% | 10/10 | 10/10 | none |
| `gpt5.6sol_lite` | `v5` | 9/10 | 90.0% | 10/10 | 10/10 | P8 (360 -> 300) |
| `gpt5.6sol_medium` | `v5` | 9/10 | 90.0% | 10/10 | 10/10 | P1 (18 -> 10) |
| `gpt5.5_medium` | `v5` | 8/10 | 80.0% | 10/10 | 10/10 | P1 (18 -> 10), P5 (3 -> 5) |
| `gpt5.6terra_lite` | `v5` | 8/10 | 80.0% | 10/10 | 10/10 | P1 (18 -> 10), P8 (360 -> 120) |

## Global Ranking

| Rank | Model/Run | Strict correct answers | Strict accuracy | Valid JSON | Errors |
|---:|---|---:|---:|---:|---|
| 1 | `gpt6_lite` | 10/10 | 100.0% | 10/10 | none |
| 2 | `gpt5.6sol_lite` | 9/10 | 90.0% | 10/10 | P8 (360 -> 300) |
| 3 | `gpt5.6sol_medium` | 9/10 | 90.0% | 10/10 | P1 (18 -> 10) |
| 4 | `gpt5.5_medium` | 8/10 | 80.0% | 10/10 | P1 (18 -> 10), P5 (3 -> 5) |
| 5 | `gpt5.6terra_lite` | 8/10 | 80.0% | 10/10 | P1 (18 -> 10), P8 (360 -> 120) |

## Error Details

| Model/Run | Problem | Expected | Predicted |
|---|---:|---:|---:|
| `gpt5.6sol_lite` | 8 | 360 | 300 |
| `gpt5.6sol_medium` | 1 | 18 | 10 |
| `gpt5.5_medium` | 1 | 18 | 10 |
| `gpt5.5_medium` | 5 | 3 | 5 |
| `gpt5.6terra_lite` | 1 | 18 | 10 |
| `gpt5.6terra_lite` | 8 | 360 | 120 |

## Conclusion

The best result was `gpt6_lite` at 10/10.
