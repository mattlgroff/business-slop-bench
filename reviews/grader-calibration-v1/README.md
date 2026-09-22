# Grader calibration packet

Ten full-context cases selected from previously reviewed drafts. The packet removes model metadata, verdicts, reviewer explanations and source-file paths. A reviewer may still recognize a model from its writing. The creator has seen the originals, so this is not independent blind validation.

## Use

1. Give the reviewer only [packet.json](packet.json) and the linked style guide. Do not include the answer key, build script, leaderboard or conversation history.
2. Copy [response-template.json](response-template.json) to a new response file. Judge only the displayed criterion. Use `pass`, `fail` or `review`; explain ambiguity rather than forcing a binary answer.
3. Quote evidence exactly. For an omission, cite the closest relevant passage and explain what is absent after reading the complete draft.
4. Preserve the submitted responses before opening [answer-key.json](answer-key.json).
5. Examine disagreements on their merits. The prior assistant verdict is a proposed label, not the final authority. Record accepted corrections separately; do not silently overwrite these artifacts or past model scores.

The cases cover proposed signing authority, ambiguous signatory wording, unsupported procurement timing, permitted factual contrasts, sample-adequacy claims, explicit versus omitted arithmetic, vague team reassurance, authoring residue and contradictory randomization statements.

The packet has three proposed passes, five failures and two unresolved cases. Selection was deliberate, based on known grading boundaries. Agreement on these cases cannot estimate general judge accuracy, and the counts should not become a pass gate for a leaderboard. No independent reviewer has submitted labels yet.

`python3 reviews/grader-calibration-v1/build.py` verifies all source-output hashes and exact case membership. Rebuilding is idempotent and refuses changes to existing packet, key or template content. New accepted policy changes require a new packet version. No model calls or primary-score changes are performed.
