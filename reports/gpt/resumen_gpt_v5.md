# Resumen GPT v5

Todas las corridas fueron evaluadas con el prompt `v5` (`Guaraní estricto con JSON reforzado`).

La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Comparación de modelos

| Modelo/Corrida | Prompt | Aciertos | Exactitud | JSON válido | Opción consistente | Errores |
|---|---|---:|---:|---:|---:|---|
| `gpt6_lite` | `v5` | 10/10 | 100.0% | 10/10 | 10/10 | ninguno |
| `gpt5.6sol_lite` | `v5` | 9/10 | 90.0% | 10/10 | 10/10 | P8 (360 -> 300) |
| `gpt5.6sol_medium` | `v5` | 9/10 | 90.0% | 10/10 | 10/10 | P1 (18 -> 10) |
| `gpt5.5_medium` | `v5` | 8/10 | 80.0% | 10/10 | 10/10 | P1 (18 -> 10), P5 (3 -> 5) |
| `gpt5.6terra_lite` | `v5` | 8/10 | 80.0% | 10/10 | 10/10 | P1 (18 -> 10), P8 (360 -> 120) |

## Ranking global

| Posición | Modelo/Corrida | Aciertos estrictos | Exactitud estricta | JSON válido | Errores |
|---:|---|---:|---:|---:|---|
| 1 | `gpt6_lite` | 10/10 | 100.0% | 10/10 | ninguno |
| 2 | `gpt5.6sol_lite` | 9/10 | 90.0% | 10/10 | P8 (360 -> 300) |
| 3 | `gpt5.6sol_medium` | 9/10 | 90.0% | 10/10 | P1 (18 -> 10) |
| 4 | `gpt5.5_medium` | 8/10 | 80.0% | 10/10 | P1 (18 -> 10), P5 (3 -> 5) |
| 5 | `gpt5.6terra_lite` | 8/10 | 80.0% | 10/10 | P1 (18 -> 10), P8 (360 -> 120) |

## Detalle de errores

| Modelo/Corrida | Problema | Esperado | Predicho |
|---|---:|---:|---:|
| `gpt5.6sol_lite` | 8 | 360 | 300 |
| `gpt5.6sol_medium` | 1 | 18 | 10 |
| `gpt5.5_medium` | 1 | 18 | 10 |
| `gpt5.5_medium` | 5 | 3 | 5 |
| `gpt5.6terra_lite` | 1 | 18 | 10 |
| `gpt5.6terra_lite` | 8 | 360 | 120 |

## Conclusión

El mejor resultado fue `gpt6_lite` con 10/10.
