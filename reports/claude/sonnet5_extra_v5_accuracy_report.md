# Reporte de prompts por modelo

## Resumen

- Archivo evaluado: `model_test_results_sonnet5_extra_evaluable.jsonl`
- Intentos leídos: 10
- Intentos evaluados para ranking: 10
- Líneas JSONL inválidas: 0
- Mejor combinación: **claude / claude-sonnet-5 / v5** (9/10)

## Ranking Por Prompt

| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | claude | claude-sonnet-5 | v5 | Guaraní estricto con JSON reforzado | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | - |

## Detalle Por Problema

| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |
|---|---:|---|---:|---:|---|---|---:|
| v5 | 1 | claude-sonnet-5 | 18 | 18 | sí | sí | 1 |
| v5 | 2 | claude-sonnet-5 | 8 | 8 | sí | sí | 2 |
| v5 | 3 | claude-sonnet-5 | 140 | 140 | sí | sí | 3 |
| v5 | 4 | claude-sonnet-5 | 600 | 600 | sí | sí | 4 |
| v5 | 5 | claude-sonnet-5 | 3 | 3 | sí | sí | 5 |
| v5 | 6 | claude-sonnet-5 | 60 | 30 | no | sí | 6 |
| v5 | 7 | claude-sonnet-5 | 91 | 91 | sí | sí | 7 |
| v5 | 8 | claude-sonnet-5 | 360 | 360 | sí | sí | 8 |
| v5 | 9 | claude-sonnet-5 | 8 | 8 | sí | sí | 9 |
| v5 | 10 | claude-sonnet-5 | 34 | 34 | sí | sí | 10 |
