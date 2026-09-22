# Uncapped comparison: Fable 5 added (non-ZDR, disqualified)

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.

## Uncapped results

| Model | Condition | Completed briefs | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Muse | default | 8/8 | 53/54 | 1 | 0 | 7/8 | 4/8 | $0.03816 |
| Muse | house | 8/8 | 53/54 | 1 | 0 | 7/8 | 5/8 | $0.05720 |
| Gemini Flash | default | 8/8 | 51/54 | 2 | 1 | 5/8 | 0/8 | $0.01866 |
| Gemini Flash | house | 8/8 | 50/54 | 3 | 1 | 4/8 | 3/8 | $0.02418 |
| Luna | default | 8/8 | 51/54 | 2 | 1 | 5/8 | 2/8 | $0.00313 |
| Luna | house | 8/8 | 52/54 | 1 | 1 | 6/8 | 4/8 | $0.00809 |
| Qwen Flash | default | 8/8 | 46/54 | 8 | 0 | 0/8 | 0/8 | $0.00376 |
| Qwen Flash | house | 8/8 | 41/54 | 11 | 2 | 0/8 | 0/8 | $0.00774 |
| Qwen Max | default | 8/8 | 49/54 | 5 | 0 | 3/8 | 1/8 | $0.02687 |
| Qwen Max | house | 8/8 | 52/54 | 2 | 0 | 4/8 | 3/8 | $0.08665 |
| GLM Flash | default | 8/8 | 49/54 | 3 | 2 | 4/8 | 1/8 | $0.00187 |
| GLM Flash | house | 8/8 | 48/54 | 6 | 0 | 3/8 | 2/8 | $0.00459 |
| GLM 5.3 | default | 8/8 | 52/54 | 2 | 0 | 4/8 | 1/8 | $0.01492 |
| GLM 5.3 | house | 8/8 | 49/54 | 5 | 0 | 3/8 | 2/8 | $0.04255 |
| DeepSeek Flash | default | 8/8 | 52/54 | 2 | 0 | 5/8 | 0/8 | $0.00286 |
| DeepSeek Flash | house | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.00837 |
| DeepSeek Pro | default | 8/8 | 51/54 | 1 | 2 | 3/8 | 1/8 | $0.00903 |
| DeepSeek Pro | house | 8/8 | 51/54 | 2 | 1 | 4/8 | 2/8 | $0.03741 |
| Kimi K3 | default | 8/8 | 51/54 | 3 | 0 | 4/8 | 0/8 | $0.05660 |
| Kimi K3 | house | 8/8 | 50/54 | 3 | 1 | 3/8 | 2/8 | $0.11798 |
| MiniMax | default | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.03275 |
| MiniMax | house | 8/8 | 44/54 | 9 | 1 | 0/8 | 0/8 | $0.03217 |
| Grok | default | 8/8 | 52/54 | 2 | 0 | 6/8 | 3/8 | $0.01822 |
| Grok | house | 8/8 | 50/54 | 3 | 1 | 4/8 | 2/8 | $0.05401 |
| Astra | default | 8/8 | 54/54 | 0 | 0 | 8/8 | 4/8 | $0.11204 |
| Astra | house | 8/8 | 54/54 | 0 | 0 | 8/8 | 8/8 | $0.35814 |
| Opus 5 | default | 8/8 | 49/54 | 4 | 1 | 1/8 | 0/8 | $0.14808 |
| Opus 5 | house | 8/8 | 49/54 | 4 | 1 | 3/8 | 3/8 | $0.28796 |
| Opus 4.6 | default | 8/8 | 49/54 | 5 | 0 | 2/8 | 0/8 | $0.07598 |
| Opus 4.6 | house | 8/8 | 49/54 | 5 | 0 | 1/8 | 1/8 | $0.18033 |
| Fable 5.1 (non-ZDR, disqualified) | default | 8/8 | 51/54 | 3 | 0 | 4/8 | 0/8 | $0.23797 |
| Fable 5.1 (non-ZDR, disqualified) | house | 8/8 | 50/54 | 3 | 1 | 3/8 | 3/8 | $0.57024 |
| Fable 5 (non-ZDR, disqualified) | default | 8/8 | 50/54 | 3 | 1 | 4/8 | 0/8 | $0.23451 |
| Fable 5 (non-ZDR, disqualified) | house | 8/8 | 51/54 | 2 | 1 | 4/8 | 4/8 | $0.54133 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax, Grok and Astra are new uncapped generations on each attempted cell; the Grok house handoff deck comes from pilot-v21 after its pilot-v20 request timed out; Opus 5 is a pilot-v21 collection with one pilot-v20 import; Opus 4.6 is a full pilot-v21 collection; Fable 5.1 and Fable 5 are pilot-v21 collections with one pilot-v20 import each on a declared non-ZDR route; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

## New review evidence

### Fable 5 / pilot-client-email / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--pilot-client-email--default.md): 6/7 content checks, 189/180 words, 3 em dashes.

- **grounding fail:** [Could we get your decision this week?](../../runs/pilot-v21/anthropic--claude-fable-5--pilot-client-email--default.md:18). Invents a reply deadline; the source authorizes none.
- **Style 5:** [so your controls stay fully intact](../../runs/pilot-v21/anthropic--claude-fable-5--pilot-client-email--default.md:12). Promotional assurance without evidence; the source states only that approval precedes access.

