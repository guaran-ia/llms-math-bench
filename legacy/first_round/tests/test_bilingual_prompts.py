import json
import unittest
from pathlib import Path

from src.language_prompts import language_prompt


class BilingualPromptTests(unittest.TestCase):
    def test_guarani_template_is_preserved(self):
        source = "Problema escrito en guaraní.\nNo uses la traducción al español.\n{problem}"
        self.assertEqual(language_prompt(source, "gn"), source)

    def test_spanish_variant_switches_language_instructions(self):
        prompts = json.loads(Path("prompts/guarani_math_prompts.json").read_text(encoding="utf-8"))
        prompt = next(item["template"] for item in prompts if item["id"] == "v10")
        if isinstance(prompt, list):
            prompt = "\n".join(prompt)
        spanish = language_prompt(prompt, "es")
        self.assertIn("Problema en español:", spanish)
        self.assertIn("español claro y simple", spanish)
        self.assertNotIn("Problema en guaraní:", spanish)
        self.assertNotIn("No uses la traducción al español.", spanish)
        self.assertNotIn("guaraníme", spanish)

    def test_legacy_template_language_constraints_are_rewritten(self):
        prompts = json.loads(Path("prompts/guarani_math_prompts.json").read_text(encoding="utf-8"))
        for prompt_id in ("v1", "v2", "v5", "v6"):
            source = next(item["template"] for item in prompts if item["id"] == prompt_id)
            if isinstance(source, list):
                source = "\n".join(source)
            spanish = language_prompt(source, "es")
            self.assertNotIn("no sea el guaraní", spanish.casefold(), prompt_id)
            self.assertNotIn("guaraníme", spanish, prompt_id)

    def test_unknown_language_is_rejected(self):
        with self.assertRaises(ValueError):
            language_prompt("template", "pt")
