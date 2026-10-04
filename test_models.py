import argparse
import json
import os
import time
from pathlib import Path

from openai import AzureOpenAI, OpenAI


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_PROBLEMS_FILE = BASE_DIR / "data" / "problemas_matematicos_guarani.json"
DEFAULT_OUTPUT_FILE = BASE_DIR / "results" / "azure" / "model_test_results_guarani.jsonl"

AZURE_ENDPOINT = "https://guarania-maas.cognitiveservices.azure.com/"
AZURE_API_VERSION = "2024-12-01-preview"
SERVICES_ENDPOINT = "https://guarania-maas.services.ai.azure.com/openai/v1"

MODELS = {
    "gpt-5.4-mini": {
        "client": "azure",
        "deployment": "gpt-5.4-mini",
        "token_param": "max_completion_tokens",
        "max_tokens": 4096,
        "supports_temperature": False,
    },
    "gpt-4.1": {
        "client": "azure",
        "deployment": "gpt-4.1",
        "token_param": "max_tokens",
        "max_tokens": 4096,
    },
    "gpt-4o-mini": {
        "client": "azure",
        "deployment": "gpt-4o-mini",
        "token_param": "max_tokens",
        "max_tokens": 4096,
    },
    "grok-4-1-fast-non-reasoning": {
        "client": "services",
        "deployment": "grok-4-1-fast-non-reasoning",
        "token_param": "max_tokens",
        "max_tokens": 4096,
    },
    "Mistral-Large-3": {
        "client": "services",
        "deployment": "Mistral-Large-3",
        "token_param": "max_tokens",
        "max_tokens": 4096,
    },
    "Llama-3.3-70B-Instruct": {
        "client": "services",
        "deployment": "Llama-3.3-70B-Instruct",
        "token_param": "max_tokens",
        "max_tokens": 4096,
    },
}

PROMPT_TEMPLATE = """Eres un profesor de matemáticas de primaria que sabe guaraní y español.

Recibirás un problema matemático escrito en guaraní.

Tu primera tarea es encontrarle sentido al problema. Lee con cuidado el enunciado, identifica las cantidades importantes y entiende qué se está preguntando. Después resuelve el problema con operaciones simples.

No traduzcas literalmente palabra por palabra si eso hace que el problema pierda sentido. Usa tu conocimiento de guaraní y español para entender la idea matemática del enunciado.

Ayuda para interpretar números y expresiones frecuentes en guaraní:
* peteĩ = 1
* mokõi = 2
* mbohapy = 3
* irundy = 4
* po = 5
* poteĩpa = 60
* mokõipa = 20
* mokõi jey = dos veces
* irundy jey = cuatro veces
* peteĩteĩ = cada uno
* ñavõ = cada
* hetave = más que
* hemby = sobra o queda

Antes de responder, revisa internamente:
1. Qué cantidad representa cada número del problema.
2. Qué significa cada unidad.
3. Qué operación corresponde.
4. Si usaste todos los datos importantes del enunciado.
5. Si final_answer.value coincide con el valor de la opción indicada por correct_option_id.

No muestres tu análisis interno.
No agregues texto antes ni después del JSON.
No uses bloques Markdown.

Reglas:
* Una opción debe ser correcta.
* Dos opciones deben ser incorrectas, pero razonables.
* Las tres opciones deben ser diferentes.
* La respuesta correcta debe aparecer en una posición aleatoria; no debe ser siempre la opción A.
* No inventes información que no aparezca en el problema.
* Usa palabras sencillas y oraciones cortas, como para un niño de 7 años.
* Divide la solución final en pasos simples.
* La explicación final debe estar en guaraní.
* Los pasos finales deben estar en guaraní.
* Las unidades finales deben estar en guaraní.
* Las opciones finales deben estar en guaraní.
* El JSON debe ser válido.
* Antes de responder, verifica que final_answer.value sea igual al valor de la opción indicada por correct_option_id.

Utiliza exactamente esta estructura:

{{
"reasoning": "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.",
"steps": [
"Peteĩha tembiapo oñemyesakãva guaraníme.",
"Mokõiha tembiapo oñemyesakãva guaraníme."
],
"final_answer": {{
"value": 0,
"unit": "unidad guaraníme"
}},
"options": [
{{
"id": "A",
"value": 0,
"unit": "unidad guaraníme"
}},
{{
"id": "B",
"value": 0,
"unit": "unidad guaraníme"
}},
{{
"id": "C",
"value": 0,
"unit": "unidad guaraníme"
}}
],
"correct_option_id": "A"
}}

Problema en guaraní:

{problem}"""


def load_dotenv(path):
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def read_api_key():
    for env_name in ("GUARANIA_API_KEY", "AZURE_OPENAI_API_KEY", "OPENAI_API_KEY"):
        value = os.getenv(env_name)
        if value:
            return value
    raise RuntimeError(
        "No se encontró API key. Define GUARANIA_API_KEY en el entorno o en un archivo .env."
    )


def build_clients(api_key):
    return {
        "azure": AzureOpenAI(
            api_version=AZURE_API_VERSION,
            azure_endpoint=AZURE_ENDPOINT,
            api_key=api_key,
        ),
        "services": OpenAI(
            base_url=SERVICES_ENDPOINT,
            api_key=api_key,
        ),
    }


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

    api_key = read_api_key()
    clients = build_clients(api_key)

    problems = json.loads(Path(args.problems).read_text(encoding="utf-8"))
    selected_problems = select_problems(problems, args.limit, args.problem_id)
    selected_models = args.models or list(MODELS.keys())

    unknown_models = [model for model in selected_models if model not in MODELS]
    if unknown_models:
        raise ValueError(f"Modelos desconocidos: {', '.join(unknown_models)}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("a", encoding="utf-8") as output_file:
        for problem in selected_problems:
            prompt = PROMPT_TEMPLATE.format(problem=problem["problem"])

            for model_name in selected_models:
                model_config = MODELS[model_name]
                started_at = time.time()
                print(f"Probando {model_name} con problema {problem['id']}...")

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
                    "model": model_name,
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
        description="Prueba los modelos de GuaranIA con problemas matemáticos."
    )
    parser.add_argument("--problems", default=str(DEFAULT_PROBLEMS_FILE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_FILE))
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--problem-id", type=int)
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
