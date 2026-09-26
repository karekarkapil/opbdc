# Decision log (template)

*Companion to Chapters 1, 3 and 15 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

A single document where you write down each meaningful decision, its date and its reason. It prevents agents, and you, from relitigating settled questions, and it lets you see when a reason no longer holds. It is the first piece of your company's written memory, started in Chapter 1.

## How to use it

- Add an entry the moment you decide, before you close the laptop.
- Record the **reason**, and what would make you change your mind. A decision without a reason will be undone by the next agent that finds a plausible alternative.
- Agents read it before changing anything settled. Their instructions say: "If a task would reverse a logged decision, stop and ask."
- The weekly operating review adds "the one decision" here every week (Chapter 15). The monthly close adds two sentences on what the numbers mean (Chapter 13).
- Never delete an entry. When a decision changes, add a new entry that supersedes the old one and links to it.

See filled-in versions: [beverage company](examples/beverage-company/decision-log.md), [software company](examples/software-company/decision-log.md).

---

## Template

```markdown
# Decision log: [Company name]

Last checked: [YYYY-MM-DD]
Rule for agents: do not reverse a decision logged here. If a task seems to require it, stop and ask.

## Open questions
Decisions you know are coming, with the date you will decide by.
- [Question] (decide by [YYYY-MM-DD]; evidence needed: [ ])

## Decisions (newest first)

### D-[number]: [Short title]
- **Date:** [YYYY-MM-DD]
- **Decision:** [What we decided, in one or two sentences.]
- **Reason:** [Why, including evidence: customer quotes, numbers, costs.]
- **Alternatives considered:** [What we did not choose, and why not.]
- **Revisit if:** [The condition that would reopen it.]
- **Status:** [active / superseded by D-[number]]
- **Files updated:** [facts sheet, agent instructions, spec ...]
```

---

## What counts as "meaningful"

Log it if any of these is true:

- [ ] It changes what customers are offered, charged or promised.
- [ ] It changes who you serve, or who you do not serve.
- [ ] It sets a rule agents must follow.
- [ ] It moves a job up or down the trust ladder.
- [ ] It chooses or drops a tool, provider or supplier.
- [ ] Reversing it later would be expensive or embarrassing.
- [ ] You argued with yourself about it for more than a day.

## Guidance notes

- **Short is fine.** Three lines with a date and a reason beat a page written a month later.
- **Link the evidence.** Point to the customer-file quote or the monthly-close numbers behind the decision.
- **Update the other files.** A decision that changes a price is not done until the facts sheet says so.
- **Portfolio decisions** (Chapter 17) go in a portfolio-level log; each company's log links to them.

## Where this breaks

- **Decisions without reasons** get relitigated, by you at eleven at night and by agents at any hour.
- **Silent reversals.** An old decision quietly undone with no new entry leaves agents following two rules.
- **Logging tasks as decisions.** "Wrote the newsletter" is not a decision. "Newsletters always open with a real customer" is.
