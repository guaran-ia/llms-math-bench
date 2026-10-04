# Experimentos De Matemática En Guaraní

Evaluar los modelos LLM resolviendo problemas matemáticos escritos en guaraní.

El objetivo principal fue medir qué tan bien distintos modelos entienden enunciados matemáticos en guaraní, comparando variantes de prompts, modelos y niveles educativos.

## Experimentos

Trabajamos con tres grupos principales de problemas:

| Dataset | Nivel | Archivo | Enunciado usado por el modelo | Respuesta esperada |
|---|---|---|---|---|
| Primaria inicial | Primaria | [`data/problemas_matematicos_guarani.json`](data/problemas_matematicos_guarani.json) | `problem` | `expected_answer` |
| Educación Media | 2.º año | [`data/problemas_matematicos_2do_año.json`](data/problemas_matematicos_2do_año.json) | `problem_gn` | `expected_answer` |
| EEB | 3.º grado | [`data/problemas_matematicos_3er_grado.json`](data/problemas_matematicos_3er_grado.json) | `problem_gn` | `expected_answer` |

En los experimentos de Educación Media y EEB, los modelos no reciben la traducción al español ni la respuesta esperada.

Los campos `problem_es`, `expected_answer`, `options` y `correct_option` se usan solo como metadata o para evaluación posterior.

## Prompts

Los prompts fuente están en [`prompts/guarani_math_prompts.json`](prompts/guarani_math_prompts.json).

También exportamos versiones en Markdown para revisar o compartir:

| Archivo | Contenido |
|---|---|
| [`prompts/prompts_v1_v9_para_equipo.md`](prompts/prompts_v1_v9_para_equipo.md) | Prompts `v1` a `v9` usados en las pruebas iniciales y comparaciones de Azure/Gemini. |
| [`prompts/prompts_v4_v7_para_equipo.md`](prompts/prompts_v4_v7_para_equipo.md) | Subconjunto comparativo de prompts `v4` a `v7`. |
| [`prompts/prompts_eem_eeb.md`](prompts/prompts_eem_eeb.md) | Prompts finales de Educación Media y EEB: `em_v1`, `em_v2`, `v10`, `v11`. |
| [`prompts/chatgpt_manual_blind_v5.md`](prompts/chatgpt_manual_blind_v5.md) | Prompt para evaluación manual blind con ChatGPT/GPT. |

| Prompt | Uso | Descripción |
|---|---|---|
| `v1` a `v4` | Primaria | Prompts iniciales con distintas estrategias de interpretación, explicación y formato JSON. |
| `v5` | Primaria | Guaraní estricto con JSON reforzado. |
| `v6` | Primaria | Variante con warmup/few-shot basada en `v5`. |
| `v7` | Primaria | Variante con warmup/few-shot basada en `v4`. |
| `v8` | Primaria | Autocomplete simple zero-shot, solo resultado numérico. |
| `v9` | Primaria | Autocomplete simple few-shot, solo resultado numérico. |
| `em_v1` | Educación Media | Problema en guaraní sin `reasoning_type`. |
| `em_v2` | Educación Media | Problema en guaraní con `reasoning_type`. |
| `v10` | 3.º grado EEB | Problema en guaraní sin `reasoning_type`. |
| `v11` | 3.º grado EEB | Problema en guaraní con `reasoning_type`. |

## Modelos 

### Azure / GuaranIA Chat Completions

Estos modelos se ejecutan desde [`test_models.py`](test_models.py):

| Modelo |
|---|
| `gpt-5.4-mini` |
| `gpt-4.1` |
| `gpt-4o-mini` |
| `grok-4-1-fast-non-reasoning` |
| `Mistral-Large-3` |
| `Llama-3.3-70B-Instruct` |

### Azure Services Responses API

Estos modelos se ejecutan con [`run_azure_services_responses_tests.py`](run_azure_services_responses_tests.py) o con el runner combinado de Educación Media/EEB:

| Modelo |
|---|
| `gpt-5.6-terra` |
| `gpt-5.5` |

### Gemini

Los experimentos Gemini se ejecutan con [`run_gemini_tests.py`](run_gemini_tests.py):

| Modelo |
|---|
| `gemini-3.1-pro-preview` |
| `gemini-3.5-flash` |
| `gemini-3-flash-preview` |
| `gemini-3.1-flash-lite` |
| `gemini-3.5-live-translate-preview` |

### Evaluaciones Manuales

También se evaluaron archivos manuales/blind de GPT y Claude/Sonnet, con reportes consolidados en:

| Proveedor | Reporte |
|---|---|
| GPT | [`reports/gpt/resumen_gpt_v5.md`](reports/gpt/resumen_gpt_v5.md) |
| Claude/Sonnet | [`reports/claude/resumen_claude_v5.md`](reports/claude/resumen_claude_v5.md) |

## Scripts 

| Script | Uso |
|---|---|
| [`test_models.py`](test_models.py) | Configuración de clientes/modelos Azure chat y helpers de API key. |
| [`run_azure_prompt_tests.py`](run_azure_prompt_tests.py) | Ejecuta modelos Azure chat con prompts específicos. |
| [`run_azure_services_responses_tests.py`](run_azure_services_responses_tests.py) | Ejecuta `gpt-5.6-terra` y `gpt-5.5` vía Azure Services Responses API. |
| [`run_gemini_tests.py`](run_gemini_tests.py) | Ejecuta modelos Gemini vía endpoint OpenAI-compatible. |
| [`run_education_media_tests.py`](run_education_media_tests.py) | Runner combinado para datasets con `problem_gn`, `problem_es` y `reasoning_type`. |
| [`evaluate_prompt_results.py`](evaluate_prompt_results.py) | Evaluador general para resultados de primaria/prompts clásicos. |
| [`evaluate_education_media_results.py`](evaluate_education_media_results.py) | Evaluador flexible para Educación Media y EEB. |

