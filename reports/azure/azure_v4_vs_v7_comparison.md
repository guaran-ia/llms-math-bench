# Comparación Azure v4 vs v7

La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Resumen por modelo

| Modelo | v4 | v7 | Delta | JSON v4 | JSON v7 | Latencia v4 | Latencia v7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grok-4-1-fast-non-reasoning` | 0/10 | 4/10 | +4 | 6/10 | 10/10 | 31.346s | 4.945s |
| `Mistral-Large-3` | 4/10 | 5/10 | +1 | 10/10 | 10/10 | 5.636s | 13.063s |
| `gpt-4o-mini` | 3/10 | 4/10 | +1 | 10/10 | 10/10 | 2.932s | 4.678s |
| `Llama-3.3-70B-Instruct` | 4/10 | 4/10 | 0 | 9/10 | 10/10 | 2.687s | 3.722s |
| `gpt-5.4-mini` | 6/10 | 5/10 | -1 | 10/10 | 10/10 | 2.934s | 3.780s |
| `gpt-4.1` | 5/10 | 4/10 | -1 | 10/10 | 9/10 | 4.031s | 3.698s |

## Ranking v7

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.780s |
| 2 | `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 13.063s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 3.722s |
| 4 | `gpt-4o-mini` | 4/10 | 40.0% | 10/10 | 4.678s |
| 5 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 4.945s |
| 6 | `gpt-4.1` | 4/10 | 40.0% | 9/10 | 3.698s |

## Cambios por problema

| Modelo | Mejoró en v7 | Empeoró en v7 | Errores v7 |
|---|---|---|---|
| `grok-4-1-fast-non-reasoning` | P2, P3, P4, P10 | - | P1 (18 -> 10), P5 (3 -> 217), P6 (60 -> 32), P7 (91 -> 15), P8 (360 -> 180), P9 (8 -> 5) |
| `Mistral-Large-3` | P2 | - | P1 (18 -> 10), P5 (3 -> 11), P6 (60 -> 8), P7 (91 -> 35), P8 (360 -> 120) |
| `gpt-4o-mini` | P5 | - | P1 (18 -> 10), P4 (600 -> 67), P6 (60 -> 6), P7 (91 -> 35), P8 (360 -> 120), P9 (8 -> 3) |
| `Llama-3.3-70B-Instruct` | - | - | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 21), P7 (91 -> 49), P8 (360 -> 66), P9 (8 -> 5) |
| `gpt-5.4-mini` | - | P6 | P1 (18 -> 10), P5 (3 -> 5), P6 (60 -> 420), P7 (91 -> 49), P8 (360 -> 120) |
| `gpt-4.1` | P7 | P9, P10 | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 21), P8 (360 -> 120), P9 (8 -> 4), P10 (34 -> None) |

## Conclusión

El mejor resultado en `v7` fue `gpt-5.4-mini` con 5/10.
