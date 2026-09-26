# Brief 04: match the company's own facts sheet

Date: 2026-09-26. Written by the coding agent at the start of the step, after the coordinator of the companion repository reported a cross-file contradiction. Carried out as written; the review record at the end says what actually happened.

## Goal

Make the app tell customers exactly what Copper Pot Mixers' facts sheet says. Readers go from the Chapter 3 context kit and the Chapter 6 spec straight into this app, and at the time of this brief the app contradicts both: it placed the company in London, priced in pounds per pack, used a Tuesday 23:00 cut-off with Thursday delivery, and gave the bars 14-day and 30-day credit terms that the company does not offer.

## Context

- The source of truth: `context-kit/examples/beverage-company/facts-sheet.md` in this repository (last checked 2026-09-01). Bengaluru; time zone Asia/Kolkata; prices in rupees per 750 ml bottle, sold in cases of six, mixed cases allowed, minimum one case; weekly cut-off Sunday 8 pm for delivery that week; a fixed delivery day by area, Monday to Thursday only, never Fridays or weekends; "other areas: ask, Meera confirms the day"; delivery free from two cases, otherwise Rs 150; payment due on delivery, no credit terms; cancel within 30 minutes, after that Meera decides. The founder is Meera.
- The same folder's `specifications.md` and `decision-log.md`: the spec's open question about owner approval was answered (two owners said yes, one asked for a notification, now in the backlog).
- `playbooks/one-page-spec.md`: the Chapter 6 spec, unchanged.
- Brief 03's review fixes, already made.

## Constraints

- Every acceptance test from Chapter 6 stays, and so do AT5 to AT8 and the 30-minute cancel window.
- Tests change only where a fact changed (a price, a day, a time zone), and each such change is listed below. No test is weakened: where the old test checked a rule that no longer exists (London's clock change), it is replaced by a test of the rule that does (India's half-hour offset from UTC).
- New rules the facts sheet brings (whole cases, the delivery charge, days by area, "Meera confirms") get failing tests first.
- The app's machine-readable copy of the facts (`facts/facts.toml` and the seed prices) must not drift from the sheet again: add a test that compares them when the sheet is present.
- The facts sheet lists no discontinued product, but AT4 needs one to demonstrate. Use one clearly marked as discontinued in the seed and tests, and say so in the report so the sheet's owner can decide whether to record it.

## Definition of done

- Facts file, seed data, spec, tests, templates, README notes and AGENTS.md all say Bengaluru, rupees, Sunday 8 pm, area days, no credit.
- `pytest` passes with warnings as errors; `ruff` passes.
- The pages walked again at phone width.

## Verification

- The red run after the tests change, and the green run after the code.
- A grep for leftovers: London, pound signs, pence, Tuesday 23:00, Thursday delivery, "30 days", "14 days".

## Questions

- Stop and ask if the facts sheet and the Chapter 6 spec disagree.
- Stop and ask if a fact needed by the page is missing from the sheet.

---

## Review record (2026-09-26)

**Why this step happened.** A reviewer working across the whole companion repository noticed that this app contradicted the company it belongs to. The fault was the builder's: brief 01 read Chapters 3, 6, 7 and 9 but not the company's own context kit, and filled the gaps with invented facts. Nothing in the book's text was wrong. The lesson is in AGENTS.md.

