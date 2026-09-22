# Uncapped comparison: Opus 5 added

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

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax, Grok and Astra are new uncapped generations on each attempted cell; the Grok house handoff deck comes from pilot-v21 after its pilot-v20 request timed out; Opus 5 is a pilot-v21 collection with one pilot-v20 import; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

## New review evidence

### Opus 5 / pilot-client-email / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--pilot-client-email--default.md): 6/7 content checks, 195/180 words, 2 em dashes.

- **grounding fail:** [Thank you for the discussion on invoice handling.](../../runs/pilot-v21/anthropic--claude-opus-5--pilot-client-email--default.md:5). Invents a prior discussion absent from the source pack.
- **Style 29:** [I want to be straightforward:](../../runs/pilot-v21/anthropic--claude-opus-5--pilot-client-email--default.md:11). Candor script preceding a fact that can be stated directly.

### Opus 5 / pilot-client-email / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--pilot-client-email--house.md): 6/7 content checks, 190/180 words, 0 em dashes.

- **grounding fail:** [propose a start date within a week of their sign-off](../../runs/pilot-v21/anthropic--claude-opus-5--pilot-client-email--house.md:13). Invents a one-week scheduling commitment the source does not authorize.

### Opus 5 / launch-delay-email / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--launch-delay-email--default.md): 5/6 content checks, 203/180 words, 1 em dashes.

- **grounding fail:** [the delay reflects that rigour rather than any slippage in delivery](../../runs/pilot-v21/anthropic--claude-opus-5--launch-delay-email--default.md:11). Invents a favorable account of review rigour and delivery performance the source does not record; the draft also casts Jordan as the one withholding authorization of a new date.
- **Style 2:** [I want to give you a clear picture of where the launch stands.](../../runs/pilot-v21/anthropic--claude-opus-5--launch-delay-email--default.md:5). Announces the update instead of stating the launch position.

### Opus 5 / launch-delay-email / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--launch-delay-email--house.md): 5/6 content checks, 210/180 words, 0 em dashes.

- **grounding fail:** [confirm by October 6](../../runs/pilot-v21/anthropic--claude-opus-5--launch-delay-email--house.md:13). Invents an October 6 reply deadline and a provisional booking released on the 7th; the draft also vouches for the team's handling of the review, which the source does not record.

### Opus 5 / vendor-decision-memo / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--vendor-decision-memo--default.md): 5/6 content checks, 286/300 words, 1 em dashes.

- **grounding review:** [Priya to finalize and execute the Alpha agreement.](../../runs/pilot-v21/anthropic--claude-opus-5--vendor-decision-memo--default.md:38). Executing the agreement implies Priya signs; the source says CFO approval precedes signing but does not say who signs.
- **Style 29:** [The cheaper option is only cheaper if it can be deployed.](../../runs/pilot-v21/anthropic--claude-opus-5--vendor-decision-memo--default.md:31). Aphoristic restatement of the preceding sentence, removable without information loss.

### Opus 5 / vendor-decision-memo / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--vendor-decision-memo--house.md): 5/6 content checks, 273/300 words, 0 em dashes.

- **grounding review:** [subject to whatever renewal terms legal negotiates](../../runs/pilot-v21/anthropic--claude-opus-5--vendor-decision-memo--house.md:33). Introduces a legal review and renewal negotiation role the source does not describe; the next steps otherwise read as proposals.

### Opus 5 / pilot-results-memo / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--pilot-results-memo--default.md): 6/7 content checks, 334/300 words, 7 em dashes.

- **grounding fail:** [five points below the 92% scaling threshold](../../runs/pilot-v21/anthropic--claude-opus-5--pilot-results-memo--default.md:21). The shortfall against the 92% threshold is 3 points, not 5.

### Opus 5 / pilot-results-memo / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--pilot-results-memo--house.md): 7/7 content checks, 264/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5 / discovery-proposal / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--discovery-proposal--default.md): 7/7 content checks, 355/350 words, 1 em dashes.

- **Style 2:** [Acceptance is straightforward:](../../runs/pilot-v21/anthropic--claude-opus-5--discovery-proposal--default.md:41). Announces the acceptance basis instead of stating it.
- **Style 4:** [the single biggest driver of discovery quality](../../runs/pilot-v21/anthropic--claude-opus-5--discovery-proposal--default.md:37). Asserts importance without evidence; the dependency itself is the fact.
- **Style 20:** [a clear, evidence-based view of your current state and a practical path forward](../../runs/pilot-v21/anthropic--claude-opus-5--discovery-proposal--default.md:8). Generic consulting language adds nothing beyond the three listed deliverables.

