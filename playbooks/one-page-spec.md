# The one-page spec

*Companion to Chapter 6, "The Spec Is the Product", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

When agents build from your words, the specification is the source code: what they build from, what they test against, what you review against, and what future agents read before they change the product. For a one-person company the right length is one page per feature, sometimes two. It has nine parts. The **no list** matters most.

This file holds the template, the reorder example from Chapter 6 in full, and two more: a software feature and a service.

## How to use it

1. Copy the template into your [specifications](../context-kit/specifications.md) file, one spec per feature.
2. Make the no list at least as long as the must-haves.
3. Write at least four acceptance tests in the given, when, then form, including one for an error or edge case.
4. Hand the spec to a coding agent as its brief (Chapter 7): tests first, then the feature.
5. Update the spec in the same change as the product, so it never drifts.

---

## Template

```
# Feature: [name]
Last updated: [YYYY-MM-DD]

**Problem:** [Two or three sentences, with at least one verbatim customer quote from the customer file.]

**For:** [The specific customer, and the situation they are in when they use it.]

**Job:** "[What the customer is trying to get done, in their words.]"

**Must-haves:** [The smallest set of capabilities that does the job. Every item traces back to the problem.]

**No list:** [What this feature will deliberately not do, and why. One reason per item.]

**Acceptance tests:**
- *Given* [a situation], *when* [the customer does something], *then* [this happens].
- *Given* ..., *when* ..., *then* ...
- *Given* [an error or edge case] ..., *then* ...

**Data:** [What it reads, where that comes from, what it creates or changes, and what it must never touch.]

**Risks and questions:** [What could go wrong, and what we do not know yet. How we will find out.]

**Worked if:** [One or two measures, and the date to check them.]
```

---

## Example 1: a physical-product business

*Copper Pot Mixers is a fictional company used for illustration. This is the example from Chapter 6, written to show the form, not to describe a real product.*

> **Feature: Reorder in one tap**
>
> **Problem:** Bar managers reorder the same mixers every week or two, usually late at night after closing, from their phones. Today they must message us, and we must reply the next morning. From the customer file: "By the time you answer, I've forgotten what I asked for."
>
> **For:** A bar manager or owner with an existing account, on a phone, at the end of a shift.
>
> **Job:** "Send me the same as last time, maybe a bit more of the pineapple."
>
> **Must-haves:** Show the last three orders. Repeat any of them with one tap. Adjust quantities before confirming. Confirm the delivery day from the facts sheet's delivery schedule.
>
> **No list:** No new products in this flow (discovery belongs elsewhere). No discounts or promotions (they complicate the confirmation). No credit or payment changes (payment terms stay as agreed on the account). No ordering for a different outlet (multi-outlet accounts come later, if at all).
>
> **Acceptance tests:**
> - *Given* a manager with two past orders, *when* they open the page, *then* both appear, newest first, with dates and totals.
> - *Given* a past order, *when* they tap "Repeat", change one quantity and confirm, *then* a new order is created with the changed quantity, and they see the delivery day.
> - *Given* an order placed after the weekly cut-off, *then* the delivery day shown is the following week's, and the page says why.
> - *Given* a product that has been discontinued, *then* it is shown as unavailable and left out of the repeat, with a note.
>
> **Data:** Reads the account's order history and the product list. Creates orders. Never changes prices, payment terms or account details.
>
> **Risks and questions:** Will managers accidentally repeat an order twice? (Add a confirmation step and a thirty-minute cancel window.) Do owners want managers ordering without approval? Ask three owners.
>
> **Worked if:** Within six weeks, half of repeat orders come through this page, and the average time from a manager's request to our confirmation falls from about ten hours to under a minute.

Notice that the no list is longer than the must-haves. That is usually a good sign.

---

## Example 2: a software business

*Ledgerly is a fictional bookkeeping-software company used for illustration.*

