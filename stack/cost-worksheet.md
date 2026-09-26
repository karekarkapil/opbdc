# Cost worksheet

*Companion to Chapter 2, "Your Agent Stack", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Also used in Chapters 5, 13 and 15. Last reviewed: September 2026.*

## What this is

A one-page calculator for three numbers: **cost per task**, **cost per customer**, and **the ten-times test**. The useful number is never your monthly AI bill on its own. It is what one task costs, what one customer costs to serve, and whether both still make sense at ten times your current size.

## How to use it

1. Pick one automated job (a support conversation, a monthly close, a product description, a nightly check).
2. Measure it on real work, not on an estimate: run it ten times and read the usage from your provider's dashboard or your agent tool's usage report.
3. Fill in Part 1, then Part 2, then run Part 3.
4. Repeat monthly for your main agents (it is on the monthly checklist in [weekly-review.md](../playbooks/weekly-review.md)).

> **A note on prices.** Providers charge per *token*, a unit of text of roughly three-quarters of a word, and the way text is split into tokens differs between models and between model versions. A price cut per token is not always a price cut per task. That is why this worksheet asks you to measure tasks, not to multiply list prices. Current list prices, as of late 2026, are in Appendix A of the book; they will move.

---

## Part 1: Cost per task

Task: [name of the job]  Model tier: [frontier / middle / small and fast / local]  Measured on: [YYYY-MM-DD]

| Line | What to enter | Value |
|---|---|---|
| A | Model usage for 10 runs of the task (from the usage report) | [amount] |
| B | Model usage per run (A / 10) | [amount] |
| C | Other per-run costs: hosted agent time, voice minutes, image generation, paid connector calls | [amount] |
| D | Per-run share of fixed tools (monthly subscription cost / runs per month) | [amount] |
| E | **Cost per task (B + C + D)** | **[amount]** |
| F | Your review time per task, in minutes | [minutes] |
| G | Value of your time per hour (be honest, not modest) | [amount] |
| H | Review cost per task (F / 60 x G) | [amount] |
| I | **Full cost per task (E + H)** | **[amount]** |
| J | What the task is worth: the price the customer pays for it, or the cost of doing it another way | [amount] |

**Read it:** if I is close to J, the job is not yet worth automating in this form. Usually the fix is a cheaper tier (Part 4), fewer review minutes (a better brief, a [golden set](../playbooks/golden-sets/support.md)), or both.

## Part 2: Cost per customer

Per month, for one average customer.

| Line | What to enter | Value |
|---|---|---|
| K | Tasks this customer triggers per month, by type (e.g. 3 support conversations, 4 orders processed, 1 invoice) | [list] |
| L | Sum of (tasks x full cost per task from Part 1) | [amount] |
| M | Direct product or service cost for this customer (goods, packaging, delivery, payment fees, hosting share) | [amount] |
| N | **Cost to serve one customer (L + M)** | **[amount]** |
| O | Revenue from one average customer per month | [amount] |
| P | **Gross margin per customer (O minus N), and as a percentage of O** | **[amount] / [percent]** |

This P is the gross margin figure in the five numbers of Chapter 13 and on the [CEO dashboard](../playbooks/ceo-dashboard.md). Include the agent costs; leaving them out is how an agent-run company flatters itself.

## Part 3: The ten-times test

Multiply your current volume by ten and ask what breaks.

| Question | Today | At 10x volume |
|---|---|---|
| Customers | [number] | [number x 10] |
| Tasks per month (all agents) | [number] | [number] |
| Monthly agent cost (production usage, not subscriptions) | [amount] | [amount] |
| Does cost per task stay flat, fall (caching, batching) or rise (longer conversations, harder cases)? | | [your estimate and why] |
| Your review minutes per week | [minutes] | [minutes] |
| Gross margin per customer | [amount] | [amount] |

**The test fails if** any of these is true at ten times:

- [ ] Agent costs grow faster than revenue.
- [ ] Gross margin per customer falls below what you need (write your floor: [percent]).
- [ ] Your review minutes exceed the time you have (review capacity is the real limit on parallel agents, Chapter 4).
- [ ] One provider's price change or product retirement would break the numbers (the fifth-factor test).

If the answer scares you, redesign now, while it is cheap. That was the lesson of the bill that opens Chapter 2.

---

## Part 4: Levers that change the numbers

| Lever | What it does | Where to check |
|---|---|---|
| Route by tier | Send volume work to the small, fast tier; keep the frontier tier for hard, high-stakes work | Review the mix monthly |
| Effort setting | Many models let the same model think briefly or deeply; lowering effort on simple jobs is often a bigger saving than switching models | Your agent tool's settings |
| Caching | Text an agent rereads often (your context kit, instructions) can be cached and reread at a small fraction of the normal price | Your provider's documentation |
| Batching | Work that can wait a few hours can often run as a batch at about half price | Your provider's documentation |
| Shorter standing instructions | Every line in an always-read file costs attention and money on every task | [agent-instructions.md](../context-kit/agent-instructions.md) |
| Smaller tasks | Checkable pieces fail less and waste less when they do fail | [agent-brief-card.md](../briefs/agent-brief-card.md) |
| Local model | Fixed cost for high-volume, simple, private work; rarely cheaper once hardware and your time are counted | [local/](local/README.md) |

## Part 5: Limits and alerts

Every production agent gets a cap and an alert. A runaway loop at three in the morning is the modern version of leaving the tap running.

| Agent | Daily cap | Monthly cap | Alert at | Alert goes to | What happens at the cap |
|---|---|---|---|---|---|
| [Agent] | [amount] | [amount] | [percent of cap] | [you, by message] | [stops and waits / drops to a cheaper tier] |

---

## Worked example: a support conversation at Copper Pot Mixers

*Illustration: Copper Pot Mixers is a fictional company. All figures below are assumptions chosen to show the arithmetic, not quotes or measurements. Measure your own.*

**Part 1.** Ten real support conversations (stock questions, delivery days, one damaged bottle) were run through the support agent on the small, fast tier.

| Line | Value (assumed) |
|---|---|
| B: model usage per conversation | $0.02 |
| C: other per-run costs | $0.00 (text only, no voice) |
| D: share of the support tool subscription | $0.05 |
| E: cost per task | $0.07 |
| F and H: founder review, 1 minute per conversation in the weekly sample of twenty, spread across all conversations | about $0.10 |
| I: full cost per task | about $0.17 |
| J: worth | a question answered at 1 am instead of at 10 am the next day |

**Part 2.** An average bar triggers about three support conversations a month (about $0.51), places four orders, and generates Rs 12,000 (about $145) of revenue. The agent cost is small next to the goods, delivery and payment fees. Here, the product costs decide the margin, not the agents.

**Part 3.** At ten times the customers, the support agent's cost rises roughly in line with conversations, which is fine. What does not scale is the founder's review time if every conversation is read. The redesign: the weekly sample stays at twenty conversations; escalations get read in full; everything else is covered by the golden set and the re-contact rate.

The lesson generalizes. For many small companies, the ten-times test fails first on **your time**, not on the bill.

## Related files

- [Permission matrix](permission-matrix.md), where the spend caps also live.
- [Validation scorecard](../playbooks/validation-scorecard.md), question 7 (unit economics) uses Part 2.
- [Monthly close](../playbooks/monthly-close.md) and [CEO dashboard](../playbooks/ceo-dashboard.md), which report agent spend against budget.
