# Resumen Azure v7

Todas las corridas fueron evaluadas con el prompt `v7` (`Profesor bilingüe con glosario y warmup`).

La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Comparación de modelos

| Modelo | Aciertos | Exactitud | JSON válido | Opción consistente | Latencia media | Errores |
|---|---:|---:|---:|---:|---:|---|
| `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 10/10 | 3.780s | P1 (18 -> 10), P5 (3 -> 5), P6 (60 -> 420), P7 (91 -> 49), P8 (360 -> 120) |
| `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 10/10 | 13.063s | P1 (18 -> 10), P5 (3 -> 11), P6 (60 -> 8), P7 (91 -> 35), P8 (360 -> 120) |
| `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 10/10 | 3.722s | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 21), P7 (91 -> 49), P8 (360 -> 66), P9 (8 -> 5) |
| `gpt-4o-mini` | 4/10 | 40.0% | 10/10 | 10/10 | 4.678s | P1 (18 -> 10), P4 (600 -> 67), P6 (60 -> 6), P7 (91 -> 35), P8 (360 -> 120), P9 (8 -> 3) |
| `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 10/10 | 4.945s | P1 (18 -> 10), P5 (3 -> 217), P6 (60 -> 32), P7 (91 -> 15), P8 (360 -> 180), P9 (8 -> 5) |
| `gpt-4.1` | 4/10 | 40.0% | 9/10 | 9/10 | 3.698s | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 21), P8 (360 -> 120), P9 (8 -> 4), P10 (34 -> None) |

## Ranking global

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.780s |
| 2 | `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 13.063s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 3.722s |
| 4 | `gpt-4o-mini` | 4/10 | 40.0% | 10/10 | 4.678s |
| 5 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 4.945s |
| 6 | `gpt-4.1` | 4/10 | 40.0% | 9/10 | 3.698s |

## Detalle de errores

| Modelo | Problema | Esperado | Predicho | JSON válido |
|---|---:|---:|---:|---|
| `gpt-5.4-mini` | 1 | 18 | 10 | sí |
| `gpt-5.4-mini` | 5 | 3 | 5 | sí |
| `gpt-5.4-mini` | 6 | 60 | 420 | sí |
| `gpt-5.4-mini` | 7 | 91 | 49 | sí |
| `gpt-5.4-mini` | 8 | 360 | 120 | sí |
| `Mistral-Large-3` | 1 | 18 | 10 | sí |
| `Mistral-Large-3` | 5 | 3 | 11 | sí |
| `Mistral-Large-3` | 6 | 60 | 8 | sí |
| `Mistral-Large-3` | 7 | 91 | 35 | sí |
| `Mistral-Large-3` | 8 | 360 | 120 | sí |
| `Llama-3.3-70B-Instruct` | 1 | 18 | 10 | sí |
| `Llama-3.3-70B-Instruct` | 5 | 3 | 1 | sí |
| `Llama-3.3-70B-Instruct` | 6 | 60 | 21 | sí |
| `Llama-3.3-70B-Instruct` | 7 | 91 | 49 | sí |
| `Llama-3.3-70B-Instruct` | 8 | 360 | 66 | sí |
| `Llama-3.3-70B-Instruct` | 9 | 8 | 5 | sí |
| `gpt-4o-mini` | 1 | 18 | 10 | sí |
| `gpt-4o-mini` | 4 | 600 | 67 | sí |
| `gpt-4o-mini` | 6 | 60 | 6 | sí |
| `gpt-4o-mini` | 7 | 91 | 35 | sí |
| `gpt-4o-mini` | 8 | 360 | 120 | sí |
| `gpt-4o-mini` | 9 | 8 | 3 | sí |
| `grok-4-1-fast-non-reasoning` | 1 | 18 | 10 | sí |
| `grok-4-1-fast-non-reasoning` | 5 | 3 | 217 | sí |
| `grok-4-1-fast-non-reasoning` | 6 | 60 | 32 | sí |
| `grok-4-1-fast-non-reasoning` | 7 | 91 | 15 | sí |
| `grok-4-1-fast-non-reasoning` | 8 | 360 | 180 | sí |
| `grok-4-1-fast-non-reasoning` | 9 | 8 | 5 | sí |
| `gpt-4.1` | 1 | 18 | 10 | sí |
| `gpt-4.1` | 5 | 3 | 10 | sí |
| `gpt-4.1` | 6 | 60 | 21 | sí |
| `gpt-4.1` | 8 | 360 | 120 | sí |
| `gpt-4.1` | 9 | 8 | 4 | sí |
| `gpt-4.1` | 10 | 34 | None | no |

## Conclusión

El mejor resultado fue `gpt-5.4-mini` con 5/10.
