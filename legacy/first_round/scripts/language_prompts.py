"""Generate matched language variants from a versioned benchmark prompt."""


def language_prompt(template, language):
    if language == "gn":
        return template
    if language != "es":
        raise ValueError("language must be 'gn' or 'es'")
    replacements = {
        "Problema en guaraní:": "Problema en español:",
        "escrito en guaraní": "escrito en español",
        "Traduce mentalmente el problema al español.": "Lee el problema en español.",
        "Traduce la explicación, los pasos, la unidad y las opciones al guaraní.": "Escribe la explicación, los pasos, la unidad y las opciones en español.",
        "Devuelve solo el JSON final en guaraní.": "Devuelve solo el JSON final en español.",
        "No puedes utilizar el español ni ningún otro idioma que no sea el guaraní en los valores de texto finales.": "Utiliza únicamente el español en los valores de texto finales.",
        "No puedes utilizar el español ni ningún otro idioma que no sea el guaraní.": "Responde únicamente en español.",
        "Ñemyesakã mbyky ha ndahasýiva mitãme g̃uarã.": "Explicación breve y clara en español.",
        "Ñemyesakã mbyky guaraníme.": "Explicación breve en español.",
        "Peteĩha tembiapo oñemyesakãva guaraníme.": "Primer paso explicado en español.",
        "Mokõiha tembiapo oñemyesakãva guaraníme.": "Segundo paso explicado en español.",
        "Peteĩha paso guaraníme.": "Primer paso en español.",
        "Mokõiha paso guaraníme.": "Segundo paso en español.",
        "unidad guaraníme": "unidad en español",
        "en guaraní claro y simple": "en español claro y simple",
        "en guaraní claro": "en español claro",
        "en guaraní": "en español",
        "No uses la traducción al español.": "",
        "No uses traducción al español.": "",
        "No muestres la traducción al español.": "",
        "No muestres el razonamiento en español.": "",
        "problem_gn": "problem_es",
    }
    for source, target in replacements.items():
        template = template.replace(source, target)
    return template
