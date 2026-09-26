# Playbooks: Ledgerly

*Companion to Chapters 2, 3 and 4 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Illustration: Ledgerly is a fictional company.*

Last checked: 2026-09-10

## Index
Rungs follow the trust ladder in [`../../../playbooks/trust-ladder.md`](../../../playbooks/trust-ladder.md).

| Playbook | Job | Trust-ladder rung | Used by | Last checked | File |
|---|---|---|---|---|---|
| Build from spec | Turn a spec into tests, then code, on its own branch | 2 Act with approval (founder reviews before merge) | Coding agent | 2026-08-14 | skills/build-from-spec/SKILL.md |
| Weekly dependency updates | Propose library updates with test results | 2 Act with approval | Scheduled coding agent | 2026-07-30 | skills/dependency-updates/SKILL.md |
| Morning summary | Read logs, errors, signups and payments; report | 4 Autonomous within guardrails | Operations agent (read only) | 2026-07-21 | skills/morning-summary/SKILL.md |
| Alert investigation | Read logs around an alert, find the recent change, report | 3 Act and report | Operations agent | 2026-07-21 | skills/alert-investigation/SKILL.md |
| Support: how-do-I questions | Answer from help docs and the facts sheet | 3 Act and report | Support agent | 2026-08-30 | skills/support-how-do-i/SKILL.md |
| Support: billing, refunds and tax questions | Prepare the answer (for tax, the fixed reply in decision D-13) and any refund, for approval | 2 Act with approval (back from rung 1 on 2026-09-01; lessons log L-7) | Support agent | 2026-09-01 | skills/support-billing-tax/SKILL.md |
| Assist monthly close | Prepare the client's close and question list | 1 Draft (founder checks and signs) | Finance agent | 2026-09-05 | skills/assist-close/SKILL.md |
| Ledgerly's own monthly close | Collect, categorize, match, reconcile, flag, draft summary | Agent prepares, founder signs off | Finance agent | 2026-09-02 | skills/own-monthly-close/SKILL.md |
| Release notes | Draft from merged changes | 1 Draft | Coding agent | 2026-06-11 | skills/release-notes/SKILL.md |
| Price changes | Decide and announce | 0 Manual | Founder | 2026-07-10 | skills/price-changes/SKILL.md |

---

## Example playbook: Assist monthly close

Last checked: 2026-09-05
Owner: the founder
Trust-ladder rung: 1 Draft (the agent prepares; the founder checks and signs off every close)

### Goal
Deliver a client's reconciled books, a one-page summary and a short list of questions by the 10th working day, with every number traceable to the bank.

### When to use
- Trigger: the 4th working day of the month, for each Assist client whose documents arrived.
- Not for: clients whose documents have not arrived (send the missing-documents reminder instead).

### Read first
- The client's rules and last month's close notes.
- Facts sheet: "Ledgerly Assist".
- The Assist golden set (three sample months with known right answers).

### Steps
1. Confirm the bank feed is complete for the month (no gaps longer than the connection's normal gap).
2. Categorize every transaction using the client's rules; mark any new supplier or unusual amount.
3. Match receipts and invoices to transactions.
4. Reconcile to the closing bank balance, to the cent.
5. List what is missing (receipts, unexplained transactions). Do not guess.
6. Draft the one-page summary and the question list.
7. Hand to the founder with the flags at the top.

### What good looks like
Reconciled to the cent; every flag has a transaction link; the question list is under ten items and written so the client can answer each in one line.

### Checks before handing back
- [ ] Closing balance matches the bank statement.
- [ ] Largest expense and largest payment received linked to their source documents.
- [ ] No transaction categorized by guess without a flag.

### Escalate when
- Anything that looks like a tax question, a legal issue or possible fraud (a changed bank detail, a payment to an unknown account).
- The client asks you to pay, move or approve anything.
- The books cannot be reconciled after two attempts.

### Limits
- May: read the client's bank feed and documents; categorize; draft.
- May not: send anything to the client, change prior closed months, contact the client's bank or suppliers.
