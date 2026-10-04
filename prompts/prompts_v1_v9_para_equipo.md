# Prompts v1 a v9

Prompts usados para evaluar problemas matemáticos en guaraní.

## Resumen

| Prompt | Nombre | Resumen |
|---|---|---|
| `v1` | Guaraní estricto | Guaraní estricto inicial con salida JSON. |
| `v2` | Traducción interna al español | Traducción interna al español antes de responder en guaraní. |
| `v3` | Profesor bilingüe con interpretación semántica | Profesor bilingüe con interpretación semántica del problema. |
| `v4` | Profesor bilingüe con glosario | Profesor bilingüe con glosario guaraní-español. |
| `v5` | Guaraní estricto con JSON reforzado | Guaraní estricto con reglas reforzadas de JSON. |
| `v6` | Guaraní estricto con JSON reforzado y warmup | v5 con warmup/few-shot matemático. |
| `v7` | Profesor bilingüe con glosario y warmup | v4 con warmup/few-shot matemático. |
| `v8` | Autocomplete simple zero-shot | Autocomplete simple zero-shot; solo resultado numérico. |
| `v9` | Autocomplete simple few-shot | Autocomplete simple few-shot; solo resultado numérico. |

## v1: Guaraní estricto

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

## v2: Traducción interna al español

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

## v3: Profesor bilingüe con interpretación semántica

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

## v4: Profesor bilingüe con glosario

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

## v5: Guaraní estricto con JSON reforzado

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

## v6: Guaraní estricto con JSON reforzado y warmup

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

Calentamiento de razonamiento matemático:

Los siguientes ejemplos están en español solo para mostrar el patrón de razonamiento.
No copies datos, números ni respuestas de estos ejemplos.
Úsalos solamente para aprender cómo razonar:
1. identificar cantidades iniciales,
2. identificar cantidades agregadas, quitadas o repetidas,
3. hacer las operaciones en orden,
4. verificar la respuesta final.

Ejemplo 1:
Pregunta: Había nueve computadoras en la sala de servidores. Se instalaron cinco computadoras cada día, de lunes a jueves. ¿Cuántas computadoras hay ahora en la sala de servidores?
Respuesta paso a paso: Hay 4 días de lunes a jueves. Se agregaron 5 computadoras cada día. Eso significa que en total se agregaron 4 * 5 = 20 computadoras. Al principio, había 9 computadoras, por lo que ahora hay 9 + 20 = 29 computadoras. La respuesta es 29.
Respuesta final: 29
Operaciones: 4 * 5 = 20. 9 + 20 = 29.

Ejemplo 2:
Pregunta: Leah tenía 32 chocolates y su hermana tenía 42. Si se comieron 35, ¿cuántos chocolates les quedan en total?
Respuesta paso a paso: Leah tenía 32 chocolates y la hermana de Leah tenía 42. Quiere decir que originalmente había 32 + 42 = 74 chocolates. Se comieron 35. Por lo tanto, en total todavía tienen 74 - 35 = 39 chocolates. La respuesta es 39.
Respuesta final: 39
Operaciones: 32 + 42 = 74. 74 - 35 = 39.

Ejemplo 3:
Pregunta: Olivia tiene $23. Compró cinco roscas a $3 cada una. ¿Cuánto dinero le queda?
Respuesta paso a paso: 5 roscas a $3 cada una deben costar 5 * 3 = 15 dólares. Olivia tenía $23 al principio, por lo tanto ahora le quedan 23 - 15 = 8 dólares. La respuesta es 8.
Respuesta final: 8
Operaciones: 5 * 3 = 15. 23 - 15 = 8.

Ahora resuelve el problema real desde cero.
No copies números ni respuestas de los ejemplos.
No muestres los ejemplos en la respuesta final.
La respuesta final debe estar en guaraní y debe ser solo el JSON solicitado.

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

## v7: Profesor bilingüe con glosario y warmup

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

Calentamiento de razonamiento matemático:

Los siguientes ejemplos están en español solo para mostrar el patrón de razonamiento.
No copies datos, números ni respuestas de estos ejemplos.
Úsalos solamente para aprender cómo razonar:
1. identificar cantidades iniciales,
2. identificar cantidades agregadas, quitadas o repetidas,
3. hacer las operaciones en orden,
4. verificar la respuesta final.

Ejemplo 1:
Pregunta: Había nueve computadoras en la sala de servidores. Se instalaron cinco computadoras cada día, de lunes a jueves. ¿Cuántas computadoras hay ahora en la sala de servidores?
Respuesta paso a paso: Hay 4 días de lunes a jueves. Se agregaron 5 computadoras cada día. Eso significa que en total se agregaron 4 * 5 = 20 computadoras. Al principio, había 9 computadoras, por lo que ahora hay 9 + 20 = 29 computadoras. La respuesta es 29.
Respuesta final: 29
Operaciones: 4 * 5 = 20. 9 + 20 = 29.

Ejemplo 2:
Pregunta: Leah tenía 32 chocolates y su hermana tenía 42. Si se comieron 35, ¿cuántos chocolates les quedan en total?
Respuesta paso a paso: Leah tenía 32 chocolates y la hermana de Leah tenía 42. Quiere decir que originalmente había 32 + 42 = 74 chocolates. Se comieron 35. Por lo tanto, en total todavía tienen 74 - 35 = 39 chocolates. La respuesta es 39.
Respuesta final: 39
Operaciones: 32 + 42 = 74. 74 - 35 = 39.

Ejemplo 3:
Pregunta: Olivia tiene $23. Compró cinco roscas a $3 cada una. ¿Cuánto dinero le queda?
Respuesta paso a paso: 5 roscas a $3 cada una deben costar 5 * 3 = 15 dólares. Olivia tenía $23 al principio, por lo tanto ahora le quedan 23 - 15 = 8 dólares. La respuesta es 8.
Respuesta final: 8
Operaciones: 5 * 3 = 15. 23 - 15 = 8.

Ahora resuelve el problema real desde cero.
No copies números ni respuestas de los ejemplos.
No muestres los ejemplos en la respuesta final.
La respuesta final debe estar en guaraní y debe ser solo el JSON solicitado.

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

## v8: Autocomplete simple zero-shot

```text
Problema: {problem}
Solución (retorna solamente el resultado numérico, sin explicación, sin unidad y sin texto adicional):
```

## v9: Autocomplete simple few-shot

```text
Pregunta: Había nueve computadoras en la sala de servidores. Se instalaron cinco computadoras cada día, de lunes a jueves. ¿Cuántas computadoras hay ahora en la sala de servidores?
Solución (retorna solamente el resultado numérico): 29

Pregunta: Leah tenía 32 chocolates y su hermana tenía 42. Si se comieron 35, ¿cuántos chocolates les quedan en total?
Solución (retorna solamente el resultado numérico): 39

Pregunta: Olivia tiene $23. Compró cinco roscas a $3 cada una. ¿Cuánto dinero le queda?
Solución (retorna solamente el resultado numérico): 8

Problema: {problem}
Solución (retorna solamente el resultado numérico, sin explicación, sin unidad y sin texto adicional):
```
