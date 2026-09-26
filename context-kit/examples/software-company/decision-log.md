# Decision log: Ledgerly

*Companion to Chapters 1, 3 and 15 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Illustration: Ledgerly is a fictional company.*

Last checked: 2026-09-12
Rule for agents: do not reverse a decision logged here. If a task seems to require it, stop and ask.

## Open questions
- Build client import, or sell it as a service? (decide by 2026-10-15; evidence needed: five bookkeeper conversations, cost to serve one import by hand)
- Move support chat from rung 3 to rung 4 for "how do I" questions? (decide at the October review; evidence: thirty consecutive sampled answers approved unchanged)

## Decisions (newest first)

Selected entries shown; the gaps in numbering are entries left out of this example.

### D-13: One fixed reply for every tax question
- **Date:** 2026-07-23
- **Decision:** the support agent answers every tax question with one fixed reply, word for word: "We can't advise on tax. Your accountant can, and Ledgerly can export everything they need." Billing, refund and tax questions drop to rung 1 (the founder sends every reply) until the fixed reply is in place and tested, then climb one rung at a time.
- **Reason:** the rule in D-7 was not enough: on 2026-07-22 the agent still told a customer a meal was "probably deductible" (lessons log L-7). A rule states the boundary; a fixed reply leaves nothing to improvise.
- **Alternatives considered:** a longer rule with examples (rejected: the agent paraphrased around the last one).
- **Revisit if:** customers repeatedly ask a tax-adjacent question the fixed reply does not fit.
- **Status:** active. **Files updated:** support instructions, voice guide "Never" list, support golden set (three tax cases), playbooks index.

### D-12: Bookkeeper plan price rises to $12 per client
- **Date:** 2026-07-10 (effective 2026-08-01, existing customers from 2026-10-01 with 60 days' notice)
- **Decision:** raise the Bookkeeper plan from $10 to $12 per client per month.
- **Reason:** cost to serve per client rose with bank-connection fees; margin per client fell below target in the June close.
- **Alternatives considered:** limiting bank connections per client (rejected: punishes the busiest clients).
- **Revisit if:** bookkeeper churn rises above its usual monthly range for two months.
- **Status:** active. **Files updated:** facts sheet (with change history), pricing page, notice email approved by the founder.

### D-9: Ledgerly Assist launched, capped at 20 clients
- **Date:** 2026-05-15
- **Decision:** offer the done-for-you close at $250/month, capped at 20 clients until checking time is under 45 minutes per client.
- **Reason:** "I don't want another app. I want the month to be done." Six of ten owner conversations asked for this; delivered by hand for three clients for two months first.
- **Revisit if:** checking time per client exceeds an hour for two consecutive months.
- **Status:** active.

### D-7: Support agent never advises on tax
- **Date:** 2026-04-02
- **Decision:** the support agent never gives tax advice or an opinion on tax treatment; it points the customer to their accountant.
- **Reason:** we are not qualified, and a wrong answer creates a liability for the customer and for us.
- **Status:** active; the wording of the reply is fixed by D-13. **Files updated:** support instructions, voice guide.

### D-5: Cash-flow prediction removed
- **Date:** 2026-03-30
- **Decision:** remove the AI cash-flow prediction feature.
- **Reason:** used by 4 percent of active customers; generated a large share of support questions; customers said they did not trust it. The original spec's no list said "no forecasts".
- **Revisit if:** customers ask for forecasting unprompted in at least five discovery calls.
- **Status:** active.

### D-3: Managed services for login, payments and database
- **Date:** 2025-11-20
- **Decision:** use a managed login provider, a hosted checkout and a managed database with automatic backups. Agents never build these from scratch.
- **Reason:** the riskiest parts of a finance product are the ones most dangerous to reinvent; managed services carry the security and backups.
- **Revisit if:** a managed provider cannot meet a data-residency or cost need.
- **Status:** active. **Files updated:** agent instructions.

### D-1: Every number traceable to the bank
- **Date:** 2025-10-05
- **Decision:** every figure in every report links to the transactions behind it.
- **Reason:** "I don't trust a number I can't trace back to the bank." Trust is the product.
- **Status:** active.
