# Guarani Mathematical Reasoning Benchmark

This study compares how five language models solve a set of 40 mathematics problems
when presented in Guarani or Spanish. It also measures the effects of seven prompt
conditions. Each problem is evaluated in both languages under every prompt condition
and model.

## Study design

### Research questions

1. How does answer accuracy vary across the five selected models and the three educational datasets?
2. For the same problem, model, and prompt, how does performance differ between Guarani and Spanish?
3. Do the seven prompt interventions change accuracy relative to the standard baseline?

### Data

| Dataset ID | Level | Items | Active source file |
|---|---|---:|---|
| `elementary` | Elementary education | 10 | [`data/math_problems_elementary.json`](data/math_problems_elementary.json) |
| `jr_highschool` | Junior high school | 10 | [`data/math_problems_jr_highschool.json`](data/math_problems_jr_highschool.json) |
| `k3_elementary` | K–3 elementary | 20 | [`data/math_problems_k3_elementary.json`](data/math_problems_k3_elementary.json) |

The active sample contains 40 problems with paired Guarani and Spanish statements
and an answer key. Models receive one language at a time; they do not receive the
paired statement or expected answer. The `reasoning_type` condition uses one
consistent category label per problem. These Guarani labels and all other Guarani
prompt text have been reviewed by a native Guarani speaker.

### Models and providers

| Study model | Provider route | Deployment / model ID setting |
|---|---|---|
| Gemini 3.5 Flash | Gemini API, OpenAI-compatible chat endpoint | `GEMINI_MODEL_ID` |
| Grok 4.1 | Azure AI Services | `AZURE_GROK41_DEPLOYMENT` |
| GPT-4o mini | Azure OpenAI | `AZURE_GPT4O_MINI_DEPLOYMENT` |
| Llama 3.3 70B | Azure AI Services | `AZURE_LLAMA33_DEPLOYMENT` |
| Mistral Large 3 | Azure AI Services | `AZURE_MISTRAL_LARGE3_DEPLOYMENT` |

Before inference starts, the runner looks up the selected models’ published metadata.
For Gemini it calls the Gemini Models API; for Azure it reads the deployment details
through Azure CLI and Azure Resource Manager. It records the discovered version, the
provider model name, lookup source/status, and a fresh `model_metadata_checked_at_utc`
timestamp in every request record. It also records the API-returned model ID when
available, endpoint/API settings, SDK version, decoding settings, request/completion
timestamps, response metadata, and dataset/prompt hashes. A provider may omit a
version; in that case the record states `version_not_returned` and retains the model
name/deployment ID.

### Prompt conditions

All seven prompt conditions are crossed with all 40 items, both languages, and all
five models. Every prompt includes the same age-neutral mathematics-teacher role
framing; this is shared context, not a separate condition. Conditions share the same
JSON answer schema and do not specify an age or grade.

| Condition ID | Intervention |
|---|---|
| `minimal` | Simple request to solve the problem |
| `standard` | Identify givens and question, choose a method, check the answer |
| `cross_language_pivot` | Internally use the counterpart language, then answer in the input language |
| `semantic_interpretation` | Interpret meaning and context rather than translate literally |
| `vocabulary_aid` | Add a bilingual, language-appropriate glossary |
| `few_shot` | Show the same two worked examples in each language |
| `reasoning_type` | Provide a consistent math-category hint |

The prompt set is in [`prompts/benchmark_prompts.json`](prompts/benchmark_prompts.json). The answer contract requests JSON with `reasoning`, `steps`, and `final_answer.value`; numeric, structured, and symbolic answer values are allowed. The minimal condition changes the task instruction only; the shared response contract is retained for comparable scoring.

### Run size

The complete design plans **2,800 model requests**: 40 problems × 2 languages × 7 prompt conditions × 5 models. The runner makes one request per cell, disables SDK retries, records failures, and does not automatically retry. Any deliberate reruns should use a separate output file and be documented; do not silently replace failed records.

### Outcomes and statistical analysis

The primary outcome is exact/correct answer accuracy from `final_answer.value`. Numeric answers use absolute tolerance `1e-4`; structured answers are compared component by component; symbolic expressions are compared with SymPy when available. The evaluator does not extract arbitrary numbers from explanatory prose. Invalid/missing answers and failed requests count as incorrect.

Reports provide accuracy by dataset, language, model, and prompt condition with 95% Wilson intervals. Paired Spanish–Guarani comparisons match the same problem, model, and prompt and use exact two-sided McNemar tests. Prompt comparisons pair each condition against `standard` on the same problem, model, and language. Holm adjustment controls family-wise error within each report comparison family. Prompt-by-dataset findings are exploratory because each dataset has only 10–20 items; confidence intervals and p-values do not remove that limitation.

