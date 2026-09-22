# Assistant comparison: Qwen Max added

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

This comparison tests whether Qwen Max improves on Flash under the same prompts. Content and editorial findings are reported separately, with unresolved interpretations retained. One output per cell does not establish reliability.

## New review evidence

### Qwen Max / pilot-client-email / default

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-client-email--default.md): 5/7 content checks, 163/180 words, 2 em dashes.

- **C03 fail:** [prove the savings case with real data](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-client-email--default.md:11). The draft labels 20% as a target but then promises to prove savings and convert that target into evidence, rather than assessing whether savings exist.
- **grounding fail:** [This pilot converts it into evidence](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-client-email--default.md:19). Promises to establish the hoped-for reduction as evidence without a baseline or existing measured savings.
- **Style 16:** [Ready to move when you are.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-client-email--default.md:21). Repeats the opening readiness claim and adds no decision or next action beyond the explicit approval request.

### Qwen Max / pilot-client-email / house

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-client-email--house.md): 6/7 content checks, 116/180 words, 0 em dashes.

- **grounding fail:** [propose a start date within the week](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-client-email--house.md:15). Invents a turnaround commitment absent from the source.

### Qwen Max / launch-delay-email / default

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--launch-delay-email--default.md): 5/6 content checks, 130/180 words, 1 em dashes.

- **grounding review:** [the team is in strong shape](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--launch-delay-email--default.md:9). Source does not establish team condition. This may be general reassurance rather than a specific readiness assertion, so it remains unresolved.
- **Style 2:** [A quick update on our launch position.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--launch-delay-email--default.md:5). Announces the update rather than starting with the changed security timeline.

### Qwen Max / launch-delay-email / house

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--launch-delay-email--house.md): 5/6 content checks, 114/180 words, 0 em dashes.

- **grounding fail:** [this delay reflects a process dependency, not a readiness gap on our side](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--launch-delay-email--house.md:7). Asserts no readiness gap despite a security review that may still require remediation. The preceding claim of strong work throughout the engagement is also unsupported.

### Qwen Max / vendor-decision-memo / default

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--vendor-decision-memo--default.md): 6/6 content checks, 154/300 words, 2 em dashes.

- **Style 10:** [Both vendors fit within the budget ceiling.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--vendor-decision-memo--default.md:16). Immediately repeats the table's Within $100K Ceiling results without additional analysis.

### Qwen Max / vendor-decision-memo / house

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--vendor-decision-memo--house.md): 6/6 content checks, 150/300 words, 0 em dashes.

- **Authoring placeholder:** [[Current date]](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--vendor-decision-memo--house.md:5). Unfilled authoring placeholder in a finished memo; this is not an intentional signature field in an approval form.

### Qwen Max / pilot-results-memo / default

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-results-memo--default.md): 7/7 content checks, 190/300 words, 3 em dashes.

- **Style 10:** [The pilot does not meet the criteria to proceed to scale.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-results-memo--default.md:5). Repeats the Do Not Scale Now heading without adding a reason.

### Qwen Max / pilot-results-memo / house

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-results-memo--house.md): 7/7 content checks, 172/300 words, 1 em dashes.

- **Style 10:** [The pilot does not meet the conditions required for a scale decision.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--pilot-results-memo--house.md:5). Repeats the preceding do-not-scale recommendation without adding information.

### Qwen Max / discovery-proposal / default

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--discovery-proposal--default.md): 7/7 content checks, 204/350 words, 0 em dashes.

- **Style 10:** [The start date is confirmed only after signature and a named client contact are in place.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--discovery-proposal--default.md:35). Repeats the immediately preceding fourth next step without adding a condition.

### Qwen Max / discovery-proposal / house

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--discovery-proposal--house.md): 7/7 content checks, 139/350 words, 0 em dashes.

- **Style 10:** [Over four weeks we will produce three artifacts:

1. Current-state process map
2. Prioritized backlog
3. Implementation recommendation](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--discovery-proposal--house.md:7). Repeats the full duration and deliverable list already given in the opening sentence, without adding scope detail.

### Qwen Max / change-order / default

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--change-order--default.md): 6/7 content checks, 229/300 words, 2 em dashes.

- **grounding fail:** [This proposal is valid for 30 days from the date above.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--change-order--default.md:52). Invents an offer-expiration term not provided in the source.
- **Style 10:** [No work will commence without that written approval.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--change-order--default.md:32). Repeats the immediately preceding requirement for written approval before connector work begins.
- **Authoring placeholder:** [[Insert Date]](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--change-order--default.md:5). Unfilled document-preparation date in the proposal header; the separate sponsor-signature date is an intentional form field.

### Qwen Max / change-order / house

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--change-order--house.md): 7/7 content checks, 181/300 words, 0 em dashes.

- **Style 10:** [| Item | Detail |](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--change-order--house.md:26). The table repeats the scope, fee, duration and dependencies already stated in the preceding sections.
- **Authoring placeholder:** [[Date]](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--change-order--house.md:4). Unfilled authoring date in the prepared-for header, distinct from the intentional sponsor-signature date field.

### Qwen Max / ai-strategy-slides / default

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--ai-strategy-slides--default.md): 6/7 content checks, 190/350 words, 0 em dashes.

- **grounding fail:** [Option A is the only pilot ready to execute this quarter](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--ai-strategy-slides--default.md:26). Changes the planning period to this quarter, contrary to the corrected next-quarter brief.

### Qwen Max / ai-strategy-slides / house

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--ai-strategy-slides--house.md): 6/7 content checks, 169/350 words, 0 em dashes.

- **grounding fail:** [Dana delivers accuracy results to COO before the next planning cycle.](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--ai-strategy-slides--house.md:26). Invents a reporting deadline. The source requires reporting before expansion, not before the next planning cycle.

### Qwen Max / handoff-slides / default

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--handoff-slides--default.md): 5/7 content checks, 204/350 words, 0 em dashes.

- **C04 fail:** [Acceptance transfers incident ownership from Engineering (Lee) to Operations (Jo)](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--handoff-slides--default.md:4). Assigns pre-acceptance incident ownership to Lee, whose stated responsibility is defect fixes only.
- **grounding fail:** [Acceptance transfers incident ownership from Engineering (Lee) to Operations (Jo)](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--handoff-slides--default.md:4). Invents incident ownership before acceptance.
- **Style 14:** [✅ Met](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--handoff-slides--default.md:11). Emojis decorate a professional status table; plain met and not met labels convey the same information.

### Qwen Max / handoff-slides / house

[Draft](../../runs/pilot-v15/alibaba--qwen3.8-max-0902--handoff-slides--house.md): 7/7 content checks, 160/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

## Adjudication boundaries

- Vague team-condition reassurance is unresolved. Claims of strong performance throughout an engagement or absence of readiness issues are factual assertions needing source support.
- Pilot assessment does not establish that savings exist; promises to prove savings are unsupported even when a nearby sentence calls the percentage a target.

[All decisions](grades.json) and [summary](summary.json) retain previous grades and exact output hashes. Partial Opus, Fable and DeepSeek house coverage remains separate. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
