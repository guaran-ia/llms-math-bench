# Azure v4 to v9 Comparison

Simple summary of existing and new Azure/GuaranIA models (`gpt-5.6-terra`, `gpt-5.5`).

Main metric: `response.final_answer.value == expected_answer`.

## Prompt Summary

| Prompt | Summary |
|---|---|
| `v4` | Bilingual teacher with a Guaraní–Spanish glossary. |
| `v5` | Strict Guaraní with reinforced JSON rules. |
| `v6` | v5 with mathematical warmup/few-shot examples. |
| `v7` | v4 with mathematical warmup/few-shot examples. |
| `v8` | Simple zero-shot autocomplete; numeric result only. |
| `v9` | Simple few-shot autocomplete; numeric result only. |

## Prompt v4

| Rank | Model | Correct answers | Accuracy | Valid JSON | Latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.5` | 10/10 | 100.0% | 10/10 | 7.258s |
| 2 | `gpt-5.6-terra` | 8/10 | 80.0% | 10/10 | 4.349s |
| 3 | `gpt-5.4-mini` | 6/10 | 60.0% | 10/10 | 2.934s |
| 4 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 4.031s |
| 5 | `Mistral-Large-3` | 4/10 | 40.0% | 10/10 | 5.636s |
| 6 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 9/10 | 2.687s |
| 7 | `gpt-4o-mini` | 3/10 | 30.0% | 10/10 | 2.932s |
| 8 | `grok-4-1-fast-non-reasoning` | 0/10 | 0.0% | 6/10 | 31.346s |

## Prompt v5

| Rank | Model | Correct answers | Accuracy | Valid JSON | Latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.5` | 9/10 | 90.0% | 10/10 | 10.438s |
| 2 | `gpt-5.6-terra` | 7/10 | 70.0% | 10/10 | 5.107s |
| 3 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 2.717s |
| 4 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.729s |
| 5 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 2.500s |
| 6 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 2.751s |
| 7 | `grok-4-1-fast-non-reasoning` | 2/10 | 20.0% | 9/10 | 4.815s |
| 8 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 7.514s |

## Prompt v6

| Rank | Model | Correct answers | Accuracy | Valid JSON | Latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.5` | 9/10 | 90.0% | 10/10 | 11.085s |
| 2 | `gpt-5.6-terra` | 7/10 | 70.0% | 10/10 | 5.516s |
| 3 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 10/10 | 3.345s |
| 4 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.577s |
| 5 | `gpt-4.1` | 4/10 | 40.0% | 10/10 | 2.694s |
| 6 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 3.954s |
| 7 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.238s |
| 8 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 4.606s |

## Prompt v7

| Rank | Model | Correct answers | Accuracy | Valid JSON | Latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.5` | 10/10 | 100.0% | 10/10 | 7.150s |
| 2 | `gpt-5.6-terra` | 8/10 | 80.0% | 10/10 | 4.013s |
| 3 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.780s |
| 4 | `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 13.063s |
| 5 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 3.722s |
| 6 | `gpt-4o-mini` | 4/10 | 40.0% | 10/10 | 4.678s |
| 7 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 4.945s |
| 8 | `gpt-4.1` | 4/10 | 40.0% | 9/10 | 3.698s |

## Prompt v8

| Rank | Model | Correct answers | Accuracy | Valid JSON | Latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.5` | 10/10 | 100.0% | 0/10 | 3.934s |
| 2 | `gpt-5.6-terra` | 7/10 | 70.0% | 0/10 | 3.152s |
| 3 | `gpt-4.1` | 4/10 | 40.0% | 0/10 | 2.146s |
| 4 | `gpt-5.4-mini` | 3/10 | 30.0% | 0/10 | 2.205s |
| 5 | `Llama-3.3-70B-Instruct` | 2/10 | 20.0% | 0/10 | 0.809s |
| 6 | `gpt-4o-mini` | 2/10 | 20.0% | 0/10 | 1.094s |
| 7 | `Mistral-Large-3` | 1/10 | 10.0% | 0/10 | 0.621s |
| 8 | `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 0/10 | 0.900s |

## Prompt v9

| Rank | Model | Correct answers | Accuracy | Valid JSON | Latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.5` | 10/10 | 100.0% | 0/10 | 4.091s |
| 2 | `gpt-5.6-terra` | 9/10 | 90.0% | 0/10 | 3.285s |
| 3 | `Llama-3.3-70B-Instruct` | 3/10 | 30.0% | 0/10 | 0.604s |
| 4 | `Mistral-Large-3` | 3/10 | 30.0% | 0/10 | 0.736s |
| 5 | `gpt-4o-mini` | 3/10 | 30.0% | 0/10 | 0.991s |
| 6 | `gpt-4.1` | 3/10 | 30.0% | 0/10 | 1.219s |
| 7 | `gpt-5.4-mini` | 3/10 | 30.0% | 0/10 | 1.435s |
| 8 | `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 0/10 | 0.637s |

## Final Comparison

| Model | v4 | v5 | v6 | v7 | v8 | v9 | Best prompt | Best result |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| `gpt-5.5` | 10/10 | 9/10 | 9/10 | 10/10 | 10/10 | 10/10 | `v7` | 10/10 |
| `gpt-5.6-terra` | 8/10 | 7/10 | 7/10 | 8/10 | 7/10 | 9/10 | `v9` | 9/10 |
| `gpt-5.4-mini` | 6/10 | 5/10 | 5/10 | 5/10 | 3/10 | 3/10 | `v4` | 6/10 |
| `Llama-3.3-70B-Instruct` | 4/10 | 4/10 | 5/10 | 4/10 | 2/10 | 3/10 | `v6` | 5/10 |
| `Mistral-Large-3` | 4/10 | 0/10 | 0/10 | 5/10 | 1/10 | 3/10 | `v7` | 5/10 |
| `gpt-4.1` | 5/10 | 5/10 | 4/10 | 4/10 | 4/10 | 3/10 | `v5` | 5/10 |
| `gpt-4o-mini` | 3/10 | 2/10 | 2/10 | 4/10 | 2/10 | 3/10 | `v7` | 4/10 |
| `grok-4-1-fast-non-reasoning` | 0/10 | 2/10 | 4/10 | 4/10 | 1/10 | 1/10 | `v6` | 4/10 |

## Conclusion

`gpt-5.5` is the best overall model: it reaches 10/10 with several prompts. `gpt-5.6-terra` comes second with 9/10 using `v9`.
