# Validation scorecard

*Companion to Chapter 5, "A Problem Worth Solving", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

After the research and the ten conversations, you usually have a handful of candidate problems. This scorecard makes you score each one honestly, from 1 to 5, on nine questions, and then spend an hour on the back-of-the-envelope economics to find the assumption that would kill the business.

## How to use it

1. An agent may prepare a first draft of the scores from your [customer file](../context-kit/customer-file.md) and conversation notes. Give it this file and ask it to justify every score with a quote or a fact.
2. Change the scores where your judgment differs. It will.
3. Apply the gate first. Then use the other six questions to choose between problems that pass it.
4. Build the envelope model for the leading problem, name the assumption that would kill it, and go test that assumption, usually with another conversation.
5. Write the decision and its reason in the [decision log](../context-kit/decision-log.md).

---

## The nine questions

| Question | What a 5 looks like |
|---|---|
| **1. Severity** | It costs them real money, time or sleep, and they said so unprompted |
| **2. Frequency** | It happens every week, not once a year |
| **3. Willingness to pay** | They already pay for a workaround, or offered to pay you |
| **4. Reachability** | You can reach a hundred people with this problem this month, cheaply |
| **5. Your insight** | You understand something about it that most people do not |
| **6. Hard to copy** | Its hard part is distribution, trust, knowledge, operations or data, not only software |
| **7. Unit economics** | The price comfortably exceeds the cost of serving a customer, including agent costs (Chapter 2) |
| **8. Founder fit** | You would happily work on it for five years |
| **9. Machine fit** | It will build or reuse the machine you want for your portfolio |

## The gate

**A problem that scores below 3 on severity, willingness to pay or reachability is not ready**, however well it scores elsewhere. Those three are the gate. The other six decide between ideas that pass it.

Question 9 is specific to building a portfolio: if two good ideas are close, prefer the one whose functions (support playbook, finance routine, content engine, brand system) you would reuse in a second and third company.

---

## Scoring sheet (up to three candidates)

| Question | [Problem A] | [Problem B] | [Problem C] | Evidence (quote or fact, with date) |
|---|---|---|---|---|
| 1. Severity | | | | |
| 2. Frequency | | | | |
| 3. Willingness to pay | | | | |
| 4. Reachability | | | | |
| 5. Your insight | | | | |
| 6. Hard to copy | | | | |
| 7. Unit economics | | | | |
| 8. Founder fit | | | | |
| 9. Machine fit | | | | |
| **Passes the gate?** (1, 3 and 4 all 3 or above) | | | | |
| **Total** (for comparison only) | | | | |

## Back-of-the-envelope economics

| Number | Your estimate | Where it comes from |
|---|---|---|
| **Price** per month or per order | | What customers said, and what they pay for workarounds today |
| **Cost to serve** one customer per month (product, payment fees, hosting, agent cost per task and per customer) | | [Cost worksheet](../stack/cost-worksheet.md) |
| **Gross margin** per customer per month (price minus cost to serve) | | |
| **Cost to acquire** one customer (time and money, first year, realistic) | | |
| **Payback** in months (cost to acquire divided by monthly margin) | | |
| **Retention**: how many months a customer stays (be pessimistic) | | |

**Warning signs:** payback longer than a few months; cost to serve close to price.

**The assumption that would kill it:** [one sentence]
**How I will test it this week:** [one action, usually a conversation]

---

## Worked example

*Copper Pot Mixers is a fictional company used for illustration. Its founder sells craft cocktail mixers to independent bars and cafes in Bengaluru and is choosing what to build next. All numbers below are invented for the illustration, not data.*

Three candidate problems came out of the research and ten conversations:

- **A. Staff do not know what to do with the mixers.** Tasting kits go unused. Quote: "My staff don't know what to do with the bottle."
- **B. Running out on a Friday night.** Bars run out of their best-selling mixer during the weekend rush, when deliveries are impossible. Quote: "We ran out of the pineapple at ten on Friday and sold soda for the rest of the night."
- **C. Menu costing.** Owners do not know the cost of each drink on their menu.

| Question | A. Staff training | B. Friday stock-outs | C. Menu costing | Evidence |
|---|---|---|---|---|
| 1. Severity | 3 | 5 | 3 | B: four of ten raised it unprompted, with lost sales named |
| 2. Frequency | 4 | 4 | 2 | C: costing is redone when the menu changes, twice a year |
| 3. Willingness to pay | 3 | 4 | **2** | C: nobody pays for it today; "I do it in my head" |
| 4. Reachability | 5 | 4 | 4 | Existing customers and the bars they talk to |
| 5. Your insight | 4 | 3 | 3 | A: the founder has trained bar staff herself |
| 6. Hard to copy | 4 | 4 | 1 | C: only software, and generic |
| 7. Unit economics | 4 | 3 | 3 | B: needs reliable Thursday deliveries |
| 8. Founder fit | 4 | 4 | 2 | |
| 9. Machine fit | 5 | 4 | 3 | A reuses the content engine; B reuses the reorder page |
| **Passes the gate?** | Yes | Yes | **No** (willingness to pay 2) | |
| **Total** | 36 | 35 | 23 | |

**Reading the result.** C fails the gate: people agree it is a problem and nobody pays to fix it. A and B both pass, and are close on total. The founder chooses **B**, because its severity is highest and it has the clearest money signal (lost sales on the busiest night), and schedules A as a smaller addition: a staff recipe card in every tasting kit.

**The envelope for B** (a standing weekly order with par levels, delivered Monday to Thursday, so the bar is stocked before the weekend):

| Number | Illustration |
|---|---|
| Price | About 3 cases a week at around Rs 3,100 (about $37) a case, no extra fee |
| Cost to serve | Product, delivery and packing, plus a small agent cost for the weekly par check |
| Gross margin | Illustrative 40 to 45 percent of the order value |
| Cost to acquire | A tasting kit plus about three hours of the founder's time per bar |
| Payback | Under two months, if the bar keeps ordering |
| Retention | Assume eight months, pessimistically |

**The assumption that would kill it:** that bar managers will agree to a standing par level instead of ordering on impulse. **Test this week:** offer a standing order to the four bars that complained most, and count how many say yes and keep it for a month.

*What happened next, in the example company's own [decision log](../context-kit/examples/beverage-company/decision-log.md): the standing order ran as a fixed weekly subscription and was retired in April 2026 (D-6) after two sign-ups in three months, because every bar orders to its own stock level. The kill assumption was the right one to test. The reorder page (D-9), built for the way bars actually order, took its place.*

## Related files

- [Customer conversations](customer-conversations.md)
- [Research agent brief](../briefs/research-agent.md)
- [Cost worksheet](../stack/cost-worksheet.md)
- [One-page spec](one-page-spec.md)
