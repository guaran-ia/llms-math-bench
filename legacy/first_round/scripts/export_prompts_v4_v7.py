import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROMPTS_FILE = BASE_DIR / "prompts" / "guarani_math_prompts.json"
OUTPUT_FILE = BASE_DIR / "prompts" / "prompts_v4_v7_para_equipo.md"
PROMPT_IDS = ["v4", "v5", "v6", "v7"]


def prompt_text(prompt):
    template = prompt["template"]
    if isinstance(template, list):
        template = "\n".join(template)
    return template.replace("{{", "{").replace("}}", "}")


def main():
    prompts = json.loads(PROMPTS_FILE.read_text(encoding="utf-8"))
    prompts_by_id = {prompt["id"]: prompt for prompt in prompts}

    lines = [
        "# Prompts v4 a v7",
        "",
        "Prompts usados para evaluar problemas matemáticos en guaraní.",
        "",
        "## Resumen",
        "",
        "| Prompt | Nombre | Descripción corta |",
        "|---|---|---|",
        "| `v4` | Profesor bilingüe con glosario | Prompt semántico con glosario guaraní-español. |",
        "| `v5` | Guaraní estricto con JSON reforzado | Prompt estricto enfocado en JSON válido. |",
        "| `v6` | Guaraní estricto con JSON reforzado y warmup | `v5` con ejemplos few-shot/warmup. |",
        "| `v7` | Profesor bilingüe con glosario y warmup | `v4` con ejemplos few-shot/warmup. |",
    ]

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
