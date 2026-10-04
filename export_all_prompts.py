import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROMPTS_FILE = BASE_DIR / "prompts" / "guarani_math_prompts.json"
OUTPUT_FILE = BASE_DIR / "prompts" / "prompts_v1_v9_para_equipo.md"
PROMPT_IDS = ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9"]

PROMPT_SUMMARIES = {
    "v1": "Guaraní estricto inicial con salida JSON.",
    "v2": "Traducción interna al español antes de responder en guaraní.",
    "v3": "Profesor bilingüe con interpretación semántica del problema.",
    "v4": "Profesor bilingüe con glosario guaraní-español.",
    "v5": "Guaraní estricto con reglas reforzadas de JSON.",
    "v6": "v5 con warmup/few-shot matemático.",
    "v7": "v4 con warmup/few-shot matemático.",
    "v8": "Autocomplete simple zero-shot; solo resultado numérico.",
    "v9": "Autocomplete simple few-shot; solo resultado numérico.",
}


def prompt_text(prompt):
    template = prompt["template"]
    if isinstance(template, list):
        template = "\n".join(template)
    return template.replace("{{", "{").replace("}}", "}")


def main():
    prompts = json.loads(PROMPTS_FILE.read_text(encoding="utf-8"))
    prompts_by_id = {prompt["id"]: prompt for prompt in prompts}

    lines = [
        "# Prompts v1 a v9",
        "",
        "Prompts usados para evaluar problemas matemáticos en guaraní.",
        "",
        "## Resumen",
        "",
        "| Prompt | Nombre | Resumen |",
        "|---|---|---|",
    ]

    for prompt_id in PROMPT_IDS:
        prompt = prompts_by_id[prompt_id]
        lines.append(
            f"| `{prompt_id}` | {prompt['name']} | {PROMPT_SUMMARIES[prompt_id]} |"
        )

    for prompt_id in PROMPT_IDS:
        prompt = prompts_by_id[prompt_id]
        lines.extend(
            [
                "",
                f"## {prompt_id}: {prompt['name']}",
                "",
                "```text",
                prompt_text(prompt),
                "```",
            ]
        )

    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Archivo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
