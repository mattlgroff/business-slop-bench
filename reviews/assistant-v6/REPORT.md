# Assistant comparison with Luna

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same corrected briefs, no tools or revisions, one generation per condition. Model identities visible. No Jev judgments.

## Completed eight-draft conditions

| Model | Condition | Content checks passed | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen Flash | default | 47/54 | 7 | 0 | 1/8 | 0/8 | $0.00345 |
| Qwen Flash | house | 41/54 | 12 | 1 | 1/8 | 1/8 | $0.00821 |
| Kimi K3 | default | 51/54 | 2 | 1 | 5/8 | 4/8 | $0.06553 |
| Kimi K3 | house | 48/54 | 6 | 0 | 3/8 | 1/8 | $0.10848 |
| Astra | default | 54/54 | 0 | 0 | 8/8 | 4/8 | $0.10989 |
| Astra | house | 54/54 | 0 | 0 | 8/8 | 7/8 | $0.36169 |
| Luna | default | 52/54 | 1 | 1 | 5/8 | 2/8 | $0.00324 |
| Luna | house | 51/54 | 1 | 2 | 5/8 | 3/8 | $0.00817 |
| DeepSeek Flash | default | 50/54 | 4 | 0 | 4/8 | 0/8 | $0.00243 |

Unresolved checks earn no point. Content ready requires all task checks, the word limit and no unintended placeholders. Ready without edits additionally requires the style gate and no supported editorial findings. Default style results measure house-style fit without supplying the house instructions. These overlapping checks are not independent trials.

Luna produced this complete set for $0.01141. It preserves most factual and commercial constraints, but misses a required calculation in the default readout and the COO decision owner in the house strategy slides. Three grounding judgments remain unresolved; the default slides also contain a Q[next] placeholder. This is a useful low-cost comparison, not proof of a general model ranking.

## Luna evidence

### pilot-client-email / default

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--pilot-client-email--default.md): 7/7 content checks, 131/180 words, 0 em dashes.

- **Style 21:** [The client’s target](../../runs/pilot-v13/openai--gpt-5.6-luna--pilot-client-email--default.md:7). Refers to the client in the third person while addressing that client directly. Your target would fit this email audience.

### pilot-client-email / house

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--pilot-client-email--house.md): 7/7 content checks, 116/180 words, 0 em dashes.

- **Style 21:** [the client’s hope](../../runs/pilot-v13/openai--gpt-5.6-luna--pilot-client-email--house.md:5). Third-person client reference is unnatural in an email directly to that client; use your target.

### launch-delay-email / default

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--launch-delay-email--default.md): 5/6 content checks, 118/180 words, 0 em dashes.

- **grounding review:** [The team remains focused on completing the required security work and moving forward responsibly.](../../runs/pilot-v13/openai--gpt-5.6-luna--launch-delay-email--default.md:7). The source does not establish current team focus or activity. This may be ordinary reassurance rather than a material factual assertion, so it remains unresolved.
- **Style 20:** [The October 8 production launch is no longer the current position.](../../runs/pilot-v13/openai--gpt-5.6-luna--launch-delay-email--default.md:5). Current position obscures the concrete message that production cannot launch on October 8.

### launch-delay-email / house

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--launch-delay-email--house.md): 5/6 content checks, 92/180 words, 0 em dashes.

- **grounding review:** [The team remains focused on completing the required work](../../runs/pilot-v13/openai--gpt-5.6-luna--launch-delay-email--house.md:7). The source does not establish current team focus or activity; ordinary reassurance is a plausible reading, so this is unresolved.

### vendor-decision-memo / default

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--vendor-decision-memo--default.md): 6/6 content checks, 219/300 words, 0 em dashes.

- **Style 13:** [the only vendor in the source pack](../../runs/pilot-v13/openai--gpt-5.6-luna--vendor-decision-memo--default.md:28). Input-packet reference does not belong in the finished CFO memo.

### vendor-decision-memo / house

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--vendor-decision-memo--house.md): 6/6 content checks, 153/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### pilot-results-memo / default

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--pilot-results-memo--default.md): 6/7 content checks, 199/300 words, 0 em dashes.

- **C01 fail:** [15 minutes at baseline](../../runs/pilot-v13/openai--gpt-5.6-luna--pilot-results-memo--default.md:9). Gives the 15- and 12-minute endpoints but omits the required 3-minute or 20% reduction.

### pilot-results-memo / house

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--pilot-results-memo--house.md): 7/7 content checks, 180/300 words, 0 em dashes.

- **Style 10:** [| Finding | Decision relevance |](../../runs/pilot-v13/openai--gpt-5.6-luna--pilot-results-memo--house.md:9). The table repeats the findings already stated in the preceding paragraphs. Consolidate the presentation while retaining the baseline quality figure and numerical reduction.

### discovery-proposal / default

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--discovery-proposal--default.md): 7/7 content checks, 191/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### discovery-proposal / house

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--discovery-proposal--house.md): 7/7 content checks, 177/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### change-order / default

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--change-order--default.md): 7/7 content checks, 181/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### change-order / house

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--change-order--house.md): 7/7 content checks, 147/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### ai-strategy-slides / default

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--ai-strategy-slides--default.md): 7/7 content checks, 179/350 words, 4 em dashes.

- **Style 13:** [Q[next]](../../runs/pilot-v13/openai--gpt-5.6-luna--ai-strategy-slides--default.md:1). Unresolved authoring notation in a finished slide title; the brief already supplies next quarter.

### ai-strategy-slides / house

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--ai-strategy-slides--house.md): 6/7 content checks, 156/350 words, 0 em dashes.

- **C05 fail:** [## Slide 4: Approval requested](../../runs/pilot-v13/openai--gpt-5.6-luna--ai-strategy-slides--house.md:22). Preserves Dana ownership and reporting but never names the COO as the pilot selection authority.

### handoff-slides / default

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--handoff-slides--default.md): 7/7 content checks, 260/350 words, 4 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### handoff-slides / house

[Draft](../../runs/pilot-v13/openai--gpt-5.6-luna--handoff-slides--house.md): 6/7 content checks, 200/350 words, 0 em dashes.

- **grounding review:** [Keep the service with Engineering pending acceptance.](../../runs/pilot-v13/openai--gpt-5.6-luna--handoff-slides--house.md:28). May expand Engineering ownership beyond the stated defect-fix role, or may be shorthand for retaining that role. Broader service ownership is not supplied.

## Adjudication boundaries

- Luna team-focus wording is unresolved, not a confirmed invention. It is less concrete than claims of proven performance or readiness, but broader than the author expressing personal confidence.
- Luna handoff: keep the service with Engineering is unresolved because it could refer to the stated defect-fix responsibility or imply broader unassigned ownership.
- Third-person client phrasing and duplicated presentation are editorial judgments, not factual failures.
- Luna change-order signature fields are intentional form fields. Q[next] in a slide title is an unintended authoring placeholder.

All decisions and exact hashes are in [grades.json](grades.json). The partial Opus, Fable and DeepSeek house sets remain ungraded where outputs are missing. Successful generation prices here include each represented draft once and exclude failures and judge diagnostics.
