# Reporte de acierto por modelo

## Resumen

- Archivo evaluado: `model_test_results_guarani_prompt_v2.jsonl`
- Intentos leídos: 60
- Intentos evaluados para ranking: 60
- Problemas únicos evaluados: 10
- Líneas JSONL inválidas: 0
- Modelo más acertado: **gpt-4.1**

El ranking principal usa el último intento disponible por cada par `(modelo, problem_id)` para evitar que problemas repetidos pesen dos veces.

## Ranking Principal

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | Aciertos recuperados | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | gpt-4.1 | 5/10 | 50.0% | 5/10 | 10/10 | 10/10 | 0 | 0 | 2.791s |
| 2 | Mistral-Large-3 | 5/10 | 50.0% | 5/10 | 10/10 | 10/10 | 0 | 0 | 5.099s |
| 3 | Llama-3.3-70B-Instruct | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 2.557s |
| 4 | gpt-5.4-mini | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 2.788s |
| 5 | gpt-4o-mini | 2/10 | 20.0% | 2/10 | 10/10 | 10/10 | 0 | 0 | 3.025s |
| 6 | grok-4-1-fast-non-reasoning | 2/10 | 20.0% | 2/10 | 9/10 | 9/10 | 0 | 1 | 13.146s |

## Detalle Por Problema

| Problema | Modelo | Esperado | Predicho | Estricto | Recuperado | JSON válido | Línea |
|---:|---|---:|---:|---|---|---|---:|
| 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | no | sí | 6 |
| 1 | Mistral-Large-3 | 18 | 10 | no | no | sí | 5 |
| 1 | gpt-4.1 | 18 | 10 | no | no | sí | 2 |
| 1 | gpt-4o-mini | 18 | 10 | no | no | sí | 3 |
| 1 | gpt-5.4-mini | 18 | 10 | no | no | sí | 1 |
| 1 | grok-4-1-fast-non-reasoning | 18 | 6 | no | no | sí | 4 |
| 2 | Llama-3.3-70B-Instruct | 8 | 7 | no | no | sí | 12 |
| 2 | Mistral-Large-3 | 8 | 20 | no | no | sí | 11 |
| 2 | gpt-4.1 | 8 | 8 | sí | sí | sí | 8 |
| 2 | gpt-4o-mini | 8 | 7 | no | no | sí | 9 |
| 2 | gpt-5.4-mini | 8 | 14 | no | no | sí | 7 |
| 2 | grok-4-1-fast-non-reasoning | 8 | 7 | no | no | sí | 10 |
| 3 | Llama-3.3-70B-Instruct | 140 | 140 | sí | sí | sí | 18 |
| 3 | Mistral-Large-3 | 140 | 140 | sí | sí | sí | 17 |
| 3 | gpt-4.1 | 140 | 140 | sí | sí | sí | 14 |
| 3 | gpt-4o-mini | 140 | 140 | sí | sí | sí | 15 |
| 3 | gpt-5.4-mini | 140 | 140 | sí | sí | sí | 13 |
| 3 | grok-4-1-fast-non-reasoning | 140 | 2 | no | no | sí | 16 |
| 4 | Llama-3.3-70B-Instruct | 600 | 600 | sí | sí | sí | 24 |
| 4 | Mistral-Large-3 | 600 | 600 | sí | sí | sí | 23 |
| 4 | gpt-4.1 | 600 | 600 | sí | sí | sí | 20 |
| 4 | gpt-4o-mini | 600 | 67 | no | no | sí | 21 |
| 4 | gpt-5.4-mini | 600 | 600 | sí | sí | sí | 19 |
| 4 | grok-4-1-fast-non-reasoning | 600 | 600 | sí | sí | sí | 22 |
| 5 | Llama-3.3-70B-Instruct | 3 | 2 | no | no | sí | 30 |
| 5 | Mistral-Large-3 | 3 | 90 | no | no | sí | 29 |
| 5 | gpt-4.1 | 3 | 1 | no | no | sí | 26 |
| 5 | gpt-4o-mini | 3 | 9 | no | no | sí | 27 |
| 5 | gpt-5.4-mini | 3 | 5 | no | no | sí | 25 |
| 5 | grok-4-1-fast-non-reasoning | 3 | 175 | no | no | sí | 28 |
| 6 | Llama-3.3-70B-Instruct | 60 | 3 | no | no | sí | 36 |
| 6 | Mistral-Large-3 | 60 | 5 | no | no | sí | 35 |
| 6 | gpt-4.1 | 60 | 28 | no | no | sí | 32 |
| 6 | gpt-4o-mini | 60 | 5 | no | no | sí | 33 |
| 6 | gpt-5.4-mini | 60 | 40 | no | no | sí | 31 |
| 6 | grok-4-1-fast-non-reasoning | 60 | None | no | no | no | 34 |
| 7 | Llama-3.3-70B-Instruct | 91 | 35 | no | no | sí | 42 |
| 7 | Mistral-Large-3 | 91 | 27 | no | no | sí | 41 |
| 7 | gpt-4.1 | 91 | 70 | no | no | sí | 38 |
| 7 | gpt-4o-mini | 91 | 7 | no | no | sí | 39 |
| 7 | gpt-5.4-mini | 91 | 35 | no | no | sí | 37 |
| 7 | grok-4-1-fast-non-reasoning | 91 | 10 | no | no | sí | 40 |
| 8 | Llama-3.3-70B-Instruct | 360 | 30 | no | no | sí | 48 |
| 8 | Mistral-Large-3 | 360 | 360 | sí | sí | sí | 47 |
| 8 | gpt-4.1 | 360 | 120 | no | no | sí | 44 |
| 8 | gpt-4o-mini | 360 | 30 | no | no | sí | 45 |
| 8 | gpt-5.4-mini | 360 | 120 | no | no | sí | 43 |
| 8 | grok-4-1-fast-non-reasoning | 360 | 120 | no | no | sí | 46 |
| 9 | Llama-3.3-70B-Instruct | 8 | 8 | sí | sí | sí | 54 |
| 9 | Mistral-Large-3 | 8 | 8 | sí | sí | sí | 53 |
| 9 | gpt-4.1 | 8 | 8 | sí | sí | sí | 50 |
| 9 | gpt-4o-mini | 8 | 6 | no | no | sí | 51 |
| 9 | gpt-5.4-mini | 8 | 8 | sí | sí | sí | 49 |
| 9 | grok-4-1-fast-non-reasoning | 8 | 4 | no | no | sí | 52 |
| 10 | Llama-3.3-70B-Instruct | 34 | 34 | sí | sí | sí | 60 |
| 10 | Mistral-Large-3 | 34 | 34 | sí | sí | sí | 59 |
| 10 | gpt-4.1 | 34 | 34 | sí | sí | sí | 56 |
| 10 | gpt-4o-mini | 34 | 34 | sí | sí | sí | 57 |
| 10 | gpt-5.4-mini | 34 | 34 | sí | sí | sí | 55 |
| 10 | grok-4-1-fast-non-reasoning | 34 | 34 | sí | sí | sí | 58 |