### Fable 5 / pilot-client-email / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--pilot-client-email--house.md): 7/7 content checks, 187/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5 / launch-delay-email / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--launch-delay-email--default.md): 5/6 content checks, 174/180 words, 3 em dashes.

- **grounding fail:** [The team is fully prepared and confident in what we've built](../../runs/pilot-v21/anthropic--claude-fable-5--launch-delay-email--default.md:9). Invents a team readiness claim the source does not record.
- **Style 2:** [I want to update you on where we stand with the launch.](../../runs/pilot-v21/anthropic--claude-fable-5--launch-delay-email--default.md:5). Announces the update instead of stating the launch position.
- **Style 28:** [we're committed to landing this well](../../runs/pilot-v21/anthropic--claude-fable-5--launch-delay-email--default.md:13). Empty positive ending that adds no decision, owner or condition.

### Fable 5 / launch-delay-email / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--launch-delay-email--house.md): 5/6 content checks, 116/180 words, 0 em dashes.

- **grounding fail:** [The team is ready either way](../../runs/pilot-v21/anthropic--claude-fable-5--launch-delay-email--house.md:11). Invents a team readiness claim the source does not record.

### Fable 5 / vendor-decision-memo / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--vendor-decision-memo--default.md): 5/6 content checks, 239/300 words, 2 em dashes.

- **grounding review:** [procurement (Priya) will proceed with contract signature](../../runs/pilot-v21/anthropic--claude-fable-5--vendor-decision-memo--default.md:39). Implies Priya signs; the source says CFO approval precedes signing but does not say who signs.

### Fable 5 / vendor-decision-memo / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--vendor-decision-memo--house.md): 5/6 content checks, 213/300 words, 0 em dashes.

- **grounding review:** [routes the agreement for CFO signature](../../runs/pilot-v21/anthropic--claude-fable-5--vendor-decision-memo--house.md:34). Implies the CFO signs; the source says CFO approval precedes signing but does not say who signs.

### Fable 5 / pilot-results-memo / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--pilot-results-memo--default.md): 7/7 content checks, 296/300 words, 3 em dashes.

- **Negative parallelism:** [The decision before the COO is **not** whether to scale](../../runs/pilot-v21/anthropic--claude-fable-5--pilot-results-memo--default.md:29). Negated framing followed by the affirmative decision; the affirmative sentence alone carries the point.

### Fable 5 / pilot-results-memo / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--pilot-results-memo--house.md): 7/7 content checks, 245/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5 / discovery-proposal / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--discovery-proposal--default.md): 7/7 content checks, 244/350 words, 2 em dashes.

- **Style 28:** [We look forward to your approval and to beginning discovery promptly](../../runs/pilot-v21/anthropic--claude-fable-5--discovery-proposal--default.md:52). Empty positive ending that adds no decision, owner or condition beyond the steps already listed.

### Fable 5 / discovery-proposal / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--discovery-proposal--house.md): 7/7 content checks, 102/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5 / change-order / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--change-order--default.md): 7/7 content checks, 248/300 words, 2 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5 / change-order / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--change-order--house.md): 7/7 content checks, 161/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5 / ai-strategy-slides / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--ai-strategy-slides--default.md): 6/7 content checks, 193/350 words, 7 em dashes.

- **grounding fail:** [Ready to launch immediately](../../runs/pilot-v21/anthropic--claude-fable-5--ai-strategy-slides--default.md:11). Approved policy documents do not establish immediate launch readiness; the deck also asserts no data or authorization barriers.

### Fable 5 / ai-strategy-slides / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--ai-strategy-slides--house.md): 6/7 content checks, 189/350 words, 0 em dashes.

- **grounding fail:** [It is fully authorized today](../../runs/pilot-v21/anthropic--claude-fable-5--ai-strategy-slides--house.md:11). Labels the knowledge-search pilot authorized before the COO selects it; the source records only approved policy documents.

### Fable 5 / handoff-slides / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--handoff-slides--default.md): 7/7 content checks, 200/350 words, 1 em dashes.

- **Style 14:** [✅ Approved](../../runs/pilot-v21/anthropic--claude-fable-5--handoff-slides--default.md:4). Decorative check and cross marks add no information to the status words.

### Fable 5 / handoff-slides / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5--handoff-slides--house.md): 7/7 content checks, 143/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

## Adjudication boundaries

Fable 5 passes 50/54 default and 51/54 house content checks. Default failures are a this-week reply deadline in the pilot email, team readiness in the launch update and immediate launch readiness in the strategy deck; house failures are team readiness in the launch update and an authorized label in the strategy deck. Both vendor memos are unresolved only on who signs. Both readouts state the reduction explicitly. Four drafts are content ready in each condition, and the house condition makes all four ready without edits while removing every em dash (23 default, 0 house) and every editorial finding (5 default, 0 house). Only the pilot emails exceed their word limit.

Fable 5 has no ZDR route on the Gateway. It was collected under the protocol non-ZDR exception because the user asked for it, and under the ZDR rule it fails the bench regardless of these scores. Its rows carry benchEligible false and are reported separately, never pooled with eligible models. These are 16 single generations, graded unblinded by the same reviewer, collected one call every seven minutes; the default pilot email is the pilot-v20 import.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
