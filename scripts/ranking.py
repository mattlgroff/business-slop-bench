"""Rank graded uncapped models with list prices and observed generation cost.
Usage: python3 scripts/ranking.py <reviewDir> <runDirWithCatalog> > <reviewDir>/RANKING.md
Prices are the Gateway catalog base input/output rates per million tokens; cost is the sum of
reported charges for the eight successful drafts in each condition. One generation per cell.
"""
import json, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
review, run = sys.argv[1], sys.argv[2]
grades = json.loads((root / review / 'grades.json').read_text())
summary = json.loads((root / review / 'summary.json').read_text())
catalog = {m['id']: m for m in json.loads((root / run / 'catalog.json').read_text())['models']}
ids = {}
for r in grades['rows']:
    stem = Path(r['path']).name
    ids.setdefault(r['model'], stem.split('--' + r['task'])[0].replace('--', '/'))
by = {}
for s in summary:
    if s['completed'] != 8:
        continue
    by.setdefault(s['model'], {})[s['condition']] = s
rows = []
for model, conds in by.items():
    if len(conds) != 2:
        continue
    mid = ids[model]
    cat = catalog.get(mid) or {}
    price = cat.get('pricing', {})
    eligible = all(c.get('benchEligible', True) for c in conds.values())
    d, h = conds['default'], conds['house']
    rows.append({
        'model': model + ('' if eligible else ' (non-ZDR, disqualified)'), 'id': mid, 'eligible': eligible,
        'zdr': cat.get('zdr'),
        'inPerM': float(price['input']) * 1e6 if price else None, 'outPerM': float(price['output']) * 1e6 if price else None,
        'd': d, 'h': h,
        'key': (eligible, h['pass'], d['pass'], h['readyWithoutEdits'] + d['readyWithoutEdits'], h['contentReady'] + d['contentReady']),
    })
rows.sort(key=lambda r: r['key'], reverse=True)
out = ['# Uncapped ranking with prices', '', f'Source: {review}/summary.json and {run}/catalog.json. Content checks are out of 54 per condition; unresolved checks earn no credit. '
       'Prices are Gateway list rates per million tokens (base tier; regional and fast tiers cost more). Observed cost is the reported charge for the eight successful drafts in that condition. '
       'One generation per cell, graded unblinded by the assistant. Disqualified models are listed last and never pooled. A $0 observed cost means the Gateway reported a zero charge at launch; the list price still applies once promotional pricing ends.', '',
       '| Rank | Model | Input $/M | Output $/M | Default checks | Default ready / no-edit | Default cost | House checks | House ready / no-edit | House cost |', '|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|']
rank = 0
for r in rows:
    if r['eligible']:
        rank += 1
        label = str(rank)
    else:
        label = '-'
    d, h = r['d'], r['h']
    cost = lambda c: '$0 (launch promo)' if c['generationCostUsd'] == 0 else f"${c['generationCostUsd']:.4f}"
    out.append(f"| {label} | {r['model']} | {r['inPerM']:.2f} | {r['outPerM']:.2f} | {d['pass']}/54 | {d['contentReady']}/8 / {d['readyWithoutEdits']}/8 | {cost(d)} | {h['pass']}/54 | {h['contentReady']}/8 / {h['readyWithoutEdits']}/8 | {cost(h)} |")
out += ['', 'Ordering: eligible models first, then house content checks, default content checks, ready-without-edits count, content-ready count. Ties remain ties; a few checks of difference is within single-generation variation.', '']
print('\n'.join(out))
