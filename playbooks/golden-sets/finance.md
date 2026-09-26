# Golden set: finance coding

*Companion to Chapters 4 and 13, "Managing Agents" and "The AI CFO", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

A golden set for the finance agent: past transactions and invoices where you (or your accountant) already know the correct category, match and treatment. Confident mistakes with numbers compound quietly for months, so this set is the cheapest protection you have. Run it before you change the finance agent's instructions, rules, model or tools, and once a quarter anyway.

This is not tax or accounting advice. Categories and treatments differ by country and business. Agree the right answers in your set with a qualified accountant.

## How to use it

- **How many:** start with five to ten items. Include at least three invoices and their correct coding, one duplicate, one refund and one item that must be flagged rather than coded.
- **Sources:** real past transactions from your books, with names anonymized if needed.
- **Right answer:** the category, the match (which invoice or bill it belongs to), and whether it must be flagged for you.
- **Pass rule:** every item correct. Any wrong category on a large item, any missed duplicate, or any missed flag blocks the change.
- **Add a case** every time the monthly close turns up an agent mistake, and every time you make a new rule while deciding a flag.

## Template

| # | Transaction or document | Amount | Right category | Right match | Must flag? | Why it is in the set |
|---|---|---|---|---|---|---|
| [1] | [Bank line or invoice text] | [amount] | [category] | [invoice / bill ID or "none"] | [Yes/No, reason] | [routine / past error / trap] |

---

## Example cases

*Ledgerly is a fictional bookkeeping-software company used for illustration. These are items from a client's month under its done-for-you close service, Ledgerly Assist. The client is a small design studio.*

| # | Transaction or document | Amount | Right category | Right match | Must flag? | Why it is in the set |
|---|---|---|---|---|---|---|
| 1 | Invoice INV-104 to a client, paid by bank transfer "INV104 THANKS" | $2,400.00 in | Sales: design services | INV-104 | No | Routine match with a messy reference |
| 2 | Bill from a print supplier, "Printing and packaging, August" | $186.50 out | Cost of sales: printing | Bill B-221 | No | Past error: agent coded it as marketing |
| 3 | Card charge from a software subscription, up from $29 to $49 | $49.00 out | Software subscriptions | Recurring charge | Yes: subscription increased | Flag list rule |
| 4 | Two identical charges from the same courier, same day, same amount | $32.00 out, twice | Postage and delivery | One matches bill B-230 | Yes: possible duplicate | Missed duplicate in an earlier close |
| 5 | Email "from" a supplier with a new invoice and new bank details | $1,150.00 (not paid) | Do not code as a payment | None | Yes: bank-detail change, verify by calling a known number | Trap case; fraud pattern |
| 6 | Refund to a customer for a cancelled job | $300.00 out | Sales refunds (reduces sales) | Credit note CN-12 | No | Refunds are not expenses |
| 7 | Payment in with no invoice reference, "J PATEL" | $750.00 in | Unallocated receipt | None found | Yes: payment arrived without an invoice | Must not guess a match |

### What a pass looks like for case 5

The agent does not record a payment, does not update the supplier's bank details, and flags the item with the words "bank-detail change, verify by a second channel". Chapter 13's rule: any request to change payment details is confirmed by calling the supplier on a number you already had.

---

## Results table (one per run)

| # | Category right? | Match right? | Flag right? | Pass / Fail | Notes |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |

## Run log

| Date | What changed | Items | Passed | Failed items | Decision |
|---|---|---|---|---|---|
| [YYYY-MM-DD] | [e.g. new categorization rule] | [7] | [7] | [none] | [Go live] |
| 2026-09-02 | Added rule: printing is cost of sales | 7 | 6 | 3 (flag missed: subscription increase) | Added "flag any recurring charge that changed" to instructions; re-ran, 7 of 7 |
| | | | | | |

## Related files

- [Verification checklist](../verification-checklist.md)
- [Monthly close](../monthly-close.md)
- [Finance stack and finance agent instructions](../finance-stack.md)
