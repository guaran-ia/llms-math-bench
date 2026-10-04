# Reporte de prompts por modelo

## Resumen

- Archivo evaluado: `model_test_results_new_models_all_prompts.jsonl`
- Intentos leídos: 180
- Intentos evaluados para ranking: 180
- Líneas JSONL inválidas: 0
- Mejor combinación: **azure-services-responses / gpt-5.5 / v7** (10/10)

## Ranking Por Prompt

| Posición | Proveedor | Modelo | Prompt | Nombre | Aciertos | Exactitud | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | azure-services-responses | gpt-5.5 | v7 | Profesor bilingüe con glosario y warmup | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 7.150s |
| 2 | azure-services-responses | gpt-5.5 | v4 | Profesor bilingüe con glosario | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 7.258s |
| 3 | azure-services-responses | gpt-5.5 | v3 | Profesor bilingüe con interpretación semántica | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 7.465s |
| 4 | azure-services-responses | gpt-5.5 | v2 | Traducción interna al español | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 7.814s |
| 5 | azure-services-responses | gpt-5.5 | v8 | Autocomplete simple zero-shot | 10/10 | 100.0% | 0/10 | 0/10 | 0 | 0 | 3.934s |
| 6 | azure-services-responses | gpt-5.5 | v9 | Autocomplete simple few-shot | 10/10 | 100.0% | 0/10 | 0/10 | 0 | 0 | 4.091s |
| 7 | azure-services-responses | gpt-5.5 | v1 | Guaraní estricto | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 10.127s |
| 8 | azure-services-responses | gpt-5.5 | v5 | Guaraní estricto con JSON reforzado | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 10.438s |
| 9 | azure-services-responses | gpt-5.5 | v6 | Guaraní estricto con JSON reforzado y warmup | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 11.085s |
| 10 | azure-services-responses | gpt-5.6-terra | v9 | Autocomplete simple few-shot | 9/10 | 90.0% | 0/10 | 0/10 | 0 | 0 | 3.285s |
| 11 | azure-services-responses | gpt-5.6-terra | v7 | Profesor bilingüe con glosario y warmup | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 4.013s |
| 12 | azure-services-responses | gpt-5.6-terra | v2 | Traducción interna al español | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 4.175s |
| 13 | azure-services-responses | gpt-5.6-terra | v4 | Profesor bilingüe con glosario | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 4.349s |
| 14 | azure-services-responses | gpt-5.6-terra | v3 | Profesor bilingüe con interpretación semántica | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 4.727s |
| 15 | azure-services-responses | gpt-5.6-terra | v5 | Guaraní estricto con JSON reforzado | 7/10 | 70.0% | 10/10 | 10/10 | 0 | 0 | 5.107s |
| 16 | azure-services-responses | gpt-5.6-terra | v6 | Guaraní estricto con JSON reforzado y warmup | 7/10 | 70.0% | 10/10 | 10/10 | 0 | 0 | 5.516s |
| 17 | azure-services-responses | gpt-5.6-terra | v1 | Guaraní estricto | 7/10 | 70.0% | 10/10 | 10/10 | 0 | 0 | 5.955s |
| 18 | azure-services-responses | gpt-5.6-terra | v8 | Autocomplete simple zero-shot | 7/10 | 70.0% | 0/10 | 0/10 | 0 | 0 | 3.152s |

## Detalle Por Problema

