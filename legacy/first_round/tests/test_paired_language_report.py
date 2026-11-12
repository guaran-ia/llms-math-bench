import unittest
from src.paired_language_report import analyze, exact_mcnemar, holm_adjust, wilson


class PairedStatisticsTests(unittest.TestCase):
    def test_wilson_interval(self):
        low, high = wilson(10, 10)
        self.assertLess(low, 1)
        self.assertEqual(high, 1)
        self.assertEqual(wilson(0, 0), (None, None))

    def test_exact_mcnemar(self):
        self.assertEqual(exact_mcnemar(0, 0), 1.0)
        self.assertEqual(exact_mcnemar(5, 0), 0.0625)
        self.assertEqual(exact_mcnemar(0, 5), 0.0625)

    def test_holm_adjustment(self):
        self.assertEqual(holm_adjust([0.01, 0.04, 0.03]), [0.03, 0.06, 0.06])

    def test_only_complete_language_pairs_are_compared(self):
        def row(language, problem_id, value):
            return {"language": language, "provider": "test", "model": "m", "prompt_pair_id": "p",
                    "problem_id": problem_id, "expected_answer": 1,
                    "response": {"final_answer": {"value": value}}}
        stats = analyze([row("gn", 1, 1), row("es", 1, 0), row("gn", 2, 1)])
        self.assertEqual(stats[0]["n"], 1)
        self.assertEqual(stats[0]["gn_only"], 1)
