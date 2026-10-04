# Reporte de prompts por modelo

## Resumen

- Archivo evaluado: `model_test_results_azure_v8.jsonl`
- Intentos leídos: 60
- Intentos evaluados para ranking: 60
- Líneas JSONL inválidas: 0
- Mejor combinación: **azure / gpt-4.1 / v8** (4/10)

## Ranking Por Prompt

| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | azure | gpt-4.1 | v8 | Autocomplete simple zero-shot | 4/10 | 40.0% | 0/10 | 0/10 | 0 | 0 | 2.146s |
| 2 | azure | gpt-5.4-mini | v8 | Autocomplete simple zero-shot | 3/10 | 30.0% | 0/10 | 0/10 | 0 | 0 | 2.205s |
| 3 | azure | Llama-3.3-70B-Instruct | v8 | Autocomplete simple zero-shot | 2/10 | 20.0% | 0/10 | 0/10 | 0 | 2 | 0.809s |
| 4 | azure | gpt-4o-mini | v8 | Autocomplete simple zero-shot | 2/10 | 20.0% | 0/10 | 0/10 | 0 | 0 | 1.094s |
| 5 | azure | Mistral-Large-3 | v8 | Autocomplete simple zero-shot | 1/10 | 10.0% | 0/10 | 0/10 | 0 | 0 | 0.621s |
| 6 | azure | grok-4-1-fast-non-reasoning | v8 | Autocomplete simple zero-shot | 1/10 | 10.0% | 0/10 | 0/10 | 0 | 0 | 0.900s |

## Detalle Por Problema

| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |
|---|---:|---|---:|---:|---|---|---:|
| v8 | 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | no | 6 |
| v8 | 1 | Mistral-Large-3 | 18 | 10 | no | no | 5 |
| v8 | 1 | gpt-4.1 | 18 | 10 | no | no | 2 |
| v8 | 1 | gpt-4o-mini | 18 | 6 | no | no | 3 |
| v8 | 1 | gpt-5.4-mini | 18 | 10 | no | no | 1 |
| v8 | 1 | grok-4-1-fast-non-reasoning | 18 | 6 | no | no | 4 |
| v8 | 2 | Llama-3.3-70B-Instruct | 8 | 7 | no | no | 12 |
| v8 | 2 | Mistral-Large-3 | 8 | 7 | no | no | 11 |
| v8 | 2 | gpt-4.1 | 8 | 8 | sí | no | 8 |
| v8 | 2 | gpt-4o-mini | 8 | 7 | no | no | 9 |
| v8 | 2 | gpt-5.4-mini | 8 | 14 | no | no | 7 |
| v8 | 2 | grok-4-1-fast-non-reasoning | 8 | 20 | no | no | 10 |
| v8 | 3 | Llama-3.3-70B-Instruct | 140 | 140 | sí | no | 18 |
| v8 | 3 | Mistral-Large-3 | 140 | 420 | no | no | 17 |
| v8 | 3 | gpt-4.1 | 140 | 140 | sí | no | 14 |
| v8 | 3 | gpt-4o-mini | 140 | 140 | sí | no | 15 |
| v8 | 3 | gpt-5.4-mini | 140 | 140 | sí | no | 13 |
| v8 | 3 | grok-4-1-fast-non-reasoning | 140 | 8 | no | no | 16 |
| v8 | 4 | Llama-3.3-70B-Instruct | 600 | 600 | sí | no | 24 |
| v8 | 4 | Mistral-Large-3 | 600 | 600 | sí | no | 23 |
| v8 | 4 | gpt-4.1 | 600 | 600 | sí | no | 20 |
| v8 | 4 | gpt-4o-mini | 600 | 12 | no | no | 21 |
| v8 | 4 | gpt-5.4-mini | 600 | 600 | sí | no | 19 |
| v8 | 4 | grok-4-1-fast-non-reasoning | 600 | 600 | sí | no | 22 |
| v8 | 5 | Llama-3.3-70B-Instruct | 3 | 8 | no | no | 30 |
| v8 | 5 | Mistral-Large-3 | 3 | 120 | no | no | 29 |
| v8 | 5 | gpt-4.1 | 3 | 8 | no | no | 26 |
| v8 | 5 | gpt-4o-mini | 3 | 12 | no | no | 27 |
| v8 | 5 | gpt-5.4-mini | 3 | 14 | no | no | 25 |
| v8 | 5 | grok-4-1-fast-non-reasoning | 3 | 70 | no | no | 28 |
| v8 | 6 | Llama-3.3-70B-Instruct | 60 | 7 | no | no | 36 |
| v8 | 6 | Mistral-Large-3 | 60 | 5 | no | no | 35 |
| v8 | 6 | gpt-4.1 | 60 | 90 | no | no | 32 |
| v8 | 6 | gpt-4o-mini | 60 | 6 | no | no | 33 |
| v8 | 6 | gpt-5.4-mini | 60 | 20300 | no | no | 31 |
| v8 | 6 | grok-4-1-fast-non-reasoning | 60 | 5 | no | no | 34 |
| v8 | 7 | Llama-3.3-70B-Instruct | 91 | 50 | no | no | 42 |
| v8 | 7 | Mistral-Large-3 | 91 | 4 | no | no | 41 |
| v8 | 7 | gpt-4.1 | 91 | 37 | no | no | 38 |
| v8 | 7 | gpt-4o-mini | 91 | 7 | no | no | 39 |
| v8 | 7 | gpt-5.4-mini | 91 | 49 | no | no | 37 |
| v8 | 7 | grok-4-1-fast-non-reasoning | 91 | 80 | no | no | 40 |
| v8 | 8 | Llama-3.3-70B-Instruct | 360 | 30 | no | no | 48 |
| v8 | 8 | Mistral-Large-3 | 360 | 120 | no | no | 47 |
| v8 | 8 | gpt-4.1 | 360 | 120 | no | no | 44 |
| v8 | 8 | gpt-4o-mini | 360 | 180 | no | no | 45 |
| v8 | 8 | gpt-5.4-mini | 360 | 30 | no | no | 43 |
| v8 | 8 | grok-4-1-fast-non-reasoning | 360 | 60 | no | no | 46 |
| v8 | 9 | Llama-3.3-70B-Instruct | 8 | 12 | no | no | 54 |
| v8 | 9 | Mistral-Large-3 | 8 | 3 | no | no | 53 |
| v8 | 9 | gpt-4.1 | 8 | 5 | no | no | 50 |
| v8 | 9 | gpt-4o-mini | 8 | 3 | no | no | 51 |
| v8 | 9 | gpt-5.4-mini | 8 | 4 | no | no | 49 |
| v8 | 9 | grok-4-1-fast-non-reasoning | 8 | 2 | no | no | 52 |
| v8 | 10 | Llama-3.3-70B-Instruct | 34 | 4 | no | no | 60 |
| v8 | 10 | Mistral-Large-3 | 34 | 38 | no | no | 59 |
| v8 | 10 | gpt-4.1 | 34 | 34 | sí | no | 56 |
| v8 | 10 | gpt-4o-mini | 34 | 34 | sí | no | 57 |
| v8 | 10 | gpt-5.4-mini | 34 | 34 | sí | no | 55 |
| v8 | 10 | grok-4-1-fast-non-reasoning | 34 | 36 | no | no | 58 |
