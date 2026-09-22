# Assistant comparison: Fable 5.1 added

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same corrected briefs and conditions; Fable coverage remains partial. Model identities visible; no Jev calls.

## Completed eight-draft conditions

| Model | Condition | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|
| Astra | default | 54/54 | 0 | 0 | 8/8 | 4/8 | $0.10989 |
| Astra | house | 54/54 | 0 | 0 | 8/8 | 7/8 | $0.36169 |
| Sol | default | 52/54 | 1 | 1 | 6/8 | 2/8 | $0.06108 |
| Sol | house | 53/54 | 1 | 0 | 7/8 | 6/8 | $0.18847 |
| Terra | default | 52/54 | 1 | 1 | 6/8 | 1/8 | $0.02792 |
| Terra | house | 52/54 | 1 | 1 | 6/8 | 5/8 | $0.07715 |
| Qwen Max | default | 47/54 | 6 | 1 | 3/8 | 0/8 | $0.02365 |
| Qwen Max | house | 51/54 | 3 | 0 | 3/8 | 1/8 | $0.08720 |
| Gemini Flash | default | 51/54 | 2 | 1 | 5/8 | 1/8 | $0.02266 |
| Gemini Flash | house | 51/54 | 3 | 0 | 5/8 | 3/8 | $0.02413 |
| GLM Flash | default | 48/54 | 6 | 0 | 3/8 | 0/8 | $0.00129 |
| GLM Flash | house | 46/54 | 7 | 1 | 2/8 | 1/8 | $0.00448 |
| Luna | default | 52/54 | 1 | 1 | 5/8 | 2/8 | $0.00324 |
| Luna | house | 51/54 | 1 | 2 | 5/8 | 3/8 | $0.00817 |
| Kimi K3 | default | 51/54 | 2 | 1 | 5/8 | 4/8 | $0.06553 |
| Kimi K3 | house | 48/54 | 6 | 0 | 3/8 | 1/8 | $0.10848 |
| Qwen Flash | default | 47/54 | 7 | 0 | 1/8 | 0/8 | $0.00345 |
| Qwen Flash | house | 41/54 | 12 | 1 | 1/8 | 1/8 | $0.00821 |
| DeepSeek Flash | default | 50/54 | 4 | 0 | 4/8 | 0/8 | $0.00243 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

Fable coverage expands only with successful responses. Failed availability requests are ungraded, and earlier pilot emails retain their grades. This is a provisional single-sample comparison.

## New review evidence

### Fable 5.1 / launch-delay-email / house

[Draft](../../runs/pilot-v15/anthropic--claude-fable-5.1--launch-delay-email--house.md): 5/6 content checks, 174/180 words, 0 em dashes.

- **grounding fail:** [The build itself is ready; the remaining work is Nia's review.](../../runs/pilot-v15/anthropic--claude-fable-5.1--launch-delay-email--house.md:7). Invents build readiness and characterizes the review as the only remaining work. The source allows remediation. The end-of-week response deadline is also unsupported.

## Adjudication boundaries

- Build readiness is a factual status claim, unlike personal confidence or ambiguous team-focus reassurance.
- A reply deadline or offer-expiration term requires source support; an open request for the next decision is allowed.

[All decisions](grades.json) and [summary](summary.json) retain previous grades and exact output hashes. Incomplete conditions remain separate from the completed-condition table. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
