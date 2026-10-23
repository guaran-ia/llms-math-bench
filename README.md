# Mathematics Experiments in Guaraní

Evaluate LLMs by solving mathematical problems written in Guaraní.

The main objective was to measure how well different models understand mathematical problems in Guaraní by comparing prompt variants, models, and educational levels.

## Experiments

We worked with three main groups of problems:

| Dataset | Level | File | Problem statement used by the model | Expected answer |
|---|---|---|---|---|
| Early primary education | Primary education | [`data/problemas_matematicos_guarani.json`](data/problemas_matematicos_guarani.json) | `problem` | `expected_answer` |
| Secondary education | Year 2 | [`data/problemas_matematicos_2do_año.json`](data/problemas_matematicos_2do_año.json) | `problem_gn` | `expected_answer` |
| EEB | Grade 3 | [`data/problemas_matematicos_3er_grado.json`](data/problemas_matematicos_3er_grado.json) | `problem_gn` | `expected_answer` |

Models receive neither the Spanish translation nor the expected answer.

The main metric is strict accuracy against `expected_answer`, usually comparing `response.final_answer.value`.

## Prompts

The source prompts are in [`prompts/guarani_math_prompts.json`](prompts/guarani_math_prompts.json).

We also export Markdown versions for review or sharing:

| File | Contents |
|---|---|
| [`prompts/prompts_v1_v9_para_equipo.md`](prompts/prompts_v1_v9_para_equipo.md) | Prompts `v1` to `v9` used in initial tests and Azure/Gemini comparisons. |
| [`prompts/prompts_v4_v7_para_equipo.md`](prompts/prompts_v4_v7_para_equipo.md) | Comparison subset of prompts `v4` to `v7`. |
| [`prompts/prompts_eem_eeb.md`](prompts/prompts_eem_eeb.md) | Final secondary education and EEB prompts: `em_v1`, `em_v2`, `v10`, `v11`. |
| [`prompts/chatgpt_manual_blind_v5.md`](prompts/chatgpt_manual_blind_v5.md) | Prompt for manual blind evaluation with ChatGPT/GPT. |

| Prompt | Purpose | Description |
|---|---|---|
| `v1` to `v4` | Primary education | Initial prompts with different interpretation, explanation, and JSON formatting strategies. |
| `v5` | Primary education | Strict Guaraní with reinforced JSON rules. |
| `v6` | Primary education | Warmup/few-shot variant based on `v5`. |
| `v7` | Primary education | Warmup/few-shot variant based on `v4`. |
| `v8` | Primary education | Simple zero-shot autocomplete, numeric result only. |
| `v9` | Primary education | Simple few-shot autocomplete, numeric result only. |
| `em_v1` | Secondary education | Guaraní problem without `reasoning_type`. |
| `em_v2` | Secondary education | Guaraní problem with `reasoning_type`. |
| `v10` | EEB Grade 3 | Guaraní problem without `reasoning_type`. |
| `v11` | EEB Grade 3 | Guaraní problem with `reasoning_type`. |

## Models

### Azure / GuaranIA Chat Completions

These models are run from [`test_models.py`](test_models.py):

| Model |
|---|
| `gpt-5.4-mini` |
| `gpt-4.1` |
| `gpt-4o-mini` |
| `grok-4-1-fast-non-reasoning` |
| `Mistral-Large-3` |
| `Llama-3.3-70B-Instruct` |

### Azure Services Responses API

These models are run with [`run_azure_services_responses_tests.py`](run_azure_services_responses_tests.py) or the combined secondary education/EEB runner:

| Model |
|---|
| `gpt-5.6-terra` |
| `gpt-5.5` |

### Gemini

Gemini experiments are run with [`run_gemini_tests.py`](run_gemini_tests.py):

| Model |
|---|
| `gemini-3.1-pro-preview` |
| `gemini-3.5-flash` |
| `gemini-3-flash-preview` |
| `gemini-3.1-flash-lite` |
| `gemini-3.5-live-translate-preview` |

### Manual Evaluations

Manual/blind GPT and Claude/Sonnet result files were also evaluated, with consolidated reports in:

| Provider | Report |
|---|---|
| GPT | [`reports/gpt/resumen_gpt_v5.md`](reports/gpt/resumen_gpt_v5.md) |
| Claude/Sonnet | [`reports/claude/resumen_claude_v5.md`](reports/claude/resumen_claude_v5.md) |

## Scripts

