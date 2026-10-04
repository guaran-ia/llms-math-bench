# Prompts y resultados Gemini v1 a v5

Evaluación sobre 10 problemas matemáticos en guaraní y 5 modelos Gemini. La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

## Prueba v1

### Prompt usado

```text
Eres un profesor de matemáticas de primaria. Tu tarea es resolver y explicar un problema matemático para un niño de 7 años.

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

{
"reasoning": "Explicación breve y sencilla para un niño de 7 años.",
"steps": [
"Primer paso explicado de manera sencilla.",
"Segundo paso explicado de manera sencilla."
],
"final_answer": {
"value": 0,
"unit": "unidad correspondiente"
},
"options": [
{"id": "A", "value": 0, "unit": "unidad correspondiente"},
{"id": "B", "value": 0, "unit": "unidad correspondiente"},
{"id": "C", "value": 0, "unit": "unidad correspondiente"}
],
"correct_option_id": "A"
}

Problema:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 9/10 | 90.0% | 10/10 | 10.139s |
| 2 | `gemini-3.1-pro-preview` | 9/10 | 90.0% | 9/10 | 25.630s |
| 3 | `gemini-3-flash-preview` | 7/10 | 70.0% | 10/10 | 14.184s |
| 4 | `gemini-3.1-flash-lite` | 5/10 | 50.0% | 10/10 | 1.940s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.920s |

## Prueba v2

### Prompt usado

```text
Eres un profesor de matemáticas de primaria y también traductor entre guaraní y español.

Recibirás un problema matemático escrito en guaraní.

Para resolverlo, sigue este proceso interno:
1. Traduce mentalmente el problema al español.
2. Resuelve el problema en español paso a paso.
3. Genera tres opciones de respuesta en español.
4. Traduce la explicación, los pasos, la unidad y las opciones al guaraní.
5. Devuelve solo el JSON final en guaraní.

No muestres la traducción al español.
No muestres el razonamiento en español.
No agregues texto antes ni después del JSON.
No uses bloques Markdown.

Reglas:
* Una opción debe ser correcta.
* Dos opciones deben ser incorrectas, pero razonables.
* Las tres opciones deben ser diferentes.
* La respuesta correcta debe aparecer en una posición aleatoria; no debe ser siempre la opción A.
* No inventes información que no aparezca en el problema.
* Usa palabras sencillas y oraciones cortas, como para un niño de 7 años.
* Divide la solución final en pasos simples.
* La explicación final debe estar en guaraní.
* Los pasos finales deben estar en guaraní.
* Las unidades finales deben estar en guaraní.
* Las opciones finales deben estar en guaraní.
* El JSON debe ser válido.
* Antes de responder, verifica que final_answer.value sea igual al valor de la opción indicada por correct_option_id.

Utiliza exactamente esta estructura:

{
"reasoning": "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.",
"steps": ["Peteĩha tembiapo oñemyesakãva guaraníme.", "Mokõiha tembiapo oñemyesakãva guaraníme."],
"final_answer": {"value": 0, "unit": "unidad guaraníme"},
"options": [{"id": "A", "value": 0, "unit": "unidad guaraníme"}, {"id": "B", "value": 0, "unit": "unidad guaraníme"}, {"id": "C", "value": 0, "unit": "unidad guaraníme"}],
"correct_option_id": "A"
}

Problema en guaraní:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 9/10 | 90.0% | 10/10 | 8.452s |
| 2 | `gemini-3-flash-preview` | 8/10 | 80.0% | 9/10 | 13.416s |
| 3 | `gemini-3.1-pro-preview` | 8/10 | 80.0% | 8/10 | 21.948s |
| 4 | `gemini-3.1-flash-lite` | 5/10 | 50.0% | 10/10 | 1.791s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.423s |

## Prueba v3

### Prompt usado

