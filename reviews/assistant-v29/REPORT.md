# Uncapped comparison: Opus 4.6 added

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

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax, Grok and Astra are new uncapped generations on each attempted cell; the Grok house handoff deck comes from pilot-v21 after its pilot-v20 request timed out; Opus 5 is a pilot-v21 collection with one pilot-v20 import; Opus 4.6 is a full pilot-v21 collection; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

## New review evidence

### Opus 4.6 / pilot-client-email / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--pilot-client-email--default.md): 7/7 content checks, 174/180 words, 2 em dashes.

- **Style 2:** [I'm writing to propose](../../runs/pilot-v21/anthropic--claude-opus-4.6--pilot-client-email--default.md:5). Announces the proposal instead of starting with the scope and fee.
- **Style 5:** [without disrupting operations](../../runs/pilot-v21/anthropic--claude-opus-4.6--pilot-client-email--default.md:16). Assures no operational disruption without a defined basis; the source records no delivery terms.

### Opus 4.6 / pilot-client-email / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--pilot-client-email--house.md): 7/7 content checks, 161/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 4.6 / launch-delay-email / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--launch-delay-email--default.md): 5/6 content checks, 178/180 words, 0 em dashes.

- **grounding fail:** [The team is executing well](../../runs/pilot-v21/anthropic--claude-opus-4.6--launch-delay-email--default.md:17). Invents a favorable delivery-performance claim the source does not record.
- **Style 2:** [I wanted to give you a clear picture of where we stand on the launch.](../../runs/pilot-v21/anthropic--claude-opus-4.6--launch-delay-email--default.md:5). Announces the update instead of stating the launch position.
- **Style 28:** [Thanks for your continued partnership.](../../runs/pilot-v21/anthropic--claude-opus-4.6--launch-delay-email--default.md:23). Empty positive ending that adds no decision, owner or condition.

### Opus 4.6 / launch-delay-email / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--launch-delay-email--house.md): 5/6 content checks, 164/180 words, 0 em dashes.

- **grounding fail:** [The team is executing well and the work is on track](../../runs/pilot-v21/anthropic--claude-opus-4.6--launch-delay-email--house.md:13). Invents favorable performance and on-track claims the source does not record.

### Opus 4.6 / vendor-decision-memo / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--vendor-decision-memo--default.md): 5/6 content checks, 231/300 words, 0 em dashes.

- **grounding fail:** [lost productivity and extended parallel costs](../../runs/pilot-v21/anthropic--claude-opus-4.6--vendor-decision-memo--default.md:32). Invents cost consequences and a contractual-guarantee framing the source does not contain; the source records only that Beta has no committed SSO delivery date.
- **Style 14:** [✅ Yes](../../runs/pilot-v21/anthropic--claude-opus-4.6--vendor-decision-memo--default.md:19). Decorative check and cross marks in the comparison table add no information to the Yes and No entries.
- **Authoring placeholder:** [[Current Date]](../../runs/pilot-v21/anthropic--claude-opus-4.6--vendor-decision-memo--default.md:5). Unfilled date placeholder in the memo header.

### Opus 4.6 / vendor-decision-memo / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--vendor-decision-memo--house.md): 6/6 content checks, 154/300 words, 0 em dashes.

- **Authoring placeholder:** [[Date]](../../runs/pilot-v21/anthropic--claude-opus-4.6--vendor-decision-memo--house.md:5). Unfilled date placeholder in the memo header.

### Opus 4.6 / pilot-results-memo / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--pilot-results-memo--default.md): 7/7 content checks, 213/300 words, 4 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 4.6 / pilot-results-memo / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--pilot-results-memo--house.md): 6/7 content checks, 175/300 words, 0 em dashes.

- **C01 fail:** [(15 min to 12 min)](../../runs/pilot-v21/anthropic--claude-opus-4.6--pilot-results-memo--house.md:5). Correct endpoints, but omits the explicit 3-minute or 20% reduction required by the frozen criterion.

### Opus 4.6 / discovery-proposal / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--discovery-proposal--default.md): 6/7 content checks, 196/350 words, 0 em dashes.

- **grounding fail:** [Kickoff payment of $8,000 is due at that time.](../../runs/pilot-v21/anthropic--claude-opus-4.6--discovery-proposal--default.md:40). Places the kickoff payment at start-date confirmation rather than at kickoff, reordering the source payment sequence.
- **Style 28:** [We look forward to working with you.](../../runs/pilot-v21/anthropic--claude-opus-4.6--discovery-proposal--default.md:42). Empty positive ending that adds no decision, owner or condition.

### Opus 4.6 / discovery-proposal / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--discovery-proposal--house.md): 6/7 content checks, 171/350 words, 0 em dashes.

- **grounding fail:** [We are ready to begin as soon as the agreement is signed.](../../runs/pilot-v21/anthropic--claude-opus-4.6--discovery-proposal--house.md:40). Invents a readiness claim and drops the named-contact condition the source sets before any start date.

### Opus 4.6 / change-order / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--change-order--default.md): 7/7 content checks, 217/300 words, 0 em dashes.

- **Authoring placeholder:** [*(to be filled)*](../../runs/pilot-v21/anthropic--claude-opus-4.6--change-order--default.md:5). Unfilled date placeholder in the change-order header.

### Opus 4.6 / change-order / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--change-order--house.md): 7/7 content checks, 180/300 words, 0 em dashes.

- **Authoring placeholder:** [[Date]](../../runs/pilot-v21/anthropic--claude-opus-4.6--change-order--house.md:4). Unfilled date placeholder in the change-order header.
- **Authoring placeholder:** [&nbsp;](../../runs/pilot-v21/anthropic--claude-opus-4.6--change-order--house.md:42). Raw HTML entity left in the document body; authoring residue.

### Opus 4.6 / ai-strategy-slides / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--ai-strategy-slides--default.md): 6/7 content checks, 216/350 words, 7 em dashes.

- **grounding fail:** [No legal blockers](../../runs/pilot-v21/anthropic--claude-opus-4.6--ai-strategy-slides--default.md:25). Approved policy documents do not establish the absence of legal blockers; the deck also invents low and high risk ratings and regulatory exposure the source does not record.
- **Style 23:** [Named owner (Dana) ensures accountability and timely reporting](../../runs/pilot-v21/anthropic--claude-opus-4.6--ai-strategy-slides--default.md:27). A named owner does not ensure timely reporting.

### Opus 4.6 / ai-strategy-slides / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--ai-strategy-slides--house.md): 6/7 content checks, 176/350 words, 0 em dashes.

- **grounding fail:** [no outstanding legal blockers](../../runs/pilot-v21/anthropic--claude-opus-4.6--ai-strategy-slides--house.md:10). Approved policy documents do not establish the absence of legal blockers; the deck also invents a quarter-start work date for Dana.

### Opus 4.6 / handoff-slides / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--handoff-slides--default.md): 6/7 content checks, 270/350 words, 4 em dashes.

- **grounding fail:** [Lee currently carries operational risk with no defined end date](../../runs/pilot-v21/anthropic--claude-opus-4.6--handoff-slides--default.md:21). Invents operational and service responsibility for Lee; the source gives Lee defect fixes only and leaves pre-acceptance incident ownership unstated.
- **Style 14:** [✅ Complete](../../runs/pilot-v21/anthropic--claude-opus-4.6--handoff-slides--default.md:9). Decorative check and cross marks in the status table add no information to the status words.
- **Negative parallelism:** [This is a **governance gap**, not a technical gap](../../runs/pilot-v21/anthropic--claude-opus-4.6--handoff-slides--default.md:29). Negated framing followed by the affirmative point; the affirmative clause alone carries it and the capability claim is unsupported.

### Opus 4.6 / handoff-slides / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-4.6--handoff-slides--house.md): 6/7 content checks, 177/350 words, 0 em dashes.

- **grounding fail:** [Lee retains ownership of all service issues](../../runs/pilot-v21/anthropic--claude-opus-4.6--handoff-slides--house.md:14). Extends Lee's ownership beyond defect fixes; the source gives Lee defect fixes only and leaves pre-acceptance incident ownership unstated.

## Adjudication boundaries

Opus 4.6 passes 49/54 content checks in both conditions with five failures and no unresolved checks in each. Four failures recur across both conditions on the same briefs: favorable performance claims in the launch updates, a kickoff payment moved ahead of kickoff and then a readiness claim in the discovery proposals, no legal blockers in both strategy decks, and operational responsibility invented for Lee in both handoff decks. The fifth default failure is invented cost consequences in the vendor memo; the fifth house failure is the readout giving endpoints without the explicit reduction. No draft exceeds its word limit.

Opus 4.6 is the only model in the cohort that leaves unfilled date placeholders in finished documents: both vendor memos and both change orders carry a header date placeholder, and the house change order also carries a raw HTML entity. Those four drafts pass every content check and are blocked from content ready only by the placeholders. The house condition removes every em dash (17 default, 0 house) and every editorial finding (8 default, 0 house), but content-ready counts stay at 2 of 8 default and 1 of 8 house because the grounding failures and placeholders persist.

These are 16 single generations, graded unblinded by the same reviewer, collected one call every seven minutes to stay inside the Anthropic per-model pacing on this account. The capped Opus 4.6 sample in assistant-v7 failed the default pilot email on a cost-of-delay claim; the uncapped default pilot email passes.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
