# Uncapped ranking with prices

Source: reviews/assistant-v41/summary.json and runs/pilot-v23/catalog.json. Content checks are out of 54 per condition; unresolved checks earn no credit. Prices are Gateway list rates per million tokens (base tier; regional and fast tiers cost more). Observed cost is the reported charge for the eight successful drafts in that condition. One generation per cell, graded unblinded by the assistant. Disqualified models are listed last and never pooled. A $0 observed cost means the Gateway reported a zero charge at launch; the list price still applies once promotional pricing ends.

| Rank | Model | Input $/M | Output $/M | Default checks | Default ready / no-edit | Default cost | House checks | House ready / no-edit | House cost |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Astra | 10.00 | 50.00 | 54/54 | 8/8 / 4/8 | $0.1120 | 54/54 | 8/8 / 8/8 | $0.3581 |
| 2 | Sol 5.6 | 4.00 | 20.00 | 52/54 | 6/8 / 0/8 | $0.0601 | 53/54 | 7/8 / 4/8 | $0.1903 |
| 3 | Terra | 2.00 | 12.00 | 52/54 | 6/8 / 3/8 | $0.0278 | 52/54 | 6/8 / 3/8 | $0.0780 |
| 4 | Luna | 0.20 | 1.20 | 51/54 | 5/8 / 2/8 | $0.0031 | 52/54 | 6/8 / 4/8 | $0.0081 |
| 5 | Qwen Max | 2.00 | 6.00 | 49/54 | 3/8 / 1/8 | $0.0269 | 52/54 | 4/8 / 3/8 | $0.0866 |
| 6 | Opus 5.5 | 4.00 | 20.00 | 52/54 | 4/8 / 2/8 | $0.1171 | 51/54 | 3/8 / 3/8 | $0.2533 |
| 7 | DeepSeek Pro | 0.66 | 1.98 | 51/54 | 3/8 / 1/8 | $0.0090 | 51/54 | 4/8 / 2/8 | $0.0374 |
| 8 | Gemini Pro | 2.00 | 12.00 | 49/54 | 3/8 / 1/8 | $0.0960 | 51/54 | 5/8 / 5/8 | $0.1492 |
| 9 | Grok | 1.20 | 3.60 | 52/54 | 6/8 / 3/8 | $0.0182 | 50/54 | 4/8 / 2/8 | $0.0540 |
| 10 | DeepSeek Flash | 0.30 | 1.20 | 52/54 | 5/8 / 0/8 | $0.0029 | 50/54 | 3/8 / 0/8 | $0.0084 |
| 11 | Gemini Flash | 0.75 | 3.75 | 51/54 | 5/8 / 0/8 | $0.0187 | 50/54 | 4/8 / 3/8 | $0.0242 |
| 12 | Kimi K3 | 3.00 | 15.00 | 51/54 | 4/8 / 0/8 | $0.0566 | 50/54 | 3/8 / 2/8 | $0.1180 |
| 13 | GLM 5.3 | 1.40 | 4.40 | 52/54 | 4/8 / 1/8 | $0.0149 | 49/54 | 3/8 / 2/8 | $0.0426 |
| 14 | Opus 5 | 5.00 | 25.00 | 49/54 | 1/8 / 0/8 | $0.1481 | 49/54 | 3/8 / 3/8 | $0.2880 |
| 15 | Opus 4.6 | 5.00 | 25.00 | 49/54 | 2/8 / 0/8 | $0.0760 | 49/54 | 1/8 / 1/8 | $0.1803 |
| 16 | GLM Flash | 0.15 | 0.50 | 49/54 | 4/8 / 1/8 | $0.0019 | 48/54 | 3/8 / 2/8 | $0.0046 |
| 17 | MiniMax | 0.30 | 1.20 | 50/54 | 3/8 / 0/8 | $0.0328 | 44/54 | 0/8 / 0/8 | $0.0322 |
| 18 | Qwen Flash | 0.15 | 0.47 | 46/54 | 0/8 / 0/8 | $0.0038 | 41/54 | 0/8 / 0/8 | $0.0077 |
| - | Muse (non-ZDR, disqualified) | 1.25 | 4.25 | 53/54 | 7/8 / 4/8 | $0.0382 | 53/54 | 7/8 / 5/8 | $0.0572 |
| - | Luna 6 (non-ZDR, disqualified) | 0.10 | 0.50 | 53/54 | 7/8 / 3/8 | $0 (launch promo) | 53/54 | 7/8 / 6/8 | $0 (launch promo) |
| - | Sol 6 (non-ZDR, disqualified) | 2.00 | 10.00 | 52/54 | 6/8 / 3/8 | $0 (launch promo) | 53/54 | 7/8 / 7/8 | $0 (launch promo) |
| - | Fable 5 (non-ZDR, disqualified) | 10.00 | 50.00 | 49/54 | 3/8 / 0/8 | $0.2345 | 51/54 | 4/8 / 4/8 | $0.5413 |
| - | Fable 5.1 (non-ZDR, disqualified) | 10.00 | 50.00 | 51/54 | 4/8 / 0/8 | $0.2380 | 50/54 | 3/8 / 3/8 | $0.5702 |

Ordering: eligible models first, then house content checks, default content checks, ready-without-edits count, content-ready count. Ties remain ties; a few checks of difference is within single-generation variation.

