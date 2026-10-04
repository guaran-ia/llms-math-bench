# Comparación Azure v4 a v9

Comparación para el equipo sobre los prompts `v4`, `v5`, `v6`, `v7`, `v8` y `v9` en los modelos Azure/GuaranIA.

La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Resumen Ejecutivo

- `v4` conserva el mejor techo individual: `gpt-5.4-mini` llegó a 6/10.
- `v7` mejora la robustez de modelos débiles, especialmente `grok`, `Mistral` y `gpt-4o-mini`, pero baja el techo máximo a 5/10.
- `v5` y `v6` no superan a `v4` en techo máximo; ambos quedan con máximo 5/10.
- `v8` y `v9` prueban el modo autocomplete simple; no superan a los prompts estructurados.
- El warmup/few-shot ayuda a algunos modelos, pero no corrige los problemas recurrentes P1, P5, P6, P7 y P8.

## Matriz v4-v9

| Modelo | v4 | v5 | v6 | v7 | v8 | v9 | Mejor prompt | Mejor resultado |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| `gpt-5.4-mini` | 6/10 | 5/10 | 5/10 | 5/10 | 3/10 | 3/10 | `v4` | 6/10 |
| `Llama-3.3-70B-Instruct` | 4/10 | 4/10 | 5/10 | 4/10 | 2/10 | 3/10 | `v6` | 5/10 |
| `Mistral-Large-3` | 4/10 | 0/10 | 0/10 | 5/10 | 1/10 | 3/10 | `v7` | 5/10 |
| `gpt-4.1` | 5/10 | 5/10 | 4/10 | 4/10 | 4/10 | 3/10 | `v5` | 5/10 |
| `gpt-4o-mini` | 3/10 | 2/10 | 2/10 | 4/10 | 2/10 | 3/10 | `v7` | 4/10 |
| `grok-4-1-fast-non-reasoning` | 0/10 | 2/10 | 4/10 | 4/10 | 1/10 | 1/10 | `v6` | 4/10 |

## Ranking Por Prompt

### v4

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 6/10 | 60.0% | 10/10 | 2.934s |
| 2 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 4.031s |
| 3 | `Mistral-Large-3` | 4/10 | 40.0% | 10/10 | 5.636s |
| 4 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 9/10 | 2.687s |
| 5 | `gpt-4o-mini` | 3/10 | 30.0% | 10/10 | 2.932s |
| 6 | `grok-4-1-fast-non-reasoning` | 0/10 | 0.0% | 6/10 | 31.346s |

### v5

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 2.717s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.729s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 2.500s |
| 4 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 2.751s |
| 5 | `grok-4-1-fast-non-reasoning` | 2/10 | 20.0% | 9/10 | 4.815s |
| 6 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 7.514s |

### v6

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 10/10 | 3.345s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.577s |
| 3 | `gpt-4.1` | 4/10 | 40.0% | 10/10 | 2.694s |
| 4 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 3.954s |
| 5 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.238s |
| 6 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 4.606s |

### v7

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.780s |
| 2 | `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 13.063s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 3.722s |
| 4 | `gpt-4o-mini` | 4/10 | 40.0% | 10/10 | 4.678s |
| 5 | `grok-4-1-fast-non-reasoning` | 4/10 | 40.0% | 10/10 | 4.945s |
| 6 | `gpt-4.1` | 4/10 | 40.0% | 9/10 | 3.698s |

### v8

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 4/10 | 40.0% | 0/10 | 2.146s |
| 2 | `gpt-5.4-mini` | 3/10 | 30.0% | 0/10 | 2.205s |
| 3 | `Llama-3.3-70B-Instruct` | 2/10 | 20.0% | 0/10 | 0.809s |
| 4 | `gpt-4o-mini` | 2/10 | 20.0% | 0/10 | 1.094s |
| 5 | `Mistral-Large-3` | 1/10 | 10.0% | 0/10 | 0.621s |
| 6 | `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 0/10 | 0.900s |

