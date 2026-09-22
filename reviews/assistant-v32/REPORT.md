# Uncapped comparison: Opus 5.5 added

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.

## Uncapped results

| Model | Condition | Completed briefs | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Muse (non-ZDR, disqualified) | default | 8/8 | 53/54 | 1 | 0 | 7/8 | 4/8 | $0.03816 |
| Muse (non-ZDR, disqualified) | house | 8/8 | 53/54 | 1 | 0 | 7/8 | 5/8 | $0.05720 |
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
| Opus 5.5 | default | 8/8 | 52/54 | 1 | 1 | 4/8 | 2/8 | $0.11713 |
| Opus 5.5 | house | 8/8 | 51/54 | 2 | 1 | 3/8 | 3/8 | $0.25326 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax, Grok and Astra are new uncapped generations on each attempted cell; the Grok house handoff deck comes from pilot-v21 after its pilot-v20 request timed out; Opus 5 is a pilot-v21 collection with one pilot-v20 import; Opus 4.6 is a full pilot-v21 collection; Fable 5.1 and Fable 5 are pilot-v21 collections with one pilot-v20 import each on a declared non-ZDR route; Opus 5.5 is a full pilot-v22 collection on a ZDR route; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

Eligibility is derived from each saved catalog and frozen request policy, including inherited rows. Muse, Fable 5 and Fable 5.1 are non-ZDR and disqualified; their writing scores remain visible. This is a routing-policy check, not independent verification of provider retention. [Eligibility evidence](eligibility-evidence.json) and [unchanged writing-score digest](eligibility-score-integrity.json).

## New review evidence

### Opus 5.5 / pilot-client-email / default

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--pilot-client-email--default.md): 7/7 content checks, 181/180 words, 0 em dashes.

- **Style 2:** [I'm writing to propose](../../runs/pilot-v22/anthropic--claude-opus-5.5--pilot-client-email--default.md:5). Announces the proposal instead of starting with the scope and fee.
- **Style 5:** [This keeps the scope contained and the risk low.](../../runs/pilot-v22/anthropic--claude-opus-5.5--pilot-client-email--default.md:9). Promotional assurance without a defined basis; the exclusion itself is the fact.

### Opus 5.5 / pilot-client-email / house

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--pilot-client-email--house.md): 7/7 content checks, 190/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5.5 / launch-delay-email / default

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--launch-delay-email--default.md): 6/6 content checks, 180/180 words, 0 em dashes.

- **Style 2:** [Here is where the launch stands.](../../runs/pilot-v22/anthropic--claude-opus-5.5--launch-delay-email--default.md:5). Announces the update instead of stating the launch position.

### Opus 5.5 / launch-delay-email / house

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--launch-delay-email--house.md): 5/6 content checks, 169/180 words, 0 em dashes.

- **grounding fail:** [The team is on track with everything it controls.](../../runs/pilot-v22/anthropic--claude-opus-5.5--launch-delay-email--house.md:11). Invents an on-track performance claim the source does not record.

### Opus 5.5 / vendor-decision-memo / default

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--vendor-decision-memo--default.md): 5/6 content checks, 316/300 words, 0 em dashes.

- **grounding review:** [Priya finalizes the contract and proceeds to signing.](../../runs/pilot-v22/anthropic--claude-opus-5.5--vendor-decision-memo--default.md:52). Implies Priya signs; the source says CFO approval precedes signing but does not say who signs.

### Opus 5.5 / vendor-decision-memo / house

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--vendor-decision-memo--house.md): 5/6 content checks, 286/300 words, 0 em dashes.

- **grounding review:** [executes the contract](../../runs/pilot-v22/anthropic--claude-opus-5.5--vendor-decision-memo--house.md:36). Implies Priya signs; the source says CFO approval precedes signing but does not say who signs.
- **Authoring placeholder:** [The source figures cover year one only.](../../runs/pilot-v22/anthropic--claude-opus-5.5--vendor-decision-memo--house.md:31). Refers to the source material inside the memo; authoring residue.

