# Security prerequisite judge study

All methods saw the same frozen drafts. Two judgments per draft; repeats do not increase the independent sample count. Author-proposed labels, not human gold. No generation calls.

| Method | Split | Matching decisions | False accepts | Unresolved |
|---|---|---:|---:|---:|
| baseline | development | 14/16 | 2 | 0 |
| baseline | validation | 27/32 | 2 | 3 |
| baseline | observed-draft | 6/8 | 2 | 0 |
| draft-only | development | 14/16 | 0 | 2 |
| draft-only | validation | 32/32 | 0 | 0 |
| draft-only | observed-draft | 8/8 | 0 | 0 |
| explicit-choice | development | 16/16 | 0 | 0 |
| explicit-choice | validation | 31/32 | 0 | 0 |
| explicit-choice | observed-draft | 8/8 | 0 | 0 |

The source-pack condition is a baseline. Draft-only Boolean isolates the text being evaluated. Explicit choice distinguishes a missing prerequisite from a contradictory statement. Results cover this requirement only.
