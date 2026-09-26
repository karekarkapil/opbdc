# Playbooks: Copper Pot Mixers

*Companion to Chapters 2, 3 and 4 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Illustration: Copper Pot Mixers is a fictional company.*

Last checked: 2026-09-08

## Index
The rungs follow the trust ladder in [`../../../playbooks/trust-ladder.md`](../../../playbooks/trust-ladder.md). The files are the company's own skills folder; only the damaged-shipment playbook is reproduced below.

| Playbook | Job | Trust-ladder rung | Used by | Last checked | File |
|---|---|---|---|---|---|
| Sort the inbox | Sort incoming email into orders, questions and spam | 4 Autonomous within guardrails | Inbox agent | 2026-05-02 | skills/sort-inbox/SKILL.md |
| Routine questions | Answer stock and delivery questions from the facts sheet; apply the capped goodwill credit for our own mistakes | 3 Act and report | Support agent | 2026-08-19 | skills/routine-questions/SKILL.md |
| Damaged shipment | Collect photo and details, prepare the replacement order for approval, hand to Meera | 1 Draft | Support agent, Meera | 2026-07-10 | skills/damaged-shipment/SKILL.md |
| Onboard a new bar | Tasting kit, account setup, welcome call notes | 1 Draft | Sales agent, Meera | 2026-04-10 | skills/onboard-bar/SKILL.md |
| Proposal for a multi-outlet account | Draft proposal from facts sheet and chat transcript | 2 Act with approval | Sales agent | 2026-08-31 | skills/proposal-multi-outlet/SKILL.md |
| Supplier reorder | Prepare purchase orders for bottles, labels and fruit; Meera pays | 2 Act with approval | Purchasing agent | 2026-07-01 | skills/supplier-reorder/SKILL.md |
| Packing and dispatch | Pack each area's orders for its delivery day; wrap and label | 0 Manual (done by the part-time packer) | Packer (a person) | 2026-06-12 | skills/packing-dispatch/SKILL.md |
| Invoices and reminders | Send the invoice at dispatch; one polite reminder once an invoice is overdue (unpaid 48 hours after delivery) | 3 Act and report (reminders to the top ten accounts: 2) | Finance agent | 2026-06-20 | skills/invoices-reminders/SKILL.md |
| Monthly close | Collect, categorize, match, reconcile, flag, draft summary | Agent prepares, Meera signs off | Finance agent | 2026-09-02 | skills/monthly-close/SKILL.md |
| Social posts | Draft posts from the pillar piece for Meera to finish | 1 Draft (rung 2 after thirty drafts in a row approved unchanged; decision D-10) | Marketing agent | 2026-09-08 | skills/social-posts/SKILL.md |
| Newsletter | Draft the monthly newsletter | 1 Draft | Marketing agent | 2026-05-12 | skills/newsletter/SKILL.md |
| Bar research | Find bars that opened in an area, with evidence | 1 Draft | Research agent | 2026-04-15 | skills/bar-research/SKILL.md |
| Wholesale prices | Decide price changes | 0 Manual | Meera | 2026-07-01 | skills/wholesale-prices/SKILL.md |

---

## Example playbook: Damaged shipment

Last checked: 2026-07-10
Owner: Meera
Trust-ladder rung: 1 Draft (the agent collects and prepares; Meera signs every substantive reply and approves every replacement)

### Goal
Replace damaged bottles quickly and keep the customer's trust. A broken case on a Friday costs a bar its drinks for the weekend.

### When to use
- Trigger: a customer reports broken, cracked, leaking or crushed bottles.
- Not for: a customer who dislikes a flavor (exchange rule in the facts sheet) or a late delivery (routine questions playbook).

### Read first
- Facts sheet: "Returns, refunds and problems" and the delivery schedule.
- The customer's last three orders.

### Steps
1. Send only a holding acknowledgement, at once: say you are the AI assistant, that you are sorry, and that Meera will reply the same working day. Do not promise a replacement, a day or a credit.
2. Ask for a photo of the damage and the box, if not already sent.
3. Check whether the report is within 48 hours of delivery. If not, still prepare the case for Meera; do not refuse.
4. Prepare a replacement order for the damaged bottles on the area's next delivery day, marked "replacement, no charge", and hold it for Meera's approval.
5. Hand over to Meera with the handover format from the agent instructions.
6. Meera approves or changes the replacement order and sends the reply herself.
7. Log the case in the damage tracker with the delivery partner, date and photo.

### What good looks like
Customer hears back within ten minutes with a holding acknowledgement; Meera's reply and the replacement confirmed the same working day; no customer is asked twice for a photo.

### Checks before handing back
- [ ] Photo attached, order number matched.
- [ ] Replacement quantities equal the damaged bottles, not the whole order (unless Meera says so).
- [ ] Delivery day taken from the schedule.
- [ ] The only message sent to the customer is the holding acknowledgement.

### Escalate when
- Always: every damaged-product case goes to Meera.
- At once, marked urgent: glass in a drink, an injury, or any mention of a lawyer, a regulator or a food-safety complaint.

### Limits
- May: read orders, send the holding acknowledgement, create a draft replacement order.
- May not: send the substantive reply, promise or approve a replacement, offer a refund or discount, or apply a goodwill credit (damage in transit is Meera's decision, not an our-mistake credit).
