import argparse
import json
import time
from pathlib import Path

from test_models import MODELS, build_clients, load_dotenv, read_api_key, select_problems


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_PROBLEMS_FILE = BASE_DIR / "data" / "problemas_matematicos_guarani.json"
DEFAULT_PROMPTS_FILE = BASE_DIR / "prompts" / "guarani_math_prompts.json"
DEFAULT_OUTPUT_FILE = BASE_DIR / "results" / "azure" / "model_test_results_azure_v5.jsonl"


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


def parse_json_response(content):
    try:
        return json.loads(content), None
    except json.JSONDecodeError as error:
        return None, str(error)


def call_model(client, model_config, prompt, temperature):
    request = {
        "model": model_config["deployment"],
        "messages": [{"role": "user", "content": prompt}],
    }
    request[model_config["token_param"]] = model_config["max_tokens"]
    if model_config.get("supports_temperature", True):
        request["temperature"] = temperature

    response = client.chat.completions.create(**request)
    return response.choices[0].message.content


def run_tests(args):
    load_dotenv(BASE_DIR / ".env")
    load_dotenv(BASE_DIR.parent / ".env")

    clients = build_clients(read_api_key())
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
                        content = call_model(
                            clients[model_config["client"]],
                            model_config,
                            prompt,
                            args.temperature,
                        )
                        parsed_response, parse_error = parse_json_response(content)
                        error = None
                    except Exception as exc:
                        content = None
                        parsed_response = None
                        parse_error = None
                        error = str(exc)

                    result = {
                        "provider": "azure",
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
        description="Prueba modelos Azure/GuaranIA con prompts versionados."
    )
    parser.add_argument("--problems", default=str(DEFAULT_PROBLEMS_FILE))
    parser.add_argument("--prompts", default=str(DEFAULT_PROMPTS_FILE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_FILE))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--problem-id", type=int)
    parser.add_argument("--prompt-id", nargs="+", default=["v5"])
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument(
        "--models",
        nargs="+",
        choices=list(MODELS.keys()),
        help="Modelos a probar. Si no se indica, prueba todos.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    run_tests(parse_args())
