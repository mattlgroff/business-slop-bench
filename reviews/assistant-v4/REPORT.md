# Assistant comparison: first-email coverage across six models

Provisional assistant-authored grades, not human gold or independent benchmark validation. Model identities were visible; no Jev judgments were used.

## Same pilot-client email, both conditions

| Model | Default content checks | House content checks | Ready default / house |
|---|---:|---:|---|
| Qwen Flash | 6/7 | 4/7 | No / No |
| Kimi K3 | 7/7 | 6/7 | Yes / No |
| Astra | 7/7 | 7/7 | No / No |
| Opus 5 | 6/7 | 6/7 | No / No |
| Fable 5.1 | 6/7 | 7/7 | No / Yes |
| DeepSeek Flash | 6/7 | 6/7 | No / No |

Ready requires all critical checks, word limit, no placeholders, clean style gate, and no supported editorial edits. A content pass alone does not mean ready. Unresolved checks earn no credit. Opus house and DeepSeek house each have one unresolved grounding check, not a confirmed grounding failure.

This single brief is a matched comparison, not a general model ranking. Fable house is usable on this review. Fable default invents prior discussions. DeepSeek repeats that mistake in its default draft; its house draft has an ambiguous approval promise and redundant wording.

## New evidence

### Fable 5.1 / pilot-client-email / default

[Draft](../../runs/pilot-v11/anthropic--claude-fable-5.1--pilot-client-email--default.md): 6/7 content checks, 167/180 words, 0 em dashes.

- **grounding fail:** [Thank you for the productive discussions so far.](../../runs/pilot-v11/anthropic--claude-fable-5.1--pilot-client-email--default.md:5). Invents productive prior discussions not supplied in the source.

### Fable 5.1 / pilot-client-email / house

[Draft](../../runs/pilot-v11/anthropic--claude-fable-5.1--pilot-client-email--house.md): 7/7 content checks, 178/180 words, 0 em dashes.

No supported content or editorial finding in this review.

### DeepSeek Flash / pilot-client-email / default

[Draft](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--pilot-client-email--default.md): 6/7 content checks, 141/180 words, 0 em dashes.

- **grounding fail:** [Following our discussions](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--pilot-client-email--default.md:5). Invents prior discussions not supplied in the source.
- **Style 29:** [I want to be transparent:](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--pilot-client-email--default.md:12). Candor preamble adds no information to the necessary baseline caveat that follows.

### DeepSeek Flash / pilot-client-email / house

[Draft](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--pilot-client-email--house.md): 6/7 content checks, 139/180 words, 0 em dashes.

- **grounding review:** [I will secure it before work begins.](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--pilot-client-email--house.md:7). May imply a guarantee of granted security approval, or may describe a plan to satisfy the prerequisite. The source authorizes the prerequisite, not a guaranteed approval outcome.
- **Style 16:** [Approving the scope and fee, subject to security clearance, lets us set that date and begin.](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--pilot-client-email--house.md:9). Repeats the approval-to-start logic immediately before another conditional approval request and scheduling promise.

### DeepSeek Flash / launch-delay-email / default

[Draft](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--launch-delay-email--default.md): 5/6 content checks, 142/180 words, 0 em dashes.

- **grounding fail:** [The team has responded well.](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--launch-delay-email--default.md:9). Invents an objective team-performance assessment absent from the source.
- **Style 2:** [I want to give you a clear update on our launch position.](../../runs/pilot-v11/deepseek--deepseek-v4.1-flash--launch-delay-email--default.md:5). Throat clearing before the actual date update.

## Coverage and operational limits

Fable 5.1 has two completed drafts. DeepSeek Flash has three. Their incomplete eight-brief samples are not compared as full model totals. A cooled Fable retry completed the house email, then the next default email returned 429. DeepSeek launch-house timed out twice at 90 seconds. No missing output receives a zero quality score.

Fable 5 and 5.1 lack ZDR support in the catalog. The runner declares their non-ZDR exception for these synthetic tasks. This changes data-retention routing, not prompts, reasoning effort, output limits or grading criteria. The rejected initial ZDR request and failed attempts remain in the budget ledger.

[Complete eight-brief samples and earlier evidence](../assistant-v3/REPORT.md). [All current decisions](grades.json). Run `python3 scripts/coverage.py` for current generation coverage without quality inference.
