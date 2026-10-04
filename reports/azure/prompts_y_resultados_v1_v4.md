# Prompts y resultados v1 a v4

Evaluación sobre 10 problemas matemáticos en guaraní y 6 modelos. La métrica principal es el acierto estricto: `response.final_answer.value == expected_answer`.

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
{
"id": "A",
"value": 0,
"unit": "unidad correspondiente"
},
{
"id": "B",
"value": 0,
"unit": "unidad correspondiente"
},
{
"id": "C",
"value": 0,
"unit": "unidad correspondiente"
}
],
"correct_option_id": "A"
}

Problema:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 6/10 | 60.0% | 10/10 | 3.583s |
| 2 | `gpt-5.4-mini` | 5/10 | 50.0% | 10/10 | 3.089s |
| 3 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 9/10 | 4.797s |
| 4 | `Mistral-Large-3` | 4/10 | 40.0% | 9/10 | 6.255s |
| 5 | `grok-4-1-fast-non-reasoning` | 3/10 | 30.0% | 10/10 | 3.640s |
| 6 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.038s |

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

Problema en guaraní:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 2.791s |
| 2 | `Mistral-Large-3` | 5/10 | 50.0% | 10/10 | 5.099s |
| 3 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 10/10 | 2.557s |
| 4 | `gpt-5.4-mini` | 4/10 | 40.0% | 10/10 | 2.788s |
| 5 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 3.025s |
| 6 | `grok-4-1-fast-non-reasoning` | 2/10 | 20.0% | 9/10 | 13.146s |

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

Problema en guaraní:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 6/10 | 60.0% | 10/10 | 2.934s |
| 2 | `Llama-3.3-70B-Instruct` | 5/10 | 50.0% | 10/10 | 2.449s |
| 3 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 2.828s |
| 4 | `Mistral-Large-3` | 4/10 | 40.0% | 10/10 | 7.044s |
| 5 | `gpt-4o-mini` | 2/10 | 20.0% | 10/10 | 2.474s |
| 6 | `grok-4-1-fast-non-reasoning` | 1/10 | 10.0% | 10/10 | 36.437s |

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

Problema en guaraní:

{problem}
```

### Resultado de los modelos

| Posición | Modelo | Aciertos estrictos | Exactitud estricta | JSON válido | Latencia media |
|---:|---|---:|---:|---:|---:|
| 1 | `gpt-5.4-mini` | 6/10 | 60.0% | 10/10 | 2.934s |
| 2 | `gpt-4.1` | 5/10 | 50.0% | 10/10 | 4.031s |
| 3 | `Mistral-Large-3` | 4/10 | 40.0% | 10/10 | 5.636s |
| 4 | `Llama-3.3-70B-Instruct` | 4/10 | 40.0% | 9/10 | 2.687s |
| 5 | `gpt-4o-mini` | 3/10 | 30.0% | 10/10 | 2.932s |
| 6 | `grok-4-1-fast-non-reasoning` | 0/10 | 0.0% | 6/10 | 31.346s |

## Comparación final

| Modelo | v1 | v2 | v3 | v4 | Mejor resultado |
|---|---:|---:|---:|---:|---:|
| `gpt-4.1` | 6/10 | 5/10 | 5/10 | 5/10 | 6/10 |
| `gpt-5.4-mini` | 5/10 | 4/10 | 6/10 | 6/10 | 6/10 |
| `Llama-3.3-70B-Instruct` | 5/10 | 4/10 | 5/10 | 4/10 | 5/10 |
| `Mistral-Large-3` | 4/10 | 5/10 | 4/10 | 4/10 | 5/10 |
| `grok-4-1-fast-non-reasoning` | 3/10 | 2/10 | 1/10 | 0/10 | 3/10 |
| `gpt-4o-mini` | 2/10 | 2/10 | 2/10 | 3/10 | 3/10 |

## Conclusión

El mejor resultado absoluto fue 6/10. Lo alcanzaron `gpt-4.1` con v1 y `gpt-5.4-mini` con v3 y v4.

El prompt v3 es el mejor candidato general: conserva el máximo de 6/10, mantiene buen desempeño en `Llama-3.3-70B-Instruct` y evita el deterioro fuerte que v4 causó en `grok-4-1-fast-non-reasoning`.
