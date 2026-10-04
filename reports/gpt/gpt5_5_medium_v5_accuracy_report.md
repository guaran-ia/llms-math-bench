# Reporte de prompts por modelo

## Resumen

- Archivo evaluado: `model_test_results_gpt5.5_medium_evaluable.jsonl`
- Intentos leídos: 10
- Intentos evaluados para ranking: 10
- Líneas JSONL inválidas: 0
- Mejor combinación: **chatgpt / gpt-5 / v5** (8/10)

## Ranking Por Prompt

| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | chatgpt | gpt-5 | v5 | Guaraní estricto con JSON reforzado | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | - |

## Detalle Por Problema

| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |
|---|---:|---|---:|---:|---|---|---:|
| v5 | 1 | gpt-5 | 18 | 10 | no | sí | 1 |
| v5 | 2 | gpt-5 | 8 | 8 | sí | sí | 2 |
| v5 | 3 | gpt-5 | 140 | 140 | sí | sí | 3 |
| v5 | 4 | gpt-5 | 600 | 600 | sí | sí | 4 |
| v5 | 5 | gpt-5 | 3 | 5 | no | sí | 5 |
| v5 | 6 | gpt-5 | 60 | 60 | sí | sí | 6 |
| v5 | 7 | gpt-5 | 91 | 91 | sí | sí | 7 |
| v5 | 8 | gpt-5 | 360 | 360 | sí | sí | 8 |
| v5 | 9 | gpt-5 | 8 | 8 | sí | sí | 9 |
| v5 | 10 | gpt-5 | 34 | 34 | sí | sí | 10 |
