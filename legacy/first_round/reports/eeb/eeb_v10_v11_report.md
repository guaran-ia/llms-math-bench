# Guaraní Mathematics Evaluation Report

## Summary

- Evaluated file: `model_test_results_3er_grado_v10_v11.jsonl`
- Attempts read: 320
- Invalid JSONL lines: 0
- Best combination: **azure-services-responses / gpt-5.5 / v11** (20/20)

## Ranking by Model and Prompt

| Rank | Provider | Model | Prompt | Correct answers | Accuracy | Valid JSON | API errors | JSON errors | Mean latency |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | azure-services-responses | gpt-5.5 | v11 | 20/20 | 100.0% | 20/20 | 0 | 0 | 4.211s |
| 2 | azure-services-responses | gpt-5.5 | v10 | 20/20 | 100.0% | 20/20 | 0 | 0 | 4.228s |
| 3 | azure-services-responses | gpt-5.6-terra | v11 | 19/20 | 95.0% | 20/20 | 0 | 0 | 3.104s |
| 4 | azure-services-responses | gpt-5.6-terra | v10 | 19/20 | 95.0% | 20/20 | 0 | 0 | 3.429s |
| 5 | azure | gpt-4.1 | v11 | 18/20 | 90.0% | 20/20 | 0 | 0 | 2.555s |
| 6 | azure | gpt-5.4-mini | v11 | 17/20 | 85.0% | 20/20 | 0 | 0 | 3.135s |
| 7 | azure | gpt-5.4-mini | v10 | 15/20 | 75.0% | 20/20 | 0 | 0 | 2.962s |
| 8 | azure | gpt-4.1 | v10 | 15/20 | 75.0% | 17/20 | 0 | 3 | 2.572s |
| 9 | azure | Llama-3.3-70B-Instruct | v11 | 14/20 | 70.0% | 20/20 | 0 | 0 | 2.305s |
| 10 | azure | Mistral-Large-3 | v11 | 12/20 | 60.0% | 18/20 | 0 | 2 | 5.564s |
| 11 | azure | gpt-4o-mini | v11 | 11/20 | 55.0% | 20/20 | 0 | 0 | 2.095s |
| 12 | azure | grok-4-1-fast-non-reasoning | v11 | 11/20 | 55.0% | 20/20 | 0 | 0 | 3.161s |
| 13 | azure | Mistral-Large-3 | v10 | 8/20 | 40.0% | 19/20 | 0 | 1 | 5.930s |
| 14 | azure | Llama-3.3-70B-Instruct | v10 | 7/20 | 35.0% | 20/20 | 0 | 0 | 2.109s |
| 15 | azure | gpt-4o-mini | v10 | 7/20 | 35.0% | 20/20 | 0 | 0 | 3.545s |
| 16 | azure | grok-4-1-fast-non-reasoning | v10 | 7/20 | 35.0% | 20/20 | 0 | 0 | 4.153s |

## Final Comparison

| Model | v10 | v11 | Best prompt | Best result |
|---|---:|---:|---|---:|
| `Llama-3.3-70B-Instruct` | 7/20 | 14/20 | `v11` | 14/20 |
| `Mistral-Large-3` | 8/20 | 12/20 | `v11` | 12/20 |
| `gpt-4.1` | 15/20 | 18/20 | `v11` | 18/20 |
| `gpt-4o-mini` | 7/20 | 11/20 | `v11` | 11/20 |
| `gpt-5.4-mini` | 15/20 | 17/20 | `v11` | 17/20 |
| `gpt-5.5` | 20/20 | 20/20 | `v11` | 20/20 |
| `gpt-5.6-terra` | 19/20 | 19/20 | `v11` | 19/20 |
| `grok-4-1-fast-non-reasoning` | 7/20 | 11/20 | `v11` | 11/20 |