## Getting started

### 1. Set up Python

Use Python 3.10 or newer. For Azure version discovery, install the Azure CLI and run
`az login` with read access to the deployment resource. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

### 2. Configure provider access

Copy `.env.example` to `.env` and fill in the credentials and deployment settings for your accounts. Keep `.env` private and do not commit it.

Required credentials:

- `GEMINI_API_KEY` for Gemini.
- `AZURE_OPENAI_API_KEY` for Azure inference.
- Azure CLI sign-in (`az login`) with permission to read the account and its model deployments; this separate management-plane access is used only for version lookup. If the intended subscription is not active, set optional `AZURE_SUBSCRIPTION_ID`.

Endpoint and deployment variables have defaults for the configured GuaranIA resource; override them only if your deployment names or endpoints differ. `AZURE_OPENAI_API_VERSION` applies to GPT-4o mini. The runner uses one Azure inference key for the configured Azure endpoints. Confirm the endpoint and deployments are accessible. Never put a credential in a command-line argument or results file.

### 3. Validate the full study without making calls

```bash
python -m src.run_benchmark --dry-run
```

The dry run validates all selected dataset-language-condition combinations and prints the planned request count and routing configuration. It makes zero provider calls and does not require credentials. During a real run, read-only metadata lookups happen before any inference requests; a failed lookup stops the run before paid model calls. The expected count for the default full design is 2,800. To review generated instructions:

```bash
python -m src.run_benchmark --dry-run --show-prompts
```

Check that the deployment IDs are correct, all Guarani instructions and labels have been reviewed, and the planned count is 2,800 before the paid run.

## Reproduce the experiments

### Guarani and Spanish comparison

The default command runs all five models, all 40 problems, both languages, and all seven conditions. It produces a new timestamped JSONL file directly under `results/`.

```bash
python -m src.run_benchmark
```

This command makes paid API calls and is expected to create up to 2,800 requests. A run can be narrowed for a deliberate subset using `--datasets`, `--models`, `--languages`, and `--conditions`; for example:

```bash
python -m src.run_benchmark --datasets elementary --models gemini-3.5-flash --languages gn es --conditions standard
```

Subset runs are not the complete study and must be described as such. The JSONL output stores one record per attempted request. Set a separate output path to keep intentional reruns distinct:

```bash
python -m src.run_benchmark --output results/pilot.jsonl
```

### Prompt comparison

Prompt comparisons use the same all-crossed run above. Each problem is evaluated under all seven conditions, in both languages, with all five models. To execute only prompt comparisons for a subset, specify multiple condition IDs and preserve the `standard` condition as the paired baseline, for example:

```bash
python -m src.run_benchmark --conditions standard minimal cross_language_pivot semantic_interpretation vocabulary_aid few_shot reasoning_type
```

### Generate the report

Use the path printed by the runner (or the explicit JSONL path) as report input:

```bash
python -m src.report_benchmark --input results/run_YYYYMMDDTHHMMSSffffffZ.jsonl
```

By default, the Markdown report is saved directly in `reports/` with a matching filename. Choose a custom destination with `--output`. The report contains the accuracy tables, paired-language tests, prompt-versus-standard tests, confidence intervals, and Holm-adjusted p-values.

## Reproducibility record

For each run, retain the JSONL output and note the repository commit, Python version, run date, provider account/deployment configuration, and any rerun decisions. Every request record contains a UTC access timestamp and completion timestamp, configured model/deployment identifiers, discovered version metadata and its UTC check time, endpoint/API settings, temperature and token limit, SDK retry setting, provider response metadata, and data/prompt hashes. The prompt-set version and file hash identify the exact prompt definitions. Provider-returned IDs or version metadata may not disclose private checkpoint/build details.

The active runner uses temperature `0` and a maximum of `2048` output tokens by default. It refuses to overwrite an existing output path; use a fresh path for each run. The code does not automatically retry failed calls.

## Repository map

- `data/`: active bilingual problem datasets and answer keys.
- `prompts/benchmark_prompts.json`: seven prompt conditions, glossary, examples, and reasoning-type labels.
- `src/run_benchmark.py`: model request runner.
- `src/report_benchmark.py`: accuracy and paired statistical report generator.
- `src/math_evaluation.py`: answer extraction and mathematical equivalence checks.
- `results/`: run JSONL files.
- `reports/`: generated Markdown reports.
