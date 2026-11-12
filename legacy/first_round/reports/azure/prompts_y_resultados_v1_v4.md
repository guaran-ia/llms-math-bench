# Prompts and Results v1 to v4

> Prompt instructions are translated into English for reference. The original experimental prompts remain in `guarani_math_prompts.json` in the prompts directory. Guaraní text and literal model outputs are preserved.

Evaluation of 10 mathematical problems in Guaraní across 6 models. The main metric is strict accuracy: `response.final_answer.value == expected_answer`.

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
{
"id": "A",
"value": 0,
"unit": "corresponding unit"
},
{
"id": "B",
"value": 0,
"unit": "corresponding unit"
},
{
"id": "C",
"value": 0,
"unit": "corresponding unit"
}
],
"correct_option_id": "A"
}

Problem:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 6/10 | 60.0% | 10/10 | 3.583s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.089s |
| 3 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 9/10 | 4.797s |
| 4 | `Mistral-Large-3` | 4/10 | 40.0% | 9/10 | 6.255s |
| 5 | `grok-4-1-fast-non-reasoning` | 3/10 | 30.0% | 10/10 | 3.640s |
| 6 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.038s |

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
"steps": [
"Peteĩha tembiapo oñemyesakãva guaraníme.",
"Mokõiha tembiapo oñemyesakãva guaraníme."
],
"final_answer": {
"value": 0,
"unit": "unidad guaraníme"
},
"options": [
{
"id": "A",
"value": 0,
"unit": "unidad guaraníme"
},
{
"id": "B",
"value": 0,
"unit": "unidad guaraníme"
},
{
"id": "C",
"value": 0,
"unit": "unidad guaraníme"
}
],
"correct_option_id": "A"
}

Problem in Guaraní:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 2.791s |
| 2 | `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 5.099s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 2.557s |
| 4 | `gpt-5.4-mini` | 4/10 | 40.0% | 10/10 | 2.788s |
| 5 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.025s |
| 6 | `grok-4-1-fast-non-reasoning` | 2/10 | 20.0% | 9/10 | 13.146s |

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
"steps": [
"Peteĩha tembiapo oñemyesakãva guaraníme.",
"Mokõiha tembiapo oñemyesakãva guaraníme."
],
"final_answer": {
"value": 0,
"unit": "unidad guaraníme"
},
"options": [
{
"id": "A",
"value": 0,
"unit": "unidad guaraníme"
},
{
"id": "B",
"value": 0,
"unit": "unidad guaraníme"
},
{
"id": "C",
"value": 0,
"unit": "unidad guaraníme"
}
],
"correct_option_id": "A"
}

Problem in Guaraní:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 6/10 | 60.0% | 10/10 | 2.934s |
| 2 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 10/10 | 2.449s |
| 3 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 2.828s |
| 4 | `Mistral-Large-3` | 4/10 | 40.0% | 10/10 | 7.044s |
| 5 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 2.474s |
| 6 | `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 10/10 | 36.437s |

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
"steps": [
"Peteĩha tembiapo oñemyesakãva guaraníme.",
"Mokõiha tembiapo oñemyesakãva guaraníme."
],
"final_answer": {
"value": 0,
"unit": "unidad guaraníme"
},
"options": [
{
"id": "A",
"value": 0,
"unit": "unidad guaraníme"
},
{
"id": "B",
"value": 0,
"unit": "unidad guaraníme"
},
{
"id": "C",
"value": 0,
"unit": "unidad guaraníme"
}
],
"correct_option_id": "A"
}

Problem in Guaraní:

{problem}
```

### Model Results

| Rank | Model | Strict correct answers | Strict accuracy | Valid JSON | Mean latency |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 6/10 | 60.0% | 10/10 | 2.934s |
| 2 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 4.031s |
| 3 | `Mistral-Large-3` | 4/10 | 40.0% | 10/10 | 5.636s |
| 4 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 9/10 | 2.687s |
| 5 | `gpt-4o-mini` | 3/10 | 30.0% | 10/10 | 2.932s |
| 6 | `grok-4-1-fast-non-reasoning` | 0/10 | 0.0% | 6/10 | 31.346s |

## Final Comparison

| Model | v1 | v2 | v3 | v4 | Best result |
|---|---:|---:|---:|---:|---:|
| `gpt-4.1` | 6/10 | 5/10 | 5/10 | 5/10 | 6/10 |
| `gpt-5.4-mini` | 5/10 | 4/10 | 6/10 | 6/10 | 6/10 |
| `Llama-3.3-70B-Instruct` | 5/10 | 4/10 | 5/10 | 4/10 | 5/10 |
| `Mistral-Large-3` | 4/10 | 5/10 | 4/10 | 4/10 | 5/10 |
| `grok-4-1-fast-non-reasoning` | 3/10 | 2/10 | 1/10 | 0/10 | 3/10 |
| `gpt-4o-mini` | 2/10 | 2/10 | 2/10 | 3/10 | 3/10 |

## Conclusion

The best absolute result was 6/10. It was achieved by `gpt-4.1` with v1 and `gpt-5.4-mini` with v3 and v4.

Prompt v3 is the best overall candidate: it retains the maximum of 6/10, maintains good performance with `Llama-3.3-70B-Instruct`, and avoids the sharp decline that v4 caused for `grok-4-1-fast-non-reasoning`.
