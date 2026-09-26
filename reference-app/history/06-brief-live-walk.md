# Brief 06: walk the running app against the acceptance tests

Date: 2026-09-26. Written at the start of the step, for a check made independently of the builder. The review record at the end says what actually happened.

*Layout note added 2026-09-26 (brief 07): this brief was first written with its six parts as bold labels under one heading. It has been set out in the same sections as briefs 01 to 05; the content is unchanged apart from US spelling.*

## Goal

Verify, independently of the builder, that the running app behaves as the spec's acceptance tests say, the way a bar manager would meet it, before the book sends readers here.

## Context

- `specs/reorder-in-one-tap.md` (acceptance tests).
- The facts sheet in `../context-kit/examples/beverage-company/facts-sheet.md`.
- `README.md` (how to run it).
- The build history in steps 1 to 5.

## Constraints

- A fresh virtual environment built from the pinned requirements, not the builder's.
- A throwaway database outside the repository.
- Change nothing unless a test first shows the problem.

## Definition of done

- Every acceptance test exercised over HTTP against a running server.
- Any gap found is fixed test-first.
- The full suite, lint and format checks pass.

## Verification

- A scripted session against the live server (sign in through demo mode at chosen Bengaluru times, read pages, submit forms with the tokens the pages served), with the output kept below.

## Questions

- Stop and ask before changing any behavior the spec does not cover.

---

## Review record (2026-09-26)

**Fresh install.** Python 3.12.4, `pip install -r requirements-dev.txt` into a new environment. Full suite in the repository folder, so the facts-sheet drift test read the real, freshly edited sheet: 93 passed. Lint and format: clean.

**Live walk** (server on a throwaway database, seeded with `python -m app.seed --reset`):

| Check | Result |
|---|---|
| AT1: last three orders, newest first, with dates, totals and Repeat links | Pass |
| AT2: repeat with a changed quantity creates an order and shows the delivery day | Pass (a first attempt added one bottle, making ten; the app correctly refused, because orders go out in whole cases of six) |
| AT3: ordered Sunday 21:00, the delivery moves to the following week and the page says why; Sunday 19:00 gets that week | Pass (Monday 28 September vs Monday 5 October for Indiranagar) |
| AT4: a discontinued flavor is left out of the repeat with a note | Pass ("Guava and Pink Salt is no longer made, so it is left out of this order") |
| AT5: cancel inside 30 minutes | Pass |
| AT6: after 30 minutes, no cancel form | Pass, but see the finding below |
| No inputs for prices, terms or account details on the review page | Pass |
| A forged form token is refused | Pass |

**Finding.** 45 minutes after an order, the order page showed no cancel form, and nothing else. The facts sheet says that after the window Meera decides, and the app did say so, but only in the error shown after a late cancel attempt, which a customer on a fresh page never sees. A customer who wanted to change the order was left without a next step.

**Fix, test first.** `test_at6_order_page_says_how_to_change_after_window` added and seen failing. Then one helper, `_window_closed_message`, now supplies the same words to the order page (once the window has closed on a placed, upcoming order) and to the late-cancel error, so the two cannot drift apart. Suite: 94 passed. Lint and format: clean. Live walk repeated: the page now reads "The 30-minute window to cancel has closed. Message us on WhatsApp or at hello@copperpot.example, and Meera will decide."

**Lessons added to AGENTS.md.** One: walk the running app against the acceptance tests, including the states between steps.
