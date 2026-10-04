# Comparación de prompts v1 a v4

## Resumen

Evaluación sobre 10 problemas matemáticos en guaraní y 6 modelos. La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

| Prompt | Archivo de resultados | Mejor modelo | Mejor acierto |
|---|---|---|---:|
| v1 | `model_test_results_guarani.jsonl` | `gpt-4.1` | 6/10 |
| v2 | `model_test_results_guarani_prompt_v2.jsonl` | `gpt-4.1` y `Mistral-Large-3` | 5/10 |
| v3 | `model_test_results_guarani_prompt_v3.jsonl` | `gpt-5.4-mini` | 6/10 |
| v4 | `model_test_results_guarani_prompt_v4.jsonl` | `gpt-5.4-mini` | 6/10 |

## Comparación Por Modelo

| Modelo | v1 | v2 | v3 | v4 | Mejor resultado |
|---|---:|---:|---:|---:|---:|
| `gpt-4.1` | 6/10 | 5/10 | 5/10 | 5/10 | 6/10 |
| `gpt-5.4-mini` | 5/10 | 4/10 | 6/10 | 6/10 | 6/10 |
| `Llama-3.3-70B-Instruct` | 5/10 | 4/10 | 5/10 | 4/10 | 5/10 |
| `Mistral-Large-3` | 4/10 | 5/10 | 4/10 | 4/10 | 5/10 |
| `grok-4-1-fast-non-reasoning` | 3/10 | 2/10 | 1/10 | 0/10 | 3/10 |
| `gpt-4o-mini` | 2/10 | 2/10 | 2/10 | 3/10 | 3/10 |

## Ranking Por Prompt

### v1

| Posición | Modelo | Aciertos |
|---:|---|---:|
| 1 | `gpt-4.1` | 6/10 |
| 2 | `gpt-5.4-mini` | 5/10 |
| 3 | `Llama-3.3-70B-Instruct` | 5/10 |
| 4 | `Mistral-Large-3` | 4/10 |
| 5 | `grok-4-1-fast-non-reasoning` | 3/10 |
| 6 | `gpt-4o-mini` | 2/10 |

### v2

| Posición | Modelo | Aciertos |
|---:|---|---:|
| 1 | `gpt-4.1` | 5/10 |
| 2 | `Mistral-Large-3` | 5/10 |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 |
| 4 | `gpt-5.4-mini` | 4/10 |
| 5 | `gpt-4o-mini` | 2/10 |
| 6 | `grok-4-1-fast-non-reasoning` | 2/10 |

### v3

| Posición | Modelo | Aciertos |
|---:|---|---:|
| 1 | `gpt-5.4-mini` | 6/10 |
| 2 | `Llama-3.3-70B-Instruct` | 5/10 |
| 3 | `gpt-4.1` | 5/10 |
| 4 | `Mistral-Large-3` | 4/10 |
| 5 | `gpt-4o-mini` | 2/10 |
| 6 | `grok-4-1-fast-non-reasoning` | 1/10 |

### v4

| Posición | Modelo | Aciertos |
|---:|---|---:|
| 1 | `gpt-5.4-mini` | 6/10 |
| 2 | `gpt-4.1` | 5/10 |
| 3 | `Mistral-Large-3` | 4/10 |
| 4 | `Llama-3.3-70B-Instruct` | 4/10 |
| 5 | `gpt-4o-mini` | 3/10 |
| 6 | `grok-4-1-fast-non-reasoning` | 0/10 |

## Conclusión

El mejor resultado absoluto fue 6/10, alcanzado por `gpt-4.1` con v1 y por `gpt-5.4-mini` con v3 y v4.

El prompt v3 parece el mejor candidato general: mantiene el máximo de 6/10 con `gpt-5.4-mini`, conserva 5/10 en `Llama-3.3-70B-Instruct` y no degrada tanto el formato JSON como v4.

El prompt v4 ayudó a `gpt-4o-mini`, pero perjudicó claramente a `grok-4-1-fast-non-reasoning` y bajó a `Llama-3.3-70B-Instruct`.