### v9

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `Llama-3.3-70B-Instruct` | 3/10 | 30.0% | 0/10 | 0.604s |
| 2 | `Mistral-Large-3` | 3/10 | 30.0% | 0/10 | 0.736s |
| 3 | `gpt-4o-mini` | 3/10 | 30.0% | 0/10 | 0.991s |
| 4 | `gpt-4.1` | 3/10 | 30.0% | 0/10 | 1.219s |
| 5 | `gpt-5.4-mini` | 3/10 | 30.0% | 0/10 | 1.435s |
| 6 | `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 0/10 | 0.637s |

## Comparación v5 vs v6

| Modelo | v5 | v6 | Delta | JSON v5 | JSON v6 | Latencia v5 | Latencia v6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grok-4-1-fast-non-reasoning` | 2/10 | 4/10 | +2 | 9/10 | 10/10 | 4.815s | 3.954s |
| `Llama-3.3-70B-Instruct` | 4/10 | 5/10 | +1 | 10/10 | 10/10 | 2.500s | 3.345s |
| `gpt-5.4-mini` | 5/10 | 5/10 | 0 | 10/10 | 10/10 | 3.729s | 3.577s |
| `gpt-4o-mini` | 2/10 | 2/10 | 0 | 10/10 | 10/10 | 2.751s | 3.238s |
| `Mistral-Large-3` | 0/10 | 0/10 | 0 | 0/10 | 0/10 | 7.514s | 4.606s |
| `gpt-4.1` | 5/10 | 4/10 | -1 | 10/10 | 10/10 | 2.717s | 2.694s |

### Cambios por problema v5 vs v6

| Modelo | Mejoró en v6 | Empeoró en v6 | Errores v6 |
|---|---|---|---|
| `Llama-3.3-70B-Instruct` | P2 | - | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 3), P7 (91 -> 45), P8 (360 -> 30) |
| `Mistral-Large-3` | - | - | P1 (18 -> 10), P2 (8 -> 8), P3 (140 -> 140), P4 (600 -> 600), P5 (3 -> 33), P6 (60 -> 4), P7 (91 -> 45), P8 (360 -> 120), P9 (8 -> 7), P10 (34 -> 34) |
| `gpt-4.1` | - | P9 | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 28), P7 (91 -> 28), P8 (360 -> 120), P9 (8 -> 7) |
| `gpt-4o-mini` | - | - | P1 (18 -> 6), P2 (8 -> 11), P4 (600 -> 67), P5 (3 -> 5), P6 (60 -> 4), P7 (91 -> 7), P8 (360 -> 180), P9 (8 -> 3) |
| `gpt-5.4-mini` | P6 | P4 | P1 (18 -> 6), P4 (600 -> 24), P5 (3 -> 5), P7 (91 -> 28), P8 (360 -> 120) |
| `grok-4-1-fast-non-reasoning` | P2, P3 | - | P1 (18 -> 6), P5 (3 -> 210), P6 (60 -> 2), P7 (91 -> 25), P8 (360 -> 180), P9 (8 -> 1) |

## Comparación v4 vs v7

| Modelo | v4 | v7 | Delta | JSON v4 | JSON v7 | Latencia v4 | Latencia v7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `grok-4-1-fast-non-reasoning` | 0/10 | 4/10 | +4 | 6/10 | 10/10 | 31.346s | 4.945s |
| `Mistral-Large-3` | 4/10 | 5/10 | +1 | 10/10 | 10/10 | 5.636s | 13.063s |
| `gpt-4o-mini` | 3/10 | 4/10 | +1 | 10/10 | 10/10 | 2.932s | 4.678s |
| `Llama-3.3-70B-Instruct` | 4/10 | 4/10 | 0 | 9/10 | 10/10 | 2.687s | 3.722s |
| `gpt-5.4-mini` | 6/10 | 5/10 | -1 | 10/10 | 10/10 | 2.934s | 3.780s |
| `gpt-4.1` | 5/10 | 4/10 | -1 | 10/10 | 9/10 | 4.031s | 3.698s |

### Cambios por problema v4 vs v7

