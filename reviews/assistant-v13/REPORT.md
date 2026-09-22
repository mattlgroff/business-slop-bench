# Assistant comparison: Muse added

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.

## Completed eight-draft conditions

| Model | Condition | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|
| Astra | default | 54/54 | 0 | 0 | 8/8 | 4/8 | $0.10989 |
| Astra | house | 54/54 | 0 | 0 | 8/8 | 7/8 | $0.36169 |
| Sol | default | 52/54 | 1 | 1 | 6/8 | 2/8 | $0.06108 |
| Sol | house | 53/54 | 1 | 0 | 7/8 | 6/8 | $0.18847 |
| Terra | default | 52/54 | 1 | 1 | 6/8 | 1/8 | $0.02792 |
| Terra | house | 52/54 | 1 | 1 | 6/8 | 5/8 | $0.07715 |
| Muse | default | 53/54 | 1 | 0 | 7/8 | 4/8 | $0.04428 |
| Muse | house | 52/54 | 2 | 0 | 6/8 | 4/8 | $0.07506 |
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

Muse is evaluated on the same briefs and house instructions. Routing differs because its provider lacks a ZDR option. These direct assistant grades remain provisional and unblinded.

## New review evidence

### Muse / pilot-client-email / default

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--pilot-client-email--default.md): 7/7 content checks, 69/180 words, 0 em dashes.

- **Style 21:** [The client hopes for 20% shorter handling time.](../../runs/pilot-v16/meta--muse-spark-1.3--pilot-client-email--default.md:7). Refers to the client in the third person inside an email addressed directly to that client.

### Muse / pilot-client-email / house

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--pilot-client-email--house.md): 7/7 content checks, 82/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / launch-delay-email / default

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--launch-delay-email--default.md): 6/6 content checks, 93/180 words, 0 em dashes.

- **Style 16:** [You choose whether to accept the staging demo.](../../runs/pilot-v16/meta--muse-spark-1.3--launch-delay-email--default.md:7). Repeats the later direct request to confirm the demo decision; removing it loses no information.

### Muse / launch-delay-email / house

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--launch-delay-email--house.md): 6/6 content checks, 74/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / vendor-decision-memo / default

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--vendor-decision-memo--default.md): 6/6 content checks, 102/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / vendor-decision-memo / house

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--vendor-decision-memo--house.md): 6/6 content checks, 98/300 words, 0 em dashes.

- **Style 14:** [Subject: Year-one vendor selection](../../runs/pilot-v16/meta--muse-spark-1.3--vendor-decision-memo--house.md:4). Duplicates the memo title exactly in a short document.

### Muse / pilot-results-memo / default

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--pilot-results-memo--default.md): 6/7 content checks, 120/300 words, 0 em dashes.

- **C01 fail:** [Baseline: 200 tickets, 15 minutes mean handling time.
Pilot: 100 tickets, 12 minutes mean handling time.](../../runs/pilot-v16/meta--muse-spark-1.3--pilot-results-memo--default.md:6). Gives both endpoints but omits the required explicit 3-minute or 20% reduction.
- **Style 10:** [Results support continued evaluation, not scaling. Lower mean handling time in pilot cannot support scaling due to differing mix and non-randomized allocation, quality is below threshold, and no savings measured.](../../runs/pilot-v16/meta--muse-spark-1.3--pilot-results-memo--default.md:19). Repeats the recommendation and all three limitations already explained in the preceding sections.

### Muse / pilot-results-memo / house

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--pilot-results-memo--house.md): 6/7 content checks, 121/300 words, 0 em dashes.

- **C01 fail:** [Mean handling time was 15 minutes at baseline on 200 tickets and 12 minutes in the pilot on 100 tickets.](../../runs/pilot-v16/meta--muse-spark-1.3--pilot-results-memo--house.md:7). Gives both endpoints but omits the required explicit 3-minute or 20% reduction.

### Muse / discovery-proposal / default

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--discovery-proposal--default.md): 7/7 content checks, 85/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / discovery-proposal / house

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--discovery-proposal--house.md): 7/7 content checks, 108/350 words, 0 em dashes.

- **Style 2:** [This proposal requests approval for four weeks of discovery.](../../runs/pilot-v16/meta--muse-spark-1.3--discovery-proposal--house.md:3). Announces what the proposal requests instead of directly asking the sponsor to approve it.

### Muse / change-order / default

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--change-order--default.md): 7/7 content checks, 99/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / change-order / house

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--change-order--house.md): 7/7 content checks, 110/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / ai-strategy-slides / default

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--ai-strategy-slides--default.md): 7/7 content checks, 102/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / ai-strategy-slides / house

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--ai-strategy-slides--house.md): 7/7 content checks, 114/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / handoff-slides / default

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--handoff-slides--default.md): 7/7 content checks, 159/350 words, 0 em dashes.

- **Style 10:** [Criterion 1: Approved runbook - Met. Runbook is approved.](../../runs/pilot-v16/meta--muse-spark-1.3--handoff-slides--default.md:7). The second slide repeats both criterion statuses and the acceptance gate already given on slide one; this line also repeats itself.

### Muse / handoff-slides / house

[Draft](../../runs/pilot-v16/meta--muse-spark-1.3--handoff-slides--house.md): 6/7 content checks, 89/350 words, 0 em dashes.

- **C03 fail:** [Sponsor Pat can assign responsibility for the rehearsal. The committee should name the owner and set the date.](../../runs/pilot-v16/meta--muse-spark-1.3--handoff-slides--house.md:11). States Pat's authority but directs the committee to name the owner, rather than requesting Pat to assign the rehearsal organizer as required.

## Adjudication boundaries

- Muse uses a declared non-ZDR route because the catalog and live request show no ZDR provider. Inputs are synthetic briefs and the public style lens.
- A direct paraphrase of the supplied client aspiration does not establish invented prior discussions; claims of prior collaboration or agreement still require support.

[All decisions](grades.json) and [summary](summary.json) retain previous grades and exact output hashes. Partial Opus, Fable and DeepSeek house coverage remains separate. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
