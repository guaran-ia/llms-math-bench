# Reporte Educación Media

## Resumen

- Archivo evaluado: `model_test_results_2do_anio_em_v1_em_v2.jsonl`
- Intentos leídos: 160
- Líneas JSONL inválidas: 0
- Mejor combinación: **azure-services-responses / gpt-5.5 / em_v2** (10/10)

## Ranking Por Modelo Y Prompt

| Posición | Proveedor | Modelo | Prompt | Aciertos | Exactitud | JSON válido | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | azure-services-responses | gpt-5.5 | em_v2 | 10/10 | 100.0% | 10/10 | 0 | 0 | 6.676s |
| 2 | azure-services-responses | gpt-5.6-terra | em_v2 | 10/10 | 100.0% | 9/10 | 0 | 1 | 4.532s |
| 3 | azure-services-responses | gpt-5.5 | em_v1 | 9/10 | 90.0% | 10/10 | 0 | 0 | 7.213s |
| 4 | azure-services-responses | gpt-5.6-terra | em_v1 | 9/10 | 90.0% | 9/10 | 0 | 1 | 5.092s |
| 5 | azure | gpt-5.4-mini | em_v2 | 8/10 | 80.0% | 10/10 | 0 | 0 | 3.732s |
| 6 | azure | gpt-5.4-mini | em_v1 | 8/10 | 80.0% | 10/10 | 0 | 0 | 3.927s |
| 7 | azure | gpt-4.1 | em_v2 | 8/10 | 80.0% | 10/10 | 0 | 0 | 4.197s |
| 8 | azure | grok-4-1-fast-non-reasoning | em_v2 | 8/10 | 80.0% | 9/10 | 0 | 1 | 4.211s |
| 9 | azure | gpt-4.1 | em_v1 | 8/10 | 80.0% | 9/10 | 0 | 1 | 4.795s |
| 10 | azure | grok-4-1-fast-non-reasoning | em_v1 | 8/10 | 80.0% | 9/10 | 0 | 1 | 5.493s |
| 11 | azure | Mistral-Large-3 | em_v1 | 8/10 | 80.0% | 6/10 | 0 | 4 | 10.042s |
| 12 | azure | Mistral-Large-3 | em_v2 | 7/10 | 70.0% | 0/10 | 0 | 10 | 8.987s |
| 13 | azure | Llama-3.3-70B-Instruct | em_v2 | 6/10 | 60.0% | 10/10 | 0 | 0 | 2.972s |
| 14 | azure | Llama-3.3-70B-Instruct | em_v1 | 6/10 | 60.0% | 10/10 | 0 | 0 | 3.338s |
| 15 | azure | gpt-4o-mini | em_v1 | 3/10 | 30.0% | 10/10 | 0 | 0 | 4.384s |
| 16 | azure | gpt-4o-mini | em_v2 | 2/10 | 20.0% | 9/10 | 0 | 1 | 3.994s |

## Comparación Final

| Modelo | em_v1 | em_v2 | Mejor prompt | Mejor resultado |
|---|---:|---:|---|---:|
| `Llama-3.3-70B-Instruct` | 6/10 | 6/10 | `em_v1` | 6/10 |
| `Mistral-Large-3` | 8/10 | 7/10 | `em_v1` | 8/10 |
| `gpt-4.1` | 8/10 | 8/10 | `em_v2` | 8/10 |
| `gpt-4o-mini` | 3/10 | 2/10 | `em_v1` | 3/10 |
| `gpt-5.4-mini` | 8/10 | 8/10 | `em_v1` | 8/10 |
| `gpt-5.5` | 9/10 | 10/10 | `em_v2` | 10/10 |
| `gpt-5.6-terra` | 9/10 | 10/10 | `em_v2` | 10/10 |
| `grok-4-1-fast-non-reasoning` | 8/10 | 8/10 | `em_v1` | 8/10 |

## Detalle De Errores

