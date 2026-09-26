# Facts sheet (template)

*Companion to Chapter 3, "Context Is the Company", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

The single source of truth for everything an agent might state to a customer: prices, pack sizes, ingredients or features, delivery areas and times, payment terms, return rules, contact details. If an agent tells a customer something factual, it must come from here. When a fact changes, it changes here first.

## How to use it

- Every customer-facing agent's instructions say: "Answer factual questions only from the facts sheet. If it is not there, say so and offer a person."
- Write each fact **once**. The voice guide, playbooks and marketing drafts point here; they do not repeat the number.
- Give every section a "Last checked" date. Prices and delivery rules go stale fastest.
- Change a fact here **before** you announce it anywhere else.
- Review monthly, line by line.

See filled-in versions: [beverage company](examples/beverage-company/facts-sheet.md), [software company](examples/software-company/facts-sheet.md).

---

## Template

```markdown
# Facts sheet: [Company name]

Last checked: [YYYY-MM-DD]
Rule for agents: state only what is written here. If a fact is missing, say "I don't know, let me find out" and escalate.

## Products or plans
| Name | What it is | Size / limits | Price | Notes |
|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] |

## What each product contains or does
- [Product]: [ingredients / features / what is included]. [Allergens, compatibility or requirements.]

## What we do not claim
- [Claims agents must never make, e.g. health benefits, guaranteed results, tax advice.]

## Ordering
- Minimum order: [ ]
- How to order: [website, message, email]
- Order cut-off: [day and time, and what happens after]
- Cancelling or changing an order: [window and method]

## Delivery or access
- Where we deliver / where the service is available: [ ]
- When: [days, times]
- How long it takes: [ ]
- Charges: [ ]
- When we do not deliver, and why: [ ]

## Payment
- Methods: [ ]
- Terms: [when payment is due; what counts as overdue]
- Invoices: [how and when they are sent]

## Returns, refunds and problems
- Damaged or faulty: [what to do, time limit, evidence needed]
- Returns: [conditions]
- Refunds and credits: [who approves; agents never promise one beyond this rule]

## Offers and discounts
- Current published offers: [offer, dates] (or "none")
- Rule: agents never offer discounts beyond a published offer.

## Contact
- Email: [ ]
- Phone or messaging: [ ]
- Hours a person responds: [ ]
- How to reach the founder: [ ]

## Change history
| Date | What changed | Old value | New value |
|---|---|---|---|
| [YYYY-MM-DD] | [ ] | [ ] | [ ] |
```

---

## Guidance notes

- **Write numbers with their units and conditions.** "Rs 150 delivery, free for two cases or more" is a fact. "Low delivery charge" is marketing.
- **Include the edge cases customers actually ask about.** The questions in your last twenty support conversations tell you what belongs here.
- **Keep the change history.** When a customer quotes an old price, you and your agents can see when it changed.
- **No internal-only facts.** Supplier costs, margins and bank details do not belong in a file customer-facing agents read.

## Where this breaks

- **Stale prices.** A facts sheet with last quarter's prices is worse than none, because agents quote it with confidence.
- **The same fact in three places.** It will soon be different in each, and agents will quote whichever they read last.
- **Silent gaps.** If a common question has no answer here, agents will guess. Add the answer, or add "we do not do this".