| Modelo | Mejoró en v7 | Empeoró en v7 | Errores v7 |
|---|---|---|---|
| `Llama-3.3-70B-Instruct` | - | - | P1 (18 -> 10), P5 (3 -> 1), P6 (60 -> 21), P7 (91 -> 49), P8 (360 -> 66), P9 (8 -> 5) |
| `Mistral-Large-3` | P2 | - | P1 (18 -> 10), P5 (3 -> 11), P6 (60 -> 8), P7 (91 -> 35), P8 (360 -> 120) |
| `gpt-4.1` | P7 | P9, P10 | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 21), P8 (360 -> 120), P9 (8 -> 4), P10 (34 -> 4) |
| `gpt-4o-mini` | P5 | - | P1 (18 -> 10), P4 (600 -> 67), P6 (60 -> 6), P7 (91 -> 35), P8 (360 -> 120), P9 (8 -> 3) |
| `gpt-5.4-mini` | - | P6 | P1 (18 -> 10), P5 (3 -> 5), P6 (60 -> 420), P7 (91 -> 49), P8 (360 -> 120) |
| `grok-4-1-fast-non-reasoning` | P2, P3, P4, P10 | - | P1 (18 -> 10), P5 (3 -> 217), P6 (60 -> 32), P7 (91 -> 15), P8 (360 -> 180), P9 (8 -> 5) |

## Comparación v8 vs v9

| Modelo | v8 | v9 | Delta | JSON v8 | JSON v9 | Latencia v8 | Latencia v9 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Mistral-Large-3` | 1/10 | 3/10 | +2 | 0/10 | 0/10 | 0.621s | 0.736s |
| `gpt-4o-mini` | 2/10 | 3/10 | +1 | 0/10 | 0/10 | 1.094s | 0.991s |
| `Llama-3.3-70B-Instruct` | 2/10 | 3/10 | +1 | 0/10 | 0/10 | 0.809s | 0.604s |
| `gpt-5.4-mini` | 3/10 | 3/10 | 0 | 0/10 | 0/10 | 2.205s | 1.435s |
| `grok-4-1-fast-non-reasoning` | 1/10 | 1/10 | 0 | 0/10 | 0/10 | 0.900s | 0.637s |
| `gpt-4.1` | 4/10 | 3/10 | -1 | 0/10 | 0/10 | 2.146s | 1.219s |

### Cambios por problema v8 vs v9

| Modelo | Mejoró en v9 | Empeoró en v9 | Errores v9 |
|---|---|---|---|
| `Llama-3.3-70B-Instruct` | P2 | - | P1 (18 -> 10), P5 (3 -> 2), P6 (60 -> 120), P7 (91 -> 71), P8 (360 -> 8), P9 (8 -> 7), P10 (34 -> 32) |
| `Mistral-Large-3` | P2, P3 | - | P1 (18 -> 10), P5 (3 -> 10), P6 (60 -> 3), P7 (91 -> 25), P8 (360 -> 180), P9 (8 -> 5), P10 (34 -> 29.5) |
| `gpt-4.1` | - | P10 | P1 (18 -> 6), P5 (3 -> 5), P6 (60 -> 80), P7 (91 -> 42), P8 (360 -> 120), P9 (8 -> 7), P10 (34 -> 35) |
| `gpt-4o-mini` | P2 | - | P1 (18 -> 6), P4 (600 -> 17), P5 (3 -> 7), P6 (60 -> 6), P7 (91 -> 10), P8 (360 -> 180), P9 (8 -> 2) |
| `gpt-5.4-mini` | P2 | P10 | P1 (18 -> 10), P5 (3 -> 7), P6 (60 -> 40), P7 (91 -> 7), P8 (360 -> 120), P9 (8 -> 2), P10 (34 -> 32) |
| `grok-4-1-fast-non-reasoning` | P2 | P4 | P1 (18 -> 12), P3 (140 -> 28), P4 (600 -> 64), P5 (3 -> 7), P6 (60 -> 29), P7 (91 -> 70), P8 (360 -> 52), P9 (8 -> 29), P10 (34 -> 17) |

## Conclusión

Para maximizar el mejor resultado individual en Azure, `v4` sigue siendo el mejor baseline porque alcanza 6/10 con `gpt-5.4-mini`.

Para una comparación de robustez entre modelos, `v7` es interesante porque mejora varios modelos que rendían mal con `v4`, pero no mejora el mejor resultado absoluto.

Los prompts autocomplete simples (`v8` zero-shot y `v9` few-shot) rindieron peor que los prompts estructurados, por lo que no son buenos candidatos como baseline principal.
