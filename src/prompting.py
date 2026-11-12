"""Prompt condition loading and paired Spanish/Guarani rendering."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.dataset import PROJECT_ROOT

PROMPTS_PATH = PROJECT_ROOT / "prompts" / "benchmark_prompts.json"
PROMPT_SET = json.loads(PROMPTS_PATH.read_text(encoding="utf-8"))
CONDITIONS = {item["id"]: item for item in PROMPT_SET["conditions"]}


def condition_ids() -> list[str]:
    return [item["id"] for item in PROMPT_SET["conditions"]]


def _reasoning_label(problem: dict[str, Any], language: str) -> str:
    label_id = problem.get("reasoning_type_id")
    if label_id:
        label = PROMPT_SET["reasoning_type_labels"].get(label_id)
        if label:
            return label[language]
    return str(problem.get("reasoning_type") or "")


def render_prompt(condition_id: str, language: str, problem_text: str, problem: dict[str, Any]) -> str:
    if condition_id not in CONDITIONS:
        raise ValueError("Unknown prompt condition: " + condition_id)
    if language not in {"gn", "es"}:
        raise ValueError("Language must be 'gn' or 'es'.")
    condition = CONDITIONS[condition_id]
    sections = [
        "Eñe’ẽ guaraníme.\n" if language == "gn" else "Responde en español.\n",
        PROMPT_SET["role_instruction"][language],
        condition["instruction"][language],
    ]
    if condition_id == "vocabulary_aid":
        sections.append("\n".join(PROMPT_SET["glossary"][language]))
    if condition_id == "few_shot":
        examples = []
        for number, example in enumerate(PROMPT_SET["few_shot_examples"][language], start=1):
            answer = {
                "reasoning": example["reasoning"],
                "steps": example["steps"],
                "final_answer": {"value": example["value"]},
            }
            examples.append(
                "Ejemplo {}:\nProblema: {}\nRespuesta JSON: {}".format(
                    number, example["problem"], json.dumps(answer, ensure_ascii=False)
                )
            )
        sections.extend(examples)
    if condition_id == "reasoning_type":
        type_label = _reasoning_label(problem, language)
        if not type_label:
            raise ValueError("Problem lacks a reasoning_type_id: " + str(problem.get("id")))
        sections.append(type_label)
    sections.extend([
        PROMPT_SET["answer_contract"][language],
        'Formato requerido: {"reasoning":"...","steps":["..."],"final_answer":{"value":0}}',
        "Problema:\n" + problem_text,
    ])
    return "\n\n".join(sections)
