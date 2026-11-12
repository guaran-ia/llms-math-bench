# Prompts v1 to v9

> Prompt instructions are translated into English for reference. The original experimental prompts remain in `guarani_math_prompts.json` in the prompts directory. Guaraní text and literal model outputs are preserved.

Prompts used to evaluate mathematical problems in Guaraní.

## Summary

| Prompt | Name | Summary |
|---|---|---|
| `v1` | Strict Guaraní | Initial strict Guaraní prompt with JSON output. |
| `v2` | Internal translation into Spanish | Internal translation into Spanish before answering in Guaraní. |
| `v3` | Bilingual teacher with semantic interpretation | Bilingual teacher with semantic interpretation of the problem. |
| `v4` | Bilingual teacher with glossary | Bilingual teacher with a Guaraní–Spanish glossary. |
| `v5` | Strict Guaraní with reinforced JSON rules | Strict Guaraní with reinforced JSON rules. |
| `v6` | Strict Guaraní with reinforced JSON rules and warmup | v5 with mathematical warmup/few-shot examples. |
| `v7` | Bilingual teacher with glossary and warmup | v4 with mathematical warmup/few-shot examples. |
| `v8` | Simple zero-shot autocomplete | Simple zero-shot autocomplete; numeric result only. |
| `v9` | Simple few-shot autocomplete | Simple few-shot autocomplete; numeric result only. |

## v1: Strict Guaraní

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

## v2: Internal translation into Spanish

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

## v3: Bilingual teacher with semantic interpretation

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

## v4: Bilingual teacher with glossary

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

## v5: Strict Guaraní with reinforced JSON rules

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

## v6: Strict Guaraní with reinforced JSON rules and warmup

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

Mathematical reasoning warmup:

The following examples are in Spanish only to illustrate the reasoning pattern.
Do not copy information, numbers, or answers from these examples.
Use them only to learn how to reason:
1. identify initial quantities,
2. identify quantities added, removed, or repeated,
3. perform the operations in order,
4. check the final answer.

Example 1:
Question: There were nine computers in the server room. Five computers were installed each day, from Monday to Thursday. How many computers are in the server room now?
Step-by-step answer: There are 4 days from Monday to Thursday. 5 computers were added each day. This means that a total of 4 * 5 = 20 computers were added. Initially, there were 9 computers, so there are now 9 + 20 = 29 computers. The answer is 29.
Final answer: 29
Operations: 4 * 5 = 20. 9 + 20 = 29.

Example 2:
Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many chocolates do they have left in total?
Step-by-step answer: Leah had 32 chocolates and Leah's sister had 42. This means there were originally 32 + 42 = 74 chocolates. They ate 35. Therefore, they still have a total of 74 - 35 = 39 chocolates. The answer is 39.
Final answer: 39
Operations: 32 + 42 = 74. 74 - 35 = 39.

Example 3:
Question: Olivia has $23. She bought five doughnuts at $3 each. How much money does she have left?
Step-by-step answer: 5 doughnuts at $3 each cost 5 * 3 = 15 dollars. Olivia initially had $23, so she now has 23 - 15 = 8 dollars left. The answer is 8.
Final answer: 8
Operations: 5 * 3 = 15. 23 - 15 = 8.

Now solve the actual problem from scratch.
Do not copy numbers or answers from the examples.
Do not show the examples in the final answer.
The final answer must be in Guaraní and contain only the requested JSON.

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

## v7: Bilingual teacher with glossary and warmup

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

Mathematical reasoning warmup:

The following examples are in Spanish only to illustrate the reasoning pattern.
Do not copy information, numbers, or answers from these examples.
Use them only to learn how to reason:
1. identify initial quantities,
2. identify quantities added, removed, or repeated,
3. perform the operations in order,
4. check the final answer.

Example 1:
Question: There were nine computers in the server room. Five computers were installed each day, from Monday to Thursday. How many computers are in the server room now?
Step-by-step answer: There are 4 days from Monday to Thursday. 5 computers were added each day. This means that a total of 4 * 5 = 20 computers were added. Initially, there were 9 computers, so there are now 9 + 20 = 29 computers. The answer is 29.
Final answer: 29
Operations: 4 * 5 = 20. 9 + 20 = 29.

Example 2:
Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many chocolates do they have left in total?
Step-by-step answer: Leah had 32 chocolates and Leah's sister had 42. This means there were originally 32 + 42 = 74 chocolates. They ate 35. Therefore, they still have a total of 74 - 35 = 39 chocolates. The answer is 39.
Final answer: 39
Operations: 32 + 42 = 74. 74 - 35 = 39.

Example 3:
Question: Olivia has $23. She bought five doughnuts at $3 each. How much money does she have left?
Step-by-step answer: 5 doughnuts at $3 each cost 5 * 3 = 15 dollars. Olivia initially had $23, so she now has 23 - 15 = 8 dollars left. The answer is 8.
Final answer: 8
Operations: 5 * 3 = 15. 23 - 15 = 8.

Now solve the actual problem from scratch.
Do not copy numbers or answers from the examples.
Do not show the examples in the final answer.
The final answer must be in Guaraní and contain only the requested JSON.

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

## v8: Simple zero-shot autocomplete

```text
Problem: {problem}
Solution (return only the numeric result, without an explanation, unit, or additional text):
```

## v9: Simple few-shot autocomplete

```text
Question: There were nine computers in the server room. Five computers were installed each day, from Monday to Thursday. How many computers are in the server room now?
Solution (return only the numeric result): 29

Question: Leah had 32 chocolates and her sister had 42. If they ate 35, how many chocolates do they have left in total?
Solution (return only the numeric result): 39

Question: Olivia has $23. She bought five doughnuts at $3 each. How much money does she have left?
Solution (return only the numeric result): 8

Problem: {problem}
Solution (return only the numeric result, without an explanation, unit, or additional text):
```
