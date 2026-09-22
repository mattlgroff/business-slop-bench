# Assistant comparison: MiniMax added

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.

## Partial uncapped comparison

| Model | Condition | Completed briefs | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Five drafts completed before the house vendor request ended with a Gateway 408 reporting a 300,000 ms HTTP headers timeout. Eleven cells remain ungraded.

## New review evidence

### MiniMax / pilot-client-email / default

[Draft](../../runs/pilot-v18/minimax--minimax-m3--pilot-client-email--default.md): 6/7 content checks, 169/180 words, 1 em dashes.

- **grounding fail:** [Thanks for our recent conversation.](../../runs/pilot-v18/minimax--minimax-m3--pilot-client-email--default.md:5). Invents a prior conversation and agreed terms. Also commits to a week-one baseline and parallel onboarding absent from the source.
- **Style 2:** [I'd like to formally propose](../../runs/pilot-v18/minimax--minimax-m3--pilot-client-email--default.md:5). Unnecessary announcement before the actual scope and fee.

### MiniMax / pilot-client-email / house

[Draft](../../runs/pilot-v18/minimax--minimax-m3--pilot-client-email--house.md): 6/7 content checks, 125/180 words, 0 em dashes.

- **grounding fail:** [Week one establishes current throughput by invoice type](../../runs/pilot-v18/minimax--minimax-m3--pilot-client-email--house.md:11). Invents scheduled work and measurement detail absent from the approved source.
- **Negative parallelism:** [a real comparison rather than a directional claim](../../runs/pilot-v18/minimax--minimax-m3--pilot-client-email--house.md:11). Uses a vague credibility contrast to promote the pilot, without a necessary factual correction or scope boundary.

### MiniMax / launch-delay-email / default

[Draft](../../runs/pilot-v18/minimax--minimax-m3--launch-delay-email--default.md): 5/6 content checks, 173/180 words, 2 em dashes.

- **grounding fail:** [The team is steady and the delivery work is intact.](../../runs/pilot-v18/minimax--minimax-m3--launch-delay-email--default.md:19). Invents delivery readiness. The next sentence also asserts that the build has not slipped, which the source does not establish.
- **Style 2:** [Quick update on launch readiness as we close out the week.](../../runs/pilot-v18/minimax--minimax-m3--launch-delay-email--default.md:5). Announces the update instead of stating the changed timeline.

### MiniMax / launch-delay-email / house

[Draft](../../runs/pilot-v18/minimax--minimax-m3--launch-delay-email--house.md): 5/6 content checks, 125/180 words, 0 em dashes.

- **grounding fail:** [The team has shipped verification work, the staging environment, and demo assets on the original schedule](../../runs/pilot-v18/minimax--minimax-m3--launch-delay-email--house.md:5). Invents completed work and on-schedule delivery. The end-of-day response deadline is also absent from the source.

### MiniMax / vendor-decision-memo / default

[Draft](../../runs/pilot-v18/minimax--minimax-m3--vendor-decision-memo--default.md): 5/6 content checks, 226/300 words, 3 em dashes.

- **grounding fail:** [no contractual remedy or delivery protection](../../runs/pilot-v18/minimax--minimax-m3--vendor-decision-memo--default.md:26). Invents contractual terms for Beta. The source only establishes unavailable SSO and no committed delivery date.

## Adjudication boundaries

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
