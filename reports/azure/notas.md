Evaluaciones realizadas en las pruebas

Prueba 1 en guarani:

Promp: 
"Eres un profesor de matemáticas de primaria. Tu tarea es resolver y explicar un problema matemático para un niño de 7 años.

Debes utilizar palabras sencillas, oraciones cortas y operaciones fáciles de seguir. La explicación no puede ser técnica ni complicada.

Resuelve el problema y genera tres opciones de respuesta:

* Una opción debe ser correcta.
* Dos opciones deben ser incorrectas, pero razonables.
* Las tres opciones deben ser diferentes.
* La respuesta correcta debe aparecer en una posición aleatoria; no debe ser siempre la opción A.
* No inventes información que no aparezca en el problema.
* Explica brevemente cómo llegaste a la respuesta.
* Divide la solución en pasos simples.
* Devuelve exclusivamente un JSON válido.
* No agregues texto antes ni después del JSON.
* No utilices bloques Markdown.
* Las respuesta deben estar en guarani.
* Las opciones deben estar en guarani.
* La explicación debe estar en guarani.
* No puedes utilizar el español ni ningún otro idioma que no sea el guaraní.

Utiliza exactamente esta estructura:

{{
"reasoning": "Explicación breve y sencilla para un niño de 7 años.",
"steps": [
"Primer paso explicado de manera sencilla.",
"Segundo paso explicado de manera sencilla."
],
"final_answer": {{
"value": 0,
"unit": "unidad correspondiente"
}},
"options": [
{{
"id": "A",
"value": 0,
"unit": "unidad correspondiente"
}},
{{
"id": "B",
"value": 0,
"unit": "unidad correspondiente"
}},
{{
"id": "C",
"value": 0,
"unit": "unidad correspondiente"
}}
],
"correct_option_id": "A"
}}"

- Modelo más acertado: **gpt-4.1**

## Ranking Principal

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | Aciertos recuperados | JSON válido | Opción consistente | Errores API | Errores JSON | Latencia media |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | gpt-4.1 | 6/10 | 60.0% | 6/10 | 10/10 | 10/10 | 0 | 0 | 3.583s |
| 2 | gpt-5.4-mini | 5/10 | 50.0% | 5/10 | 10/10 | 10/10 | 0 | 0 | 3.089s |
| 3 | Llama-3.3-70B-Instruct | 5/10 | 50.0% | 5/10 | 9/10 | 9/10 | 0 | 1 | 4.797s |
| 4 | Mistral-Large-3 | 4/10 | 40.0% | 4/10 | 9/10 | 10/10 | 0 | 1 | 6.255s |
| 5 | grok-4-1-fast-non-reasoning | 3/10 | 30.0% | 3/10 | 10/10 | 10/10 | 0 | 0 | 3.640s |
| 6 | gpt-4o-mini | 2/10 | 20.0% | 2/10 | 10/10 | 10/10 | 0 | 0 | 3.038s |


Prueba 2, cambios en el promp.

