# Prueba Blind ChatGPT v5

Usa el siguiente prompt y resuelve los problemas listados al final.

No tienes respuestas esperadas.

Devuelve solamente JSONL.

Una línea JSON válida por problema.

No uses Markdown.

No agregues texto antes ni después del JSONL.

Cada línea debe tener esta estructura:

```json
{"provider":"chatgpt","model":"gpt-5","prompt_id":"v5","prompt_name":"Guaraní estricto con JSON reforzado","problem_id":1,"response":{"reasoning":"...","steps":["...","..."],"final_answer":{"value":0,"unit":"..."},"options":[{"id":"A","value":0,"unit":"..."},{"id":"B","value":0,"unit":"..."},{"id":"C","value":0,"unit":"..."}],"correct_option_id":"A"}}
```

Prompt v5:

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

Problemas:

```json
[
  {
    "id": 1,
    "problem": "Jimmy oreko hetave 2$ ombojo'a rire Ethel orekóva viru. Ethel orekórõ 8$, ¿Mboy viru oreko Jimmy?"
  },
  {
    "id": 2,
    "problem": "Porandu: Olivia oguereko 23$. Ojogua po mbujape he'ẽva 3$ peteĩteĩva. ¿Mboy pirapirépa hemby chupe?."
  },
  {
    "id": 3,
    "problem": "Peteĩ yvytu’i puku ou yguasúgui ojaty hag̃ua peteĩ táva. 10 minuto oiporu ojaty hag̃ua 3 milla tavapegua. Táva oñembojasoráramo 42 milla y rembe’y guive pehẽngue py’aguiguáicha peve, mboýpa minuto oiporúta yvytu’i puku ojaty haguã táva opaite?"
  },
  {
    "id": 4,
    "problem": "Dan oñotỹ 3 rósa máta. Cáda rósa máta 25 irrósa. Cáda rósa 8 hatĩ. Mbovy rósa ratĩpa oĩ?"
  },
  {
    "id": 5,
    "problem": "Opa  pyhare, Frankie oma'ẽ ta'ãngambyryre  omohu'ã rire hembiaporã. Arakõi ha Arapokõi pyharekue, oma'ẽ peteĩ episodio peteĩ aravo pukúva iprograma oguerohoryvévagui peteĩteĩ pyhare. Arapoteĩme, oma'ẽ heta episodio peteĩ programa 30 aravo'i pukúvagui. Arapo amóime, omohu'ã hembiaporã pya'e ha oma'ẽ peteĩ episodio peteĩ aravo pukúva ha avei peteĩ programa 30 aravo'i pukúva. Arapoteĩme, opyta opáy areve arapokõindy rehehápe ha oma'ẽ mokõi episodio peteĩ aravo pukúva. Ohecháramo 7 aravo televísiõ opaite, mboy episodio 30 aravo'i pukúvapa ohecha Arapoteĩme?"
  },
  {
    "id": 6,
    "problem": "Kelian oguereko mokõi tembi’u aporã: peteĩ oguereko mokõipa ñe'ẽryru ha mokoiha oguereko joyvy ñe'ẽryru peteĩha. ¿Mboy ñe'ẽryru omoñe'ẽ va'erã Kelian ojapo haguã  mokõi tembi'u ?"
  },
  {
    "id": 7,
    "problem": "Ary pukukuépe Tom oñotỹ 10 yvyramáta. Mokõi yvyramáta oikytĩ ñavõ ary.\n50 yvyramátagui oñepyrũ. Ohasa rire 10 ary , umi yvyramátagui  30% ipiru. Mboy yvyramátapiko hemby ichupe."
  },
  {
    "id": 8,
    "problem": "Jhon ojogua mokõi júnta sapatu mbohapyvéva ita'yra kuéra pe g̃uarã. Ambue oñehepyme'ẽ $60 (poteĩpa) . ¿Mboy ohepyme'ẽ?"
  },
  {
    "id": 9,
    "problem": "Brandon iPhone itujave irundy jey Ben iPhon-gui. Ben iPhone itujave mokõi jey Suzy iPhone-gui. Suzy iphone oguerekóramo 1 ary, Mboy arýpiko Brandon iphone oguereko"
  },
  {
    "id": 10,
    "problem": "Raphael oho ojogua mbaʼe oñekotevẽva mbo'ehaópe g̃uarã. Ojogua 4 haiha 1,5$ peteĩteĩva, 2 kuatiahai 4$ peteĩteĩva ha peteĩ aty kuatia bond ohupytýva 20$.  ¿Mboýpa ohupyty Raphael-pe opaite mba'e?"
  }
]
```
