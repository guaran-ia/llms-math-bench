# Gemini Prompts and Results v1 to v5

> Prompt instructions are translated into English for reference. The original experimental prompts remain in `guarani_math_prompts.json` in the prompts directory. Guaraní text and literal model outputs are preserved.

Evaluation of 10 mathematical problems in Guaraní across 5 Gemini models. The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

## Test v1

### Prompt Used

```text
You are a primary school mathematics teacher. Your task is to solve and explain a mathematical problem for a 7-year-old child.

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

{
"reasoning": "A brief, simple explanation for a 7-year-old child.",
"steps": [
"First step explained simply.",
"Second step explained simply."
],
"final_answer": {
"value": 0,
"unit": "corresponding unit"
},
"options": [
{"id": "A", "value": 0, "unit": "corresponding unit"},
{"id": "B", "value": 0, "unit": "corresponding unit"},
{"id": "C", "value": 0, "unit": "corresponding unit"}
],
"correct_option_id": "A"
}

Problem:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 9/10 | 90.0% | 10/10 | 10.139s |
| 2 | `gemini-3.1-pro-preview` | 9/10 | 90.0% | 9/10 | 25.630s |
| 3 | `gemini-3-flash-preview` | 7/10 | 70.0% | 10/10 | 14.184s |
| 4 | `gemini-3.1-flash-lite` | 5/10 | 50.0% | 10/10 | 1.940s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.920s |

## Test v2

### Prompt Used

```text
You are a primary school mathematics teacher and also a translator between Guaraní and Spanish.

You will receive a mathematical problem written in Guaraní.

To solve it, follow this internal process:
1. Mentally translate the problem into Spanish.
2. Solve the problem in Spanish step by step.
3. Generate three answer options in Spanish.
4. Translate the explanation, steps, unit, and options into Guaraní.
5. Return only the final JSON in Guaraní.

Do not show the Spanish translation.
Do not show reasoning in Spanish.
Do not add any text before or after the JSON.
Do not use Markdown blocks.

Rules:
* One option must be correct.
* Two options must be incorrect but reasonable.
* All three options must be different.
* The correct answer must appear in a random position; it must not always be option A.
* Do not invent information that is not in the problem.
* Use simple words and short sentences, as if speaking to a 7-year-old child.
* Break the final solution into simple steps.
* The final explanation must be in Guaraní.
* The final steps must be in Guaraní.
* The final units must be in Guaraní.
* The final options must be in Guaraní.
* The JSON must be valid.
* Before responding, check that final_answer.value equals the value of the option indicated by correct_option_id.

Use exactly this structure:

{
"reasoning": "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.",
"steps": ["Peteĩha tembiapo oñemyesakãva guaraníme.", "Mokõiha tembiapo oñemyesakãva guaraníme."],
"final_answer": {"value": 0, "unit": "unidad guaraníme"},
"options": [{"id": "A", "value": 0, "unit": "unidad guaraníme"}, {"id": "B", "value": 0, "unit": "unidad guaraníme"}, {"id": "C", "value": 0, "unit": "unidad guaraníme"}],
"correct_option_id": "A"
}

Problem in Guaraní:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 9/10 | 90.0% | 10/10 | 8.452s |
| 2 | `gemini-3-flash-preview` | 8/10 | 80.0% | 9/10 | 13.416s |
| 3 | `gemini-3.1-pro-preview` | 8/10 | 80.0% | 8/10 | 21.948s |
| 4 | `gemini-3.1-flash-lite` | 5/10 | 50.0% | 10/10 | 1.791s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.423s |

## Test v3

### Prompt Used

