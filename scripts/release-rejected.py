"""Release reservations for requests the Gateway rejected before generation.
Eligible: status error, HTTP 429, no generation ID, under one second elapsed.
The reservation amount stays on the entry as evidence; only the charge drops to zero.
"""
from pathlib import Path
import json, sys, datetime
root = Path(__file__).resolve().parents[1]
runs = root / 'runs'
apply = '--apply' in sys.argv
lock = runs / '.lock'
with lock.open('x'):
    try:
        ledger_path = runs / 'budget.json'
        ledger = json.loads(ledger_path.read_text())
        released = []
        for entry in ledger['entries']:
            if entry['status'] not in ('reserved', 'unknown') or entry['charged'] == 0:
                continue
            run, _, name = entry['id'].partition('::')
            record = runs / run / (name + '.json')
            if not record.exists():
                continue
            failure = json.loads(record.read_text())
            error = failure.get('error', {})
            eligible = (failure.get('status') == 'error' and error.get('statusCode') == 429
                        and not error.get('generationId') and failure.get('elapsedMs', 10**9) < 1000)
            if not eligible:
                continue
            released.append({'id': entry['id'], 'reservation': entry['charged'], 'elapsedMs': failure['elapsedMs'], 'message': error.get('message', '')[:80]})
            if apply:
                entry['releasedCharge'] = entry['charged']
                entry['charged'] = 0
                entry['status'] = 'released'
        for r in released:
            print(json.dumps(r))
        print('total released', round(sum(r['reservation'] for r in released), 6), 'applied' if apply else 'dry run')
        if apply and released:
            temp = ledger_path.with_suffix('.tmp')
            temp.write_text(json.dumps(ledger, indent=2) + '\n')
            temp.replace(ledger_path)
            with (runs / 'manual-releases.jsonl').open('a') as log:
                log.write(json.dumps({'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'rule': 'sub-second 429 with no generation ID', 'released': released}) + '\n')
    finally:
        lock.unlink()
