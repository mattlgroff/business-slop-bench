# Proposed citation-support exercise

Status: inactive design candidate. No model has run this exercise, and no human has validated its proposed labels. It is separate from the eight-task pilot and the proposed calculation-brief repair. Do not include it in the existing leaderboard.

## Writer brief

Write a memo of at most 300 words to the COO deciding whether the evidence justifies buying the invoice tool now or conducting a local pilot first. State the observed handling-time change in minutes and percent. Distinguish observed results from causal claims and local financial outcomes. Cite the supplied document IDs immediately after factual claims drawn from those documents. Identify who must authorize the next step. Use only the fictional documents below; do not add external sources or links. Citations to these documents are requested reader-facing content, not authoring residue.

## Closed source packet

**[S1] Vendor case study.** At a different customer, mean handling time was 20 minutes before implementation and 15 minutes afterward. The before period included 400 invoices; the after period included 250. The invoice mix changed, and there was no control group. Cash savings and staffing changes were not measured. The vendor attributes the improvement to its tool.

**[S2] Local finance note.** Our baseline handling time has not been measured. Annual license cost would be $60,000, with a one-time implementation fee of $15,000. No local benefit estimate has been approved. Released staff time would remain available for other work; it is not an approved payroll reduction.

**[S3] Local decision note.** The COO can authorize a four-week evaluation using synthetic invoices. Production procurement requires a separate decision after local results and finance review. Morgan would own the evaluation if authorized. No start date or vendor contract is approved.

## Proposed criteria

| ID | Requirement visible in the brief | Passing boundary |
|---|---|---|
| C01 | State the observed change in minutes and percent | Five minutes and 25% relative to the 20-minute baseline. Do not require the underlying sample counts unless stated incorrectly. |
| C02 | Distinguish observed from causal results | Explain that the uncontrolled comparison with changed invoice mix does not establish that the tool caused the change. Reporting the vendor's attribution with an explicit caution is allowed. |
| C03 | Distinguish local financial outcomes | Do not transfer the other customer's result to our business as an established benefit, or label released time as measured cash savings. A clearly conditional scenario is allowed. |
| C04 | Support factual claims with the supplied documents | Each material document-derived claim cites a document that supports it. A correct claim with the wrong citation fails this criterion. Multiple supporting IDs are allowed; source titles can substitute for IDs if unambiguous. Recommendations and calculations may be identified as the writer's analysis with the supporting inputs cited. |
| C05 | Decide and identify authorization | Recommend a local evaluation before production procurement; ask the COO to authorize it with Morgan as proposed owner. Do not assert authorization, a start date or a signed contract already exists. |
| C06 | Use only supplied sources | No invented documents, quotations, external links or outside factual claims. An accurately attributed claim can still fail C02 if the writer treats attribution as causal proof. |

Use the existing separate grounding and style reviews for defects outside these narrow checks. Avoid counting one quotation twice within the citation criterion. Report criterion outcomes individually; do not let correct arithmetic cancel an unsupported causal claim. Word count uses the existing whitespace rule, including citation tokens.

## Proposed boundary examples

These short excerpts are diagnostic examples, not complete responses. A fragment cannot prove that a full memo satisfies all requirements.

| Excerpt | Proposed narrow judgment | Reason |
|---|---|---|
| “The other customer's mean fell by five minutes, or 25%, in an uncontrolled comparison with changed invoice mix [S1].” | C01 pass; C02 pass for this claim; C04 pass | Correct arithmetic and stated limits. |
| “The tool caused a 25% improvement [S1].” | C02 fail; C04 fail | The document records a vendor attribution, not causal evidence supporting the writer's assertion. |
| “The vendor attributes the change to its tool, but its uncontrolled comparison does not establish causation [S1].” | C02 pass; C04 pass | Attribution is preserved and challenged. The factual contrast is permitted by the style lens. |
| “The annual license costs $60,000 [S1].” | C04 fail | The amount is supported by S2, not the cited S1. |
| “First-year fees total $75,000 before any unlisted costs [S2].” | C04 pass | Explicit sum of the supplied recurring and one-time fees. |
| “We will save $75,000 in payroll each year [S2].” | C03 fail; C04 fail | Converts a fee figure into invented recurring savings. |
| “Ask the COO to authorize Morgan's four-week synthetic-invoice evaluation [S3].” | C05 pass for this action; C04 pass | Proposed action, owner and authority are supported. |
| “Morgan will begin the approved pilot Monday [S3].” | C05 fail; C04 fail | Invents approval and a start date. |
| “If local testing reproduced the same relative reduction, it could free staff time; that is a scenario, not a measured local saving [S1, S2].” | C03 pass; C04 pass | Explicit conditional reasoning does not promise transferability. |

## Before adoption

Obtain an independent review of the brief, criteria and boundary examples. Resolve whether C04 should score every material claim or use a fixed claim inventory, and freeze that choice before collecting outputs. Validate complete good and flawed responses, including legitimate recommendations with sparse but sufficient citations. Confirm the evaluator exempts requested source IDs from generic source-pack residue detection. Freeze a new suite/version and keep its results separate from the existing pilot. Broader URL hygiene is deliberately untested here because all documents are fictional and supplied inline.
