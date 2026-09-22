# Decision Memo: Year-One Vendor Selection

**To:** CFO
**From:** Procurement (Priya)
**Subject:** Vendor selection — Alpha vs. Beta

## Options
| Vendor | Subscription | Setup | Year-One Total | SSO |
|---|---|---|---|---|
| Alpha | $72,000 | $20,000 | $92,000 | Available |
| Beta | $60,000 | $10,000 | $70,000 | Unavailable, no committed delivery date |

## Constraint Evaluation
- **Budget ($100,000 incl. setup):** Both vendors are under budget. Alpha leaves $8,000 headroom; Beta leaves $30,000.
- **SSO (mandatory before production):** Alpha meets it. Beta does not, and has no committed delivery date.
- **Other requirements:** Both vendors meet all other stated requirements.

## Analysis
Beta is $22,000 cheaper in year one, but SSO is a mandatory gate before production and Beta cannot satisfy it. With no committed delivery date, Beta's timeline is unbounded, creating risk that production launch is blocked indefinitely regardless of cost savings.

Alpha is fully compliant today: SSO is available, and the $92,000 total fits within the $100,000 ceiling with $8,000 of headroom. Its higher cost is offset by immediate go-live capability.

## Recommendation
**Select Alpha for year one.** It is the only vendor that satisfies the mandatory SSO constraint before production, and its total year-one cost of $92,000 is within budget.

**Contingency:** If Beta commits to an SSO delivery date that supports production launch, revisit in year two, where Beta's lower subscription ($60,000 vs. $72,000) could yield savings without setup recurrence.

**Approval:** CFO sign-off required before Priya executes the contract.