import argparse
import hashlib
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI
from src.language_prompts import language_prompt

from src.test_models import MODELS as CHAT_MODELS
from src.test_models import build_clients, load_dotenv, read_api_key


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_PROBLEMS_FILE = BASE_DIR / "data" / "problemas_matematicos_2do_año.json"
DEFAULT_PROMPTS_FILE = BASE_DIR / "prompts" / "guarani_math_prompts.json"
DEFAULT_OUTPUT_FILE = BASE_DIR / "results" / "educacion_media" / "model_test_results_em.jsonl"
SERVICES_ENDPOINT = "https://guarania-maas.services.ai.azure.com/openai/v1"

RESPONSES_MODELS = {
    "gpt-5.6-terra": {"deployment": "gpt-5.6-terra", "max_output_tokens": 4096},
    "gpt-5.5": {"deployment": "gpt-5.5", "max_output_tokens": 4096},
}


def read_services_api_key():
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("No se encontró AZURE_OPENAI_API_KEY en el entorno o en .env.")
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


def format_prompt(prompt_template, problem):
    return prompt_template.format(
        problem=problem.get("problem_gn") or problem.get("problem") or "",
        problem_es=problem.get("problem_es") or problem.get("problema_es", ""),
        reasoning_type=problem.get("reasoning_type", ""),
        grade=problem.get("grade", ""),
        subject=problem.get("subject", ""),
    )


def file_sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def call_chat_model(clients, model_name, prompt, temperature):
    model_config = CHAT_MODELS[model_name]
    request = {
        "model": model_config["deployment"],
        "messages": [{"role": "user", "content": prompt}],
    }
    request[model_config["token_param"]] = model_config["max_tokens"]
    if model_config.get("supports_temperature", True):
        request["temperature"] = temperature
    response = clients[model_config["client"]].chat.completions.create(**request)
    return response.choices[0].message.content


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


def call_responses_model(client, model_name, prompt):
    model_config = RESPONSES_MODELS[model_name]
    response = client.responses.create(
        model=model_config["deployment"],
        input=prompt,
        max_output_tokens=model_config["max_output_tokens"],
    )
    return extract_response_text(response)


def run_tests(args):
    load_dotenv(BASE_DIR / ".env")
    load_dotenv(BASE_DIR.parent / ".env")

    chat_clients = build_clients(read_api_key())
    responses_client = OpenAI(base_url=SERVICES_ENDPOINT, api_key=read_services_api_key())
    prompts = select_prompts(load_prompts(args.prompts), args.prompt_id)
    problems = json.loads(Path(args.problems).read_text(encoding="utf-8"))
    selected_problems = select_problems(problems, args.limit, args.problem_id)

    all_models = {**CHAT_MODELS, **RESPONSES_MODELS}
    selected_models = args.models or list(all_models.keys())
    unknown_models = [model for model in selected_models if model not in all_models]
    if unknown_models:
        raise ValueError(f"Modelos desconocidos: {', '.join(unknown_models)}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    languages = ["gn", "es"] if args.language == "both" else [args.language]
    run_started_at = datetime.now(timezone.utc).isoformat()
    problems_sha256 = file_sha256(args.problems)
    prompts_sha256 = file_sha256(args.prompts)
    with output_path.open("a", encoding="utf-8") as output_file:
        for language in languages:
            for prompt_config in prompts:
                template = language_prompt(prompt_config["template"], language)
                for problem in selected_problems:
                    problem_text = (problem.get("problem_gn") or problem.get("problem")) if language == "gn" else (problem.get("problem_es") or problem.get("problema_es"))
                    if not problem_text:
                        raise ValueError(f"El problema {problem.get('id')} no tiene texto para language={language}.")
                    localized_problem = dict(problem, problem_gn=problem_text, problem_es=problem_text)
                    prompt = format_prompt(template, localized_problem)
                    for model_name in selected_models:
                        started_at = time.time()
                        print(
                            f"Probando {model_name} con prompt {prompt_config['id']} "
                            f"y problema {problem['id']}..."
                        )

                        try:
                            if model_name in RESPONSES_MODELS:
                                provider = "azure-services-responses"
                                content = call_responses_model(responses_client, model_name, prompt)
                            else:
                                provider = "azure"
                                content = call_chat_model(chat_clients, model_name, prompt, args.temperature)
                            parsed_response, parse_error = parse_json_response(content)
                            error = None
                        except Exception as exc:
                            provider = "azure-services-responses" if model_name in RESPONSES_MODELS else "azure"
                            content = None
                            parsed_response = None
                            parse_error = None
                            error = str(exc)

                        result = {
                            "provider": provider,
                            "model": model_name,
                            "requested_model_id": all_models[model_name]["deployment"],
                            "prompt_id": f"{prompt_config['id']}_{language}" if args.language == "both" else prompt_config["id"],
                            "prompt_pair_id": prompt_config["id"],
                            "prompt_name": prompt_config.get("name"),
                            "language": language,
                            "language_pair_id": f"{prompt_config['id']}:{problem['id']}:{model_name}",
                            "run_started_at": run_started_at,
                            "prompt_version": f"paired-v1/{prompt_config['id']}/{language}",
                            "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                            "dataset_sha256": problems_sha256,
                            "prompts_file_sha256": prompts_sha256,
                            "temperature": args.temperature if model_name not in RESPONSES_MODELS else None,
                            "max_output_tokens": (RESPONSES_MODELS[model_name]["max_output_tokens"] if model_name in RESPONSES_MODELS else all_models[model_name]["max_tokens"]),
                            "problem_id": problem["id"],
                            "problem": problem_text,
                            "problem_es": problem.get("problem_es"),
                            "expected_answer": problem.get("expected_answer"),
                            "reasoning_type": problem.get("reasoning_type"),
                            "difficulty": problem.get("difficulty"),
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
    all_model_names = list(CHAT_MODELS.keys()) + list(RESPONSES_MODELS.keys())
    parser = argparse.ArgumentParser(description="Prueba modelos con problemas de Educación Media.")
    parser.add_argument("--problems", default=str(DEFAULT_PROBLEMS_FILE))
    parser.add_argument("--prompts", default=str(DEFAULT_PROMPTS_FILE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_FILE))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--problem-id", type=int)
    parser.add_argument("--prompt-id", nargs="+", default=["em_v1", "em_v2"])
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--language", choices=["gn", "es", "both"], default="gn",
                        help="Language for a run; both performs paired Guarani and Spanish conditions.")
    parser.add_argument("--models", nargs="+", choices=all_model_names)
    return parser.parse_args()


if __name__ == "__main__":
    run_tests(parse_args())
