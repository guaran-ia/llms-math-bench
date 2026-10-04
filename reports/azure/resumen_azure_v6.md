# Resumen Azure v6

Todas las corridas fueron evaluadas con el prompt `v6` (`Guaraní estricto con JSON reforzado y warmup`).

La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Comparación de modelos

| Modelo | Aciertos | Exactitud | JSON válido | Opción consistente | Latencia media | Errores |
|---|---:|---:|---:|---:|---:|---|
| `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 10/10 | 10/10 | 3.345s | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 3), P7 (91 -> 45), P8 (360 -> 30) |
| `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 10/10 | 3.577s | P1 (18 -> 6), P4 (600 -> 24), P5 (3 -> 5), P7 (91 -> 28), P8 (360 -> 120) |
| `gpt-4.1` | 4/10 | 40.0% | 10/10 | 10/10 | 2.694s | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 28), P7 (91 -> 28), P8 (360 -> 120), P9 (8 -> 7) |
| `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 10/10 | 3.954s | P1 (18 -> 6), P5 (3 -> 210), P6 (60 -> 2), P7 (91 -> 25), P8 (360 -> 180), P9 (8 -> 1) |
| `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 10/10 | 3.238s | P1 (18 -> 6), P2 (8 -> 11), P4 (600 -> 67), P5 (3 -> 5), P6 (60 -> 4), P7 (91 -> 7), P8 (360 -> 180), P9 (8 -> 3) |
| `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 10/10 | 4.606s | P1 (18 -> 10), P2 (8 -> 8), P3 (140 -> 140), P4 (600 -> 600), P5 (3 -> 33), P6 (60 -> 4), P7 (91 -> 45), P8 (360 -> 120), P9 (8 -> 7), P10 (34 -> 34) |

## Ranking global

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 10/10 | 3.345s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.577s |
| 3 | `gpt-4.1` | 4/10 | 40.0% | 10/10 | 2.694s |
| 4 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 3.954s |
| 5 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.238s |
| 6 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 4.606s |

## Detalle de errores

| Modelo | Problema | Esperado | Predicho | JSON válido |
|---|---:|---:|---:|---|
| `Llama-3.3-70B-Instruct` | 1 | 18 | 10 | sí |
| `Llama-3.3-70B-Instruct` | 5 | 3 | 1 | sí |
| `Llama-3.3-70B-Instruct` | 6 | 60 | 3 | sí |
| `Llama-3.3-70B-Instruct` | 7 | 91 | 45 | sí |
| `Llama-3.3-70B-Instruct` | 8 | 360 | 30 | sí |
| `gpt-5.4-mini` | 1 | 18 | 6 | sí |
| `gpt-5.4-mini` | 4 | 600 | 24 | sí |
| `gpt-5.4-mini` | 5 | 3 | 5 | sí |
| `gpt-5.4-mini` | 7 | 91 | 28 | sí |
| `gpt-5.4-mini` | 8 | 360 | 120 | sí |
| `gpt-4.1` | 1 | 18 | 10 | sí |
| `gpt-4.1` | 5 | 3 | 10 | sí |
| `gpt-4.1` | 6 | 60 | 28 | sí |
| `gpt-4.1` | 7 | 91 | 28 | sí |
| `gpt-4.1` | 8 | 360 | 120 | sí |
| `gpt-4.1` | 9 | 8 | 7 | sí |
| `grok-4-1-fast-non-reasoning` | 1 | 18 | 6 | sí |
| `grok-4-1-fast-non-reasoning` | 5 | 3 | 210 | sí |
| `grok-4-1-fast-non-reasoning` | 6 | 60 | 2 | sí |
| `grok-4-1-fast-non-reasoning` | 7 | 91 | 25 | sí |
| `grok-4-1-fast-non-reasoning` | 8 | 360 | 180 | sí |
| `grok-4-1-fast-non-reasoning` | 9 | 8 | 1 | sí |
| `gpt-4o-mini` | 1 | 18 | 6 | sí |
| `gpt-4o-mini` | 2 | 8 | 11 | sí |
| `gpt-4o-mini` | 4 | 600 | 67 | sí |
| `gpt-4o-mini` | 5 | 3 | 5 | sí |
| `gpt-4o-mini` | 6 | 60 | 4 | sí |
| `gpt-4o-mini` | 7 | 91 | 7 | sí |
| `gpt-4o-mini` | 8 | 360 | 180 | sí |
| `gpt-4o-mini` | 9 | 8 | 3 | sí |
| `Mistral-Large-3` | 1 | 18 | 10 | no |
| `Mistral-Large-3` | 2 | 8 | 8 | no |
| `Mistral-Large-3` | 3 | 140 | 140 | no |
| `Mistral-Large-3` | 4 | 600 | 600 | no |
| `Mistral-Large-3` | 5 | 3 | 33 | no |
| `Mistral-Large-3` | 6 | 60 | 4 | no |
| `Mistral-Large-3` | 7 | 91 | 45 | no |
| `Mistral-Large-3` | 8 | 360 | 120 | no |
| `Mistral-Large-3` | 9 | 8 | 7 | no |
| `Mistral-Large-3` | 10 | 34 | 34 | no |

## Conclusión

El mejor resultado fue `Llama-3.3-70B-Instruct` con 5/10.