## Reportes

### Primaria Y Prompts `v1` A `v9`

| Reporte | Contenido |
|---|---|
| [`reports/azure/prompts_y_resultados_v1_v4.md`](reports/azure/prompts_y_resultados_v1_v4.md) | Comparación inicial de prompts `v1` a `v4`. |
| [`reports/azure/prompt_comparison_v1_v4.md`](reports/azure/prompt_comparison_v1_v4.md) | Comparación resumida de prompts iniciales. |
| [`reports/azure/azure_v4_v9_team_comparison.md`](reports/azure/azure_v4_v9_team_comparison.md) | Comparación de prompts `v4` a `v9` en modelos Azure. |
| [`reports/azure_services/summary_new_vs_existing_models.md`](reports/azure_services/summary_new_vs_existing_models.md) | Comparación de modelos nuevos `gpt-5.5` y `gpt-5.6-terra` contra modelos anteriores. |
| [`reports/azure_services/azure_all_models_v4_v9_simple.md`](reports/azure_services/azure_all_models_v4_v9_simple.md) | Tabla simple de todos los modelos Azure con prompts `v4` a `v9`. |

### Educación Media

| Reporte | Contenido |
|---|---|
| [`reports/educacion_media/education_media_2do_anio_em_v1_em_v2_report.md`](reports/educacion_media/education_media_2do_anio_em_v1_em_v2_report.md) | Evaluación de `data/problemas_matematicos_2do_año.json` con `em_v1` y `em_v2`. |

Resultado principal: `gpt-5.5` y `gpt-5.6-terra` llegaron a `10/10` con `em_v2` después de ajustar equivalencias válidas en el evaluador.

### 3.º Grado EEB

| Reporte | Contenido |
|---|---|
| [`reports/eeb/eeb_v10_v11_report.md`](reports/eeb/eeb_v10_v11_report.md) | Evaluación de `data/problemas_matematicos_3er_grado.json` con `v10` y `v11`. |

Resultado principal: `gpt-5.5` llegó a `20/20` con `v10` y `v11`. En la mayoría de modelos, `v11` mejoró claramente sobre `v10`, lo que sugiere que `reasoning_type` ayuda especialmente en modelos menos robustos.

### Gemini

| Reporte | Contenido |
|---|---|
| [`reports/gemini/resumen_gemini_v1_v5.md`](reports/gemini/resumen_gemini_v1_v5.md) | Resumen global Gemini con prompts `v1` a `v5`. |
| [`reports/gemini/prompts_y_resultados_gemini_v1_v5.md`](reports/gemini/prompts_y_resultados_gemini_v1_v5.md) | Detalle de prompts y resultados Gemini. |

Resultados destacados:

| Modelo | Mejor prompt | Resultado |
|---|---|---:|
| `gemini-3.5-flash` | `v4` | 10/10 |
| `gemini-3.1-pro-preview` | `v5` | 10/10 |
| `gemini-3-flash-preview` | `v3` | 8/10 |
| `gemini-3.1-flash-lite` | `v3` | 6/10 |

## Comandos ejemplos

### Educación Media

```powershell
python run_education_media_tests.py --problems "data/problemas_matematicos_2do_año.json" --limit 10 --prompt-id em_v1 em_v2 --output "results/educacion_media/model_test_results_2do_anio_em_v1_em_v2.jsonl"
python evaluate_education_media_results.py --input "results/educacion_media/model_test_results_2do_anio_em_v1_em_v2.jsonl" --output "reports/educacion_media/education_media_2do_anio_em_v1_em_v2_report.md"
```

### 3.º Grado EEB

```powershell
python run_education_media_tests.py --problems "data/problemas_matematicos_3er_grado.json" --limit 20 --prompt-id v10 v11 --output "results/eeb/model_test_results_3er_grado_v10_v11.jsonl"
python evaluate_education_media_results.py --input "results/eeb/model_test_results_3er_grado_v10_v11.jsonl" --output "reports/eeb/eeb_v10_v11_report.md"
```

## .env

Los runners esperan claves de API en variables de entorno o en `.env` local.

| Variable | Uso |
|---|---|
| `AZURE_OPENAI_API_KEY` | Azure Services Responses API para `gpt-5.6-terra` y `gpt-5.5`. |
| `GEMINI_API_KEY` | Endpoint OpenAI-compatible de Gemini. |

Los archivos `.env` no deben subirse al repositorio.

## Notas

La métrica principal es acierto estricto contra `expected_answer`, usualmente comparando `response.final_answer.value`.

Para Educación Media se agregaron equivalencias flexibles para evitar falsos negativos en respuestas matemáticamente equivalentes, por ejemplo puntos como `[0, 0]` contra `(0, 0)` o claves `centro/radio` contra `center/radius`.

Para prompts tipo autocomplete (`v8`, `v9`), puede haber baja tasa de JSON válido aunque la respuesta numérica sea correcta, porque esos prompts piden solo el número.
