# Resumen Azure v9

Todas las corridas fueron evaluadas con el prompt `v9` (`Autocomplete simple few-shot`).

La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Comparación de modelos

| Modelo | Aciertos | Exactitud | JSON válido | Opción consistente | Latencia media | Errores |
|---|---:|---:|---:|---:|---:|---|
| `Llama-3.3-70B-Instruct` | 3/10 | 30.0% | 0/10 | 0/10 | 0.604s | P1 (18 -> 10), P5 (3 -> 2), P6 (60 -> 120), P7 (91 -> 71), P8 (360 -> 8), P9 (8 -> 7), P10 (34 -> 32) |
| `Mistral-Large-3` | 3/10 | 30.0% | 0/10 | 0/10 | 0.736s | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 3), P7 (91 -> 25), P8 (360 -> 180), P9 (8 -> 5), P10 (34 -> 29.5) |
| `gpt-4o-mini` | 3/10 | 30.0% | 0/10 | 0/10 | 0.991s | P1 (18 -> 6), P4 (600 -> 17), P5 (3 -> 7), P6 (60 -> 6), P7 (91 -> 10), P8 (360 -> 180), P9 (8 -> 2) |
| `gpt-4.1` | 3/10 | 30.0% | 0/10 | 0/10 | 1.219s | P1 (18 -> 6), P5 (3 -> 5), P6 (60 -> 80), P7 (91 -> 42), P8 (360 -> 120), P9 (8 -> 7), P10 (34 -> 35) |
| `gpt-5.4-mini` | 3/10 | 30.0% | 0/10 | 0/10 | 1.435s | P1 (18 -> 10), P5 (3 -> 7), P6 (60 -> 40), P7 (91 -> 7), P8 (360 -> 120), P9 (8 -> 2), P10 (34 -> 32) |
| `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 0/10 | 0/10 | 0.637s | P1 (18 -> 12), P3 (140 -> 28), P4 (600 -> 64), P5 (3 -> 7), P6 (60 -> 29), P7 (91 -> 70), P8 (360 -> 52), P9 (8 -> 29), P10 (34 -> 17) |

## Ranking global

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `Llama-3.3-70B-Instruct` | 3/10 | 30.0% | 0/10 | 0.604s |
| 2 | `Mistral-Large-3` | 3/10 | 30.0% | 0/10 | 0.736s |
| 3 | `gpt-4o-mini` | 3/10 | 30.0% | 0/10 | 0.991s |
| 4 | `gpt-4.1` | 3/10 | 30.0% | 0/10 | 1.219s |
| 5 | `gpt-5.4-mini` | 3/10 | 30.0% | 0/10 | 1.435s |
| 6 | `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 0/10 | 0.637s |

## Detalle de errores

| Modelo | Problema | Esperado | Predicho | JSON válido |
|---|---:|---:|---:|---|
| `Llama-3.3-70B-Instruct` | 1 | 18 | 10 | no |
| `Llama-3.3-70B-Instruct` | 5 | 3 | 2 | no |
| `Llama-3.3-70B-Instruct` | 6 | 60 | 120 | no |
| `Llama-3.3-70B-Instruct` | 7 | 91 | 71 | no |
| `Llama-3.3-70B-Instruct` | 8 | 360 | 8 | no |
| `Llama-3.3-70B-Instruct` | 9 | 8 | 7 | no |
| `Llama-3.3-70B-Instruct` | 10 | 34 | 32 | no |
| `Mistral-Large-3` | 1 | 18 | 10 | no |
| `Mistral-Large-3` | 5 | 3 | 10 | no |
| `Mistral-Large-3` | 6 | 60 | 3 | no |
| `Mistral-Large-3` | 7 | 91 | 25 | no |
| `Mistral-Large-3` | 8 | 360 | 180 | no |
| `Mistral-Large-3` | 9 | 8 | 5 | no |
| `Mistral-Large-3` | 10 | 34 | 29.5 | no |
| `gpt-4o-mini` | 1 | 18 | 6 | no |
| `gpt-4o-mini` | 4 | 600 | 17 | no |
| `gpt-4o-mini` | 5 | 3 | 7 | no |
| `gpt-4o-mini` | 6 | 60 | 6 | no |
| `gpt-4o-mini` | 7 | 91 | 10 | no |
| `gpt-4o-mini` | 8 | 360 | 180 | no |
| `gpt-4o-mini` | 9 | 8 | 2 | no |
| `gpt-4.1` | 1 | 18 | 6 | no |
| `gpt-4.1` | 5 | 3 | 5 | no |
| `gpt-4.1` | 6 | 60 | 80 | no |
| `gpt-4.1` | 7 | 91 | 42 | no |
| `gpt-4.1` | 8 | 360 | 120 | no |
| `gpt-4.1` | 9 | 8 | 7 | no |
| `gpt-4.1` | 10 | 34 | 35 | no |
| `gpt-5.4-mini` | 1 | 18 | 10 | no |
| `gpt-5.4-mini` | 5 | 3 | 7 | no |
| `gpt-5.4-mini` | 6 | 60 | 40 | no |
| `gpt-5.4-mini` | 7 | 91 | 7 | no |
| `gpt-5.4-mini` | 8 | 360 | 120 | no |
| `gpt-5.4-mini` | 9 | 8 | 2 | no |
| `gpt-5.4-mini` | 10 | 34 | 32 | no |
| `grok-4-1-fast-non-reasoning` | 1 | 18 | 12 | no |
| `grok-4-1-fast-non-reasoning` | 3 | 140 | 28 | no |
| `grok-4-1-fast-non-reasoning` | 4 | 600 | 64 | no |
| `grok-4-1-fast-non-reasoning` | 5 | 3 | 7 | no |
| `grok-4-1-fast-non-reasoning` | 6 | 60 | 29 | no |
| `grok-4-1-fast-non-reasoning` | 7 | 91 | 70 | no |
| `grok-4-1-fast-non-reasoning` | 8 | 360 | 52 | no |
| `grok-4-1-fast-non-reasoning` | 9 | 8 | 29 | no |
| `grok-4-1-fast-non-reasoning` | 10 | 34 | 17 | no |

## Conclusión

El mejor resultado fue `Llama-3.3-70B-Instruct` con 3/10.
