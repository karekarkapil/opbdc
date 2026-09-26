# Example brief: design

*Companion to Chapters 3 and 8, "Context Is the Company" and "Design Without a Designer", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Copper Pot Mixers is a fictional company used for illustration.* The spec for "Reorder in one tap" is written (see the [one-page spec](../../playbooks/one-page-spec.md)). Before building it properly, the founder wants three prototypes to test with five bar managers.

## The brief

> **Goal:** Build three genuinely different clickable prototypes of the reorder screen, so I can test them with five bar managers and keep the one that lets them reorder fastest with the least confusion.
>
> **Context:** Read the one-page spec for "Reorder in one tap" (the must-haves, the no list and the acceptance tests), the design system, and the customer file notes on how managers order: late at night, after closing, on a phone, often one-handed in a dim back room. Our customers mostly use mid-range Android phones on patchy mobile data.
>
> **Constraints:** Stay inside the design system: its colors, type, components and interface words. Each version must be built around a *different* idea of what matters most, and each must still meet every must-have in the spec and pass all four acceptance tests. Suggested starting points: (A) last order front and center with one big "Repeat" button; (B) a list of the last three orders with quantity steppers inline; (C) a "usuals" view that shows each product the bar buys with last quantity pre-filled. Nothing from the no list: no new products, no discounts, no payment changes, no other outlets. Prototype data only; no connection to real orders or accounts.
>
> **Done:** Three prototypes, each at its own preview link, that work on a phone. A one-paragraph note per version: the idea behind it, and what you expect a manager to find hard.
>
> **Verification:** For each version, walk through the four acceptance tests in the spec and show a screenshot of each step at phone size. Run an accessibility check: text size, color contrast, tap-target size, screen-reader labels. List any failure.
>
> **Questions:** Ask me before adding any element not in the design system, or if a must-have cannot be met in one of the three ideas.

## Why this brief works

- It asks for **different ideas, not three colorways** of the same screen. The choosing is the design work.
- It writes down the **real conditions** (tired, one-handed, dim, cheap phone, slow data), which agents otherwise replace with an imaginary large, fast screen.
- The **design system and the no list** keep every version on-brand and in scope.
- It makes the **acceptance tests** the evidence, so the prototypes are ready for a five-person test.

## What to check when it comes back

- [ ] Open all three on a real, inexpensive phone, on mobile data, in a dim room.
- [ ] Are the three versions really different, or one idea in three outfits?
- [ ] Can you complete each acceptance test without hunting? Is "Repeat" always one tap away, never inside a menu?
- [ ] Do the interface words follow the design system: plain, truthful, no blame, no tricks?
- [ ] Do not choose by preference. Take all three to five real bar managers, give them a task ("reorder last week's order with two more cases of the pineapple"), and watch in silence ([five-person test](../../playbooks/five-person-test.md)).
- [ ] Afterward, throw the rejected versions away and write the reasons in the design system.

See the [design system template](../../context-kit/design-system.md).
