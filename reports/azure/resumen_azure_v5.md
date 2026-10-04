# Resumen Azure v5

Todas las corridas fueron evaluadas con el prompt `v5` (`Guaraní estricto con JSON reforzado`).

La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Comparación de modelos

| Modelo | Aciertos | Exactitud | JSON válido | Opción consistente | Latencia media | Errores |
|---|---:|---:|---:|---:|---:|---|
| `gpt-4.1` | 5/10 | 50.0% | 10/10 | 10/10 | 2.717s | P1 (18 -> 10), P5 (3 -> 14), P6 (60 -> 61), P7 (91 -> 35), P8 (360 -> 120) |
| `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 10/10 | 3.729s | P1 (18 -> 10), P5 (3 -> 0), P6 (60 -> 40), P7 (91 -> 35), P8 (360 -> 120) |
| `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 10/10 | 2.500s | P1 (18 -> 10), P2 (8 -> 20), P5 (3 -> 2), P6 (60 -> 21), P7 (91 -> 49), P8 (360 -> 30) |
| `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 10/10 | 2.751s | P1 (18 -> 10), P2 (8 -> 7), P4 (600 -> 67), P5 (3 -> 4), P6 (60 -> 3), P7 (91 -> 5), P8 (360 -> 180), P9 (8 -> 3) |
| `grok-4-1-fast-non-reasoning` | 2/10 | 20.0% | 9/10 | 9/10 | 4.815s | P1 (18 -> 6), P2 (8 -> 2), P3 (140 -> 14), P5 (3 -> 210), P6 (60 -> 2), P7 (91 -> 20), P8 (360 -> None), P9 (8 -> 1) |
| `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 10/10 | 7.514s | P1 (18 -> 6), P2 (8 -> 20), P3 (140 -> 140), P4 (600 -> 600), P5 (3 -> 4), P6 (60 -> 3), P7 (91 -> 43), P8 (360 -> 360), P9 (8 -> 8), P10 (34 -> 34) |

## Ranking global

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 2.717s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.729s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 2.500s |
| 4 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 2.751s |
| 5 | `grok-4-1-fast-non-reasoning` | 2/10 | 20.0% | 9/10 | 4.815s |
| 6 | `Mistral-Large-3` | 0/10 | 0.0% | 0/10 | 7.514s |

## Detalle de errores

| Modelo | Problema | Esperado | Predicho | JSON válido |
|---|---:|---:|---:|---|
| `gpt-4.1` | 1 | 18 | 10 | sí |
| `gpt-4.1` | 5 | 3 | 14 | sí |
| `gpt-4.1` | 6 | 60 | 61 | sí |
| `gpt-4.1` | 7 | 91 | 35 | sí |
| `gpt-4.1` | 8 | 360 | 120 | sí |
| `gpt-5.4-mini` | 1 | 18 | 10 | sí |
| `gpt-5.4-mini` | 5 | 3 | 0 | sí |
| `gpt-5.4-mini` | 6 | 60 | 40 | sí |
| `gpt-5.4-mini` | 7 | 91 | 35 | sí |
| `gpt-5.4-mini` | 8 | 360 | 120 | sí |
| `Llama-3.3-70B-Instruct` | 1 | 18 | 10 | sí |
| `Llama-3.3-70B-Instruct` | 2 | 8 | 20 | sí |
| `Llama-3.3-70B-Instruct` | 5 | 3 | 2 | sí |
| `Llama-3.3-70B-Instruct` | 6 | 60 | 21 | sí |
| `Llama-3.3-70B-Instruct` | 7 | 91 | 49 | sí |
| `Llama-3.3-70B-Instruct` | 8 | 360 | 30 | sí |
| `gpt-4o-mini` | 1 | 18 | 10 | sí |
| `gpt-4o-mini` | 2 | 8 | 7 | sí |
| `gpt-4o-mini` | 4 | 600 | 67 | sí |
| `gpt-4o-mini` | 5 | 3 | 4 | sí |
| `gpt-4o-mini` | 6 | 60 | 3 | sí |
| `gpt-4o-mini` | 7 | 91 | 5 | sí |
| `gpt-4o-mini` | 8 | 360 | 180 | sí |
| `gpt-4o-mini` | 9 | 8 | 3 | sí |
| `grok-4-1-fast-non-reasoning` | 1 | 18 | 6 | sí |
| `grok-4-1-fast-non-reasoning` | 2 | 8 | 2 | sí |
| `grok-4-1-fast-non-reasoning` | 3 | 140 | 14 | sí |
| `grok-4-1-fast-non-reasoning` | 5 | 3 | 210 | sí |
| `grok-4-1-fast-non-reasoning` | 6 | 60 | 2 | sí |
| `grok-4-1-fast-non-reasoning` | 7 | 91 | 20 | sí |
| `grok-4-1-fast-non-reasoning` | 8 | 360 | None | no |
| `grok-4-1-fast-non-reasoning` | 9 | 8 | 1 | sí |
| `Mistral-Large-3` | 1 | 18 | 6 | no |
| `Mistral-Large-3` | 2 | 8 | 20 | no |
| `Mistral-Large-3` | 3 | 140 | 140 | no |
| `Mistral-Large-3` | 4 | 600 | 600 | no |
| `Mistral-Large-3` | 5 | 3 | 4 | no |
| `Mistral-Large-3` | 6 | 60 | 3 | no |
| `Mistral-Large-3` | 7 | 91 | 43 | no |
| `Mistral-Large-3` | 8 | 360 | 360 | no |
| `Mistral-Large-3` | 9 | 8 | 8 | no |
| `Mistral-Large-3` | 10 | 34 | 34 | no |

## Conclusión

El mejor resultado fue `gpt-4.1` con 5/10.
