# Monthly close

*Companion to Chapter 13, "The AI CFO", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

The routine that turns a month of transactions into numbers you can trust. The agent does six steps; you do four. With the [finance stack](finance-stack.md) in place, your part takes about an hour.

## How to use it

1. Schedule the close agent for the [first working day] of each month, using the brief at the end of this file.
2. When it reports, do your four steps. Do not skip the three-number check.
3. Every rule you make while deciding flags goes into the finance agent's categorization rules, so it is never asked again.
4. File the one-page summary with the month's records, and update the cash forecast.

> This is not financial, tax or accounting advice. Your accountant decides how things are treated for tax and statutory purposes.

---

## The agent's checklist (six steps)

- [ ] **1. Collect** every transaction from the bank, the payment provider and the card statements for [month].
- [ ] **2. Categorize** each one, following the rules in its instructions and last month's decisions.
- [ ] **3. Match** payments received to invoices sent, and bills paid to bills received.
- [ ] **4. Reconcile** the books to the bank balance, to the rupee or cent. Show opening balance, closing balance and any difference.
- [ ] **5. Flag** anything unusual (the flag list below).
- [ ] **6. Draft the summary:** revenue, costs, profit or loss, cash in the bank, and who owes you what (template below).

## The flag list

The first five come straight from Chapter 13. The rest are common additions; keep the ones that fit your business.

| Flag | Source |
|---|---|
| A new supplier | Chapter 13 |
| A duplicate charge | Chapter 13 |
| A subscription that increased | Chapter 13 |
| A payment that arrived without an invoice | Chapter 13 |
| An invoice more than thirty days unpaid | Chapter 13 |
| Any request to change bank or payment details (possible fraud) | Chapter 13, controls |
| A new recurring charge of any size | Common addition |
| A round-number transfer, or a transfer made at a weekend or late at night | Common addition |
| An expense more than [N] times its usual monthly amount | Common addition |
| A refund or credit you do not remember approving | Common addition |
| A transaction that fits no categorization rule | Common addition |
| Agent card spend over its limit, or any charge on it you did not expect | Common addition |

Each flag is shown with: the transaction, why it was flagged, and the agent's suggestion.

## Your four steps

- [ ] **1. Read the flags, and decide each one.** Write any new rule into the finance agent's categorization rules.
- [ ] **2. Check three numbers against their source yourself** (about five minutes):
  - [ ] the closing bank balance, against the bank's own statement;
  - [ ] the largest expense, against its bill or receipt;
  - [ ] the largest payment received, against the invoice and the bank line.
  If any one is wrong, do not trust the rest until the cause is found.
- [ ] **3. Read the summary**, and write two sentences in the [decision log](../context-kit/decision-log.md) about what it means.
- [ ] **4. Sign off.** The month is closed.

---

## One-page summary template

```markdown
# Monthly close: [Month YYYY], [Company name]
Prepared by: finance agent, [date]. Signed off by: [founder], [date].

## The month
| | This month | Last month | Same month last year |
|---|---|---|---|
| Revenue | | | |
| of which repeat customers | | | |
| Costs | | | |
| Profit or loss | | | |
| Cash in the bank (closing) | | | |

## Who owes you what
| Customer | Invoice | Amount | Days overdue |
|---|---|---|---|

## The five numbers
1. Cash and runway: [cash], [N] months at current burn
2. Revenue, and share that repeats: [amount], [N]%
3. Gross margin per [unit or customer], incl. agent costs: [amount or %]
4. Cost to acquire a customer, and payback: [amount], [N] months
5. Money owed to you: [total], of which over 30 days: [amount]

## Forecast against actual
| | Forecast | Actual | Difference | Why |
|---|---|---|---|---|
| Revenue | | | | |
| Costs | | | | |
| Closing cash | | | | |

## Flags decided
| Flag | Decision | New rule added? |
|---|---|---|

## The three-number check
Closing balance [ok/not ok]; largest expense [ok/not ok];
largest payment received [ok/not ok].

## Two sentences for the decision log
[What this month means, and what, if anything, changes.]

## Sign-off
Month closed: [yes/no], [date], [initials].
```

---

## The twelve-month cash forecast

One simple forecast: cash, month by month, for the next twelve months, in three versions. The agent builds it from actual numbers and the assumptions you choose, and updates it after each close.

**Assumptions (you choose, write them down):**

| Assumption | Expected | Pessimistic | Very pessimistic |
|---|---|---|---|
| Revenue growth per month | [%] | [%] | [%] |
| Monthly costs | [amount] | [amount] | [amount] |
| Average days until customers pay | [N] | [N] | [N] |
| One-off costs (month and amount) | | | |

**Forecast table (repeat for each version):**

| Month | Opening cash | Cash in | Cash out | Closing cash | Months of runway |
|---|---|---|---|---|---|
| [M1] | | | | | |
| [M2] | | | | | |
| ... | | | | | |
| [M12] | | | | | |

The agent also reports: **the first month any version falls below [minimum cash]**, and **the single assumption the forecast is most sensitive to.** Watch that assumption closely.

### Illustration (fictional)

Copper Pot Mixers is a fictional company used for illustration. Its founder sets a floor of Rs 3,00,000 (about $3,600) in the bank. In the very pessimistic version (two large bar accounts stop ordering and payments slip by a week), cash crosses that floor in month seven. The most sensitive assumption is repeat orders from the ten largest accounts, so that becomes a line on her [CEO dashboard](ceo-dashboard.md).

---

## Brief for the close agent

> **Goal:** Close the books for [month] and prepare the one-page summary and updated cash forecast, so the founder can close the month in about an hour.
>
> **Context:** Read your standing instructions (finance agent), the categorization rules, last month's close and its decisions, the facts sheet for prices and payment terms, and the current cash forecast.
>
> **Constraints:** Read and draft only. Do not pay, refund, credit, change bank details or send any message except the pre-approved reminder. Do not change last month's closed figures; propose corrections instead.
>
> **Done:** The six steps complete; the summary in the template above; the three forecast versions updated; all flags listed.
>
> **Verification:** Show the reconciliation (opening balance, closing balance, difference). For each flag, show the transaction and the reason. List every transaction you categorized without a matching rule.
>
> **Questions:** Stop and ask if the books do not reconcile after two attempts, if any message asks to change payment details, or if you find a transaction you cannot explain.

## Related files
- [Finance stack](finance-stack.md)
- [Golden set for finance](golden-sets/finance.md)
- [CEO dashboard](ceo-dashboard.md)
- [Weekly review](weekly-review.md)
