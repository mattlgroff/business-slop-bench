# Claude Haiku 5.5

October 7, 2026. Exact model: `anthropic/claude-haiku-5.5`. Low reasoning, eight frozen briefs in both conditions, no output-token cap. All sixteen calls completed normally, with no warnings, retries or provider fallback attempts. Every writer input matches Sol 6.1 exactly.

| Condition | Checks | Content ready | Ready without edits | Reported cost |
|---|---:|---:|---:|---:|
| Plain | 50/54 | 4/8 | 2/8 | $0.0027352 |
| House | 49/54 | 2/8 | 2/8 | $0.0078934 |

Total: $0.0106286. Zero em dashes and no word-limit violations across all sixteen drafts. Ranked 13th of 24 eligible models on plain briefs and 18th with house rules under the existing ordering.

The plain vendor memo and change order were ready without edits. Under house rules, the change order and handoff deck were ready without edits. The house condition removed some stylistic problems but introduced or retained unsupported substance: a same-day security-request commitment, prior team performance, a payment trigger changed from delivery to acceptance, and a definite next-quarter production prohibition where approval was only pending. A source-pack reference and unfilled deadline also blocked readiness.

Both pilot readouts give the correct 15-minute and 12-minute endpoints but omit the explicitly graded reduction of 3 minutes or 20%. This is an analytical-completeness failure under the unchanged rubric, not incorrect arithmetic. The existing rubric audit identifies that the brief does not explicitly request that calculation; that limitation remains visible and no historical grade was changed.

| Model | Plain checks | House checks | House ready without edits |
|---|---:|---:|---:|
| Haiku 5.5 | 50/54 | 49/54 | 2/8 |
| Sonnet 5.5 | 50/54 | 51/54 | 2/8 |
| Sol 6.1 | 53/54 | 54/54 | 4/8 |
| Astra primary | 54/54 | 54/54 | 8/8 |
| Mistral Large 4 | 46/54 | 48/54 | 1/8 |

Astra's two full house repeats each returned 6/8 ready without edits. Mistral used provider-default reasoning because Gateway ignored its setting, so it is not a controlled low-reasoning comparison. Other rows retain their primary attempts. These are provisional unblinded assistant judgments on one small panel, not independent human validation or a reliability estimate.

[Full findings](REPORT.md), [decisions](decisions.json), [paired-input verification](input-verification.json), [ranking](RANKING.md).
