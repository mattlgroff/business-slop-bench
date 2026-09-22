import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('calibration_response', ROOT / 'reviews/grader-calibration-v1/validate-response.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ResponseValidationTest(unittest.TestCase):
    def setUp(self):
        self.packet = {'cases': [{'id': 'case-a', 'deliverable': 'Approval is pending.'},
                                 {'id': 'case-b', 'deliverable': 'The total is $16,000.'}]}
        self.rows = [{'id': 'case-a', 'verdict': 'review', 'reason': 'Ambiguous authority.', 'evidenceQuote': 'Approval is pending.'},
                     {'id': 'case-b', 'verdict': 'pass', 'reason': 'Correct amount.', 'evidenceQuote': '$16,000'}]

    def test_accepts_unresolved_and_preserves_input(self):
        original = copy.deepcopy(self.rows)
        self.assertEqual(MODULE.validate(self.packet, self.rows), 2)
        self.assertEqual(self.rows, original)

    def test_rejects_missing_duplicate_and_unknown_cases(self):
        for rows in [self.rows[:1], self.rows + self.rows[:1], [dict(self.rows[0], id='unknown'), self.rows[1]]]:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                MODULE.validate(self.packet, rows)

    def test_rejects_unfilled_or_invented_evidence(self):
        for update in [{'verdict': None}, {'reason': ' '}, {'evidenceQuote': ''}, {'evidenceQuote': '$18,000'}]:
            with self.subTest(update=update), self.assertRaises(ValueError):
                MODULE.validate(self.packet, [self.rows[0], dict(self.rows[1], **update)])
