# Reporte de prompts por modelo

## Resumen

- Archivo evaluado: `model_test_results_azure_v7.jsonl`
- Intentos leídos: 60
- Intentos evaluados para ranking: 60
- Líneas JSONL inválidas: 0
- Mejor combinación: **azure / gpt-5.4-mini / v7** (5/10)

## Ranking Por Prompt

| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | azure | gpt-5.4-mini | v7 | Profesor bilingüe con glosario y warmup | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 3.780s |
| 2 | azure | Mistral-Large-3 | v7 | Profesor bilingüe con glosario y warmup | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 13.063s |
| 3 | azure | Llama-3.3-70B-Instruct | v7 | Profesor bilingüe con glosario y warmup | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 3.722s |
| 4 | azure | gpt-4o-mini | v7 | Profesor bilingüe con glosario y warmup | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 4.678s |
| 5 | azure | grok-4-1-fast-non-reasoning | v7 | Profesor bilingüe con glosario y warmup | 4/10 | 40.0% | 10/10 | 10/10 | 0 | 0 | 4.945s |
| 6 | azure | gpt-4.1 | v7 | Profesor bilingüe con glosario y warmup | 4/10 | 40.0% | 9/10 | 9/10 | 0 | 1 | 3.698s |

## Detalle Por Problema

| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |
|---|---:|---|---:|---:|---|---|---:|
| v7 | 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | sí | 6 |
| v7 | 1 | Mistral-Large-3 | 18 | 10 | no | sí | 5 |
| v7 | 1 | gpt-4.1 | 18 | 10 | no | sí | 2 |
| v7 | 1 | gpt-4o-mini | 18 | 10 | no | sí | 3 |
| v7 | 1 | gpt-5.4-mini | 18 | 10 | no | sí | 1 |
| v7 | 1 | grok-4-1-fast-non-reasoning | 18 | 10 | no | sí | 4 |
| v7 | 2 | Llama-3.3-70B-Instruct | 8 | 8 | sí | sí | 12 |
| v7 | 2 | Mistral-Large-3 | 8 | 8 | sí | sí | 11 |
| v7 | 2 | gpt-4.1 | 8 | 8 | sí | sí | 8 |
| v7 | 2 | gpt-4o-mini | 8 | 8 | sí | sí | 9 |
| v7 | 2 | gpt-5.4-mini | 8 | 8 | sí | sí | 7 |
| v7 | 2 | grok-4-1-fast-non-reasoning | 8 | 8 | sí | sí | 10 |
| v7 | 3 | Llama-3.3-70B-Instruct | 140 | 140 | sí | sí | 18 |
| v7 | 3 | Mistral-Large-3 | 140 | 140 | sí | sí | 17 |
| v7 | 3 | gpt-4.1 | 140 | 140 | sí | sí | 14 |
| v7 | 3 | gpt-4o-mini | 140 | 140 | sí | sí | 15 |
| v7 | 3 | gpt-5.4-mini | 140 | 140 | sí | sí | 13 |
| v7 | 3 | grok-4-1-fast-non-reasoning | 140 | 140 | sí | sí | 16 |
| v7 | 4 | Llama-3.3-70B-Instruct | 600 | 600 | sí | sí | 24 |
| v7 | 4 | Mistral-Large-3 | 600 | 600 | sí | sí | 23 |
| v7 | 4 | gpt-4.1 | 600 | 600 | sí | sí | 20 |
| v7 | 4 | gpt-4o-mini | 600 | 67 | no | sí | 21 |
| v7 | 4 | gpt-5.4-mini | 600 | 600 | sí | sí | 19 |
| v7 | 4 | grok-4-1-fast-non-reasoning | 600 | 600 | sí | sí | 22 |
| v7 | 5 | Llama-3.3-70B-Instruct | 3 | 1 | no | sí | 30 |
| v7 | 5 | Mistral-Large-3 | 3 | 11 | no | sí | 29 |
| v7 | 5 | gpt-4.1 | 3 | 10 | no | sí | 26 |
| v7 | 5 | gpt-4o-mini | 3 | 3 | sí | sí | 27 |
| v7 | 5 | gpt-5.4-mini | 3 | 5 | no | sí | 25 |
| v7 | 5 | grok-4-1-fast-non-reasoning | 3 | 217 | no | sí | 28 |
| v7 | 6 | Llama-3.3-70B-Instruct | 60 | 21 | no | sí | 36 |
| v7 | 6 | Mistral-Large-3 | 60 | 8 | no | sí | 35 |
| v7 | 6 | gpt-4.1 | 60 | 21 | no | sí | 32 |
| v7 | 6 | gpt-4o-mini | 60 | 6 | no | sí | 33 |
| v7 | 6 | gpt-5.4-mini | 60 | 420 | no | sí | 31 |
| v7 | 6 | grok-4-1-fast-non-reasoning | 60 | 32 | no | sí | 34 |
| v7 | 7 | Llama-3.3-70B-Instruct | 91 | 49 | no | sí | 42 |
| v7 | 7 | Mistral-Large-3 | 91 | 35 | no | sí | 41 |
| v7 | 7 | gpt-4.1 | 91 | 91 | sí | sí | 38 |
| v7 | 7 | gpt-4o-mini | 91 | 35 | no | sí | 39 |
| v7 | 7 | gpt-5.4-mini | 91 | 49 | no | sí | 37 |
| v7 | 7 | grok-4-1-fast-non-reasoning | 91 | 15 | no | sí | 40 |
| v7 | 8 | Llama-3.3-70B-Instruct | 360 | 66 | no | sí | 48 |
| v7 | 8 | Mistral-Large-3 | 360 | 120 | no | sí | 47 |
| v7 | 8 | gpt-4.1 | 360 | 120 | no | sí | 44 |
| v7 | 8 | gpt-4o-mini | 360 | 120 | no | sí | 45 |
| v7 | 8 | gpt-5.4-mini | 360 | 120 | no | sí | 43 |
| v7 | 8 | grok-4-1-fast-non-reasoning | 360 | 180 | no | sí | 46 |
| v7 | 9 | Llama-3.3-70B-Instruct | 8 | 5 | no | sí | 54 |
| v7 | 9 | Mistral-Large-3 | 8 | 8 | sí | sí | 53 |
| v7 | 9 | gpt-4.1 | 8 | 4 | no | sí | 50 |
| v7 | 9 | gpt-4o-mini | 8 | 3 | no | sí | 51 |
| v7 | 9 | gpt-5.4-mini | 8 | 8 | sí | sí | 49 |
| v7 | 9 | grok-4-1-fast-non-reasoning | 8 | 5 | no | sí | 52 |
| v7 | 10 | Llama-3.3-70B-Instruct | 34 | 34 | sí | sí | 60 |
| v7 | 10 | Mistral-Large-3 | 34 | 34 | sí | sí | 59 |
| v7 | 10 | gpt-4.1 | 34 | None | no | no | 56 |
| v7 | 10 | gpt-4o-mini | 34 | 34 | sí | sí | 57 |
| v7 | 10 | gpt-5.4-mini | 34 | 34 | sí | sí | 55 |
| v7 | 10 | grok-4-1-fast-non-reasoning | 34 | 34 | sí | sí | 58 |
