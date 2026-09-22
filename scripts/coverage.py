"""Read-only coverage accounting for the current task set, without quality inference."""
import argparse
import hashlib
import json
from pathlib import Path


def classify_records(records):
    """An HTTP success can still be an empty or token-capped generation."""
    good = [r for r in records if r['status'] == 'ok'
            and r.get('text', '').strip() and r.get('finishReason') != 'length']
    if good:
        assert len({hashlib.sha256(r['text'].encode()).hexdigest() for r in good}) == 1, 'Multiple samples require an explicit selection policy'
        return 'generated', None
    if any(r['status'] == 'ok' for r in records):
        return 'incomplete', None
    if records:
        return 'failed', str(records[-1].get('error', {}).get('statusCode', 'unknown'))
    return 'unattempted', None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cohort', choices=['legacy-capped', 'uncapped'], default='legacy-capped')
    cohort = parser.parse_args().cohort
    root = Path(__file__).resolve().parents[1]
    models = json.loads((root / 'data/models.json').read_text())
    tasks = json.loads((root / 'data/tasks-v2.json').read_text())
    task_hash = hashlib.sha256(json.dumps(tasks, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
    runs = []
    for name in ['pilot-v10', 'pilot-v11', 'pilot-v12', 'pilot-v13', 'pilot-v14', 'pilot-v15', 'pilot-v16', 'pilot-v17', 'pilot-v18', 'pilot-v19', 'pilot-v20', 'pilot-v21', 'pilot-v22', 'pilot-v23']:
        path = root / 'runs' / name
        if (path / 'protocol.json').exists():
            protocol = json.loads((path / 'protocol.json').read_text())
            assert protocol['tasksHash'] == task_hash, 'Different task versions must not be combined'
            run_cohort = 'uncapped' if protocol['limits'].get('maxOutputTokens') is None else 'legacy-capped'
            if run_cohort == cohort:
                runs.append(path)
    rows = []
    for model in models:
        counts = dict(generated=0, incomplete=0, failed=0, unattempted=0)
        errors = []
        for task in tasks:
            for condition in ['default', 'house']:
                stem = f'{model["id"].replace("/", "--")}--{task["id"]}--{condition}'
                records = [json.loads((run / (stem + '.json')).read_text())
                           for run in runs if (run / (stem + '.json')).exists()]
                outcome, error = classify_records(records)
                counts[outcome] += 1
                if error is not None:
                    errors.append(error)
        rows.append({'model': model['id'], **counts, 'errorCodes': sorted(set(errors))})
    print(json.dumps({'cohort': cohort, 'taskFile': 'data/tasks-v2.json', 'expectedModels': len(models),
                      'expectedDrafts': len(models) * len(tasks) * 2, 'models': rows}, indent=2))


if __name__ == '__main__':
    main()
