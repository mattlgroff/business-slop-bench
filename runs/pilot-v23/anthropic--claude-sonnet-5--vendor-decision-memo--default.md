# Decision Memo: Vendor Selection – Year One

**To:** CFO
**From:** Priya, Procurement
**Re:** Vendor selection recommendation

## Cost Comparison

| Item | Alpha | Beta |
|---|---|---|
| Annual subscription | $72,000 | $60,000 |
| One-time setup | $20,000 | $10,000 |
| **Year-one total** | **$92,000** | **$70,000** |
| Budget ceiling | $100,000 | $100,000 |
| Headroom remaining | $8,000 | $30,000 |

Both options fit within the $100,000 budget ceiling on cost alone.

## Constraint Check: SSO (Mandatory)

SSO is a mandatory, non-negotiable requirement before any production deployment.

- **Alpha:** SSO is available now. This requirement is satisfied.
- **Beta:** SSO is unavailable, with **no committed delivery date**. This is a hard blocker with unknown resolution timing.

All other stated requirements are met equally by both vendors, so SSO availability is the deciding factor.

## Analysis

Beta is cheaper by $22,000 in year one and leaves more budget headroom. However, cost is irrelevant if the solution cannot go into production. Because SSO is mandatory and Beta has no committed delivery date, Beta carries unacceptable timeline risk — we could sign a contract and still be unable to deploy, with no visibility into when (or if) that changes.

Alpha satisfies the mandatory SSO requirement today and fits within budget ($92,000 of $100,000, leaving $8,000 headroom). This is sufficient to proceed.

## Recommendation

**Select Alpha for year one.**

Rationale:
1. Alpha meets the mandatory SSO requirement now; Beta does not and has no delivery commitment.
2. Alpha's total year-one cost ($92,000) is within the $100,000 ceiling.
3. Beta's lower price does not offset the risk of an indefinite production blocker.

**Next step:** Priya to proceed with Alpha contracting, pending CFO sign-off. Recommend revisiting Beta in future years only if SSO becomes available with a firm date.