### Opus 5.5 / pilot-results-memo / default

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--pilot-results-memo--default.md): 7/7 content checks, 318/300 words, 4 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5.5 / pilot-results-memo / house

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--pilot-results-memo--house.md): 7/7 content checks, 292/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5.5 / discovery-proposal / default

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--discovery-proposal--default.md): 7/7 content checks, 317/350 words, 0 em dashes.

- **Style 20:** [a clear view of your current state and a practical path forward](../../runs/pilot-v22/anthropic--claude-opus-5.5--discovery-proposal--default.md:8). Generic consulting language adds nothing beyond the three listed deliverables.

### Opus 5.5 / discovery-proposal / house

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--discovery-proposal--house.md): 7/7 content checks, 241/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5.5 / change-order / default

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--change-order--default.md): 7/7 content checks, 275/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5.5 / change-order / house

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--change-order--house.md): 7/7 content checks, 229/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5.5 / ai-strategy-slides / default

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--ai-strategy-slides--default.md): 6/7 content checks, 270/350 words, 0 em dashes.

- **grounding fail:** [Option A can start now.](../../runs/pilot-v22/anthropic--claude-opus-5.5--ai-strategy-slides--default.md:20). Invents readiness for the knowledge-search pilot; the source records approved policy documents and a COO selection, not a start condition.
- **Authoring placeholder:** [No blocker in the source pack](../../runs/pilot-v22/anthropic--claude-opus-5.5--ai-strategy-slides--default.md:17). Refers to the source pack inside the executive deck; authoring residue.

### Opus 5.5 / ai-strategy-slides / house

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--ai-strategy-slides--house.md): 6/7 content checks, 184/350 words, 0 em dashes.

- **grounding fail:** [Knowledge search is ready to start](../../runs/pilot-v22/anthropic--claude-opus-5.5--ai-strategy-slides--house.md:9). Invents readiness for the knowledge-search pilot; the source records approved policy documents and a COO selection, not a start condition.

### Opus 5.5 / handoff-slides / default

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--handoff-slides--default.md): 7/7 content checks, 267/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5.5 / handoff-slides / house

[Draft](../../runs/pilot-v22/anthropic--claude-opus-5.5--handoff-slides--house.md): 7/7 content checks, 282/350 words, 0 em dashes.

- **Authoring placeholder:** [The source pack assigns no incident owner](../../runs/pilot-v22/anthropic--claude-opus-5.5--handoff-slides--house.md:24). Refers to the source pack inside the committee deck; authoring residue.

## Adjudication boundaries

Opus 5.5 passes 52/54 default and 51/54 house content checks. Its only default failure is readiness for the knowledge-search pilot in the strategy deck; house repeats that failure and adds an on-track team claim in the launch update that the default draft did not make. Both vendor memos are unresolved only on who signs. Both readouts state the 3-minute and 20% reduction and the correct 3-point and 5-point differences. No draft invents a reply deadline, a start date or a prior discussion, which every other Anthropic model in this cohort did at least once. Three default drafts and one house draft exceed their word limits, by 1 to 18 words.

Against the release note claim the user asked about: the house rules remove every em dash (4 default, 0 house) and every editorial finding (4 default, 0 house), exactly as they do for Opus 5, so this bench cannot separate the two models on rule-following. On putting the point up front, Opus 5.5 opens two default drafts with an announcing sentence and Opus 5 also opens two that way, so there is no measurable difference there either. Where Opus 5.5 does differ is grounding: one and two failures against four and four for Opus 5, and content-ready counts of 4 of 8 default and 3 of 8 house against 1 and 3. Its default change order and handoff deck are ready without edits, which no other Anthropic default draft in this cohort achieves. Two house drafts and one default draft refer to the source pack in the body, which blocks content ready.

These are 16 single generations, graded unblinded by the same reviewer, collected one call every seven minutes on a ZDR route on the day the model was released. A difference of a few checks between Opus 5.5 and Opus 5 is within what a second generation could change, and the Astra sample remains the only one with every draft content ready.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
