# Reporte de prompts por modelo

## Resumen

- Archivo evaluado: `model_test_results_gemini_3.1_flash_lite.jsonl`
- Intentos leídos: 50
- Intentos evaluados para ranking: 50
- Líneas JSONL inválidas: 0
- Mejor combinación: **gemini / gemini-3.1-flash-lite / v3** (6/10)

## Ranking Por Prompt

| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | gemini | gemini-3.1-flash-lite | v3 | Profesor bilingüe con interpretación semántica | 6/10 | 60.0% | 10/10 | 10/10 | 0 | 0 | 1.538s |
| 2 | gemini | gemini-3.1-flash-lite | v4 | Profesor bilingüe con glosario | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 1.628s |
| 3 | gemini | gemini-3.1-flash-lite | v2 | Traducción interna al español | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 1.791s |
| 4 | gemini | gemini-3.1-flash-lite | v5 | Guaraní estricto con JSON reforzado | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 1.803s |
| 5 | gemini | gemini-3.1-flash-lite | v1 | Guaraní estricto | 5/10 | 50.0% | 10/10 | 10/10 | 0 | 0 | 1.940s |

## Detalle Por Problema

| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |
|---|---:|---|---:|---:|---|---|---:|
| v1 | 1 | gemini-3.1-flash-lite | 18 | 10 | no | sí | 1 |
| v1 | 2 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 2 |
| v1 | 3 | gemini-3.1-flash-lite | 140 | 140 | sí | sí | 3 |
| v1 | 4 | gemini-3.1-flash-lite | 600 | 600 | sí | sí | 4 |
| v1 | 5 | gemini-3.1-flash-lite | 3 | 4 | no | sí | 5 |
| v1 | 6 | gemini-3.1-flash-lite | 60 | 21 | no | sí | 6 |
| v1 | 7 | gemini-3.1-flash-lite | 91 | 31 | no | sí | 7 |
| v1 | 8 | gemini-3.1-flash-lite | 360 | 120 | no | sí | 8 |
| v1 | 9 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 9 |
| v1 | 10 | gemini-3.1-flash-lite | 34 | 34 | sí | sí | 10 |
| v2 | 1 | gemini-3.1-flash-lite | 18 | 10 | no | sí | 11 |
| v2 | 2 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 12 |
| v2 | 3 | gemini-3.1-flash-lite | 140 | 140 | sí | sí | 13 |
| v2 | 4 | gemini-3.1-flash-lite | 600 | 600 | sí | sí | 14 |
| v2 | 5 | gemini-3.1-flash-lite | 3 | 2 | no | sí | 15 |
| v2 | 6 | gemini-3.1-flash-lite | 60 | 40 | no | sí | 16 |
| v2 | 7 | gemini-3.1-flash-lite | 91 | 15 | no | sí | 17 |
| v2 | 8 | gemini-3.1-flash-lite | 360 | 120 | no | sí | 18 |
| v2 | 9 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 19 |
| v2 | 10 | gemini-3.1-flash-lite | 34 | 34 | sí | sí | 20 |
| v3 | 1 | gemini-3.1-flash-lite | 18 | 10 | no | sí | 21 |
| v3 | 2 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 22 |
| v3 | 3 | gemini-3.1-flash-lite | 140 | 140 | sí | sí | 23 |
| v3 | 4 | gemini-3.1-flash-lite | 600 | 600 | sí | sí | 24 |
| v3 | 5 | gemini-3.1-flash-lite | 3 | 3 | sí | sí | 25 |
| v3 | 6 | gemini-3.1-flash-lite | 60 | 30 | no | sí | 26 |
| v3 | 7 | gemini-3.1-flash-lite | 91 | 35 | no | sí | 27 |
| v3 | 8 | gemini-3.1-flash-lite | 360 | 120 | no | sí | 28 |
| v3 | 9 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 29 |
| v3 | 10 | gemini-3.1-flash-lite | 34 | 34 | sí | sí | 30 |
| v4 | 1 | gemini-3.1-flash-lite | 18 | 10 | no | sí | 31 |
| v4 | 2 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 32 |
| v4 | 3 | gemini-3.1-flash-lite | 140 | 140 | sí | sí | 33 |
| v4 | 4 | gemini-3.1-flash-lite | 600 | 600 | sí | sí | 34 |
| v4 | 5 | gemini-3.1-flash-lite | 3 | 2 | no | sí | 35 |
| v4 | 6 | gemini-3.1-flash-lite | 60 | 40 | no | sí | 36 |
| v4 | 7 | gemini-3.1-flash-lite | 91 | 15 | no | sí | 37 |
| v4 | 8 | gemini-3.1-flash-lite | 360 | 120 | no | sí | 38 |
| v4 | 9 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 39 |
| v4 | 10 | gemini-3.1-flash-lite | 34 | 34 | sí | sí | 40 |
| v5 | 1 | gemini-3.1-flash-lite | 18 | 10 | no | sí | 41 |
| v5 | 2 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 42 |
| v5 | 3 | gemini-3.1-flash-lite | 140 | 140 | sí | sí | 43 |
| v5 | 4 | gemini-3.1-flash-lite | 600 | 600 | sí | sí | 44 |
| v5 | 5 | gemini-3.1-flash-lite | 3 | 10 | no | sí | 45 |
| v5 | 6 | gemini-3.1-flash-lite | 60 | 22 | no | sí | 46 |
| v5 | 7 | gemini-3.1-flash-lite | 91 | 22 | no | sí | 47 |
| v5 | 8 | gemini-3.1-flash-lite | 360 | 120 | no | sí | 48 |
| v5 | 9 | gemini-3.1-flash-lite | 8 | 8 | sí | sí | 49 |
| v5 | 10 | gemini-3.1-flash-lite | 34 | 34 | sí | sí | 50 |
