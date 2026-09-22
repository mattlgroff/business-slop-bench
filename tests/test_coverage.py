import importlib.util
import unittest
import json
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location('coverage_report', Path(__file__).resolve().parents[1] / 'scripts/coverage.py')
coverage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coverage)


class CoverageTest(unittest.TestCase):
    def test_discovers_future_runs_without_mixing_briefs_caps_or_archives(self):
        with tempfile.TemporaryDirectory(prefix='businessslop-coverage-') as directory:
            root = Path(directory)
            for name, task_hash, cap in [
                ('pilot-v9', 'current', None),
                ('pilot-v24', 'current', None),
                ('pilot-v100', 'current', None),
                ('pilot-v25', 'other-briefs', None),
                ('pilot-v26', 'current', 4096),
                ('pilot-v24-backup', 'current', None),
            ]:
                path = root / name
                path.mkdir()
                (path / 'protocol.json').write_text(json.dumps({
                    'tasksHash': task_hash, 'limits': {'maxOutputTokens': cap}}))
            (root / 'pilot-v101').mkdir()  # A run not yet frozen is not eligible.
            self.assertEqual([p.name for p in coverage.matching_runs(root, 'current', 'uncapped')],
                             ['pilot-v9', 'pilot-v24', 'pilot-v100'])
            self.assertEqual([p.name for p in coverage.matching_runs(root, 'current', 'legacy-capped')],
                             ['pilot-v26'])

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
