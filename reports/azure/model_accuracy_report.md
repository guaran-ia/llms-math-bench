# Reporte de acierto por modelo

## Resumen

- Archivo evaluado: `model_test_results_guarani.jsonl`
- Intentos leídos: 126
- Intentos evaluados para ranking: 60
- Problemas únicos evaluados: 10
- Líneas JSONL inválidas: 0
- Modelo más acertado: **gpt-4.1**

El ranking principal usa el último intento disponible por cada par `(modelo, problem_id)` para evitar que problemas repetidos pesen dos veces.

## Ranking Principal

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | Aciertos recuperados | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | gpt-4.1 | 6/10 | 60.0% | 6/10 | 10/10 | 10/10 | 0 | 0 | 2.340s |
| 2 | Mistral-Large-3 | 5/10 | 50.0% | 5/10 | 10/10 | 10/10 | 0 | 0 | 4.443s |
| 3 | Llama-3.3-70B-Instruct | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 2.684s |
| 4 | gpt-5.4-mini | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 2.898s |
| 5 | grok-4-1-fast-non-reasoning | 4/10 | 40.0% | 4/10 | 10/10 | 10/10 | 0 | 0 | 4.117s |
| 6 | gpt-4o-mini | 2/10 | 20.0% | 2/10 | 10/10 | 10/10 | 0 | 0 | 2.829s |

## Detalle Por Problema

| Problema | Modelo | Esperado | Predicho | Estricto | Recuperado | JSON válido | Línea |
|---:|---|---:|---:|---|---|---|---:|
| 1 | Llama-3.3-70B-Instruct | 18 | 10 | no | no | sí | 72 |
| 1 | Mistral-Large-3 | 18 | 10 | no | no | sí | 71 |
| 1 | gpt-4.1 | 18 | 10 | no | no | sí | 68 |
| 1 | gpt-4o-mini | 18 | 10 | no | no | sí | 69 |
| 1 | gpt-5.4-mini | 18 | 10 | no | no | sí | 67 |
| 1 | grok-4-1-fast-non-reasoning | 18 | 6 | no | no | sí | 70 |
| 2 | Llama-3.3-70B-Instruct | 8 | 20 | no | no | sí | 78 |
| 2 | Mistral-Large-3 | 8 | 20 | no | no | sí | 77 |
| 2 | gpt-4.1 | 8 | 8 | sí | sí | sí | 74 |
| 2 | gpt-4o-mini | 8 | 7 | no | no | sí | 75 |
| 2 | gpt-5.4-mini | 8 | 14 | no | no | sí | 73 |
| 2 | grok-4-1-fast-non-reasoning | 8 | 7 | no | no | sí | 76 |
| 3 | Llama-3.3-70B-Instruct | 140 | 140 | sí | sí | sí | 84 |
| 3 | Mistral-Large-3 | 140 | 140 | sí | sí | sí | 83 |
| 3 | gpt-4.1 | 140 | 140 | sí | sí | sí | 80 |
| 3 | gpt-4o-mini | 140 | 140 | sí | sí | sí | 81 |
| 3 | gpt-5.4-mini | 140 | 140 | sí | sí | sí | 79 |
| 3 | grok-4-1-fast-non-reasoning | 140 | 140 | sí | sí | sí | 82 |
| 4 | Llama-3.3-70B-Instruct | 600 | 600 | sí | sí | sí | 90 |
| 4 | Mistral-Large-3 | 600 | 600 | sí | sí | sí | 89 |
| 4 | gpt-4.1 | 600 | 600 | sí | sí | sí | 86 |
| 4 | gpt-4o-mini | 600 | 9 | no | no | sí | 87 |
| 4 | gpt-5.4-mini | 600 | 600 | sí | sí | sí | 85 |
| 4 | grok-4-1-fast-non-reasoning | 600 | 600 | sí | sí | sí | 88 |
| 5 | Llama-3.3-70B-Instruct | 3 | 2 | no | no | sí | 96 |
| 5 | Mistral-Large-3 | 3 | 60 | no | no | sí | 95 |
| 5 | gpt-4.1 | 3 | 1 | no | no | sí | 92 |
| 5 | gpt-4o-mini | 3 | 5 | no | no | sí | 93 |
| 5 | gpt-5.4-mini | 3 | 1 | no | no | sí | 91 |
| 5 | grok-4-1-fast-non-reasoning | 3 | 7 | no | no | sí | 94 |
| 6 | Llama-3.3-70B-Instruct | 60 | 5 | no | no | sí | 102 |
| 6 | Mistral-Large-3 | 60 | 4 | no | no | sí | 101 |
| 6 | gpt-4.1 | 60 | 40 | no | no | sí | 98 |
| 6 | gpt-4o-mini | 60 | 4 | no | no | sí | 99 |
| 6 | gpt-5.4-mini | 60 | 40 | no | no | sí | 97 |
| 6 | grok-4-1-fast-non-reasoning | 60 | 4 | no | no | sí | 100 |
| 7 | Llama-3.3-70B-Instruct | 91 | 30 | no | no | sí | 108 |
| 7 | Mistral-Large-3 | 91 | 43 | no | no | sí | 107 |
| 7 | gpt-4.1 | 91 | 91 | sí | sí | sí | 104 |
| 7 | gpt-4o-mini | 91 | 7 | no | no | sí | 105 |
| 7 | gpt-5.4-mini | 91 | 35 | no | no | sí | 103 |
| 7 | grok-4-1-fast-non-reasoning | 91 | 28 | no | no | sí | 106 |
| 8 | Llama-3.3-70B-Instruct | 360 | 20 | no | no | sí | 114 |
| 8 | Mistral-Large-3 | 360 | 360 | sí | sí | sí | 113 |
| 8 | gpt-4.1 | 360 | 120 | no | no | sí | 110 |
| 8 | gpt-4o-mini | 360 | 120 | no | no | sí | 111 |
| 8 | gpt-5.4-mini | 360 | 120 | no | no | sí | 109 |
| 8 | grok-4-1-fast-non-reasoning | 360 | 360 | sí | sí | sí | 112 |
| 9 | Llama-3.3-70B-Instruct | 8 | 8 | sí | sí | sí | 120 |
| 9 | Mistral-Large-3 | 8 | 8 | sí | sí | sí | 119 |
| 9 | gpt-4.1 | 8 | 8 | sí | sí | sí | 116 |
| 9 | gpt-4o-mini | 8 | 4 | no | no | sí | 117 |
| 9 | gpt-5.4-mini | 8 | 8 | sí | sí | sí | 115 |
| 9 | grok-4-1-fast-non-reasoning | 8 | 2 | no | no | sí | 118 |
| 10 | Llama-3.3-70B-Instruct | 34 | 34 | sí | sí | sí | 126 |
| 10 | Mistral-Large-3 | 34 | 34 | sí | sí | sí | 125 |
| 10 | gpt-4.1 | 34 | 34 | sí | sí | sí | 122 |
| 10 | gpt-4o-mini | 34 | 34 | sí | sí | sí | 123 |
| 10 | gpt-5.4-mini | 34 | 34 | sí | sí | sí | 121 |
| 10 | grok-4-1-fast-non-reasoning | 34 | 34 | sí | sí | sí | 124 |
