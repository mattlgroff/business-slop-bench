# Anti-slop judge comparison

Author-proposed labels, not human gold. Each example was judged twice; repeated decisions are not independent examples. Both methods saw the same audience context and draft. Actual model drafts are diagnostic only and have no preassigned expected labels. No writing model calls were made.

| Method | Split | Matches | False accepts | False rejects | Unresolved |
|---|---|---:|---:|---:|---:|
| baseline | category-controls | 114/116 | 0 | 0 | 2 |
| baseline | transfer | 24/24 | 0 | 0 | 0 |
| baseline | observed-draft | 0/32 | 0 | 0 | 3 |
| revised | category-controls | 116/116 | 0 | 0 | 0 |
| revised | transfer | 24/24 | 0 | 0 | 0 |
| revised | observed-draft | 0/32 | 0 | 0 | 8 |

The revised method distinguishes clean/defect/unclear and selects an exact original paragraph as evidence. Status/evidence disagreement remains unresolved. A matching passage proves the quotation exists, not that the semantic allegation is correct.