| Script | Purpose |
|---|---|
| [`test_models.py`](test_models.py) | Azure chat client/model configuration and API key helpers. |
| [`run_azure_prompt_tests.py`](run_azure_prompt_tests.py) | Runs Azure chat models with specific prompts. |
| [`run_azure_services_responses_tests.py`](run_azure_services_responses_tests.py) | Runs `gpt-5.6-terra` and `gpt-5.5` through the Azure Services Responses API. |
| [`run_gemini_tests.py`](run_gemini_tests.py) | Runs Gemini models through an OpenAI-compatible endpoint. |
| [`run_education_media_tests.py`](run_education_media_tests.py) | Combined runner for datasets with `problem_gn`, `problem_es`, and `reasoning_type`. |
| [`evaluate_prompt_results.py`](evaluate_prompt_results.py) | General evaluator for primary education results/classic prompts. |
| [`evaluate_education_media_results.py`](evaluate_education_media_results.py) | Flexible evaluator for secondary education and EEB. |

## Reports

### Primary Education and Prompts `v1` to `v9`

| Report | Contents |
|---|---|
| [`reports/azure/prompts_y_resultados_v1_v4.md`](reports/azure/prompts_y_resultados_v1_v4.md) | Initial comparison of prompts `v1` to `v4`. |
| [`reports/azure/prompt_comparison_v1_v4.md`](reports/azure/prompt_comparison_v1_v4.md) | Summary comparison of initial prompts. |
| [`reports/azure/azure_v4_v9_team_comparison.md`](reports/azure/azure_v4_v9_team_comparison.md) | Comparison of prompts `v4` to `v9` on Azure models. |
| [`reports/azure_services/summary_new_vs_existing_models.md`](reports/azure_services/summary_new_vs_existing_models.md) | Comparison of new models `gpt-5.5` and `gpt-5.6-terra` against earlier models. |
| [`reports/azure_services/azure_all_models_v4_v9_simple.md`](reports/azure_services/azure_all_models_v4_v9_simple.md) | Simple table of all Azure models with prompts `v4` to `v9`. |

### Secondary Education

| Report | Contents |
|---|---|
| [`reports/educacion_media/education_media_2do_anio_em_v1_em_v2_report.md`](reports/educacion_media/education_media_2do_anio_em_v1_em_v2_report.md) | Evaluation of `data/problemas_matematicos_2do_año.json` with `em_v1` and `em_v2`. |

Main result: `gpt-5.5` and `gpt-5.6-terra` reached `10/10` with `em_v2` after the evaluator was adjusted to accept valid equivalent answers.

### EEB Grade 3

| Report | Contents |
|---|---|
| [`reports/eeb/eeb_v10_v11_report.md`](reports/eeb/eeb_v10_v11_report.md) | Evaluation of `data/problemas_matematicos_3er_grado.json` with `v10` and `v11`. |

Main result: `gpt-5.5` reached `20/20` with both `v10` and `v11`. For most models, `v11` clearly improved on `v10`, suggesting that `reasoning_type` is especially helpful for less robust models.

### Gemini

| Report | Contents |
|---|---|
| [`reports/gemini/resumen_gemini_v1_v5.md`](reports/gemini/resumen_gemini_v1_v5.md) | Overall Gemini summary with prompts `v1` to `v5`. |
| [`reports/gemini/prompts_y_resultados_gemini_v1_v5.md`](reports/gemini/prompts_y_resultados_gemini_v1_v5.md) | Details of Gemini prompts and results. |

Highlighted results:

| Model | Best prompt | Result |
|---|---|---:|
| `gemini-3.5-flash` | `v4` | 10/10 |
| `gemini-3.1-pro-preview` | `v5` | 10/10 |
| `gemini-3-flash-preview` | `v3` | 8/10 |
| `gemini-3.1-flash-lite` | `v3` | 6/10 |

## Example Commands

### Secondary Education

```powershell
python run_education_media_tests.py --problems "data/problemas_matematicos_2do_año.json" --limit 10 --prompt-id em_v1 em_v2 --output "results/educacion_media/model_test_results_2do_anio_em_v1_em_v2.jsonl"
python evaluate_education_media_results.py --input "results/educacion_media/model_test_results_2do_anio_em_v1_em_v2.jsonl" --output "reports/educacion_media/education_media_2do_anio_em_v1_em_v2_report.md"
```

### EEB Grade 3

```powershell
python run_education_media_tests.py --problems "data/problemas_matematicos_3er_grado.json" --limit 20 --prompt-id v10 v11 --output "results/eeb/model_test_results_3er_grado_v10_v11.jsonl"
python evaluate_education_media_results.py --input "results/eeb/model_test_results_3er_grado_v10_v11.jsonl" --output "reports/eeb/eeb_v10_v11_report.md"
```

## .env

The runners expect API keys in environment variables or a local `.env` file.

| Variable | Purpose |
|---|---|
| `AZURE_OPENAI_API_KEY` | Azure Services Responses API for `gpt-5.6-terra` and `gpt-5.5`. |
| `GEMINI_API_KEY` | Gemini OpenAI-compatible endpoint. |
