"""Dataset loading and language-specific problem normalization."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASETS = {
    "elementary": {
        "name": "Elementary education",
        "level": "Elementary education",
        "path": "data/math_problems_elementary.json",
    },
    "jr_highschool": {
        "name": "Junior high school",
        "level": "Junior high school",
        "path": "data/math_problems_jr_highschool.json",
    },
    "k3_elementary": {
        "name": "K–3 elementary",
        "level": "K–3 elementary",
        "path": "data/math_problems_k3_elementary.json",
    },
}
LANGUAGES = ("gn", "es")


def load_dataset(dataset_id: str) -> tuple[list[dict[str, Any]], Path]:
    if dataset_id not in DATASETS:
        raise ValueError("Unknown dataset: " + dataset_id)
    path = PROJECT_ROOT / DATASETS[dataset_id]["path"]
    rows = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise ValueError("Dataset must be a JSON list: " + str(path))
    return rows, path


def problem_text(row: dict[str, Any], language: str) -> str:
    if language not in LANGUAGES:
        raise ValueError("Language must be 'gn' or 'es'.")
    if language == "gn":
        value = row.get("problem_gn") or row.get("problem")
    else:
        value = row.get("problem_es") or row.get("problema_es")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Problem has no text for language=" + language + ", id=" + str(row.get("id")))
    return value.strip()
