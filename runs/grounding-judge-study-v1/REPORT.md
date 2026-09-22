# Grounding judge comparison

Author-proposed labels, not human gold. Each example was judged twice; repeated decisions are not independent examples. Both methods saw the same facts and draft. No writing model calls were made.

| Method | Split | Matches | False accepts | False rejects | Unresolved |
|---|---|---:|---:|---:|---:|
| baseline | development | 12/16 | 2 | 0 | 2 |
| baseline | validation | 40/40 | 0 | 0 | 0 |
| baseline | observed-draft | 4/8 | 2 | 0 | 2 |
| revised | development | 15/16 | 0 | 0 | 1 |
| revised | validation | 40/40 | 0 | 0 | 0 |
| revised | observed-draft | 6/8 | 0 | 0 | 2 |

The revised method distinguishes grounded/unsupported/unclear and selects an exact original paragraph as evidence. Status/evidence disagreement remains unresolved. A matching passage proves the quotation exists, not that the semantic allegation is correct.
