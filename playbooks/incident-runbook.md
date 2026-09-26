# Incident runbook

*Companion to Chapter 9, "Ship It, Run It", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

A one-page procedure for when something goes wrong, written in advance so that at the moment of crisis nobody has to think from scratch. Five steps: **Detect, Contain, Communicate, Fix, Learn.** Contain before you diagnose. This file also holds customer message templates, a template for the incident account, a filled example, and the absence note.

## How to use it

- Print the one-page section, or keep it where you can open it from your phone.
- Fill in the brackets for your company now: where the rollback button is, where the feature switches are, how to post a notice.
- After every incident, fill in an incident account, add the lesson to the [lessons log](../context-kit/lessons-log.md), and demote the affected job on the [trust ladder](trust-ladder.md) until the cause is fixed.

---

## The one page

| Step | What happens | Agent | You |
|---|---|---|---|
| **1. Detect** | An alert, an agent's summary or a customer message says something is wrong | Investigates at once: logs, recent changes, reproduction; sends a summary with evidence | Note the time. Open this page |
| **2. Contain** | Stop the damage before you understand it | Automatic rollback if the cause is a recent release | Roll back the last release, switch off the broken feature, or put up an honest notice. Do this first |
| **3. Communicate** | Tell affected customers what happened and what you are doing | Drafts the messages from the templates below; lists affected customers | Edit and send. Customers forgive problems more readily than silence |
| **4. Fix** | Find the real cause and fix it properly | Drafts the fix and a test that reproduces the problem; opens it for review | Review and release through the normal [ship checklist](ship-checklist.md), not a shortcut |
| **5. Learn** | Make sure it cannot recur the same way | Drafts the incident account | Edit it, add the lesson to the lessons log, change one thing |

**My containment switches** (fill in now):
- Roll back: [where, how]
- Feature switches: [where, which features]
- Status notice: [where, how to post it from a phone]
- Kill switch for all agent access: [how, tested on YYYY-MM-DD]

**Anything that touches customers or money stays at rung 2:** the agent drafts the refund or the apology; you send it.

---

## Customer message templates

The words follow the standard in Chapter 8: no distress, truthful, useful. Say what happened, what it means for them, what you are doing, and when they will hear from you next. No blame, no jargon, no "Error 402". Never say something is fixed until it is.

### First notice (as soon as you have contained it, even before you know the cause)

> Subject: [Short plain description, e.g. "A problem with delivery dates on your order"]
>
> Hi [name],
>
> [What happened, in one sentence, e.g. "Between 9 pm and 11 pm on Tuesday, our reorder page showed the wrong delivery day for some orders."] [What it means for them, e.g. "Your order is safe, but the delivery day it showed was wrong."]
>
> [What we have done, e.g. "We have switched the page back to the previous version."] [What they need to do, or "You don't need to do anything."]
>
> I'll write again by [time and day] with an update. If you need anything before then, reply to this email or call [number].
>
> [Name]

### Update

> Hi [name], an update on [the problem]. [What we now know.] [What we are doing.] [What it means for you.] Next update by [time], or sooner if it's resolved.

### Resolved

> Hi [name], [the problem] is fixed as of [time]. [What caused it, in one plain sentence.] [What we have changed so it doesn't happen again.] [Anything they should check.] Thank you for your patience.

### Apology with what changed (for customers who were actually harmed)

> Hi [name],
>
> I'm sorry. [What happened to you specifically, e.g. "Your delivery arrived a week late because our page showed the wrong day."] That was our mistake, not yours.
>
> [What we are doing for you, decided by the founder, e.g. "Your next delivery is free."] [What we have changed, e.g. "Every change to the reorder page now has a test for the delivery-day rule before it can go live."]
>
> If anything else went wrong because of this, tell me and I'll put it right.
>
> [Founder's name]

---

## Incident account template

```
# Incident: [short name]
Date: [YYYY-MM-DD]   Written by: [agent draft, edited by founder]   Status: [open / closed]

## What happened
[Plain description.]

## When
- Started: [time]
- Detected: [time, by what]
- Contained: [time, how]
- Resolved: [time]

## Why
[The real cause. Then: why did our checks not catch it?]

## What was affected
[Customers (how many, who), orders, money, data. Messages sent and when.]

## What will prevent it next time
- [One change to the system, e.g. a new test, a new alert, a permission removed]
- [Lessons log entry: link]
- [Trust ladder change, if any]
```

## Filled example

*Copper Pot Mixers is a fictional company used for illustration.*

```
# Incident: Reorder page showed the wrong delivery day
Date: 2026-09-15   Written by: operations agent draft, edited by founder   Status: closed

## What happened
After a release on Monday evening, the "Reorder in one tap" page showed this
week's delivery day for orders placed after the Sunday 8 pm cut-off, instead
of the following week's.

## When
- Started: 7:40 pm Monday (release)
- Detected: 8:55 am Tuesday, a bar manager's message: "It says Tuesday, is that today?"
- Contained: 9:05 am, rolled back to the previous version
- Resolved: 4:30 pm, fix released through the normal path

## Why
A change to how dates are displayed reversed the cut-off comparison. The
acceptance test for the cut-off existed in the spec but had never been
automated, so the checks passed.

## What was affected
Six orders from five bars showed the wrong day. No payments or data were
affected. Money was: two bars needed a free case on the next van to cover
the week, approved by the founder (two cases of goods given away). All five
bars were messaged by 10 am with the correct delivery day.

## What will prevent it next time
- The cut-off acceptance test is now automated and runs on every change.
- The morning summary agent now compares shown delivery days with the schedule.
- Lessons log: "every acceptance test in a spec is automated before release."
- Trust ladder: the coding agent's customer-facing ordering changes drop from
  rung 2 to rung 1 (the founder finishes each change) until the cause is fixed;
  the track-record count resets to zero, and the job climbs back one rung at a time.
```

---

## The absence note

In a company of one, you are a single point of failure. Write this note and keep it somewhere a trusted person can find it. Do not put passwords in it; say where they are kept and how the trusted person gets access.

```
# If I am ill or unreachable
Last updated: [YYYY-MM-DD]

Trusted person: [name, phone]
How they get into the password manager or vault: [procedure, e.g. emergency access]

1. Put up a notice to customers: [where, how, draft text below]
2. Pause agents that act on their own: [how; the kill switch]
3. Platforms and where they are: hosting [ ], payments [ ], email [ ], domain [ ], accounting [ ]
4. This runbook: [link]
5. People to tell: accountant [ ], key customers [ ], suppliers [ ], lawyer [ ]
6. What can safely wait, and what cannot: [e.g. payroll date, supplier payments, tax deadlines]

Draft customer notice:
"[Company] is paused for a few days for a personal reason. Orders already
confirmed will be delivered as planned. New orders will be confirmed when we
are back. For anything urgent, contact [trusted person, email]."
```

## Related files

- [Ship checklist](ship-checklist.md)
- [Lessons log template](../context-kit/lessons-log.md)
- [Trust ladder](trust-ladder.md)
