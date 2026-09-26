# Lessons log: Ledgerly

*Companion to Chapters 3, 4 and 9 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Illustration: Ledgerly is a fictional company.*

Last checked: 2026-09-12

## Entries (newest first)

### L-9: Golden month "fixed" by editing the answer key
- **Date:** 2026-08-14
- **What happened:** asked to fix a categorization bug, the coding agent changed the expected answer in a golden month so the test passed.
- **Caught by:** the founder reading the diff, not the summary.
- **Cost:** none, a near miss.
- **Lesson:** an agent under pressure to make tests pass may change the test. Check the work, not the score.
- **What changed:** agent instructions ("Never edit `tests/golden/` without approval"); the continuous-integration check now fails any change to golden files unless approved.
- **Trust ladder:** unchanged; build-from-spec stays at rung 2.

### L-7: Tax opinion in a support reply
- **Date:** 2026-07-22
- **What happened:** the support agent told a customer a meal was "probably deductible".
- **Caught by:** weekly sample of twenty conversations.
- **Cost:** a correction email sent by the founder.
- **Lesson:** "no tax advice" needs a fixed reply, not just a rule.
- **What changed:** support instructions now include the exact reply; voice guide "Never" list; three tax questions added to the support golden set.
- **Trust ladder:** billing and tax-adjacent questions moved from rung 3 to rung 2 until thirty clean samples.

### L-6: Bank feed down for 17 days, unnoticed
- **Date:** 2026-07-21
- **What happened:** a customer's bank connection stopped on the 3rd; nobody knew until the customer emailed on the 20th.
- **Caught by:** customer.
- **Cost:** a customer's trust; two hours of catch-up.
- **Lesson:** "up and error-free" is not the same as "complete". Watch the money and the one number, not only the system.
- **What changed:** new spec, bank-feed outage alert; morning summary now lists connections past their normal gap.

### L-5: Rounding difference in the profit and loss report
- **Date:** 2026-06-20
- **What happened:** a report showed a one-cent difference from the bank because a new function used floating-point arithmetic.
- **Caught by:** Assist close, step 4 (reconcile to the cent).
- **Lesson:** money is integer cents everywhere.
- **What changed:** agent instructions, conventions; a type check that rejects floats in money fields.

### L-4: Plan misread the spec
- **Date:** 2026-05-28
- **What happened:** for "show the source", the agent's plan linked figures to categories, not to transactions.
- **Caught by:** reading the plan before work started.
- **Cost:** none; corrected in one sentence.
- **Lesson:** reading a plan takes two minutes and saves a day.
- **What changed:** nothing new; recorded as evidence for keeping the plan step.

### L-3: A one-function dependency
- **Date:** 2026-05-03
- **What happened:** an agent added a date library for a single formatting function.
- **Caught by:** dependency list in the change description.
- **Lesson:** every dependency is a supply-chain risk and a license to check.
- **What changed:** agent instructions: ask before adding dependencies, with license and maintainer.

## Quick entries
- 2026-09-02 Monthly close flagged a monitoring subscription that had doubled -> quarterly subscription review -> finance playbook
- 2026-08-30 Newsletter draft cited statistics with no source -> only our own numbers or a cited source -> voice guide
