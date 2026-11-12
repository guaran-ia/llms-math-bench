# Prompt Comparison v1 to v4

## Summary

Evaluation of 10 mathematical problems in Guaraní across 6 models. The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

| Prompt | Results file | Best model | Best score |
|---|---|---|---:|
| v1 | `model_test_results_guarani.jsonl` | `gpt-4.1` | 6/10 |
| v2 | `model_test_results_guarani_prompt_v2.jsonl` | `gpt-4.1` and `Mistral-Large-3` | 5/10 |
| v3 | `model_test_results_guarani_prompt_v3.jsonl` | `gpt-5.4-mini` | 6/10 |
| v4 | `model_test_results_guarani_prompt_v4.jsonl` | `gpt-5.4-mini` | 6/10 |

## Comparison by Model

| Model | v1 | v2 | v3 | v4 | Best result |
|---|---:|---:|---:|---:|---:|
| `gpt-4.1` | 6/10 | 5/10 | 5/10 | 5/10 | 6/10 |
| `gpt-5.4-mini` | 5/10 | 4/10 | 6/10 | 6/10 | 6/10 |
| `Llama-3.3-70B-Instruct` | 5/10 | 4/10 | 5/10 | 4/10 | 5/10 |
| `Mistral-Large-3` | 4/10 | 5/10 | 4/10 | 4/10 | 5/10 |
| `grok-4-1-fast-non-reasoning` | 3/10 | 2/10 | 1/10 | 0/10 | 3/10 |
| `gpt-4o-mini` | 2/10 | 2/10 | 2/10 | 3/10 | 3/10 |

## Ranking by Prompt

### v1

| Rank | Model | Correct answers |
|---:|---|---:|
| 1 | `gpt-4.1` | 6/10 |
| 2 | `gpt-5.4-mini` | 5/10 |
| 3 | `Llama-3.3-70B-Instruct` | 5/10 |
| 4 | `Mistral-Large-3` | 4/10 |
| 5 | `grok-4-1-fast-non-reasoning` | 3/10 |
| 6 | `gpt-4o-mini` | 2/10 |

### v2

| Rank | Model | Correct answers |
|---:|---|---:|
| 1 | `gpt-4.1` | 5/10 |
| 2 | `Mistral-Large-3` | 5/10 |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 |
| 4 | `gpt-5.4-mini` | 4/10 |
| 5 | `gpt-4o-mini` | 2/10 |
| 6 | `grok-4-1-fast-non-reasoning` | 2/10 |

### v3

| Rank | Model | Correct answers |
|---:|---|---:|
| 1 | `gpt-5.4-mini` | 6/10 |
| 2 | `Llama-3.3-70B-Instruct` | 5/10 |
| 3 | `gpt-4.1` | 5/10 |
| 4 | `Mistral-Large-3` | 4/10 |
| 5 | `gpt-4o-mini` | 2/10 |
| 6 | `grok-4-1-fast-non-reasoning` | 1/10 |

### v4

| Rank | Model | Correct answers |
|---:|---|---:|
| 1 | `gpt-5.4-mini` | 6/10 |
| 2 | `gpt-4.1` | 5/10 |
| 3 | `Mistral-Large-3` | 4/10 |
| 4 | `Llama-3.3-70B-Instruct` | 4/10 |
| 5 | `gpt-4o-mini` | 3/10 |
| 6 | `grok-4-1-fast-non-reasoning` | 0/10 |

## Conclusion

The best absolute result was 6/10, achieved by `gpt-4.1` with v1 and `gpt-5.4-mini` with v3 and v4.

Prompt v3 appears to be the best overall candidate: it maintains the maximum of 6/10 with `gpt-5.4-mini`, retains 5/10 with `Llama-3.3-70B-Instruct`, and does not degrade JSON formatting as much as v4.

Prompt v4 helped `gpt-4o-mini`, but clearly hurt `grok-4-1-fast-non-reasoning` and lowered the score for `Llama-3.3-70B-Instruct`.
