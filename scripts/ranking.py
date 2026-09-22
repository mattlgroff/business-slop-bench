"""Rank graded uncapped models with list prices and observed generation cost, one table per condition.
Usage: python3 scripts/ranking.py <reviewDir> <runDirWithCatalog> [--json out.json] [--ignore-zdr] > <reviewDir>/RANKING.md
--ignore-zdr ranks non-ZDR models alongside the rest (a what-if view; the bench rule still disqualifies them).
Prices are the Gateway catalog base input/output rates per million tokens; cost is the sum of
reported charges for the eight successful drafts in each condition. One generation per cell.
"""
import json, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
args = [a for a in sys.argv[1:] if not a.startswith('--')]
review, run = args[0], args[1]
json_out = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else None
ignore_zdr = '--ignore-zdr' in sys.argv
grades = json.loads((root / review / 'grades.json').read_text())
summary = json.loads((root / review / 'summary.json').read_text())
catalog = {m['id']: m for m in json.loads((root / run / 'catalog.json').read_text())['models']}
DISPLAY = {'openai/gpt-6-astra': 'GPT-6 Astra', 'openai/gpt-6-sol': 'GPT-6 Sol', 'openai/gpt-6-luna': 'GPT-6 Luna',
           'openai/gpt-5.6-sol': 'GPT-5.6 Sol', 'openai/gpt-5.6-terra': 'GPT-5.6 Terra', 'openai/gpt-5.6-luna': 'GPT-5.6 Luna',
           'anthropic/claude-opus-5.5': 'Claude Opus 5.5', 'anthropic/claude-opus-5': 'Claude Opus 5', 'anthropic/claude-opus-4.6': 'Claude Opus 4.6',
           'anthropic/claude-sonnet-5': 'Claude Sonnet 5', 'anthropic/claude-fable-5': 'Claude Fable 5', 'anthropic/claude-fable-5.1': 'Claude Fable 5.1',
           'google/gemini-3.8-flash': 'Gemini 3.8 Flash', 'google/gemini-3.1-pro-preview': 'Gemini 3.1 Pro', 'meta/muse-spark-1.3': 'Muse Spark 1.3',
           'deepseek/deepseek-v4-pro-0813': 'DeepSeek V4 Pro', 'deepseek/deepseek-v4.1-flash': 'DeepSeek V4.1 Flash', 'zai/glm-5.3': 'GLM 5.3', 'zai/glm-5.3-flash': 'GLM 5.3 Flash',
           'alibaba/qwen3.8-max-0902': 'Qwen 3.8 Max', 'alibaba/qwen3.8-flash': 'Qwen 3.8 Flash', 'moonshotai/kimi-k3': 'Kimi K3', 'minimax/minimax-m3': 'MiniMax M3',
           'xiaomi/mimo-v2.6-pro': 'MiMo V2.6 Pro', 'spacexai/grok-4.7': 'Grok 4.7'}
ids = {}
for r in grades['rows']:
    stem = Path(r['path']).name
    ids.setdefault(r['model'], stem.split('--' + r['task'])[0].replace('--', '/'))
by = {}
for s in summary:
    if s['completed'] == 8:
        by.setdefault(s['model'], {})[s['condition']] = s
models = []
for model, conds in by.items():
    if len(conds) != 2:
        continue
    mid = ids[model]
    price = (catalog.get(mid) or {}).get('pricing', {})
    eligible = all(c.get('benchEligible', True) for c in conds.values())
    models.append({'model': DISPLAY.get(mid, model), 'reviewLabel': model, 'id': mid, 'eligible': eligible, 'zdr': (catalog.get(mid) or {}).get('zdr'),
                   'inPerM': float(price['input']) * 1e6 if price else None, 'outPerM': float(price['output']) * 1e6 if price else None,
                   'plain': conds['default'], 'house': conds['house']})
LABEL = {'plain': 'Plain brief, no house rules', 'house': 'Same brief plus the house anti-slop rules'}
QUESTION = {'plain': 'Which models write the least slop unprompted?', 'house': 'Which models perform best once told exactly what slop means?'}
def table(cond):
    key = lambda m: (m['eligible'] or ignore_zdr, m[cond]['pass'], m[cond]['readyWithoutEdits'], m[cond]['contentReady'], -m[cond]['fail'])
    rows = sorted(models, key=key, reverse=True)
    out = [f'## {LABEL[cond]}', '', QUESTION[cond], '',
           '| Rank | Model | Checks passed (of 54) | Failed | Unresolved | Content ready (of 8) | Ready without edits (of 8) | Input $/M | Output $/M | Observed cost, 8 drafts |',
           '|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    rank = 0
    for m in rows:
        c = m[cond]
        label = '-'
        if m['eligible'] or ignore_zdr:
            rank += 1; label = str(rank)
        name = m['model'] + ('' if m['eligible'] else (' (non-ZDR)' if ignore_zdr else ' (non-ZDR, disqualified)'))
        cost = '$0 (reported)' if c['generationCostUsd'] == 0 else f"${c['generationCostUsd']:.4f}"
        out.append(f"| {label} | {name} | {c['pass']} | {c['fail']} | {c['review']} | {c['contentReady']} | {c['readyWithoutEdits']} | {m['inPerM']:.2f} | {m['outPerM']:.2f} | {cost} |")
    return out + ['']
out = ['# Uncapped ranking with prices' + (' (ZDR rule ignored)' if ignore_zdr else ''), '',
       *(['This is a what-if view: models with no zero-data-retention route are ranked alongside the rest. The bench rule still disqualifies them; the committed ranking is RANKING.md.', ''] if ignore_zdr else []),
       f'Source: {review}/summary.json and {run}/catalog.json. Eight business briefs, one generation per brief and condition, graded by the assistant unblinded. {('This what-if table includes models disqualified by the recorded ZDR policy; it does not change their bench eligibility.' if ignore_zdr else 'Models disqualified by the recorded ZDR policy are shown for information without a rank.')}', '',
       '## What the columns mean', '',
       '- **Plain brief**: the model gets the task and the source facts only. This measures how much slop it writes unprompted.',
       '- **With house rules**: the same brief plus Matthew Groff\'s Zero Defect anti-slop rules. This measures how well it performs once told exactly what slop means.',
       '- **Checks passed**: each brief has six or seven total content checks, including a grounding check that every material claim traces to the source. 54 per condition. Unresolved means the reviewer could not settle it from the source; it earns no credit.',
       '- **Content ready**: the draft passes every check, stays within the word limit and has no authoring residue such as a `[Date]` placeholder or a reference to the source pack. Editorial findings may still require revision.',
       '- **Ready without edits**: content ready, plus zero em dashes, no negative-parallelism rhetoric, and no supported slop finding (throat clearing, puffery, empty closers, repeated summaries). No edit was identified by this provisional review; this is not independent validation.',
       '- **Prices**: Gateway list rates per million tokens, base tier; regional and fast tiers cost more. Observed cost is the reported charge for the eight drafts in that condition; $0 means the stored response reported zero charge; the reason is not inferred from that number.', '',
       ('Ordering within each table: ' + ('' if ignore_zdr else 'eligible models first, then ') + 'checks passed, ready without edits, content ready, fewer failures. A difference of one or two checks is within what a second generation could change.'), '']
out += table('plain') + table('house')
print('\n'.join(out))
if json_out:
    Path(json_out).write_text(json.dumps({'review': review, 'run': run, 'models': models}, indent=1) + '\n')
