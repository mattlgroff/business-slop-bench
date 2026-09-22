# Uncapped comparison: Fable 5.1 added (non-ZDR, disqualified)

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

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax, Grok and Astra are new uncapped generations on each attempted cell; the Grok house handoff deck comes from pilot-v21 after its pilot-v20 request timed out; Opus 5 is a pilot-v21 collection with one pilot-v20 import; Opus 4.6 is a full pilot-v21 collection; Fable 5.1 is a pilot-v21 collection with one pilot-v20 import on a declared non-ZDR route; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

## New review evidence

### Fable 5.1 / pilot-client-email / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--pilot-client-email--default.md): 6/7 content checks, 176/180 words, 1 em dashes.

- **grounding fail:** [Following our discussions](../../runs/pilot-v21/anthropic--claude-fable-5.1--pilot-client-email--default.md:5). Invents prior discussions absent from the source pack.
- **Style 5:** [No variable costs or surprises.](../../runs/pilot-v21/anthropic--claude-fable-5.1--pilot-client-email--default.md:9). Promotional assurance without a defined comparison; the fixed fee already states the commercial terms.
- **Style 17:** [We fully recognize](../../runs/pilot-v21/anthropic--claude-fable-5.1--pilot-client-email--default.md:13). Empty intensifier before a stated prerequisite.

### Fable 5.1 / pilot-client-email / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--pilot-client-email--house.md): 6/7 content checks, 181/180 words, 0 em dashes.

- **grounding fail:** [Can you confirm approval of the scope and fee by Friday](../../runs/pilot-v21/anthropic--claude-fable-5.1--pilot-client-email--house.md:17). Invents a Friday reply deadline; the draft also promises a start-date proposal the same week and states that approving costs nothing until clearance, a payment term the source does not contain.

### Fable 5.1 / launch-delay-email / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--launch-delay-email--default.md): 5/6 content checks, 174/180 words, 0 em dashes.

- **grounding fail:** [The team is in good shape and ready either way.](../../runs/pilot-v21/anthropic--claude-fable-5.1--launch-delay-email--default.md:19). Invents a team readiness and condition claim the source does not record.
- **Style 2:** [A quick update on where the launch stands.](../../runs/pilot-v21/anthropic--claude-fable-5.1--launch-delay-email--default.md:5). Announces the update instead of stating the launch position.

### Fable 5.1 / launch-delay-email / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--launch-delay-email--house.md): 5/6 content checks, 130/180 words, 0 em dashes.

- **grounding fail:** [Please let me know by end of day Thursday](../../runs/pilot-v21/anthropic--claude-fable-5.1--launch-delay-email--house.md:9). Invents a Thursday reply deadline; the draft also asserts the demo environment is ready, which the source does not record.

### Fable 5.1 / vendor-decision-memo / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--vendor-decision-memo--default.md): 6/6 content checks, 263/300 words, 1 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5.1 / vendor-decision-memo / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--vendor-decision-memo--house.md): 5/6 content checks, 270/300 words, 0 em dashes.

- **grounding review:** [Priya signs after CFO approval.](../../runs/pilot-v21/anthropic--claude-fable-5.1--vendor-decision-memo--house.md:38). Implies Priya signs; the source says CFO approval precedes signing but does not say who signs.
- **Authoring placeholder:** [The source pack lists no other year-one costs](../../runs/pilot-v21/anthropic--claude-fable-5.1--vendor-decision-memo--house.md:28). Refers to the source pack inside the client-facing memo; authoring residue.

### Fable 5.1 / pilot-results-memo / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--pilot-results-memo--default.md): 7/7 content checks, 307/300 words, 3 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5.1 / pilot-results-memo / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--pilot-results-memo--house.md): 7/7 content checks, 302/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5.1 / discovery-proposal / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--discovery-proposal--default.md): 7/7 content checks, 190/350 words, 0 em dashes.

- **Style 28:** [We look forward to your approval and to beginning discovery.](../../runs/pilot-v21/anthropic--claude-fable-5.1--discovery-proposal--default.md:51). Empty positive ending that adds no decision, owner or condition.

### Fable 5.1 / discovery-proposal / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--discovery-proposal--house.md): 7/7 content checks, 183/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5.1 / change-order / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--change-order--default.md): 7/7 content checks, 254/300 words, 2 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5.1 / change-order / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--change-order--house.md): 7/7 content checks, 229/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5.1 / ai-strategy-slides / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--ai-strategy-slides--default.md): 6/7 content checks, 193/350 words, 6 em dashes.

- **grounding fail:** [authorized, affordable, owned, and measurable](../../runs/pilot-v21/anthropic--claude-fable-5.1--ai-strategy-slides--default.md:22). Labels the knowledge-search pilot authorized before the COO selects it; the deck also invents the absence of external data risk.

### Fable 5.1 / ai-strategy-slides / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--ai-strategy-slides--house.md): 6/7 content checks, 257/350 words, 0 em dashes.

- **grounding fail:** [this is the one that can start on day one](../../runs/pilot-v21/anthropic--claude-fable-5.1--ai-strategy-slides--house.md:6). Invents day-one readiness; the deck also asserts that no new data or legal approval is needed to start.

### Fable 5.1 / handoff-slides / default

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--handoff-slides--default.md): 7/7 content checks, 278/350 words, 4 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Fable 5.1 / handoff-slides / house

[Draft](../../runs/pilot-v21/anthropic--claude-fable-5.1--handoff-slides--house.md): 7/7 content checks, 202/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

## Adjudication boundaries

Fable 5.1 passes 51/54 default and 50/54 house content checks with three grounding failures in each condition, all on the same three briefs: prior discussions in the default pilot email and a Friday reply deadline with an invented payment term in the house one, team readiness in both launch updates, and an authorized or day-one label for the knowledge-search pilot in both strategy decks. The house vendor memo is unresolved on who signs and refers to the source pack in its body. Both readouts state the reduction explicitly; both discovery proposals and change orders are content ready in both conditions. Three drafts exceed their word limits by one to seven words.

The house condition removes every em dash (17 default, 0 house) and every editorial finding (4 default, 0 house), and gives three drafts ready without edits against none by default. It does not change the failure pattern: the same three briefs fail either way, and the house pilot email adds a deadline the default did not have.

Fable 5.1 has no ZDR route on the Gateway. It was collected under the protocol non-ZDR exception because the user asked for it, and under the ZDR rule it fails the bench regardless of these scores. Its rows carry benchEligible false and are reported separately, never pooled with eligible models. These are 16 single generations, graded unblinded by the same reviewer, collected one call every seven minutes; the default pilot email is the pilot-v20 import.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
