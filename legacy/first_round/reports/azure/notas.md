Evaluations carried out during testing

> Prompt instructions are translated into English for reference. The original experimental prompts remain in `guarani_math_prompts.json` in the prompts directory. Guaraní text and literal model outputs are preserved.

Test 1 in Guaraní:

Prompt:
"You are a primary school mathematics teacher. Your task is to solve and explain a mathematical problem for a 7-year-old child.

You must use simple words, short sentences, and operations that are easy to follow. The explanation must not be technical or complicated.

Solve the problem and generate three answer options:

* One option must be correct.
* Two options must be incorrect but reasonable.
* All three options must be different.
* The correct answer must appear in a random position; it must not always be option A.
* Do not invent information that is not in the problem.
* Briefly explain how you arrived at the answer.
* Break the solution into simple steps.
* Return only valid JSON.
* Do not add any text before or after the JSON.
* Do not use Markdown blocks.
* Answers must be in Guaraní.
* Options must be in Guaraní.
* The explanation must be in Guaraní.
* You must not use Spanish or any language other than Guaraní.

Use exactly this structure:

{{
"reasoning": "A brief, simple explanation for a 7-year-old child.",
"steps": [
"First step explained simply.",
"Second step explained simply."
],
"final_answer": {{
"value": 0,
"unit": "corresponding unit"
}},
"options": [
{{
"id": "A",
"value": 0,
"unit": "corresponding unit"
}},
{{
"id": "B",
"value": 0,
"unit": "corresponding unit"
}},
{{
"id": "C",
"value": 0,
"unit": "corresponding unit"
}}
],
"correct_option_id": "A"
}}"

- Most accurate model: **gpt-4.1**

## Main Ranking

| Rank | Model | Strict correct answers | Strict accuracy | Recovered correct answers | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | gpt-4.1 | 6/10 | 60.0% | 6/10 | 10/10 | 10/10 | 0 | 0 | 3.583s |
| 2 | gpt-5.4-mini | 5/10 | 50.0% | 5/10 | 10/10 | 10/10 | 0 | 0 | 3.089s |
| 3 | Llama-3.3-70B-Instruct | 5/10 | 50.0% | 5/10 | 9/10 | 9/10 | 0 | 1 | 4.797s |
| 4 | Mistral-Large-3 | 4/10 | 40.0% | 4/10 | 9/10 | 10/10 | 0 | 1 | 6.255s |
| 5 | grok-4-1-fast-non-reasoning | 3/10 | 30.0% | 3/10 | 10/10 | 10/10 | 0 | 0 | 3.640s |
| 6 | gpt-4o-mini | 2/10 | 20.0% | 2/10 | 10/10 | 10/10 | 0 | 0 | 3.038s |


Test 2, prompt changes.