> **Feature: Match a receipt from your phone**
>
> **Problem:** Owners of small businesses keep paper receipts in a pocket or a drawer and match them to bank lines weeks later, usually at night. Unmatched receipts pile up and the month cannot close. From the customer file: "I spend every Sunday night matching receipts to bank lines."
>
> **For:** A Ledgerly user on the Starter or Plus plan, on a phone, just after paying for something.
>
> **Job:** "Take a picture of this and put it with the right payment, so I can throw the paper away."
>
> **Must-haves:** Take a photo of a receipt in the app. Read the date, amount and merchant from it. Suggest the most likely unmatched bank line. Match with one tap, or pick another line. Keep the photo attached to the transaction.
>
> **No list:** No categorizing in this flow (categorization rules run separately, so there is one place to fix them). No editing of bank lines (bank data is never changed by hand). No expense claims or reimbursements (a different job, later if at all). No receipts by email in this version (the photo flow first; email forwarding is on the backlog). No matching to a bank line in a different company in the same login (companies stay separate).
>
> **Acceptance tests:**
> - *Given* an unmatched bank line of $42.18 at a stationery shop yesterday, *when* the user photographs a receipt for $42.18 from that shop, *then* that line is suggested first and one tap matches it.
> - *Given* two unmatched lines with the same amount, *when* the user photographs a receipt, *then* both are shown with dates and merchants, and nothing is matched until the user chooses.
> - *Given* a receipt with no bank line yet (the payment has not cleared), *then* the receipt is saved as "waiting", and matched suggestions appear when the line arrives.
> - *Given* a blurry photo where the amount cannot be read, *then* the app says so plainly and offers to type the amount, without guessing.
>
> **Data:** Reads the user's unmatched bank lines for the selected company. Stores the photo and the match. Never changes bank lines, categories or another company's data. Photos are stored with the transaction and deleted with it.
>
> **Risks and questions:** Will reading the amount from photos be accurate enough on crumpled receipts? (Test on 50 real receipts from three users before release.) Do bookkeepers want clients matching, or only uploading? Ask five bookkeepers.
>
> **Worked if:** By the end of the next quarter, 40 percent of receipts on active accounts are matched within a day of payment, and support messages about "unmatched items at month end" fall by half.

---

## Example 3: a service business

*Ledgerly Assist is a fictional done-for-you monthly close service used for illustration. It follows Chapter 6's "Specs Beyond Software": what the customer sends, what they receive, by when, what counts as done, what we never do, and what happens when something is missing.*

> **Service: Ledgerly Assist, the done-for-you monthly close**
>
> **Problem:** Small business owners know they should close their books every month and rarely do. Months pile up, and the accountant's year-end bill grows. From the customer file: "I don't trust a number I can't trace back to the bank."
>
> **For:** A micro business (one to ten staff) using Ledgerly, whose owner wants reliable monthly numbers and has no bookkeeper.
>
> **Job:** "Close my month properly and tell me, in plain words, how the business did."
>
> **Must-haves:**
> - *The customer sends:* access to Ledgerly with the bank feed connected, receipts uploaded by the 3rd working day of the new month, and answers to our questions within two working days.
> - *The customer receives:* a closed month (every transaction categorized and matched, books reconciled to the bank balance), a list of items that need their decision, and a one-page summary: revenue, costs, profit or loss, cash, who owes them what.
> - *By when:* the 10th working day of the new month.
> - *Done means:* reconciled to the bank to the cent, every flag either decided by the customer or listed as open, summary sent, checked and signed off by a qualified bookkeeper (the founder).
>
> **No list:** We never file taxes or returns on the customer's behalf, and never without their signature. We never pay bills or move the customer's money. We never give tax advice (we refer to their accountant). We never change prior closed months without the customer's written approval. We never contact the customer's customers or suppliers. No payroll in this service.
>
> **When something is missing:** a receipt missing by the 3rd working day is listed as "unmatched, receipt missing" in the summary, not guessed; a transaction we cannot categorize is flagged with our best suggestion and left for the customer; if bank access fails, we tell the customer the same day and the delivery date moves by the delay.
>
> **Acceptance tests** (sample months with known right answers, the golden set from Chapter 4):
> - *Given* a sample month with 120 transactions and a known closing balance, *when* the close runs, *then* the books reconcile to that balance to the cent.
> - *Given* a month containing one duplicate supplier charge, *then* it is flagged as a possible duplicate, not coded twice.
> - *Given* an email asking to change a supplier's bank details, *then* nothing is changed and the item is flagged for verification by a second channel.
> - *Given* a missing receipt, *then* it appears in the summary as missing and the close is still delivered on time.
>
> **Data:** Reads the customer's Ledgerly company, bank feed and receipts. Writes categories, matches and the summary. Never touches payment functions, other customers' companies or prior closed months.
>
> **Risks and questions:** Can one bookkeeper check 30 closes a month properly? (Measure the checking time per close for the first ten customers.) Will customers answer questions within two working days? If not, how does that change the delivery date?
>
> **Worked if:** After three months, 90 percent of closes are delivered by the 10th working day, the golden set passes every month, and at least eight of the first ten customers renew.

See the [finance golden set](golden-sets/finance.md) for sample cases.

---

## The backlog, and one rule

Keep the backlog (the list of things you might build) with evidence attached to every item. Weigh each candidate on three questions:

| Candidate | Impact (who, how much, per the evidence) | Confidence (conversations and data, not enthusiasm) | Total cost to own (testing, support, complexity, context, review) | Evidence (quotes, measures) |
|---|---|---|---|---|
| [Feature] | [High / Medium / Low] | [High / Medium / Low] | [High / Medium / Low] | [link to customer file entries] |

Items with no evidence sink to the bottom. Delete them after a quarter.

**The rule:** for every feature you add, consider one you could remove. Complexity is the tax you pay forever.

## Related files

- [Specifications template](../context-kit/specifications.md)
- [Validation scorecard](validation-scorecard.md)
- [Ship checklist](ship-checklist.md)