| Modelo | Prompt | Problema | Tipo | Esperado | Predicho | JSON válido |
|---|---|---:|---|---|---|---|
| `gpt-5.5` | `em_v1` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | {"columnas": ["C", "P"], "matriz_total": [[122, 40], [81, 48]]} | sí |
| `gpt-5.6-terra` | `em_v1` | 5 | ecuación_de_circunferencia | (x + 5)^2 + (y - 1)^2 = 49/9 | 2 | no |
| `gpt-5.4-mini` | `em_v2` | 1 | logaritmos | 1.2465 | 17.64 | sí |
| `gpt-5.4-mini` | `em_v2` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | [["C + C", "P + P"], [122, 40], [81, 48]] | sí |
| `gpt-5.4-mini` | `em_v1` | 1 | logaritmos | 1.2465 | 17.64 | sí |
| `gpt-5.4-mini` | `em_v1` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | {"matriz_A": [[0, 0], [50, 15], [47, 36]], "matriz_B": [[0, 0], [72, 25], [34, 12]], "nota": "Pe C ha P oñepresenta hag̃ua símbolo ramo, ndikatúi oñemoambue valor exacto oñeipytyvõ'ỹre ambue dato; upévare oñeheja 0 hag̃ua JSON valid rehe, pero hag̃ua matemáticamente ojeporu hag̃ua símbolo."} | sí |
| `gpt-4.1` | `em_v2` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | [["2C", "2P"], [122, 40], [81, 48]] | sí |
| `gpt-4.1` | `em_v2` | 9 | determinante_metodo_de_sarrus | -1 | 1 | sí |
| `grok-4-1-fast-non-reasoning` | `em_v2` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | [[null, null], [122, 40], [81, 48]] | no |
| `grok-4-1-fast-non-reasoning` | `em_v2` | 9 | determinante_metodo_de_sarrus | -1 | 0 | sí |
| `gpt-4.1` | `em_v1` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | 50 | no |
| `gpt-4.1` | `em_v1` | 7 | interseccion_de_rectas_y_ecuacion_de_circunferencia | (x - 4)^2 + y^2 = 52 | (x - 4)² + y² = 85 | sí |
| `grok-4-1-fast-non-reasoning` | `em_v1` | 8 | vertice_de_parabola | (0, 0) | x² = 8y | sí |
| `grok-4-1-fast-non-reasoning` | `em_v1` | 9 | determinante_metodo_de_sarrus | -1 | -0.15384615384615385 | sí |
| `Mistral-Large-3` | `em_v1` | 1 | logaritmos | 1.2465 | 17.64 | sí |
| `Mistral-Large-3` | `em_v1` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | [[-22, -10], [13, 24]] | no |
| `Mistral-Large-3` | `em_v2` | 1 | logaritmos | 1.2465 | 17.64 | no |
| `Mistral-Large-3` | `em_v2` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | [["C + 72", "P + 25"], [84, 27]] | no |
| `Mistral-Large-3` | `em_v2` | 7 | interseccion_de_rectas_y_ecuacion_de_circunferencia | (x - 4)^2 + y^2 = 52 | (x - 4)^2 + y^2 = 6760/121 | no |
| `Llama-3.3-70B-Instruct` | `em_v2` | 1 | logaritmos | 1.2465 | 17.64 | sí |
| `Llama-3.3-70B-Instruct` | `em_v2` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | [[null, null], [122, 40], [81, 48]] | sí |
| `Llama-3.3-70B-Instruct` | `em_v2` | 7 | interseccion_de_rectas_y_ecuacion_de_circunferencia | (x - 4)^2 + y^2 = 52 | (x - 4)^2 + y^2 = 15476/961 | sí |
| `Llama-3.3-70B-Instruct` | `em_v2` | 8 | vertice_de_parabola | (0, 0) | [0, -2] | sí |
| `Llama-3.3-70B-Instruct` | `em_v1` | 1 | logaritmos | 1.2465 | log(x) = 2 * log(4.2) | sí |
| `Llama-3.3-70B-Instruct` | `em_v1` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | [[null, null], [122, 40], [81, 48]] | sí |
| `Llama-3.3-70B-Instruct` | `em_v1` | 7 | interseccion_de_rectas_y_ecuacion_de_circunferencia | (x - 4)^2 + y^2 = 52 | (x - 4)^2 + y^2 = ((80/31 - 4)^2 + (-124/31)^2) | sí |
| `Llama-3.3-70B-Instruct` | `em_v1` | 8 | vertice_de_parabola | (0, 0) | [0, -2] | sí |
| `gpt-4o-mini` | `em_v1` | 1 | logaritmos | 1.2465 | 3.528 | sí |
| `gpt-4o-mini` | `em_v1` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | [[2, 2], [122, 40], [81, 48]] | sí |
| `gpt-4o-mini` | `em_v1` | 3 | determinante_regla_de_laplace | -2 | -12 | sí |
| `gpt-4o-mini` | `em_v1` | 6 | circunferencia_a_partir_del_diametro | (x + 1)^2 + (y - 1)^2 = 25 | (x + 4)² + (y - 5)² = 25 | sí |
| `gpt-4o-mini` | `em_v1` | 7 | interseccion_de_rectas_y_ecuacion_de_circunferencia | (x - 4)^2 + y^2 = 52 | {"intersections": [[-2, 3], [4, 0]], "circumference_equation": "(x - 4)² + y² = r²"} | sí |
| `gpt-4o-mini` | `em_v1` | 8 | vertice_de_parabola | (0, 0) | [0, -1] | sí |
| `gpt-4o-mini` | `em_v1` | 9 | determinante_metodo_de_sarrus | -1 | 2x - 10 = 0 | sí |
| `gpt-4o-mini` | `em_v2` | 1 | logaritmos | 1.2465 | 17.64 | sí |
| `gpt-4o-mini` | `em_v2` | 2 | suma_de_matrices | [[122, 40], [81, 48]] | 50 | no |
| `gpt-4o-mini` | `em_v2` | 3 | determinante_regla_de_laplace | -2 | -24 | sí |
| `gpt-4o-mini` | `em_v2` | 5 | ecuación_de_circunferencia | (x + 5)^2 + (y - 1)^2 = 49/9 | (x + 5)² + (y - 1)² = (7/3)² | sí |
| `gpt-4o-mini` | `em_v2` | 7 | interseccion_de_rectas_y_ecuacion_de_circunferencia | (x - 4)^2 + y^2 = 52 | {"circunferencia": "Ecuación: (x - 4)² + y² = 25", "intersección": [[3, -5], [0.8, 2.6]]} | sí |
| `gpt-4o-mini` | `em_v2` | 8 | vertice_de_parabola | (0, 0) | [0, -1] | sí |
| `gpt-4o-mini` | `em_v2` | 9 | determinante_metodo_de_sarrus | -1 | 2x + 4 = 0 | sí |
| `gpt-4o-mini` | `em_v2` | 10 | centro_y_radio_de_circunferencia | {"center": [-6, 5], "radius": 1} | {"centro": [-6.0, 5.0], "radio": 7.0} | sí |
