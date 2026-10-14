# Corrected legacy comparison: explicit authority required for future tests

October 13, 2026. Provisional, unblinded assistant grades. 33 models, 528 primary drafts; 56 repeat drafts remain separate.

## What was wrong

The v2 source says Priya owns procurement and CFO approval is needed before signing. It never names the signatory. Some drafts lost credit for proceeding to signing, while similar Astra and Sol wording passed. This was an inconsistent grading boundary, not evidence that one model understood authority better.

## Historical correction

For the legacy v2 vendor brief only, do not score the identity of the contract signatory or an implied assignment of that role: the source did not specify it and adjudication was inconsistent. Continue scoring other unsupported facts, deadlines, approvals and commitments. C05 still requires Priya procurement ownership and CFO approval before signing. This exception does not validate a guessed signatory and does not apply to v3.

The six existing vendor checks remain, including grounding against all other source facts. Seventeen grounding verdicts change to pass because the sole recorded finding was retired. This means no remaining scored grounding defect, not confirmation of signing authority. Two mixed findings retain their original verdict after removing the signatory allegation. The correction applies to all 66 primary vendor memos. Astra and Luna full repeats and the Sol/Astra comparison have no signatory deductions, so their numerical results do not change.

The raw outputs, frozen v2 inputs and earlier reviews remain untouched. This is a revised scoring edition of the same drafts, not a new generation or a pass on the new authority task. No other content judgment, style finding or cost changed.

| Model | Condition | Grounding before | Grounding now | Checks now | Content ready | Ready without edits |
|---|---|---|---|---:|---:|---:|
| Gemini Flash | house | review | pass | 51/54 | 5/8 | 3/8 |
| Qwen Flash | house | review | pass | 42/54 | 1/8 | 1/8 |
| GLM Flash | default | review | review | 49/54 | 4/8 | 1/8 |
| Kimi K3 | house | review | pass | 51/54 | 4/8 | 3/8 |
| MiniMax | house | review | pass | 45/54 | 1/8 | 0/8 |
| GLM 5.3 | house | fail | fail | 49/54 | 3/8 | 2/8 |
| Opus 5 | default | review | pass | 50/54 | 2/8 | 0/8 |
| Fable 5.1 | house | review | pass | 51/54 | 3/8 | 3/8 |
| Fable 5 | default | review | pass | 50/54 | 4/8 | 0/8 |
| Fable 5 | house | review | pass | 52/54 | 5/8 | 5/8 |
| Opus 5.5 | default | review | pass | 53/54 | 4/8 | 2/8 |
| Opus 5.5 | house | review | pass | 52/54 | 3/8 | 3/8 |
| Terra | default | review | pass | 53/54 | 7/8 | 3/8 |
| Gemini Pro | default | review | pass | 50/54 | 4/8 | 1/8 |
| Sonnet 5 | house | review | pass | 49/54 | 3/8 | 1/8 |
| Sonnet 5.5 | default | review | pass | 51/54 | 3/8 | 2/8 |
| Mistral Large 4 | house | fail | pass | 49/54 | 3/8 | 2/8 |
| Gemini 4 Argon | house | fail | pass | 51/54 | 5/8 | 4/8 |
| Muse Wonder 1.0 | house | review | pass | 54/54 | 8/8 | 7/8 |

## Replacement for future runs

`data/tasks-v3.json` replaces only the vendor ownership fact and C05. Priya coordinates procurement and cannot sign; Alex, the commercial director, is the sole signatory; CFO approval precedes Alex signing and does not delegate authority. C05 requires all three roles and the order explicitly. Wrong or omitted roles fail. Saying only "proceed with signing" cannot substitute for identifying Alex. The eight-brief total remains 54 checks.

The collector targets unused pilot-v33, protocol 0.33.0, with v3 tasks. No model has run v3 yet. Never compare a new v3 panel directly with these v2 scores or import a v2 vendor answer as a v3 success. The unrelated proposed readout revision remains inactive. The authored [boundary examples](../../data/vendor-authority-controls-v3.json) illustrate pass/fail decisions; they are not independent human calibration.

## Evidence and reproduction

- [Exact before/after decisions and retained quotes](corrections.json)
- [Cumulative grades](grades.json), [summary](summary.json), [ranking and prices](RANKING.md)
- [Muse Wonder versus Astra and other new models](MUSE-COMPARISON.md)
- [Argon original review](../assistant-v50/REPORT.md), [Nemotron and Muse original review](../assistant-v51/REPORT.md)

Run `python3 reviews/assistant-v52/build.py` and `python3 scripts/ranking.py reviews/assistant-v52 runs/pilot-v32`. These read saved files and make no API calls.