```text
Eres un profesor de matemáticas de primaria que sabe guaraní y español.

Recibirás un problema matemático escrito en guaraní.

Tu primera tarea es encontrarle sentido al problema. Lee con cuidado el enunciado, identifica las cantidades importantes y entiende qué se está preguntando. Después resuelve el problema con operaciones simples.

No traduzcas literalmente palabra por palabra si eso hace que el problema pierda sentido. Usa tu conocimiento de guaraní y español para entender la idea matemática del enunciado.

No muestres tu análisis interno.
No agregues texto antes ni después del JSON.
No uses bloques Markdown.

Reglas:
* Una opción debe ser correcta.
* Dos opciones deben ser incorrectas, pero razonables.
* Las tres opciones deben ser diferentes.
* La respuesta correcta debe aparecer en una posición aleatoria; no debe ser siempre la opción A.
* No inventes información que no aparezca en el problema.
* Usa palabras sencillas y oraciones cortas, como para un niño de 7 años.
* Divide la solución final en pasos simples.
* La explicación final debe estar en guaraní.
* Los pasos finales deben estar en guaraní.
* Las unidades finales deben estar en guaraní.
* Las opciones finales deben estar en guaraní.
* El JSON debe ser válido.
* Antes de responder, verifica que final_answer.value sea igual al valor de la opción indicada por correct_option_id.

Utiliza exactamente esta estructura:

{
"reasoning": "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.",
"steps": ["Peteĩha tembiapo oñemyesakãva guaraníme.", "Mokõiha tembiapo oñemyesakãva guaraníme."],
"final_answer": {"value": 0, "unit": "unidad guaraníme"},
"options": [{"id": "A", "value": 0, "unit": "unidad guaraníme"}, {"id": "B", "value": 0, "unit": "unidad guaraníme"}, {"id": "C", "value": 0, "unit": "unidad guaraníme"}],
"correct_option_id": "A"
}

Problema en guaraní:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 9/10 | 90.0% | 10/10 | 8.295s |
| 2 | `gemini-3-flash-preview` | 8/10 | 80.0% | 10/10 | 13.913s |
| 3 | `gemini-3.1-pro-preview` | 8/10 | 80.0% | 8/10 | 21.954s |
| 4 | `gemini-3.1-flash-lite` | 6/10 | 60.0% | 10/10 | 1.538s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.417s |

## Prueba v4

### Prompt usado

```text
Eres un profesor de matemáticas de primaria que sabe guaraní y español.

Recibirás un problema matemático escrito en guaraní.

Tu primera tarea es encontrarle sentido al problema. Lee con cuidado el enunciado, identifica las cantidades importantes y entiende qué se está preguntando. Después resuelve el problema con operaciones simples.

No traduzcas literalmente palabra por palabra si eso hace que el problema pierda sentido. Usa tu conocimiento de guaraní y español para entender la idea matemática del enunciado.

Ayuda para interpretar números y expresiones frecuentes en guaraní:
* peteĩ = 1
* mokõi = 2
* mbohapy = 3
* irundy = 4
* po = 5
* poteĩpa = 60
* mokõipa = 20
* mokõi jey = dos veces
* irundy jey = cuatro veces
* peteĩteĩ = cada uno
* ñavõ = cada
* hetave = más que
* hemby = sobra o queda

Antes de responder, revisa internamente:
1. Qué cantidad representa cada número del problema.
2. Qué significa cada unidad.
3. Qué operación corresponde.
4. Si usaste todos los datos importantes del enunciado.
5. Si final_answer.value coincide con el valor de la opción indicada por correct_option_id.

No muestres tu análisis interno.
No agregues texto antes ni después del JSON.
No uses bloques Markdown.

Reglas:
* Una opción debe ser correcta.
* Dos opciones deben ser incorrectas, pero razonables.
* Las tres opciones deben ser diferentes.
* La respuesta correcta debe aparecer en una posición aleatoria; no debe ser siempre la opción A.
* No inventes información que no aparezca en el problema.
* Usa palabras sencillas y oraciones cortas, como para un niño de 7 años.
* Divide la solución final en pasos simples.
* La explicación final debe estar en guaraní.
* Los pasos finales deben estar en guaraní.
* Las unidades finales deben estar en guaraní.
* Las opciones finales deben estar en guaraní.
* El JSON debe ser válido.
* Antes de responder, verifica que final_answer.value sea igual al valor de la opción indicada por correct_option_id.

Utiliza exactamente esta estructura:

{
"reasoning": "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.",
"steps": ["Peteĩha tembiapo oñemyesakãva guaraníme.", "Mokõiha tembiapo oñemyesakãva guaraníme."],
"final_answer": {"value": 0, "unit": "unidad guaraníme"},
"options": [{"id": "A", "value": 0, "unit": "unidad guaraníme"}, {"id": "B", "value": 0, "unit": "unidad guaraníme"}, {"id": "C", "value": 0, "unit": "unidad guaraníme"}],
"correct_option_id": "A"
}

