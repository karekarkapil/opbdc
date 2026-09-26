# Lessons log (template)

*Companion to Chapters 3, 4 and 9 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

What went wrong, what you learned, and what changed as a result. Every mistake an agent makes should end up here as a rule, so it is made only once. It is fed by the "Record" step of the delegation loop (brief, plan, execute, verify, record), by incident accounts and by the weekly operating review.

## How to use it

- Write the entry the same day. Two lines are enough.
- Every entry ends with **what changed**: a line added to agent instructions, a fact fixed, a playbook step added, a job moved on the trust ladder. A lesson that changed nothing will be learned again.
- Include near misses and things that went right in a way you want repeated.
- Review it weekly. When a lesson applies to every company you run, move it into the shared playbooks (Chapter 17).

See filled-in versions: [beverage company](examples/beverage-company/lessons-log.md), [software company](examples/software-company/lessons-log.md).

---

## Template

```markdown
# Lessons log: [Company name]

Last checked: [YYYY-MM-DD]

## Entries (newest first)

### L-[number]: [Short title]
- **Date:** [YYYY-MM-DD]
- **What happened:** [One or two sentences. Facts, no blame.]
- **Who or what:** [agent and job / you / supplier / system]
- **Caught by:** [your review / weekly sample / golden set / customer / alert]
- **Cost:** [none, a near miss / time / money / a customer's trust]
- **Lesson:** [The general rule, in one sentence.]
- **What changed:** [file and line updated, e.g. "research playbook, step 4: confirm the business is still open"]
- **Trust ladder:** [unchanged / demoted from rung X to Y until [condition]]
```

## Quick-entry form

For small lessons, one line is enough:

```markdown
- [YYYY-MM-DD] [what happened] -> [rule] -> [file changed]
```

---

## Where lessons usually go

| If the lesson is about... | Change this file |
|---|---|
| A fact the agent did not have or got wrong | Facts sheet |
| A misunderstanding of the job | The brief template or the agent instructions |
| A better way to do a recurring job | The playbook for that job |
| Tone, words or style | Voice guide (rejection log) |
| Something visual | Design system |
| A risky action | Permission matrix and trust ladder |
| A product behavior | The spec, and a new acceptance test |
| An outage or security event | Incident log and runbook |

## Guidance notes

- **Blame the system, not the agent.** An agent pursuing the goal you stated rather than the one you meant is telling you the brief was unclear.
- **Count repeats.** If the same lesson appears twice, the "what changed" did not work. Change something stronger: a permission, a check, a test.

## Where this breaks

- **Lessons with no change attached.** The log becomes a diary.
- **Only big failures logged.** Most useful lessons are small: a closed business on a research list, a bland newsletter.
- **Never read.** A log nobody reviews is a napkin by another name.
