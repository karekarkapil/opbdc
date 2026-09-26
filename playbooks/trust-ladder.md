# The trust ladder

*Companion to Chapter 4, "Managing Agents", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

Supervision is expensive, so you want to relax it wherever it is safe, and nowhere else. The trust ladder has five rungs. Every recurring job in your company sits on one of them. This file holds the rungs, the rules for moving a job up or down, the jobs that never climb past rung 2, and a register you keep for your own company.

## How to use it

1. List every job you or your agents do more than once a month in the register below.
2. Give each a rung, and write why.
3. Circle (mark "Yes" in the last column) every job that must never go above rung 2.
4. Build each rung into the [permission matrix](../stack/permission-matrix.md), so the ladder is enforced by access, not by memory.
5. Review the register in the weekly operating review: promote one job that has earned it, demote any job that had an incident.

---

## The five rungs

| Rung | Name | The agent... | You... |
|---|---|---|---|
| 0 | Manual | Does nothing | Do the job yourself, and write down how |
| 1 | Draft | Prepares the work | Review and finish every piece |
| 2 | Act with approval | Prepares actions ready to go | Approve each one before it happens |
| 3 | Act and report | Acts within set limits | Review a daily or weekly sample and all exceptions |
| 4 | Autonomous within guardrails | Acts and escalates only exceptions | Review metrics, samples and the log in your weekly rhythm |

## Promotion rules

A job climbs **one rung at a time** when all three are true:

- [ ] **Track record.** The agent has a record on this job, for example thirty consecutive pieces of work you approved unchanged.
- [ ] **Reversible.** The actions are reversible, or cheap to fix.
- [ ] **Small error cost.** The cost of a single error is small.

Before promoting, also check:

- [ ] The job has a golden set, and it passed on the current instructions and tools ([verification checklist](verification-checklist.md)).
- [ ] The permissions for the new rung are set in the permission matrix (for example, rung 3 gets limits: a maximum credit, a maximum number of actions a day).
- [ ] The exceptions the agent must escalate are written into its instructions.
- [ ] The reason for the promotion is written in the decision log.

## Demotion rules

**What counts as an incident:** any mistake that reached a customer, touched money or data, or broke an agent's limits. A mistake caught before it reached anyone (by your review, a golden-set run or a pre-release check) is a **near miss**: log it and fix the cause, with no rung change. A style slip that you correct in the weekly sample (too long, too stiff) is neither; fix the voice guide.

- A job comes **back down the ladder after any incident**, until the cause is understood and fixed.
- Drop it at least one rung, or to rung 1 if the incident touched a customer, money or data.
- Reset its track-record count to zero.
- Record the incident in the [lessons log](../context-kit/lessons-log.md) and the rule that came from it in the agent's instructions.
- Also demote when you change the model, tool or instructions in a way the golden set did not cover, until it has been re-run.

## Never above rung 2

However good the agents become, these jobs stay at rung 2 (act with approval) or below, for good:

- anything that **moves money out** of the company;
- anything that **signs or changes a contract**;
- anything that **deletes data**;
- anything that **makes a public statement**;
- anything that **changes terms for existing customers** (prices, policies, payment terms).

These are the irreversible actions. Build the rule into permissions: the agent should not *hold* the power to do these alone, so the rule does not depend on your remembering it.

**The one exception (Chapters 10, 12 and 14):** a support agent may apply a small goodwill credit, up to a fixed limit you set, to the customer's own account, and every credit is logged. That is the only money power an agent that reads customer messages may hold. Refunds, replacements, discounts, larger credits and any payment out stay at rung 2.

---

## Job register (template)

| Job | Rung | Why | Track record (approved unchanged in a row) | Last incident | Next review | Never above 2? |
|---|---|---|---|---|---|---|
| [Job] | [0 to 4] | [reason] | [count] | [YYYY-MM-DD, or none; near misses are not incidents] | [YYYY-MM-DD] | [Yes/No] |
| | | | | | | |
| | | | | | | |

## Worked example

*Copper Pot Mixers is a fictional company used for illustration. It sells craft cocktail mixers to independent bars and cafes. This is the example from Chapter 4, not a record of any real company.*

| Job | Rung | Why |
|---|---|---|
| Sorting incoming email into orders, questions and spam | 4 | Reversible, high volume, long track record |
| Answering routine questions about stock and delivery | 3 | Answers come only from the facts sheet; weekly sample |
| Drafting social media posts | 1 | Brand voice is still being refined |
| Reordering bottles and labels from suppliers | 2 | Money leaves the company |
| Replying to a complaint about a damaged shipment | 1 | Relationship at risk; the founder signs every reply |
| Changing wholesale prices | 0 | A decision, not a task |

The same jobs, as they would appear in the full register (as of 2026-09-08), with one job the chapter's table leaves out, the goodwill credit:

| Job | Rung | Why | Track record | Last incident | Next review | Never above 2? |
|---|---|---|---|---|---|---|
| Email sorting | 4 | Reversible, high volume | 400+ | none | 2026-12-01 | No |
| Routine stock and delivery answers | 3 | Facts sheet only; weekly sample | 52 | 2026-07-02 (a guessed delivery day reached a customer; demoted to rung 1, back at rung 3 from 2026-08-10; lessons log L-8). The 2026-08-18 golden-set failure was a near miss, caught before release | 2026-10-05 | No |
| Goodwill credits for our own mistakes | 3 | Part of the routine-questions job, switched on 2026-08-10 when that job was back at rung 3; capped in the order system at Rs 300 per customer per month, on the customer's own account, every credit logged (decision D-8) | 18 credits since 2026-08-10, all within the rule | none | 2026-10-05 | Rung 3 only: the one capped exception; never higher |
| Social posts | 1 | Voice still being refined; rung 2 at thirty in a row (decision D-10) | 11 | none | 2026-10-05 | Yes (public statement) |
| Supplier reorders | 2 | Money out; the founder pays | 24 | none | 2026-11-02 | Yes (money out) |
| Damaged-shipment replies | 1 | Relationship at risk; a free replacement is the founder's decision | n/a | n/a | 2026-12-01 | Stays at rung 1 by choice: the founder signs every reply |
| Wholesale price changes | 0 | A decision | n/a | n/a | n/a | Yes (terms for existing customers) |

## How rungs map to permissions

| Rung | Typical permissions in the [permission matrix](../stack/permission-matrix.md) |
|---|---|
| 0 | No access for any agent to this job's systems |
| 1 | Read the context and the data needed; write drafts only, to a drafts folder |
| 2 | Read; prepare actions in a queue (draft email, draft payment, draft order) that only you can release |
| 3 | Read and act within hard limits (amount caps, daily action caps, specific tools only); every action logged |
| 4 | As rung 3, with wider limits and alerts on exceptions; still no delete and no money out |

## Related files

- [Verification checklist](verification-checklist.md)
- [Permission matrix](../stack/permission-matrix.md)
- [Weekly review](weekly-review.md)
