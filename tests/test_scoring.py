import unittest
from tools.check_predictions import parse_answer, score


class ScoringTests(unittest.TestCase):
    def test_rejects_ambiguous_or_non_integer_answers(self):
        for text in ["<answer>2</answer><answer>3</answer>",
                     "<answer>2.0</answer>", "2", "", None]:
            self.assertIsNone(parse_answer(text))
        self.assertEqual(parse_answer(" <answer>-3</answer>\n"), -3)

    def test_invalid_predictions_remain_in_denominator(self):
        result = score([
            {"id": "a", "expected": "2", "prediction": "<answer>2</answer>"},
            {"id": "b", "expected": "2", "prediction": "invalid"},
        ])
        self.assertEqual(result["accuracy"], 0.5)
        self.assertEqual(result["format_rate"], 0.5)

    def test_rejects_empty_and_duplicate_data(self):
        with self.assertRaises(ValueError):
            score([])
        row = {"id": "a", "expected": "2", "prediction": "<answer>2</answer>"}
        with self.assertRaises(ValueError):
            score([row, row])


if __name__ == "__main__":
    unittest.main()
