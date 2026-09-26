# The five-person test

*Companion to Chapter 8, "Design Without a Designer", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

The simplest design test there is, and the one most often skipped: **watch five real people try to do their most common tasks with your design, before it launches.** It costs an afternoon. This file holds the prototyping habit that feeds it, the five-step protocol from Chapter 8, a task sheet, an observation sheet, and what agents may and may not do around it.

## How to use it

1. Build three genuinely different prototypes of the key screen, all within your [design system](../context-kit/design-system.md) (see the [design brief example](../briefs/examples/design.md)).
2. Run the protocol below with five real people, on the phones and in the conditions your design system describes.
3. Keep the version that let them complete the job fastest and with the least confusion. Throw the others away.
4. Fix the worst problem first, then test again.

---

## Before the test: the prototyping habit

- [ ] **Three genuinely different versions** of the key screen, all within the design system, each built around a different idea of what matters most to the customer.
- [ ] Each version meets every must-have in the [spec](one-page-spec.md) and can pass its acceptance tests.
- [ ] **Do not choose by preference.** Your taste decides what is acceptable; customers decide which one works.
- [ ] Paper is allowed. A sketch on a napkin, shown to a customer at the end of a shift, beats a beautiful mockup shown to a friend.

## The protocol (Chapter 8)

1. **Recruit five real customers,** or people exactly like them. Not friends, not other founders.
2. **Give them tasks, not a tour.** Use the acceptance tests from your spec, written as tasks.
3. **Watch in silence.** Do not help, explain or defend. When they hesitate, note where. When they fail, note why.
4. **Ask afterward,** not during: what did you expect to happen here?
5. **Fix the worst problem first,** then test again.

Test on the real device and in the real conditions: the phone they use, the connection they have, where they are standing. If your customers use your product at one in the morning in a dim back room, do not test at noon at your desk.

## Task sheet (write before the session)

Turn each acceptance test into a task in the customer's words. Never name the button you want them to find.

| # | Task, as you will say it | The acceptance test it comes from | Done means |
|---|---|---|---|
| 1 | [e.g. "Reorder what you ordered last week, but with two more cases of the pineapple mixer."] | [Given a past order, when they tap Repeat, change one quantity and confirm...] | [a new order with the changed quantity; they saw the delivery day] |
| 2 | | | |
| 3 | | | |

## Observation sheet (one per person, per version)

Person: [role, business type; no names or contact details in files agents read]  Version: [A / B / C]  Date: [YYYY-MM-DD]  Device and conditions: [ ]

| Task | Completed? | Time | Where they hesitated | Where they failed, and why | What they expected (asked afterward) |
|---|---|---|---|---|---|
| 1 | [yes / no / with help] | [mm:ss] | | | |
| 2 | | | | | |
| 3 | | | | | |

## After five people

| Version | Tasks completed (of 5 people x tasks) | Median time on task 1 | The worst problem seen |
|---|---|---|---|
| A | | | |
| B | | | |
| C | | | |

- [ ] **Keep:** [version], because [it let them finish fastest with least confusion].
- [ ] **The worst problem, fixed first:** [what, and the change].
- [ ] **Test again** after the fix: [date].
- [ ] **Throw the others away,** and write the reasons into the design system, so no agent rebuilds a rejected idea.
- [ ] The customers' own words go into the [customer file](../context-kit/customer-file.md), dated.

## What agents may and may not do

| Agents may | You must |
|---|---|
| Recruit from your customer list (drafting invitations you send) | Choose who is invited, and send the invitations yourself |
| Schedule the sessions | Be there, and watch at least the key moments yourself |
| Transcribe recordings (with each person's permission) | Get that permission before recording |
| Summarize where each person hesitated, from your notes and the transcripts | Read the summary against what you saw; the flicker of confusion on a face is not in any transcript |
| Build the prototypes, within the design system | Decide which version survives |

## Illustration

*Copper Pot Mixers is a fictional company used for illustration.* For "Reorder in one tap", the founder asks five bar managers, at the end of their shifts, in their own back rooms, on their own phones, to "reorder what you ordered last week, but with two more cases of the pineapple mixer", and then to "tell me which day it will arrive". She says nothing while they try each of the three prototypes from the design brief. The version she keeps is the one where every manager found "Repeat" without looking for it and read the delivery day aloud without being asked. The worst problem, in the version she keeps, is a quantity stepper too close to the confirm button for a tired thumb; it is fixed first, and the test is run again.

## Where this breaks

- **Testing with friends.** Friends are kind. Customers are busy. Only the second tells you the truth.
- **Helping.** The moment you explain, you are testing your explanation, not your design.
- **Choosing by taste after all.** If you keep the version you liked instead of the one that worked, you have run a ceremony, not a test.
- **Wrong conditions.** A design that works on your large screen at noon can fail on a cracked phone at one in the morning.

## Related files

- [Design system](../context-kit/design-system.md): the real conditions, the interface words and the accessibility minimums the prototypes must meet.
- [Design brief example](../briefs/examples/design.md): the brief for the three prototypes.
- [One-page spec](one-page-spec.md): the acceptance tests the tasks come from.