| Prompt | Problema | Modelo | Esperado | Predicho | Correcto | JSON válido | Línea |
|---|---:|---|---:|---:|---|---|---:|
| v1 | 1 | gpt-5.5 | 18 | 10 | no | sí | 2 |
| v1 | 1 | gpt-5.6-terra | 18 | 10 | no | sí | 1 |
| v1 | 2 | gpt-5.5 | 8 | 8 | sí | sí | 4 |
| v1 | 2 | gpt-5.6-terra | 8 | 8 | sí | sí | 3 |
| v1 | 3 | gpt-5.5 | 140 | 140 | sí | sí | 6 |
| v1 | 3 | gpt-5.6-terra | 140 | 140 | sí | sí | 5 |
| v1 | 4 | gpt-5.5 | 600 | 600 | sí | sí | 8 |
| v1 | 4 | gpt-5.6-terra | 600 | 600 | sí | sí | 7 |
| v1 | 5 | gpt-5.5 | 3 | 3 | sí | sí | 10 |
| v1 | 5 | gpt-5.6-terra | 3 | 3 | sí | sí | 9 |
| v1 | 6 | gpt-5.5 | 60 | 60 | sí | sí | 12 |
| v1 | 6 | gpt-5.6-terra | 60 | 30 | no | sí | 11 |
| v1 | 7 | gpt-5.5 | 91 | 91 | sí | sí | 14 |
| v1 | 7 | gpt-5.6-terra | 91 | 91 | sí | sí | 13 |
| v1 | 8 | gpt-5.5 | 360 | 360 | sí | sí | 16 |
| v1 | 8 | gpt-5.6-terra | 360 | 120 | no | sí | 15 |
| v1 | 9 | gpt-5.5 | 8 | 8 | sí | sí | 18 |
| v1 | 9 | gpt-5.6-terra | 8 | 8 | sí | sí | 17 |
| v1 | 10 | gpt-5.5 | 34 | 34 | sí | sí | 20 |
| v1 | 10 | gpt-5.6-terra | 34 | 34 | sí | sí | 19 |
| v2 | 1 | gpt-5.5 | 18 | 18 | sí | sí | 22 |
| v2 | 1 | gpt-5.6-terra | 18 | 10 | no | sí | 21 |
| v2 | 2 | gpt-5.5 | 8 | 8 | sí | sí | 24 |
| v2 | 2 | gpt-5.6-terra | 8 | 8 | sí | sí | 23 |
| v2 | 3 | gpt-5.5 | 140 | 140 | sí | sí | 26 |
| v2 | 3 | gpt-5.6-terra | 140 | 140 | sí | sí | 25 |
| v2 | 4 | gpt-5.5 | 600 | 600 | sí | sí | 28 |
| v2 | 4 | gpt-5.6-terra | 600 | 600 | sí | sí | 27 |
| v2 | 5 | gpt-5.5 | 3 | 3 | sí | sí | 30 |
| v2 | 5 | gpt-5.6-terra | 3 | 3 | sí | sí | 29 |
| v2 | 6 | gpt-5.5 | 60 | 60 | sí | sí | 32 |
| v2 | 6 | gpt-5.6-terra | 60 | 60 | sí | sí | 31 |
| v2 | 7 | gpt-5.5 | 91 | 91 | sí | sí | 34 |
| v2 | 7 | gpt-5.6-terra | 91 | 91 | sí | sí | 33 |
| v2 | 8 | gpt-5.5 | 360 | 360 | sí | sí | 36 |
| v2 | 8 | gpt-5.6-terra | 360 | 120 | no | sí | 35 |
| v2 | 9 | gpt-5.5 | 8 | 8 | sí | sí | 38 |
| v2 | 9 | gpt-5.6-terra | 8 | 8 | sí | sí | 37 |
| v2 | 10 | gpt-5.5 | 34 | 34 | sí | sí | 40 |
| v2 | 10 | gpt-5.6-terra | 34 | 34 | sí | sí | 39 |
| v3 | 1 | gpt-5.5 | 18 | 18 | sí | sí | 42 |
| v3 | 1 | gpt-5.6-terra | 18 | 10 | no | sí | 41 |
| v3 | 2 | gpt-5.5 | 8 | 8 | sí | sí | 44 |
| v3 | 2 | gpt-5.6-terra | 8 | 8 | sí | sí | 43 |
| v3 | 3 | gpt-5.5 | 140 | 140 | sí | sí | 46 |
| v3 | 3 | gpt-5.6-terra | 140 | 140 | sí | sí | 45 |
| v3 | 4 | gpt-5.5 | 600 | 600 | sí | sí | 48 |
| v3 | 4 | gpt-5.6-terra | 600 | 600 | sí | sí | 47 |
| v3 | 5 | gpt-5.5 | 3 | 3 | sí | sí | 50 |
| v3 | 5 | gpt-5.6-terra | 3 | 3 | sí | sí | 49 |
| v3 | 6 | gpt-5.5 | 60 | 60 | sí | sí | 52 |
| v3 | 6 | gpt-5.6-terra | 60 | 60 | sí | sí | 51 |
| v3 | 7 | gpt-5.5 | 91 | 91 | sí | sí | 54 |
| v3 | 7 | gpt-5.6-terra | 91 | 91 | sí | sí | 53 |
| v3 | 8 | gpt-5.5 | 360 | 360 | sí | sí | 56 |
| v3 | 8 | gpt-5.6-terra | 360 | 120 | no | sí | 55 |
| v3 | 9 | gpt-5.5 | 8 | 8 | sí | sí | 58 |
| v3 | 9 | gpt-5.6-terra | 8 | 8 | sí | sí | 57 |
| v3 | 10 | gpt-5.5 | 34 | 34 | sí | sí | 60 |
| v3 | 10 | gpt-5.6-terra | 34 | 34 | sí | sí | 59 |
| v4 | 1 | gpt-5.5 | 18 | 18 | sí | sí | 62 |
| v4 | 1 | gpt-5.6-terra | 18 | 10 | no | sí | 61 |
| v4 | 2 | gpt-5.5 | 8 | 8 | sí | sí | 64 |
| v4 | 2 | gpt-5.6-terra | 8 | 8 | sí | sí | 63 |
| v4 | 3 | gpt-5.5 | 140 | 140 | sí | sí | 66 |
| v4 | 3 | gpt-5.6-terra | 140 | 140 | sí | sí | 65 |
| v4 | 4 | gpt-5.5 | 600 | 600 | sí | sí | 68 |
| v4 | 4 | gpt-5.6-terra | 600 | 600 | sí | sí | 67 |
| v4 | 5 | gpt-5.5 | 3 | 3 | sí | sí | 70 |
| v4 | 5 | gpt-5.6-terra | 3 | 3 | sí | sí | 69 |
| v4 | 6 | gpt-5.5 | 60 | 60 | sí | sí | 72 |
| v4 | 6 | gpt-5.6-terra | 60 | 60 | sí | sí | 71 |
| v4 | 7 | gpt-5.5 | 91 | 91 | sí | sí | 74 |
| v4 | 7 | gpt-5.6-terra | 91 | 91 | sí | sí | 73 |
| v4 | 8 | gpt-5.5 | 360 | 360 | sí | sí | 76 |
| v4 | 8 | gpt-5.6-terra | 360 | 120 | no | sí | 75 |
| v4 | 9 | gpt-5.5 | 8 | 8 | sí | sí | 78 |
| v4 | 9 | gpt-5.6-terra | 8 | 8 | sí | sí | 77 |
| v4 | 10 | gpt-5.5 | 34 | 34 | sí | sí | 80 |
| v4 | 10 | gpt-5.6-terra | 34 | 34 | sí | sí | 79 |
| v5 | 1 | gpt-5.5 | 18 | 10 | no | sí | 82 |
| v5 | 1 | gpt-5.6-terra | 18 | 10 | no | sí | 81 |
| v5 | 2 | gpt-5.5 | 8 | 8 | sí | sí | 84 |
| v5 | 2 | gpt-5.6-terra | 8 | 8 | sí | sí | 83 |
| v5 | 3 | gpt-5.5 | 140 | 140 | sí | sí | 86 |
| v5 | 3 | gpt-5.6-terra | 140 | 140 | sí | sí | 85 |
| v5 | 4 | gpt-5.5 | 600 | 600 | sí | sí | 88 |
| v5 | 4 | gpt-5.6-terra | 600 | 600 | sí | sí | 87 |
| v5 | 5 | gpt-5.5 | 3 | 3 | sí | sí | 90 |
| v5 | 5 | gpt-5.6-terra | 3 | 3 | sí | sí | 89 |
| v5 | 6 | gpt-5.5 | 60 | 60 | sí | sí | 92 |
| v5 | 6 | gpt-5.6-terra | 60 | 40 | no | sí | 91 |
| v5 | 7 | gpt-5.5 | 91 | 91 | sí | sí | 94 |
| v5 | 7 | gpt-5.6-terra | 91 | 91 | sí | sí | 93 |
| v5 | 8 | gpt-5.5 | 360 | 360 | sí | sí | 96 |
| v5 | 8 | gpt-5.6-terra | 360 | 120 | no | sí | 95 |
| v5 | 9 | gpt-5.5 | 8 | 8 | sí | sí | 98 |
| v5 | 9 | gpt-5.6-terra | 8 | 8 | sí | sí | 97 |
| v5 | 10 | gpt-5.5 | 34 | 34 | sí | sí | 100 |
| v5 | 10 | gpt-5.6-terra | 34 | 34 | sí | sí | 99 |
| v6 | 1 | gpt-5.5 | 18 | 10 | no | sí | 102 |
| v6 | 1 | gpt-5.6-terra | 18 | 10 | no | sí | 101 |
| v6 | 2 | gpt-5.5 | 8 | 8 | sí | sí | 104 |
| v6 | 2 | gpt-5.6-terra | 8 | 8 | sí | sí | 103 |
| v6 | 3 | gpt-5.5 | 140 | 140 | sí | sí | 106 |
| v6 | 3 | gpt-5.6-terra | 140 | 140 | sí | sí | 105 |
| v6 | 4 | gpt-5.5 | 600 | 600 | sí | sí | 108 |
| v6 | 4 | gpt-5.6-terra | 600 | 600 | sí | sí | 107 |
| v6 | 5 | gpt-5.5 | 3 | 3 | sí | sí | 110 |
| v6 | 5 | gpt-5.6-terra | 3 | 3 | sí | sí | 109 |
| v6 | 6 | gpt-5.5 | 60 | 60 | sí | sí | 112 |
| v6 | 6 | gpt-5.6-terra | 60 | 40 | no | sí | 111 |
| v6 | 7 | gpt-5.5 | 91 | 91 | sí | sí | 114 |
| v6 | 7 | gpt-5.6-terra | 91 | 91 | sí | sí | 113 |
| v6 | 8 | gpt-5.5 | 360 | 360 | sí | sí | 116 |
| v6 | 8 | gpt-5.6-terra | 360 | 120 | no | sí | 115 |
| v6 | 9 | gpt-5.5 | 8 | 8 | sí | sí | 118 |
| v6 | 9 | gpt-5.6-terra | 8 | 8 | sí | sí | 117 |
| v6 | 10 | gpt-5.5 | 34 | 34 | sí | sí | 120 |
| v6 | 10 | gpt-5.6-terra | 34 | 34 | sí | sí | 119 |
| v7 | 1 | gpt-5.5 | 18 | 18 | sí | sí | 122 |
| v7 | 1 | gpt-5.6-terra | 18 | 10 | no | sí | 121 |
| v7 | 2 | gpt-5.5 | 8 | 8 | sí | sí | 124 |
| v7 | 2 | gpt-5.6-terra | 8 | 8 | sí | sí | 123 |
| v7 | 3 | gpt-5.5 | 140 | 140 | sí | sí | 126 |
| v7 | 3 | gpt-5.6-terra | 140 | 140 | sí | sí | 125 |
| v7 | 4 | gpt-5.5 | 600 | 600 | sí | sí | 128 |
| v7 | 4 | gpt-5.6-terra | 600 | 600 | sí | sí | 127 |
| v7 | 5 | gpt-5.5 | 3 | 3 | sí | sí | 130 |
| v7 | 5 | gpt-5.6-terra | 3 | 3 | sí | sí | 129 |
| v7 | 6 | gpt-5.5 | 60 | 60 | sí | sí | 132 |
| v7 | 6 | gpt-5.6-terra | 60 | 40 | no | sí | 131 |
| v7 | 7 | gpt-5.5 | 91 | 91 | sí | sí | 134 |
| v7 | 7 | gpt-5.6-terra | 91 | 91 | sí | sí | 133 |
| v7 | 8 | gpt-5.5 | 360 | 360 | sí | sí | 136 |
| v7 | 8 | gpt-5.6-terra | 360 | 360 | sí | sí | 135 |
| v7 | 9 | gpt-5.5 | 8 | 8 | sí | sí | 138 |
| v7 | 9 | gpt-5.6-terra | 8 | 8 | sí | sí | 137 |
| v7 | 10 | gpt-5.5 | 34 | 34 | sí | sí | 140 |
| v7 | 10 | gpt-5.6-terra | 34 | 34 | sí | sí | 139 |
| v8 | 1 | gpt-5.5 | 18 | 18 | sí | no | 142 |
| v8 | 1 | gpt-5.6-terra | 18 | 10 | no | no | 141 |
| v8 | 2 | gpt-5.5 | 8 | 8 | sí | no | 144 |
| v8 | 2 | gpt-5.6-terra | 8 | 8 | sí | no | 143 |
| v8 | 3 | gpt-5.5 | 140 | 140 | sí | no | 146 |
| v8 | 3 | gpt-5.6-terra | 140 | 140 | sí | no | 145 |
| v8 | 4 | gpt-5.5 | 600 | 600 | sí | no | 148 |
| v8 | 4 | gpt-5.6-terra | 600 | 600 | sí | no | 147 |
| v8 | 5 | gpt-5.5 | 3 | 3 | sí | no | 150 |
| v8 | 5 | gpt-5.6-terra | 3 | 3 | sí | no | 149 |
| v8 | 6 | gpt-5.5 | 60 | 60 | sí | no | 152 |
| v8 | 6 | gpt-5.6-terra | 60 | 60 | sí | no | 151 |
| v8 | 7 | gpt-5.5 | 91 | 91 | sí | no | 154 |
| v8 | 7 | gpt-5.6-terra | 91 | 91 | sí | no | 153 |
| v8 | 8 | gpt-5.5 | 360 | 360 | sí | no | 156 |
| v8 | 8 | gpt-5.6-terra | 360 | 1440 | no | no | 155 |
| v8 | 9 | gpt-5.5 | 8 | 8 | sí | no | 158 |
| v8 | 9 | gpt-5.6-terra | 8 | 4 | no | no | 157 |
| v8 | 10 | gpt-5.5 | 34 | 34 | sí | no | 160 |
| v8 | 10 | gpt-5.6-terra | 34 | 34 | sí | no | 159 |
| v9 | 1 | gpt-5.5 | 18 | 18 | sí | no | 162 |
| v9 | 1 | gpt-5.6-terra | 18 | 10 | no | no | 161 |
| v9 | 2 | gpt-5.5 | 8 | 8 | sí | no | 164 |
| v9 | 2 | gpt-5.6-terra | 8 | 8 | sí | no | 163 |
| v9 | 3 | gpt-5.5 | 140 | 140 | sí | no | 166 |
| v9 | 3 | gpt-5.6-terra | 140 | 140 | sí | no | 165 |
| v9 | 4 | gpt-5.5 | 600 | 600 | sí | no | 168 |
| v9 | 4 | gpt-5.6-terra | 600 | 600 | sí | no | 167 |
| v9 | 5 | gpt-5.5 | 3 | 3 | sí | no | 170 |
| v9 | 5 | gpt-5.6-terra | 3 | 3 | sí | no | 169 |
| v9 | 6 | gpt-5.5 | 60 | 60 | sí | no | 172 |
| v9 | 6 | gpt-5.6-terra | 60 | 60 | sí | no | 171 |
| v9 | 7 | gpt-5.5 | 91 | 91 | sí | no | 174 |
| v9 | 7 | gpt-5.6-terra | 91 | 91 | sí | no | 173 |
| v9 | 8 | gpt-5.5 | 360 | 360 | sí | no | 176 |
| v9 | 8 | gpt-5.6-terra | 360 | 360 | sí | no | 175 |
| v9 | 9 | gpt-5.5 | 8 | 8 | sí | no | 178 |
| v9 | 9 | gpt-5.6-terra | 8 | 8 | sí | no | 177 |
| v9 | 10 | gpt-5.5 | 34 | 34 | sí | no | 180 |
| v9 | 10 | gpt-5.6-terra | 34 | 34 | sí | no | 179 |
