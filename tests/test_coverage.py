import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('coverage_report', Path(__file__).resolve().parents[1] / 'scripts/coverage.py')
coverage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coverage)


class CoverageTest(unittest.TestCase):
    def test_transport_success_does_not_make_an_incomplete_draft_generated(self):
        complete = {'status': 'ok', 'text': 'Finished memo.', 'finishReason': 'stop'}
        empty = {'status': 'ok', 'text': '', 'finishReason': 'length'}
        clipped = {'status': 'ok', 'text': 'Partial memo', 'finishReason': 'length'}
        error = {'status': 'error', 'error': {'statusCode': 429}}
        for record in [empty, clipped, {**empty, 'finishReason': 'stop'}]:
            self.assertEqual(coverage.classify_records([record]), ('incomplete', None))
        self.assertEqual(coverage.classify_records([error]), ('failed', '429'))
        self.assertEqual(coverage.classify_records([]), ('unattempted', None))
        self.assertEqual(coverage.classify_records([error, empty, complete]), ('generated', None))
        self.assertEqual(coverage.classify_records([complete, dict(complete)]), ('generated', None))
        with self.assertRaises(AssertionError):
            coverage.classify_records([complete, {**complete, 'text': 'Different finished memo.'}])


if __name__ == '__main__':
    unittest.main()