### Opus 5 / discovery-proposal / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--discovery-proposal--house.md): 7/7 content checks, 193/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5 / change-order / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--change-order--default.md): 7/7 content checks, 297/300 words, 1 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5 / change-order / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--change-order--house.md): 7/7 content checks, 210/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Opus 5 / ai-strategy-slides / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--ai-strategy-slides--default.md): 6/7 content checks, 350/350 words, 8 em dashes.

- **grounding fail:** [Option A Is Ready to Execute](../../runs/pilot-v21/anthropic--claude-opus-5--ai-strategy-slides--default.md:22). Invents readiness for the knowledge-search pilot; the deck also states production use is permitted for Option A and that no new data authorization is required, none of which the source records.
- **Negative parallelism:** [It is not rejected on merit — it is blocked on authorization.](../../runs/pilot-v21/anthropic--claude-opus-5--ai-strategy-slides--default.md:18). Negated framing followed by the affirmative reason; the affirmative clause alone carries the point.

### Opus 5 / ai-strategy-slides / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--ai-strategy-slides--house.md): 6/7 content checks, 250/350 words, 0 em dashes.

- **grounding fail:** [Why credit decisions cannot start next quarter](../../runs/pilot-v21/anthropic--claude-opus-5--ai-strategy-slides--house.md:15). Pending legal approval and unauthorized production use do not establish that the pilot cannot start; the deck also asserts no new content approval is needed for Option A.

### Opus 5 / handoff-slides / default

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--handoff-slides--default.md): 7/7 content checks, 414/350 words, 5 em dashes.

- **Authoring placeholder:** [described in the source pack](../../runs/pilot-v21/anthropic--claude-opus-5--handoff-slides--default.md:36). Refers to the source pack inside the committee deck; authoring residue.
- **Authoring placeholder:** [This pack does not state a rehearsal date](../../runs/pilot-v21/anthropic--claude-opus-5--handoff-slides--default.md:40). Refers to the source pack inside the committee deck; authoring residue.

### Opus 5 / handoff-slides / house

[Draft](../../runs/pilot-v21/anthropic--claude-opus-5--handoff-slides--house.md): 6/7 content checks, 264/350 words, 0 em dashes.

- **grounding fail:** [| Runbook approved | Met | Lee |](../../runs/pilot-v21/anthropic--claude-opus-5--handoff-slides--house.md:14). Assigns runbook ownership to Lee; the source names no runbook owner.
- **Negative parallelism:** [That absence, not a failed test, is why the service sits short of acceptance.](../../runs/pilot-v21/anthropic--claude-opus-5--handoff-slides--house.md:17). Negated contrast where the affirmative cause alone carries the point.

## Adjudication boundaries

Opus 5 passes 49/54 content checks in both conditions, with four grounding failures and one unresolved check in each. Every failure is an invented claim rather than a wrong number: a prior discussion and a one-week start-date promise in the pilot emails, favorable review performance and an October 6 reply deadline in the launch updates, a 5-point shortfall against the 92% threshold that is actually 3 points in the default readout, readiness and permitted production use for the knowledge-search pilot in both strategy decks, and runbook ownership assigned to Lee in the house handoff deck. Both vendor memos are unresolved only on who signs. Both readouts state the 3-minute reduction explicitly.

The house condition removes every em dash (26 default, 0 house) and every editorial finding (6 default, 0 house), and lifts content-ready drafts from 1 of 8 to 3 of 8, all three of which are ready without edits. It does not remove the invented commitments: the same two emails fail in both conditions, and the house launch update adds a reply deadline the default did not have. Five default drafts and two house drafts exceed the word limit, so length is the main reason default drafts are not content ready. The default handoff deck refers to the source pack twice.

These are 16 single generations, graded unblinded by the same reviewer, collected one call every seven minutes to stay inside the Anthropic per-model pacing on this account; the default pilot email is the pilot-v20 import. The capped Opus 5 sample in assistant-v7 failed the same launch update on the same kind of claim.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
