import argparse
import json
import os
import time
from pathlib import Path

try:
    from openai import OpenAI
except ModuleNotFoundError as exc:
    if exc.name != "openai":
        raise
    raise SystemExit(
        "Falta instalar la dependencia 'openai'.\n"
        "Instálala con: python -m pip install -r requirements.txt"
    ) from exc


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_PROBLEMS_FILE = BASE_DIR / "data" / "problemas_matematicos_guarani.json"
DEFAULT_PROMPTS_FILE = BASE_DIR / "prompts" / "guarani_math_prompts.json"
DEFAULT_OUTPUT_FILE = (
    BASE_DIR / "results" / "azure_services" / "model_test_results_services_responses.jsonl"
)

SERVICES_ENDPOINT = "https://guarania-maas.services.ai.azure.com/openai/v1"

MODELS = {
    "gpt-5.6-terra": {
        "deployment": "gpt-5.6-terra",
        "max_output_tokens": 4096,
    },
    "gpt-5.5": {
        "deployment": "gpt-5.5",
        "max_output_tokens": 4096,
    },
}


def load_dotenv(path):
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def read_api_key():
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "No se encontró AZURE_OPENAI_API_KEY en el entorno o en .env."
        )
    return api_key


def load_prompts(path):
    prompts = json.loads(Path(path).read_text(encoding="utf-8"))
    for prompt in prompts:
        template = prompt.get("template")
        if isinstance(template, list):
            prompt["template"] = "\n".join(template)
        if not prompt.get("id") or not prompt.get("template"):
            raise ValueError("Cada prompt debe tener 'id' y 'template'.")
    return prompts


def select_prompts(prompts, prompt_ids):
    if not prompt_ids:
        return prompts

    selected = [prompt for prompt in prompts if prompt["id"] in prompt_ids]
    found_ids = {prompt["id"] for prompt in selected}
    missing_ids = [prompt_id for prompt_id in prompt_ids if prompt_id not in found_ids]
    if missing_ids:
        raise ValueError(f"Prompts no encontrados: {', '.join(missing_ids)}")
    return selected


def select_problems(problems, limit, problem_id):
    if problem_id is not None:
        for problem in problems:
            if problem["id"] == problem_id:
                return [problem]
        raise ValueError(f"No existe un problema con id {problem_id}.")
    return problems[:limit]


def parse_json_response(content):
    try:
        return json.loads(content), None
    except json.JSONDecodeError as error:
        return None, str(error)


def extract_response_text(response):
    output_text = getattr(response, "output_text", None)
    if output_text:
        return output_text

    output = getattr(response, "output", None)
    if not output:
        return None

    parts = []
    for item in output:
        content = getattr(item, "content", None)
        if not content:
            continue
        for content_item in content:
            text = getattr(content_item, "text", None)
            if text:
                parts.append(text)
    if parts:
        return "\n".join(parts)

    return str(output)


def call_model(client, model_config, prompt):
    response = client.responses.create(
        model=model_config["deployment"],
        input=prompt,
        max_output_tokens=model_config["max_output_tokens"],
    )
    return extract_response_text(response)


def run_tests(args):
    load_dotenv(BASE_DIR / ".env")
    load_dotenv(BASE_DIR.parent / ".env")

    client = OpenAI(base_url=SERVICES_ENDPOINT, api_key=read_api_key())
    prompts = select_prompts(load_prompts(args.prompts), args.prompt_id)
    problems = json.loads(Path(args.problems).read_text(encoding="utf-8"))
    selected_problems = select_problems(problems, args.limit, args.problem_id)
    selected_models = args.models or list(MODELS.keys())

    unknown_models = [model for model in selected_models if model not in MODELS]
    if unknown_models:
        raise ValueError(f"Modelos desconocidos: {', '.join(unknown_models)}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("a", encoding="utf-8") as output_file:
        for prompt_config in prompts:
            for problem in selected_problems:
                prompt = prompt_config["template"].format(problem=problem["problem"])
                for model_name in selected_models:
                    model_config = MODELS[model_name]
                    started_at = time.time()
                    print(
                        f"Probando {model_name} con prompt {prompt_config['id']} "
                        f"y problema {problem['id']}..."
                    )

                    try:
                        content = call_model(client, model_config, prompt)
                        parsed_response, parse_error = parse_json_response(content)
                        error = None
                    except Exception as exc:
                        content = None
                        parsed_response = None
                        parse_error = None
                        error = str(exc)

                    result = {
                        "provider": "azure-services-responses",
                        "model": model_name,
                        "prompt_id": prompt_config["id"],
                        "prompt_name": prompt_config.get("name"),
                        "problem_id": problem["id"],
                        "problem": problem["problem"],
                        "expected_answer": problem.get("expected_answer"),
                        "response": parsed_response,
                        "raw_response": content,
                        "json_parse_error": parse_error,
                        "error": error,
                        "latency_seconds": round(time.time() - started_at, 3),
                    }
                    output_file.write(json.dumps(result, ensure_ascii=False) + "\n")
                    output_file.flush()

    print(f"Resultados guardados en {output_path}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Prueba modelos Azure Services con Responses API."
    )
    parser.add_argument("--problems", default=str(DEFAULT_PROBLEMS_FILE))
    parser.add_argument("--prompts", default=str(DEFAULT_PROMPTS_FILE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_FILE))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--problem-id", type=int)
    parser.add_argument("--prompt-id", nargs="+", default=["v4"])
    parser.add_argument(
        "--models",
        nargs="+",
        choices=list(MODELS.keys()),
        help="Modelos a probar. Si no se indica, prueba todos.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    run_tests(parse_args())
