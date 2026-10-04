# Reporte de prompts por modelo

## Resumen

- Archivo evaluado: `model_test_results_azure_v5.jsonl`
- Intentos leídos: 60
- Intentos evaluados para ranking: 60
- Líneas JSONL inválidas: 0
- Mejor combinación: **azure / gpt-4.1 / v5** (5/10)

## Ranking Por Prompt

| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | azure | gpt-4.1 | v5 | Guaraní estricto con JSON reforzado | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 2.717s |
| 2 | azure | gpt-5.4-mini | v5 | Guaraní estricto con JSON reforzado | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 3.729s |
| 3 | azure | Llama-3.3-70B-Instruct | v5 | Guaraní estricto con JSON reforzado | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 2.500s |
| 4 | azure | gpt-4o-mini | v5 | Guaraní estricto con JSON reforzado | 2/10 | 20.0% | 10/10 | 10/10 | 0 | 0 | 2.751s |
| 5 | azure | grok-4-1-fast-non-reasoning | v5 | Guaraní estricto con JSON reforzado | 2/10 | 20.0% | 9/10 | 9/10 | 0 | 1 | 4.815s |
| 6 | azure | Mistral-Large-3 | v5 | Guaraní estricto con JSON reforzado | 0/10 | 0.0% | 0/10 | 10/10 | 0 | 10 | 7.514s |

## Detalle Por Problema

| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |
|---|---:|---|---:|---:|---|---|---:|
| v5 | 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | sí | 6 |
| v5 | 1 | Mistral-Large-3 | 18 | 6 | no | no | 5 |
| v5 | 1 | gpt-4.1 | 18 | 10 | no | sí | 2 |
| v5 | 1 | gpt-4o-mini | 18 | 10 | no | sí | 3 |
| v5 | 1 | gpt-5.4-mini | 18 | 10 | no | sí | 1 |
| v5 | 1 | grok-4-1-fast-non-reasoning | 18 | 6 | no | sí | 4 |
| v5 | 2 | Llama-3.3-70B-Instruct | 8 | 20 | no | sí | 12 |
| v5 | 2 | Mistral-Large-3 | 8 | 20 | no | no | 11 |
| v5 | 2 | gpt-4.1 | 8 | 8 | sí | sí | 8 |
| v5 | 2 | gpt-4o-mini | 8 | 7 | no | sí | 9 |
| v5 | 2 | gpt-5.4-mini | 8 | 8 | sí | sí | 7 |
| v5 | 2 | grok-4-1-fast-non-reasoning | 8 | 2 | no | sí | 10 |
| v5 | 3 | Llama-3.3-70B-Instruct | 140 | 140 | sí | sí | 18 |
| v5 | 3 | Mistral-Large-3 | 140 | 140 | no | no | 17 |
| v5 | 3 | gpt-4.1 | 140 | 140 | sí | sí | 14 |
| v5 | 3 | gpt-4o-mini | 140 | 140 | sí | sí | 15 |
| v5 | 3 | gpt-5.4-mini | 140 | 140 | sí | sí | 13 |
| v5 | 3 | grok-4-1-fast-non-reasoning | 140 | 14 | no | sí | 16 |
| v5 | 4 | Llama-3.3-70B-Instruct | 600 | 600 | sí | sí | 24 |
| v5 | 4 | Mistral-Large-3 | 600 | 600 | no | no | 23 |
| v5 | 4 | gpt-4.1 | 600 | 600 | sí | sí | 20 |
| v5 | 4 | gpt-4o-mini | 600 | 67 | no | sí | 21 |
| v5 | 4 | gpt-5.4-mini | 600 | 600 | sí | sí | 19 |
| v5 | 4 | grok-4-1-fast-non-reasoning | 600 | 600 | sí | sí | 22 |
| v5 | 5 | Llama-3.3-70B-Instruct | 3 | 2 | no | sí | 30 |
| v5 | 5 | Mistral-Large-3 | 3 | 4 | no | no | 29 |
| v5 | 5 | gpt-4.1 | 3 | 14 | no | sí | 26 |
| v5 | 5 | gpt-4o-mini | 3 | 4 | no | sí | 27 |
| v5 | 5 | gpt-5.4-mini | 3 | 0 | no | sí | 25 |
| v5 | 5 | grok-4-1-fast-non-reasoning | 3 | 210 | no | sí | 28 |
| v5 | 6 | Llama-3.3-70B-Instruct | 60 | 21 | no | sí | 36 |
| v5 | 6 | Mistral-Large-3 | 60 | 3 | no | no | 35 |
| v5 | 6 | gpt-4.1 | 60 | 61 | no | sí | 32 |
| v5 | 6 | gpt-4o-mini | 60 | 3 | no | sí | 33 |
| v5 | 6 | gpt-5.4-mini | 60 | 40 | no | sí | 31 |
| v5 | 6 | grok-4-1-fast-non-reasoning | 60 | 2 | no | sí | 34 |
| v5 | 7 | Llama-3.3-70B-Instruct | 91 | 49 | no | sí | 42 |
| v5 | 7 | Mistral-Large-3 | 91 | 43 | no | no | 41 |
| v5 | 7 | gpt-4.1 | 91 | 35 | no | sí | 38 |
| v5 | 7 | gpt-4o-mini | 91 | 5 | no | sí | 39 |
| v5 | 7 | gpt-5.4-mini | 91 | 35 | no | sí | 37 |
| v5 | 7 | grok-4-1-fast-non-reasoning | 91 | 20 | no | sí | 40 |
| v5 | 8 | Llama-3.3-70B-Instruct | 360 | 30 | no | sí | 48 |
| v5 | 8 | Mistral-Large-3 | 360 | 360 | no | no | 47 |
| v5 | 8 | gpt-4.1 | 360 | 120 | no | sí | 44 |
| v5 | 8 | gpt-4o-mini | 360 | 180 | no | sí | 45 |
| v5 | 8 | gpt-5.4-mini | 360 | 120 | no | sí | 43 |
| v5 | 8 | grok-4-1-fast-non-reasoning | 360 | None | no | no | 46 |
| v5 | 9 | Llama-3.3-70B-Instruct | 8 | 8 | sí | sí | 54 |
| v5 | 9 | Mistral-Large-3 | 8 | 8 | no | no | 53 |
| v5 | 9 | gpt-4.1 | 8 | 8 | sí | sí | 50 |
| v5 | 9 | gpt-4o-mini | 8 | 3 | no | sí | 51 |
| v5 | 9 | gpt-5.4-mini | 8 | 8 | sí | sí | 49 |
| v5 | 9 | grok-4-1-fast-non-reasoning | 8 | 1 | no | sí | 52 |
| v5 | 10 | Llama-3.3-70B-Instruct | 34 | 34 | sí | sí | 60 |
| v5 | 10 | Mistral-Large-3 | 34 | 34 | no | no | 59 |
| v5 | 10 | gpt-4.1 | 34 | 34 | sí | sí | 56 |
| v5 | 10 | gpt-4o-mini | 34 | 34 | sí | sí | 57 |
| v5 | 10 | gpt-5.4-mini | 34 | 34 | sí | sí | 55 |
| v5 | 10 | grok-4-1-fast-non-reasoning | 34 | 34 | sí | sí | 58 |
