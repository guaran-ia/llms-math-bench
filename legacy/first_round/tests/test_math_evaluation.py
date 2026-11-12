import unittest
import importlib.util

from src.math_evaluation import equivalent, evaluate, extract_json


class MathEvaluationTests(unittest.TestCase):
    def test_numeric_and_decimal_comma(self):
        self.assertTrue(equivalent(1.5, "1,5"))
        self.assertFalse(equivalent(10, True))
        self.assertFalse(equivalent(100, "Answer: 100"))

    @unittest.skipUnless(importlib.util.find_spec("sympy"), "SymPy is optional in the test environment")
    def test_sympy_equivalence(self):
        self.assertTrue(equivalent("(x + 2)^2 + (y + 4)^2 = 18", "(y+4)**2+(x+2)**2=18"))
        self.assertTrue(equivalent("(x+1)^2+(y-1)^2=25", "x^2+y^2+2*x-2*y-23=0"))

    def test_structured_values(self):
        self.assertTrue(equivalent({"center": [-6, 5], "radius": 1}, {"centro": [-6, 5], "radio": "1"}))
        self.assertTrue(equivalent([1, 2], "(1, 2)"))
        self.assertFalse(equivalent({"radius": 1}, {"radius": 2}))

    def test_json_recovery_requires_explicit_final_answer(self):
        recovered = extract_json('Result: {"final_answer": {"value": 7}}')
        self.assertEqual(recovered["final_answer"]["value"], 7)
        row = {"expected_answer": 7, "raw_response": "The calculation mentions 7, but no answer field."}
        self.assertFalse(evaluate(row)["correct"])

    def test_malformed_json_is_not_scored_from_arbitrary_number(self):
        row = {"expected_answer": 12, "raw_response": "I tried 12 but could not solve it."}
        self.assertFalse(evaluate(row)["correct"])


if __name__ == "__main__":
    unittest.main()
