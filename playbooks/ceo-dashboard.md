# CEO dashboard

*Companion to Chapter 15, "The Operating Rhythm", and Chapter 17, "The Holding Company Machine", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

One screen, compiled by an agent each morning, that you can read in two minutes. A handful of numbers, each with a threshold you set in advance for amber and red. It opens every [weekly review](weekly-review.md).

## How to use it

1. Fill in the thresholds table for your company. Set them when you are calm, not when a number has just moved.
2. Brief the dashboard agent (brief below) to compile it every morning at [time].
3. Read it daily in two minutes. Act only on amber and red.
4. Once a quarter, remove any number that has been green for months with no decision depending on it.

---

## The layout (one screen)

```text
[Company name]  CEO dashboard  [YYYY-MM-DD]  compiled [time]

AREA            NUMBER                                          STATUS
Cash            [cash in bank]  runway [N] months                [G/A/R]
Revenue         week [x]  month [x]  repeat share [N]%            [G/A/R]
Margin          gross margin per [unit/customer] [x] incl agents  [G/A/R]
Customers       new this week [N]  from: [channel list]           [G/A/R]
Money owed      overdue [total]  oldest [N] days                  [G/A/R]
Support         confirmed resolutions [N]%  waiting for you [N]
                re-contact rate [N]%                              [G/A/R]
System          uptime [N]%  errors [trend]  morning flags [N]    [G/A/R]
Agents          spend month-to-date [x] of budget [x]
                over limit: [none / list]                         [G/A/R]
The one number  [your measure] [value]                            [G/A/R]

Missing or stale data: [list, or "none"]
```

## The thresholds (fill in)

| Area | The number | Green | Amber | Red | Source |
|---|---|---|---|---|---|
| Cash | Cash in the bank and months of runway | [above N months] | [N to N months] | [below N months] | [bank feed] |
| Revenue | This week and this month, and the share from repeat customers | [at or above plan] | [below plan by N%] | [below plan by N%] | [payment provider, accounting] |
| Margin | Gross margin per unit or per customer, including agent costs | [above N%] | [N to N%] | [below N%] | [accounting, cost worksheet] |
| Customers | New customers this week, and where they came from | [N or more] | [N] | [none for N weeks] | [CRM or customer file] |
| Money owed | Invoices overdue, by amount and age | [none over N days] | [any over N days] | [any over N days, or total above x] | [accounting] |
| Support | Confirmed resolutions, escalations waiting for you, re-contact rate | [above N%, none waiting over N hours] | [...] | [...] | [support tool] |
| System | Uptime, errors and anything the morning summary flagged | [no flags] | [one or more flags] | [outage or error spike] | [monitoring, morning summary] |
| Agents | Spend this month against budget; any agent over its limit | [on pace] | [above N% of pace] | [any agent over limit] | [provider usage pages] |
| The one number | The measure that best shows your product is doing its job | [...] | [...] | [...] | [...] |

### Illustration (fictional)

Copper Pot Mixers is a fictional company used for illustration. These are its founder's own choices, not benchmarks.

| Area | Green | Amber | Red |
|---|---|---|---|
| Cash | 6 months of runway or more | 3 months to under 6 | under 3 months |
| Revenue | month at 90% of plan or above, and repeat share 70% or more | month at 80% to under 90% of plan, or repeat share 60% to under 70% | month under 80% of plan, or repeat share under 60% |
| Margin | gross margin 55% or more per case | 45% to under 55% | under 45% |
| Customers | 2 or more new bars this week | 1 new bar this week, or none for one or two weeks | none for 3 weeks in a row |
| Money owed | nothing overdue (an invoice is overdue 48 hours after delivery) | anything overdue up to 7 days, and Rs 20,000 or less in total | anything overdue more than 7 days, or more than Rs 20,000 (about $240) in total |
| Support | 90% or more confirmed resolutions, and nothing waiting over 4 hours | 80% to under 90%, or anything waiting over 4 and up to 12 hours | under 80%, or anything waiting over 12 hours |
| System | order page up; no flags | order page up; one or more flags | order page down, or no orders when normally expected |
| Agents | spend up to 20% ahead of pace | more than 20% ahead of pace, and no agent over its limit | any agent over its limit |
| The one number | 50% or more of repeat orders through "Reorder in one tap" | 35% to under 50% | under 35% |

Each row's bands meet without gaps or overlaps: every value falls in exactly one color. Where a row has two measures, the worse one decides.

---

## Rules

- **Two minutes.** If it takes longer to read, it has too much on it.
- **Resist adding to it.** Every extra number dilutes attention from the ones that matter.
- **Thresholds are set in advance,** in writing, and changed only in the weekly review with a reason in the decision log.
- **Remove what nobody uses.** If a number has been green for months and no decision depends on it, remove it.
- **Missing data is shown as missing,** never filled with an estimate.

---

## Brief for the dashboard agent

> **Goal:** Compile the one-screen CEO dashboard for [Company name] every morning by [time], so the founder can see the health of the company in two minutes.
>
> **Context:** Read this file for the layout and thresholds. Sources: [bank feed], [payment provider], [accounting software], [support tool], [monitoring], [provider usage pages], [the one number's source]. Take the plan figures from the current cash forecast and plan in the latest [monthly close](monthly-close.md), not from the facts sheet, which holds only what customers may be told.
>
> **Constraints:** Read-only access to every source. Never change a threshold, never estimate or fill in a missing number, never round a red into an amber. Do not act on anything you see; report it.
>
> **Done:** The dashboard in the layout above, saved to [location] and sent to [channel], with each number's status set by the thresholds table.
>
> **Verification:** Under the dashboard, list each number's source and the time it was read. If a source was unreachable or its data is older than [24 hours], show the number as "missing" or "stale", with the reason.
>
> **Questions:** If any number is red, or two or more are missing, send the founder a short separate message straight away rather than waiting to be read.

---

## Portfolio variant (Chapter 17)

One line per company, then the combined position. Each company's line is compiled with that company's permissions only.

| Company | Cash and runway | Revenue (month) | Margin | New customers | Escalations waiting | Agent spend vs budget | Status |
|---|---|---|---|---|---|---|---|
| [Company 1] | | | | | | | [G/A/R] |
| [Company 2] | | | | | | | [G/A/R] |
| [Company 3] | | | | | | | [G/A/R] |
| **Portfolio** | [total cash] | [total] | [blended] | [total] | [total] | [total] | |

A company's status is its worst area: one red makes the line red.

## Related files
- [Weekly review](weekly-review.md)
- [Monthly close](monthly-close.md)
- [Cost worksheet](../stack/cost-worksheet.md)
- [Portfolio map](../portfolio/portfolio-map.md)
