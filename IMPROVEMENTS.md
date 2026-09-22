# Grader improvement log

## Unsupported assurances and evidence, v6

The grounding judge now distinguishes supported statements, unsupported statements and unresolved interpretations. A second typed question selects an original paragraph as evidence. The code verifies that the paragraph exists at its recorded offset and line. A failure requires both an unsupported judgment and a real passage; disagreements remain unresolved. A real quotation establishes location, not the truth of the allegation.

The frozen comparison covers eight development snippets, 20 separate validation snippets and the four saved drafts, each judged twice. It includes source-authorized staffing holds, authorized dates, and an approved conditional fee credit, so strong commitments can pass when the source supports them. Ordinary requests and proposals also pass. Labels are author-proposed, not human gold.

| Approach | Development matches | Validation matches | Existing drafts | False accepts across all decisions |
|---|---:|---:|---:|---:|
| Previous Boolean grounding | 12/16 | 40/40 | 4/8 | 4 |
| Choice plus original passage | 15/16 | 40/40 | 6/8 | 0 |

The remaining three revised judgments were unresolved, including both repeats of Opus's staffing-pressure sentence. The status judgment and selected passage did not support a definitive failure consistently. This ambiguity is preserved, not forced into the expected label.

The integrated v6 regrade finds:

- Qwen default: unsupported prior-discussion claim, original paragraph P3, line 5.
- Qwen house: grounding passes; the independently validated missing security prerequisite still fails.
- Opus default: unsupported blanket cost assurance, paragraph P5, line 9.
- Opus house: unresolved staffing-pressure wording, paragraph P7, line 13. Its deterministic word-count failure remains.

Links: [fixtures](data/grounding-judge-study.json), [study report](runs/grounding-judge-study-v1/REPORT.md), [updated scores](runs/pilot-v6/REPORT.md). Grounding score JSON files now contain verified paragraph anchors; the report's older generic footnote about semantic flags without anchors applies to the other semantic checks.

Nine tests and TypeScript checking pass. The same four writer outputs were reused, with input hashes verified and import provenance retained. No new generation was purchased. Jev reported zero new billed charges in this pass. Conservative cumulative accounting is approximately $1.9509 of $20. Broader criterion validation and the full model run remain unfinished; the goal remains active.

## Security prerequisite, v5

The v4 grader incorrectly accepted Qwen's house-style email as explicitly requiring security approval before data access. Its text only promised to submit an access request after the client replied. That is a missing condition, even though the source pack contains the condition.

The v5 requirement judge receives the deliverable alone and distinguishes `met`, `missing`, and `contradicted`. It accepts equivalent wording and conditions spread across sentences. A request for approval does not count as granted approval, and a contradictory permission overrides a correct sentence elsewhere. The other Boolean checks retain the original v4 operating thresholds during this regrading comparison.

### Evidence

The frozen study contains eight development snippets, 16 separate validation snippets, and the four existing model drafts. Each was judged twice by three approaches. These are author-proposed diagnostic labels, not human-validated gold. Repeats are not additional independent examples.

| Approach | Development exact matches | Validation exact matches | Existing drafts | False accepts across all decisions |
|---|---:|---:|---:|---:|
| Original Boolean with source pack | 14/16 | 27/32 | 6/8 | 6 |
| Narrow Boolean, draft only | 14/16 | 32/32 | 8/8 | 0 |
| Explicit choice, draft only | 16/16 | 31/32 | 8/8 | 0 |

The choice discrepancy was `missing` versus `contradicted`, both failures. All choice pass/fail decisions matched the proposed labels in this study. That does not establish general judging accuracy, and only this requirement has been changed.

- [Frozen fixtures](data/security-judge-study.json)
- [Study report](runs/security-judge-study-v1/REPORT.md)
- [Raw judgments](runs/security-judge-study-v1/rows.json)
- [Updated four-draft report](runs/pilot-v5/REPORT.md)

The original four drafts were reused only after verifying their saved input hashes match current writer prompts and settings. No new writer generation was purchased. Source generation IDs and original protocol hashes are preserved; copied outputs are marked `importedFrom` and must not be counted as additional spending or independent samples.

Qwen's house-style security grade changed from **pass** to **missing**, with the live choice response assigning 0.99 to missing. Its content-ready result is now false. The other three drafts passed this specific requirement. Broader content/style results remain provisional.

### Running and boundaries

`npx tsx src/judge-study.ts` resumes the frozen comparison and reuses existing responses. Explicit bounded retries have their own budget entries and preserve safe request identifiers and retry headers. SDK retries remain disabled.

`npm run bench -- regrade-v4` regrades the four saved drafts with v5. It marks the inherited Boolean calibration as insufficient for a full v5 pilot, so widening the run remains gated until broader validation is performed. Do not claim that every other criterion was validated by the security study.

Seven focused tests and TypeScript checking pass. Successful Jev calls in this improvement pass reported zero billed cost under the observed promotion. Conservative accounting across all work is about $1.9463 of the $20 ceiling, including old failed-call reservations. The goal remains active: other missing prerequisites, unsupported assurances, style interpretation and judge consistency still need evaluation before a broad model ranking is justified.
