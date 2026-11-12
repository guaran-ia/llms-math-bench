import json
from pathlib import Path

from openpyxl import load_workbook


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data.xlsx"
OUTPUT_FILE = BASE_DIR / "data" / "problems.json"
SHEET_NAME = "test_mgsm_es_to_gn"
LIMIT = 25
DIFFICULTY = "fácil"


def normalize_answer(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def main():
    workbook = load_workbook(INPUT_FILE, read_only=True, data_only=True)
    sheet = workbook[SHEET_NAME]

    rows = sheet.iter_rows(values_only=True)
    headers = next(rows)
    columns = {name: index for index, name in enumerate(headers) if name}

    question_index = columns["question"]
    answer_index = columns["answer_number"]

    problems = []
    for row in rows:
        if len(problems) == LIMIT:
            break

        question = row[question_index]
        answer = row[answer_index]
        if question is None or answer is None:
            continue

        problems.append(
            {
                "id": len(problems) + 1,
                "problem": question,
                "expected_answer": normalize_answer(answer),
                "difficulty": DIFFICULTY,
            }
        )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(problems, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