**What changed.**
- `facts/facts.toml`: rewritten from the facts sheet, with each value next to the sentence it comes from. Bengaluru time; Sunday 8 pm cut-off; the twelve areas and their days; no deliveries Friday to Sunday; cases of six; Rs 150 delivery under two cases; 30-minute cancel; rupees. One page rule, not a company fact, is marked as such: at most 60 bottles of a flavor.
- Delivery rule (`app/delivery.py`): the delivery day now depends on the bar's area. This forced a real design question. With a Sunday cut-off, "after the cut-off" cannot mean "after this week's cut-off": a manager ordering at 1 am on Monday is after Sunday's cut-off, but also before next Sunday's. The rule now compares the delivery day with the soonest day the area is ever served, today included. If the order goes later than that, it missed a cut-off, and the page says which delivery it missed and why (AT3). This is decision B2 in the spec.
- New rules from the sheet, each with failing tests first: whole cases of six, flavors mixed (B8); the delivery charge (B14); a day by area; "Day to be confirmed, Meera will message you" for areas without one (B15); after the cancel window, "Meera will decide" (AT6).
- Money: paise, written the Indian way (Rs 1,40,000), in `app/money.py`.
- Seed data: the five flavors and prices from the sheet, 750 ml bottles, "Due on delivery" for every bar (the 14-day and 30-day credit terms are gone). Four fictional bars: Indiranagar (Mondays), Koramangala (Tuesdays), Jayanagar (Thursdays, no orders yet) and Whitefield (no fixed day).
- Spec: the facts sheet named as the source of truth; the owner-approval question marked answered, from the company's specifications file; decisions renumbered B1 to B15 so they cannot be confused with the company decision log's D-numbers.
- A new guard, `tests/test_facts_sheet.py`, reads the facts sheet and fails if the cut-off, cancel window, case size, delivery charge, bottle size, payment terms, area days or prices differ from the app's copies. It has a positive control: a copy of the sheet with a changed cut-off and price must be caught.

**Tests changed, and why.** Every change is a fact change, not a loosening:
- Fixtures: London to Bengaluru, pence to paise, packs to bottles in whole cases, bars given areas, products and prices from the sheet. Expected dates, totals and messages follow the new facts (for example "Rs 3,270", "Monday 28 September 2026", "Add at least one case", the 60-bottle limit).
- Removed, because the rule they tested no longer exists: the London clock-change test, the summer and winter UTC tests, the Tuesday and Thursday schedule tests, and the "Friday noon cut-off, Monday delivery" schedule test.
- Replaced by tests of the rules that do exist: IST's half-hour offset at the cut-off (14:29:59 UTC is in time, 14:30 UTC is not); a server still on Sunday while Bengaluru is on Monday; the cut-off boundary for Monday, Tuesday, Wednesday and Thursday areas; the cut-off written as the sheet writes it ("Sunday 8 pm"); a facts file with a Friday delivery day, or an area listed twice, is refused.
- The discontinued product was "Elderflower Cordial"; it is now "Guava and Pink Salt", marked in the seed as not on the sheet because it is no longer sold. The facts sheet lists no discontinued product, so this one is an addition, flagged for the sheet's owner.

**Runs.**
1. Tests rewritten, code not yet: `33 failed, 55 errors, 1 passed` (the errors were fixtures calling the new schema).
2. After the code: `89 passed`.
3. The facts-sheet guard, first run: 1 failed. The fault was in the test: the sheet's change-history table ("| 2026-07-01 | Tender Coconut and Lemongrass price | Rs 520 | Rs 560 |") matched the price-row pattern. Parsing was limited to the Products section. Then `91 passed`.
4. Walking the re-localized pages at 375 pixels (the list, AT4, a whole-cases error, AT2, AT1 for the cafe, AT3 at a pretend Sunday 9:30 pm, and a Whitefield bar) found two things the tests did not: rupee amounts wrapped onto two lines on the confirmation, and the whole-case rule surfaced only after tapping Confirm (leaving out the discontinued guava makes 9 bottles). A failing test for the second, then a "Before you confirm" note on the review screen and a CSS fix for the first.
5. Final: `93 passed in 2.35s` with warnings as errors; `ruff check` and `ruff format --check` clean.

**Leftover check.** A search outside `history/` for London, pound signs, pence, 23:00, "Tuesday 23", 30-day or 14-day terms, Elderflower, Harbour and Europe/ finds only the lesson line in AGENTS.md that describes the mistake. `history/` keeps the old facts on purpose, because it is the record of what happened.

**Lessons added to AGENTS.md.** Two: read the company's own files before inventing a fact; parse only the section of a document you mean.

**For the facts sheet's owner.** (1) The demo needs a discontinued product for AT4; "Guava and Pink Salt" is used, and is not on the sheet. (2) The sheet does not name a time zone; the app assumes Bengaluru's (India Standard Time).

*Note added 2026-09-26 (brief 07): both questions are now answered on the facts sheet, which lists Guava and Pink Salt as no longer sold and states that its times are Bengaluru time. `tests/test_facts_sheet.py` checks both.*
