# Resumen Claude v5

Todas las corridas fueron evaluadas con el prompt `v5` (`Guaraní estricto con JSON reforzado`).

La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Comparación de modelos

| Modelo/Corrida | Modelo reportado | Prompt | Aciertos | Exactitud | JSON válido | Opción consistente | Errores |
|---|---|---|---:|---:|---:|---:|---|
| `sonnet5_extra` | `claude-sonnet-5` | `v5` | 9/10 | 90.0% | 10/10 | 10/10 | P6 (60 -> 30) |
| `sonnet5_hard` | `gpt-5` | `v5` | 8/10 | 80.0% | 10/10 | 10/10 | P6 (60 -> 2.5), P8 (360 -> 120) |
| `sonnet5_medium` | `gpt-5` | `v5` | 7/10 | 70.0% | 10/10 | 10/10 | P1 (18 -> 10), P3 (140 -> 280), P6 (60 -> 3) |

## Ranking global

| Posición | Modelo/Corrida | Aciertos estrictos | Exactitud estricta | JSON válido | Errores |
|---:|---|---:|---:|---:|---|
| 1 | `sonnet5_extra` | 9/10 | 90.0% | 10/10 | P6 (60 -> 30) |
| 2 | `sonnet5_hard` | 8/10 | 80.0% | 10/10 | P6 (60 -> 2.5), P8 (360 -> 120) |
| 3 | `sonnet5_medium` | 7/10 | 70.0% | 10/10 | P1 (18 -> 10), P3 (140 -> 280), P6 (60 -> 3) |

## Detalle de errores

| Modelo/Corrida | Problema | Esperado | Predicho |
|---|---:|---:|---:|
| `sonnet5_extra` | 6 | 60 | 30 |
| `sonnet5_hard` | 6 | 60 | 2.5 |
| `sonnet5_hard` | 8 | 360 | 120 |
| `sonnet5_medium` | 1 | 18 | 10 |
| `sonnet5_medium` | 3 | 140 | 280 |
| `sonnet5_medium` | 6 | 60 | 3 |

## Conclusión

El mejor resultado fue `sonnet5_extra` con 9/10.
