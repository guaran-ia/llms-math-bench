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
DEFAULT_OUTPUT_FILE = BASE_DIR / "results" / "gemini" / "model_test_results_gemini_3.5_live_translate_preview.jsonl"

GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/openai/"
DEFAULT_MODEL = "gemini-3.5-live-translate-preview"


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
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("No se encontró GEMINI_API_KEY en el entorno o en .env.")
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


def call_gemini(client, model, prompt, temperature, max_tokens, use_response_format):
    request = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if use_response_format:
        request["response_format"] = {"type": "json_object"}

    try:
        response = client.chat.completions.create(**request)
        return response.choices[0].message.content, use_response_format
    except Exception:
        if not use_response_format:
            raise

    request.pop("response_format", None)
    response = client.chat.completions.create(**request)
    return response.choices[0].message.content, False


def repair_json_response(client, model, raw_response, temperature, max_tokens, use_response_format):
    repair_prompt = f"""Tu respuesta anterior no fue JSON válido.
Corrige únicamente el formato JSON.
No cambies la respuesta matemática.
No cambies los valores numéricos.
No agregues texto antes ni después del JSON.
No uses Markdown.

Respuesta anterior:
{raw_response}"""
    return call_gemini(
        client,
        model=model,
        prompt=repair_prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        use_response_format=use_response_format,
    )


def run_tests(args):
    load_dotenv(BASE_DIR / ".env")
    load_dotenv(BASE_DIR.parent / ".env")

    client = OpenAI(base_url=GEMINI_ENDPOINT, api_key=read_api_key())
    prompts = select_prompts(load_prompts(args.prompts), args.prompt_id)
    problems = json.loads(Path(args.problems).read_text(encoding="utf-8"))
    selected_problems = select_problems(problems, args.limit, args.problem_id)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("a", encoding="utf-8") as output_file:
        for prompt_config in prompts:
            for problem in selected_problems:
                prompt = prompt_config["template"].format(problem=problem["problem"])
                started_at = time.time()
                print(
                    f"Probando {args.model} con prompt {prompt_config['id']} "
                    f"y problema {problem['id']}..."
                )

                try:
                    content, response_format_used = call_gemini(
                        client,
                        args.model,
                        prompt,
                        args.temperature,
                        args.max_tokens,
                        not args.no_response_format,
                    )
                    parsed_response, parse_error = parse_json_response(content)
                    raw_response_before_repair = None
                    repair_attempted = False
                    repair_success = False

                    if parse_error and not args.no_repair:
                        repair_attempted = True
                        raw_response_before_repair = content
                        repaired_content, repair_response_format_used = repair_json_response(
                            client,
                            args.model,
                            content,
                            args.temperature,
                            args.max_tokens,
                            not args.no_response_format,
                        )
                        repaired_response, repaired_parse_error = parse_json_response(repaired_content)
                        if repaired_parse_error is None:
                            content = repaired_content
                            parsed_response = repaired_response
                            parse_error = None
                            repair_success = True
                        response_format_used = response_format_used or repair_response_format_used

                    error = None
                except Exception as exc:
                    content = None
                    parsed_response = None
                    parse_error = None
                    response_format_used = False
                    raw_response_before_repair = None
                    repair_attempted = False
                    repair_success = False
                    error = str(exc)

                result = {
                    "provider": "gemini",
                    "model": args.model,
                    "prompt_id": prompt_config["id"],
                    "prompt_name": prompt_config.get("name"),
                    "problem_id": problem["id"],
                    "problem": problem["problem"],
                    "expected_answer": problem.get("expected_answer"),
                    "response": parsed_response,
                    "raw_response": content,
                    "raw_response_before_repair": raw_response_before_repair,
                    "json_parse_error": parse_error,
                    "response_format_used": response_format_used,
                    "repair_attempted": repair_attempted,
                    "repair_success": repair_success,
                    "error": error,
                    "latency_seconds": round(time.time() - started_at, 3),
                }
                output_file.write(json.dumps(result, ensure_ascii=False) + "\n")
                output_file.flush()

    print(f"Resultados guardados en {output_path}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Prueba Gemini con varios prompts y problemas matemáticos en guaraní."
    )
    parser.add_argument("--problems", default=str(DEFAULT_PROBLEMS_FILE))
    parser.add_argument("--prompts", default=str(DEFAULT_PROMPTS_FILE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_FILE))
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--problem-id", type=int)
    parser.add_argument("--prompt-id", nargs="+", help="IDs de prompts a probar, por ejemplo: v3 v4")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--no-response-format", action="store_true")
    parser.add_argument("--no-repair", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    run_tests(parse_args())