```text
You are a primary school mathematics teacher who knows Guaraní and Spanish.

You will receive a mathematical problem written in Guaraní.

Your first task is to make sense of the problem. Read the statement carefully, identify the important quantities, and understand what is being asked. Then solve the problem using simple operations.

Do not translate literally word for word if doing so makes the problem lose its meaning. Use your knowledge of Guaraní and Spanish to understand the mathematical idea in the statement.

Do not show your internal analysis.
Do not add any text before or after the JSON.
Do not use Markdown blocks.

Rules:
* One option must be correct.
* Two options must be incorrect but reasonable.
* All three options must be different.
* The correct answer must appear in a random position; it must not always be option A.
* Do not invent information that is not in the problem.
* Use simple words and short sentences, as if speaking to a 7-year-old child.
* Break the final solution into simple steps.
* The final explanation must be in Guaraní.
* The final steps must be in Guaraní.
* The final units must be in Guaraní.
* The final options must be in Guaraní.
* The JSON must be valid.
* Before responding, check that final_answer.value equals the value of the option indicated by correct_option_id.

Use exactly this structure:

{
"reasoning": "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.",
"steps": ["Peteĩha tembiapo oñemyesakãva guaraníme.", "Mokõiha tembiapo oñemyesakãva guaraníme."],
"final_answer": {"value": 0, "unit": "unidad guaraníme"},
"options": [{"id": "A", "value": 0, "unit": "unidad guaraníme"}, {"id": "B", "value": 0, "unit": "unidad guaraníme"}, {"id": "C", "value": 0, "unit": "unidad guaraníme"}],
"correct_option_id": "A"
}

Problem in Guaraní:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 9/10 | 90.0% | 10/10 | 8.295s |
| 2 | `gemini-3-flash-preview` | 8/10 | 80.0% | 10/10 | 13.913s |
| 3 | `gemini-3.1-pro-preview` | 8/10 | 80.0% | 8/10 | 21.954s |
| 4 | `gemini-3.1-flash-lite` | 6/10 | 60.0% | 10/10 | 1.538s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.417s |

## Test v4

### Prompt Used

```text
You are a primary school mathematics teacher who knows Guaraní and Spanish.

You will receive a mathematical problem written in Guaraní.

Your first task is to make sense of the problem. Read the statement carefully, identify the important quantities, and understand what is being asked. Then solve the problem using simple operations.

Do not translate literally word for word if doing so makes the problem lose its meaning. Use your knowledge of Guaraní and Spanish to understand the mathematical idea in the statement.

Help with interpreting common numbers and expressions in Guaraní:
* peteĩ = 1
* mokõi = 2
* mbohapy = 3
* irundy = 4
* po = 5
* poteĩpa = 60
* mokõipa = 20
* mokõi jey = twice
* irundy jey = four times
* peteĩteĩ = each one
* ñavõ = each
* hetave = more than
* hemby = left over or remaining

Before responding, check internally:
1. What quantity each number in the problem represents.
2. What each unit means.
3. Which operation is appropriate.
4. Whether you used all the important information in the statement.
5. Whether final_answer.value matches the value of the option indicated by correct_option_id.

Do not show your internal analysis.
Do not add any text before or after the JSON.
Do not use Markdown blocks.

Rules:
* One option must be correct.
* Two options must be incorrect but reasonable.
* All three options must be different.
* The correct answer must appear in a random position; it must not always be option A.
* Do not invent information that is not in the problem.
* Use simple words and short sentences, as if speaking to a 7-year-old child.
* Break the final solution into simple steps.
* The final explanation must be in Guaraní.
* The final steps must be in Guaraní.
* The final units must be in Guaraní.
* The final options must be in Guaraní.
* The JSON must be valid.
* Before responding, check that final_answer.value equals the value of the option indicated by correct_option_id.

Use exactly this structure:

{
"reasoning": "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.",
"steps": ["Peteĩha tembiapo oñemyesakãva guaraníme.", "Mokõiha tembiapo oñemyesakãva guaraníme."],
"final_answer": {"value": 0, "unit": "unidad guaraníme"},
"options": [{"id": "A", "value": 0, "unit": "unidad guaraníme"}, {"id": "B", "value": 0, "unit": "unidad guaraníme"}, {"id": "C", "value": 0, "unit": "unidad guaraníme"}],
"correct_option_id": "A"
}

