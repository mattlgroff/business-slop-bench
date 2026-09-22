# Assistant grades: corrected task set

Provisional assistant-authored grades, not human gold or independent benchmark validation. Model identities were visible. No Jev judgments were used.

Only the capacity statement in the AI strategy brief changed to next quarter. Four affected Qwen/Kimi drafts regenerated once each. Prior grades carried only across byte-identical outputs and identical tasks. Opus remains partial due to Gateway 429 failures.

## Complete eight-brief comparison

| Model | Condition | Content checks passed | Failed | Unresolved | Ready without edits |
|---|---|---:|---:|---:|---:|
| Qwen Flash | default | 47/54 | 7 | 0 | 0/8 |
| Qwen Flash | house | 41/54 | 12 | 1 | 1/8 |
| Kimi K3 | default | 51/54 | 2 | 1 | 4/8 |
| Kimi K3 | house | 48/54 | 6 | 0 | 1/8 |

Unresolved checks earn no credit. Ready without edits requires all task-content checks to pass, the word limit, no placeholders, the style gate, and no supported editorial findings. Default style results describe house-style fit without supplying those instructions. These overlapping checks are not independent observations.

## Opus: incomplete, not a comparable model total

| Condition | Generated and graded | Content checks passed | Failed | Unresolved | Word-limit failures | Ready without edits |
|---|---:|---:|---:|---:|---:|---:|
| default | 2/8 | 11/13 | 2 | 0 | 2 | 0/2 |
| house | 1/8 | 6/7 | 0 | 1 | 1 | 0/1 |

Missing outputs are ungraded, not failures or zero-quality scores. The 429 message does not establish whether the cause is provider capacity, model access, or account rate restriction.

## Newly reviewed evidence

### Qwen Flash / ai-strategy-slides / default

[Draft](../../runs/pilot-v10/alibaba--qwen3.8-flash--ai-strategy-slides--default.md), 177/350 words, 2 em dashes.

- **grounding fail:** [Low risk; no external dependencies](../../runs/pilot-v10/alibaba--qwen3.8-flash--ai-strategy-slides--default.md:18). Invents absence of external dependencies, legal clearance, and a specific Q3 quarter not given in the brief.

### Qwen Flash / ai-strategy-slides / house

[Draft](../../runs/pilot-v10/alibaba--qwen3.8-flash--ai-strategy-slides--house.md), 129/350 words, 0 em dashes.

- **C01 fail:** [Slide 4: Evaluation & Next Steps](../../runs/pilot-v10/alibaba--qwen3.8-flash--ai-strategy-slides--house.md:21). No specific recommendation between the two pilots.
- **grounding fail:** [Risk of budget overrun is high.](../../runs/pilot-v10/alibaba--qwen3.8-flash--ai-strategy-slides--house.md:19). Invents budget-overrun risk and states that no legal barriers exist for Option A without evidence.

### Kimi K3 / ai-strategy-slides / default

[Draft](../../runs/pilot-v10/moonshotai--kimi-k3--ai-strategy-slides--default.md), 193/350 words, 4 em dashes.

No content or editorial defect found in this review; any em dash violations remain separate.

### Kimi K3 / ai-strategy-slides / house

[Draft](../../runs/pilot-v10/moonshotai--kimi-k3--ai-strategy-slides--house.md), 233/350 words, 0 em dashes.

- **grounding fail:** [no path to use](../../runs/pilot-v10/moonshotai--kimi-k3--ai-strategy-slides--house.md:26). Overstates pending authorization as no path to use; also rules out use for a whole quarter without an approval date.

### Opus 5 / pilot-client-email / default

[Draft](../../runs/pilot-v10/anthropic--claude-opus-5--pilot-client-email--default.md), 191/180 words, 3 em dashes.

- **grounding fail:** [No variable costs, no overrun exposure.](../../runs/pilot-v10/anthropic--claude-opus-5--pilot-client-email--default.md:9). A fixed pilot fee does not establish no variable costs or overrun exposure for the client. Also invents prior discussions.
- **Style 16:** [This pilot exists to produce that evidence](../../runs/pilot-v10/anthropic--claude-opus-5--pilot-client-email--default.md:7). The lengthy rationale repeats the evidence gap and scope boundary; the email exceeds the explicit word limit.

### Opus 5 / pilot-client-email / house

[Draft](../../runs/pilot-v10/anthropic--claude-opus-5--pilot-client-email--house.md), 185/180 words, 0 em dashes.

- **grounding review:** [I'd rather hold the team's availability than release it and rebook later.](../../runs/pilot-v10/anthropic--claude-opus-5--pilot-client-email--house.md:13). Creates staffing-pressure implications absent from the source. Wording may describe a proposed scheduling preference rather than a definite existing hold.
- **Style 16:** [That measurement gives you a defensible number either way](../../runs/pilot-v10/anthropic--claude-opus-5--pilot-client-email--house.md:7). Long hypothetical outcomes delay the approval request; the email exceeds the explicit word limit.

### Opus 5 / launch-delay-email / default

[Draft](../../runs/pilot-v10/anthropic--claude-opus-5--launch-delay-email--default.md), 204/180 words, 2 em dashes.

- **grounding fail:** [not a gap in execution](../../runs/pilot-v10/anthropic--claude-opus-5--launch-delay-email--default.md:11). Rules out execution problems without supplied evidence; claims review thoroughness and team control.
- **Style 2:** [An update on the launch position and one decision I need from you.](../../runs/pilot-v10/anthropic--claude-opus-5--launch-delay-email--default.md:5). Throat clearing delays the material date change; the email exceeds the word limit.

Unchanged draft decisions and explanations are retained in [grades.json](grades.json), with their original grade provenance. [Previous full evidence report](../assistant-v1/REPORT.md). The correction and new generation are not a causal experiment: output differences may reflect sampling variation.