Problema en guaraní:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 10/10 | 100.0% | 10/10 | 10.360s |
| 2 | `gemini-3.1-pro-preview` | 8/10 | 80.0% | 8/10 | 22.091s |
| 3 | `gemini-3-flash-preview` | 6/10 | 60.0% | 8/10 | 19.332s |
| 4 | `gemini-3.1-flash-lite` | 5/10 | 50.0% | 10/10 | 1.628s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.420s |

## Prueba v5

### Prompt usado

```text
Eres un profesor de matemáticas de primaria. Tu tarea es resolver y explicar un problema matemático para un niño de 7 años.

Debes utilizar palabras sencillas, oraciones cortas y operaciones fáciles de seguir. La explicación no puede ser técnica ni complicada.

Resuelve el problema y genera tres opciones de respuesta:

* Una opción debe ser correcta.
* Dos opciones deben ser incorrectas, pero razonables.
* Las tres opciones deben ser diferentes.
* La respuesta correcta debe aparecer en una posición aleatoria; no debe ser siempre la opción A.
* No inventes información que no aparezca en el problema.
* Explica brevemente cómo llegaste a la respuesta.
* Divide la solución en pasos simples.
* Las respuestas deben estar en guaraní.
* Las opciones deben estar en guaraní.
* La explicación debe estar en guaraní.
* No puedes utilizar el español ni ningún otro idioma que no sea el guaraní en los valores de texto finales.

Reglas estrictas de formato:
* Devuelve exclusivamente un JSON válido.
* No agregues texto antes ni después del JSON.
* No utilices bloques Markdown.
* No uses comillas simples para nombres de propiedades ni strings JSON.
* No agregues signos como ! fuera de strings.
* Todos los nombres de propiedades deben usar comillas dobles.
* Todos los textos deben estar entre comillas dobles.
* No dejes strings sin cerrar.
* No dejes listas u objetos sin cerrar.
* Antes de responder, verifica que el JSON pueda ser parseado con json.loads.
* Antes de responder, verifica que final_answer.value sea igual al valor de la opción indicada por correct_option_id.

Utiliza exactamente esta estructura:

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

Problema:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.1-pro-preview` | 10/10 | 100.0% | 10/10 | 22.127s |
| 2 | `gemini-3.5-flash` | 8/10 | 80.0% | 10/10 | 9.250s |
| 3 | `gemini-3-flash-preview` | 6/10 | 60.0% | 10/10 | 15.333s |
| 4 | `gemini-3.1-flash-lite` | 5/10 | 50.0% | 10/10 | 1.803s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.541s |

## Comparación final

| Modelo | v1 | v2 | v3 | v4 | v5 | Mejor resultado |
|---|---:|---:|---:|---:|---:|---:|
| `gemini-3.5-flash` | 9/10 | 9/10 | 9/10 | 10/10 | 8/10 | 10/10 |
| `gemini-3.1-pro-preview` | 9/10 | 8/10 | 8/10 | 8/10 | 10/10 | 10/10 |
| `gemini-3-flash-preview` | 7/10 | 8/10 | 8/10 | 6/10 | 6/10 | 8/10 |
| `gemini-3.1-flash-lite` | 5/10 | 5/10 | 6/10 | 5/10 | 5/10 | 6/10 |
| `gemini-3.5-live-translate-preview` | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 | 0/10 |

## Ranking global

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gemini-3.5-flash` | 10/10 | 100.0% | 10/10 | 10.360s |
| 2 | `gemini-3.1-pro-preview` | 10/10 | 100.0% | 10/10 | 22.127s |
| 3 | `gemini-3-flash-preview` | 8/10 | 80.0% | 10/10 | 13.913s |
| 4 | `gemini-3.1-flash-lite` | 6/10 | 60.0% | 10/10 | 1.538s |
| 5 | `gemini-3.5-live-translate-preview` | 0/10 | 0.0% | 0/10 | 0.417s |

## Conclusión

El mejor resultado absoluto fue 10/10. Lo alcanzó `gemini-3.5-flash` con `v4`.