Problem in Guaraní:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 10/10 | 100.0% | 10/10 | 10.360s |
| 2 | `gemini-3.1-pro-preview` | 8/10 | 80.0% | 8/10 | 22.091s |
| 3 | `gemini-3-flash-preview` | 6/10 | 60.0% | 8/10 | 19.332s |
| 4 | `gemini-3.1-flash-lite` | 5/10 | 50.0% | 10/10 | 1.628s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.420s |

## Test v5

### Prompt Used

```text
You are a primary school mathematics teacher. Your task is to solve and explain a mathematical problem for a 7-year-old child.

You must use simple words, short sentences, and operations that are easy to follow. The explanation must not be technical or complicated.

Solve the problem and generate three answer options:

* One option must be correct.
* Two options must be incorrect but reasonable.
* All three options must be different.
* The correct answer must appear in a random position; it must not always be option A.
* Do not invent information that is not in the problem.
* Briefly explain how you arrived at the answer.
* Break the solution into simple steps.
* Answers must be in Guaraní.
* Options must be in Guaraní.
* The explanation must be in Guaraní.
* You must not use Spanish or any language other than Guaraní in the final text values.

Strict formatting rules:
* Return only valid JSON.
* Do not add any text before or after the JSON.
* Do not use Markdown blocks.
* Do not use single quotes for property names or JSON strings.
* Do not add symbols such as ! outside strings.
* All property names must use double quotes.
* All text must be enclosed in double quotes.
* Do not leave strings unclosed.
* Do not leave lists or objects unclosed.
* Before responding, check that the JSON can be parsed with json.loads.
* Before responding, check that final_answer.value equals the value of the option indicated by correct_option_id.

Use exactly this structure:

{
"reasoning": "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.",
"steps": [
"Peteĩha tembiapo oñemyesakãva guaraníme.",
"Mokõiha tembiapo oñemyesakãva guaraníme."
],
"final_answer": {
"value": 0,
"unit": "unidad guaraníme"
},
"options": [
{"id": "A", "value": 0, "unit": "unidad guaraníme"},
{"id": "B", "value": 0, "unit": "unidad guaraníme"},
{"id": "C", "value": 0, "unit": "unidad guaraníme"}
],
"correct_option_id": "A"
}

Problem:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.1-pro-preview` | 10/10 | 100.0% | 10/10 | 22.127s |
| 2 | `gemini-3.5-flash` | 8/10 | 80.0% | 10/10 | 9.250s |
| 3 | `gemini-3-flash-preview` | 6/10 | 60.0% | 10/10 | 15.333s |
| 4 | `gemini-3.1-flash-lite` | 5/10 | 50.0% | 10/10 | 1.803s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.541s |

## Final Comparison

| Model | v1 | v2 | v3 | v4 | v5 | Best result |
|---|---:|---:|---:|---:|---:|---:|
| `gemini-3.5-flash` | 9/10 | 9/10 | 9/10 | 10/10 | 8/10 | 10/10 |
| `gemini-3.1-pro-preview` | 9/10 | 8/10 | 8/10 | 8/10 | 10/10 | 10/10 |
| `gemini-3-flash-preview` | 7/10 | 8/10 | 8/10 | 6/10 | 6/10 | 8/10 |
| `gemini-3.1-flash-lite` | 5/10 | 5/10 | 6/10 | 5/10 | 5/10 | 6/10 |
| `gemini-3.5-live-translate-preview` | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |

## Global Ranking

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 10/10 | 100.0% | 10/10 | 10.360s |
| 2 | `gemini-3.1-pro-preview` | 10/10 | 100.0% | 10/10 | 22.127s |
| 3 | `gemini-3-flash-preview` | 8/10 | 80.0% | 10/10 | 13.913s |
| 4 | `gemini-3.1-flash-lite` | 6/10 | 60.0% | 10/10 | 1.538s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.417s |

## Conclusion

The best absolute result was 10/10, achieved by `gemini-3.5-flash` with `v4`.
