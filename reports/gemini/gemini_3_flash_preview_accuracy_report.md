# Reporte de prompts por modelo

## Resumen

- Archivo evaluado: `model_test_results_gemini_3_flash_preview.jsonl`
- Intentos leídos: 50
- Intentos evaluados para ranking: 50
- Líneas JSONL inválidas: 0
- Mejor combinación: **gemini / gemini-3-flash-preview / v3** (8/10)

## Ranking Por Prompt

| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | gemini | gemini-3-flash-preview | v3 | Profesor bilingüe con interpretación semántica | 8/10 | 80.0% | 10/10 | 9/10 | 0 | 0 | 13.913s |
| 2 | gemini | gemini-3-flash-preview | v2 | Traducción interna al español | 8/10 | 80.0% | 9/10 | 8/10 | 0 | 1 | 13.416s |
| 3 | gemini | gemini-3-flash-preview | v1 | Guaraní estricto | 7/10 | 70.0% | 10/10 | 9/10 | 0 | 0 | 14.184s |
| 4 | gemini | gemini-3-flash-preview | v5 | Guaraní estricto con JSON reforzado | 6/10 | 60.0% | 10/10 | 7/10 | 0 | 0 | 15.333s |
| 5 | gemini | gemini-3-flash-preview | v4 | Profesor bilingüe con glosario | 6/10 | 60.0% | 8/10 | 6/10 | 0 | 2 | 19.332s |

## Detalle Por Problema

| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |
|---|---:|---|---:|---:|---|---|---:|
| v1 | 1 | gemini-3-flash-preview | 18 | 10 | no | sí | 1 |
| v1 | 2 | gemini-3-flash-preview | 8 | 8 | sí | sí | 2 |
| v1 | 3 | gemini-3-flash-preview | 140 | 140 | sí | sí | 3 |
| v1 | 4 | gemini-3-flash-preview | 600 | 600 | sí | sí | 4 |
| v1 | 5 | gemini-3-flash-preview | 3 | 3 | sí | sí | 5 |
| v1 | 6 | gemini-3-flash-preview | 60 | 60 | sí | sí | 6 |
| v1 | 7 | gemini-3-flash-preview | 91 | 91 | sí | sí | 7 |
| v1 | 8 | gemini-3-flash-preview | 360 | 120 | no | sí | 8 |
| v1 | 9 | gemini-3-flash-preview | 8 | 8 | sí | sí | 9 |
| v1 | 10 | gemini-3-flash-preview | 34 | None | no | sí | 10 |
| v2 | 1 | gemini-3-flash-preview | 18 | 10 | no | sí | 11 |
| v2 | 2 | gemini-3-flash-preview | 8 | 8 | sí | sí | 12 |
| v2 | 3 | gemini-3-flash-preview | 140 | 140 | sí | sí | 13 |
| v2 | 4 | gemini-3-flash-preview | 600 | 600 | sí | sí | 14 |
| v2 | 5 | gemini-3-flash-preview | 3 | None | no | no | 15 |
| v2 | 6 | gemini-3-flash-preview | 60 | 60 | sí | sí | 16 |
| v2 | 7 | gemini-3-flash-preview | 91 | 91 | sí | sí | 17 |
| v2 | 8 | gemini-3-flash-preview | 360 | 360 | sí | sí | 18 |
| v2 | 9 | gemini-3-flash-preview | 8 | 8 | sí | sí | 19 |
| v2 | 10 | gemini-3-flash-preview | 34 | 34 | sí | sí | 20 |
| v3 | 1 | gemini-3-flash-preview | 18 | 10 | no | sí | 21 |
| v3 | 2 | gemini-3-flash-preview | 8 | 8 | sí | sí | 22 |
| v3 | 3 | gemini-3-flash-preview | 140 | 140 | sí | sí | 23 |
| v3 | 4 | gemini-3-flash-preview | 600 | 600 | sí | sí | 24 |
| v3 | 5 | gemini-3-flash-preview | 3 | 3 | sí | sí | 25 |
| v3 | 6 | gemini-3-flash-preview | 60 | 60 | sí | sí | 26 |
| v3 | 7 | gemini-3-flash-preview | 91 | 91 | sí | sí | 27 |
| v3 | 8 | gemini-3-flash-preview | 360 | None | no | sí | 28 |
| v3 | 9 | gemini-3-flash-preview | 8 | 8 | sí | sí | 29 |
| v3 | 10 | gemini-3-flash-preview | 34 | 34 | sí | sí | 30 |
| v4 | 1 | gemini-3-flash-preview | 18 | 10 | no | sí | 31 |
| v4 | 2 | gemini-3-flash-preview | 8 | 8 | sí | sí | 32 |
| v4 | 3 | gemini-3-flash-preview | 140 | 140 | sí | sí | 33 |
| v4 | 4 | gemini-3-flash-preview | 600 | None | no | sí | 34 |
| v4 | 5 | gemini-3-flash-preview | 3 | None | no | no | 35 |
| v4 | 6 | gemini-3-flash-preview | 60 | 60 | sí | sí | 36 |
| v4 | 7 | gemini-3-flash-preview | 91 | 91 | sí | sí | 37 |
| v4 | 8 | gemini-3-flash-preview | 360 | None | no | no | 38 |
| v4 | 9 | gemini-3-flash-preview | 8 | 8 | sí | sí | 39 |
| v4 | 10 | gemini-3-flash-preview | 34 | 34 | sí | sí | 40 |
| v5 | 1 | gemini-3-flash-preview | 18 | 10 | no | sí | 41 |
| v5 | 2 | gemini-3-flash-preview | 8 | None | no | sí | 42 |
| v5 | 3 | gemini-3-flash-preview | 140 | 140 | sí | sí | 43 |
| v5 | 4 | gemini-3-flash-preview | 600 | 600 | sí | sí | 44 |
| v5 | 5 | gemini-3-flash-preview | 3 | None | no | sí | 45 |
| v5 | 6 | gemini-3-flash-preview | 60 | 60 | sí | sí | 46 |
| v5 | 7 | gemini-3-flash-preview | 91 | 91 | sí | sí | 47 |
| v5 | 8 | gemini-3-flash-preview | 360 | None | no | sí | 48 |
| v5 | 9 | gemini-3-flash-preview | 8 | 8 | sí | sí | 49 |
| v5 | 10 | gemini-3-flash-preview | 34 | 34 | sí | sí | 50 |
