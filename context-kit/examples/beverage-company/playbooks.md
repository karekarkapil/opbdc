# Playbooks: Copper Pot Mixers

*Companion to Chapters 2, 3 and 4 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Illustration: Copper Pot Mixers is a fictional company.*

Last checked: 2026-09-08

## Index
The rungs follow the trust ladder in [`../../../playbooks/trust-ladder.md`](../../../playbooks/trust-ladder.md).

| Playbook | Job | Rung | Used by | Last checked |
|---|---|---|---|---|
| Sort the inbox | Sort incoming email into orders, questions and spam | 4 Autonomous within guardrails | Inbox agent | 2026-05-02 |
| Routine questions | Answer stock and delivery questions from the facts sheet | 3 Act and report | Support agent | 2026-08-19 |
| Damaged shipment | Collect photo and details, prepare the replacement, hand to Meera | 1 Draft | Support agent, Meera | 2026-06-12 |
| Onboard a new bar | Tasting kit, account setup, welcome call notes | 1 Draft | Sales agent, Meera | 2026-04-10 |
| Proposal for a multi-outlet account | Draft proposal from facts sheet and chat transcript | 2 Act with approval | Sales agent | 2026-08-29 |
| Supplier reorder | Prepare purchase orders for bottles, labels and fruit | 2 Act with approval | Ops agent | 2026-07-01 |
| Invoices and reminders | Send invoice at dispatch; polite reminder when 48 hours overdue | 3 Act and report (reminders to top ten accounts: 2) | Finance agent | 2026-06-20 |
| Monthly close | Collect, categorize, match, reconcile, flag, draft summary | Agent prepares, Meera signs off | Finance agent | 2026-09-02 |
| Social posts | Prepare posts from the pillar piece | 2 Act with approval | Marketing agent | 2026-09-08 |
| Newsletter | Draft the monthly newsletter | 1 Draft | Marketing agent | 2026-05-12 |
| Bar research | Find bars that opened in an area, with evidence | 1 Draft | Research agent | 2026-04-15 |
| Wholesale prices | Decide price changes | 0 Manual | Meera | 2026-07-01 |

---

## Example playbook: Damaged shipment

Last checked: 2026-06-12
Owner: Meera
Trust-ladder rung: 1 Draft (the agent prepares; Meera sends every reply)

### Goal
Replace damaged bottles quickly and keep the customer's trust. A broken case on a Friday costs a bar its drinks for the weekend.

### When to use
- Trigger: a customer reports broken, cracked, leaking or crushed bottles.
- Not for: a customer who dislikes a flavor (exchange rule in the facts sheet) or a late delivery (routine questions playbook).

### Read first
- Facts sheet: "Returns, refunds and problems" and the delivery schedule.
- The customer's last three orders.

### Steps
1. Reply at once: say you are the AI assistant, that you are sorry, and that Meera will confirm the replacement today.
2. Ask for a photo of the damage and the box, if not already sent.
3. Check the report is within 48 hours of delivery. If not, still prepare the case for Meera; do not refuse.
4. Prepare a replacement order for the damaged bottles on the next available delivery day, marked "replacement, no charge", and hold it for approval.
5. Hand over to Meera with the summary format from the agent instructions.
6. After Meera approves, confirm the day to the customer.
7. Log the case in the damage tracker with the delivery partner, date and photo.

### What good looks like
Customer hears back within ten minutes; replacement confirmed the same working day; no customer is asked twice for a photo.

### Checks before handing back
- [ ] Photo attached, order number matched.
- [ ] Replacement quantities equal the damaged bottles, not the whole order (unless Meera says so).
- [ ] Delivery day taken from the schedule.

### Escalate when
- Always: every damaged-product case goes to Meera.
- At once, marked urgent: glass in a drink, an injury, or any mention of a lawyer, a regulator or a food-safety complaint.

### Limits
- May: read orders, draft replies, create a draft replacement order.
- May not: send the reply, approve a replacement, offer a refund, credit or discount.
