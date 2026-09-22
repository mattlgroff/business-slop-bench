"""Archive one failed transient attempt while preserving its full budget charge.
Run only after inspecting the failure. Then rerun the same bench command.
"""
from pathlib import Path
import json, sys, datetime
root = Path(__file__).resolve().parents[1]
runs = root / 'runs'
path = Path(sys.argv[1]).resolve()
assert path.parent.parent == runs and path.parent.name.startswith('pilot-'), 'Expected a run result JSON'
lock = runs / '.lock'
with lock.open('x'):
    try:
        failure = json.loads(path.read_text())
        error = failure.get('error', {})
        gateway_timeout = error.get('statusCode') == 500 and error.get('name') == 'GatewayResponseError' and 'operation was aborted due to timeout' in error.get('message', '')
        assert failure.get('status') == 'error' and (error.get('statusCode') in (429, 502, 503, 504) or gateway_timeout), 'Only inspected transient errors are eligible'
        name = path.stem
        attempts = list(path.parent.glob(name + '--failed-attempt-*.json'))
        assert len(attempts) < 2, 'Two manual retries already used; diagnose before more spending'
        archived = name + '--failed-attempt-' + str(len(attempts) + 1)
        ledger_path = runs / 'budget.json'
        ledger = json.loads(ledger_path.read_text())
        entry = next(x for x in ledger['entries'] if x['id'] == path.parent.name + '::' + name)
        assert entry['status'] in ('reserved', 'unknown') and entry['charged'] == entry['reserve']
        entry['originalId'] = entry['id']
        entry['id'] = path.parent.name + '::' + archived
        entry['status'] = 'unknown'
        temp = ledger_path.with_suffix('.tmp')
        temp.write_text(json.dumps(ledger, indent=2) + '\n')
        temp.replace(ledger_path)
        path.rename(path.with_name(archived + '.json'))
        with (runs / 'manual-retries.jsonl').open('a') as log:
            log.write(json.dumps({'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'failedRecord': str(path.relative_to(root)), 'archivedRecord': archived, 'priorReservationRetained': entry['charged']}) + '\n')
        print('Archived failed attempt; its full reservation remains charged. Rerun the original command.')
    finally:
        lock.unlink()
