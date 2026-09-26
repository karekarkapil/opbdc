# Brief 03: independent review, then fixes

Date: 2026-09-26. Written by the coding agent at the start of the step. Carried out as written; the review record at the end says what actually happened.

## Goal

Get the change reviewed by an agent that did not write it (Chapter 7: "never only the agent that wrote the code"), then fix what the review finds, so that the spec, the tests and the code agree before any continuous integration or deployment is set up.

## Context

- The reviewer gets `specs/reorder-in-one-tap.md`, `AGENTS.md`, `app/`, `tests/` and `facts/`, and nothing of the builder's reasoning, so it judges the work and not the explanation.
- The reviewer's rubric: does the code do what the spec says; is anything on the no list reachable; do the tests check what their names claim, or could any pass while the behavior is wrong; security (inputs, cookies, SQL, templates); anything a bar manager on a phone would trip over; readability for a founder.

## Constraints

- The reviewer reads and runs tests only. It changes no files.
- The builder fixes findings one at a time, each with a failing test first where a behavior changes.
- A finding the builder disagrees with is not silently dropped: it is recorded below with the reason.
- The no list and the decisions in the spec do not change without being written into the spec.

## Definition of done

- Every finding is fixed, or recorded as declined or deferred with a reason.
- `pytest` and `ruff` pass.

## Verification

- The test count before and after, and the new tests named.
- A short table of findings and what happened to each.

## Questions

- Stop and ask if a finding would change what a customer is promised or widen the spec.

---

## Review record (2026-09-26)

**The review.** A separate agent, given only the spec, `AGENTS.md`, the code and the tests, reviewed against the rubric above. It ran the suite (61 passed), tried edge cases in-process (odd form values, other bars' ids, time boundaries, a pretend-time cookie outside demo mode), changed no files, and reported ten findings. It confirmed the no list held under tampering, and that with demo mode off every page except `/healthz` returned 503 or 404 and the demo cookies were ignored.

**Findings and what happened to each.**

| # | Finding (reviewer's severity) | Outcome |
|---|---|---|
| 1 | The "one-time token" was any string the browser sent, so it stopped double taps but not another website posting an order; the cancel form had no token at all (medium) | **Fixed.** New `app/tokens.py`: tokens are signed with a server secret over purpose, account and order. Confirm and cancel both check them. `COPPER_POT_SECRET` documented; `current_account` now says the login cookie must stay SameSite=Lax or Strict. |
| 2 | Pressing Back, changing a quantity and confirming again silently returned the first order (medium) | **Fixed.** The order page now says the order was already placed at a given time and the changes were not applied, and how to change it. The notice is a fixed text chosen by a flag, never text from the URL. |
| 3 | `"²"` and 30-digit ids crashed with a 500; `/repeat/abc` returned raw JSON (low to medium) | **Fixed.** Ids must be 1 to 9 plain digits; path ids are bounded; a bad id is a friendly "Not found". |
| 4 | Demo mode: a pretend time earlier than an order reopened its cancel window; a bad pretend time was silently ignored (low) | **Fixed.** The cancel window never opens before the order was placed; `/demo` refuses a bad pretend time. |
| 5 | After a price change (D6) the manager saw the new total only after confirming (low) | **Fixed.** The review screen shows the total, and an "Update total" button recalculates it without placing anything (no JavaScript). It is the first button, so pressing Enter in a quantity box updates the total rather than ordering. |
| 6 | The list showed a discontinued product like any other (low) | **Fixed.** Struck through, with "(no longer available)". |
| 7 | Cancel was one tap and the largest button; "until 00:20" did not say which day (low) | **Partly fixed.** The deadline now names the day, and the button is no longer full width. **Declined:** a second "are you sure" step. Cancelling is the rescue for an accidental double order, it is undone by repeating the order again, and a second step slows the rescue. |
| 8 | Test gaps: forged tokens, a resend with changed quantities, the demo clock outside demo mode, AT3 on the review screen, AT8 not checking the lines of historic orders, an untested race branch that could raise `TypeError` | **Fixed.** A test for each; the race branch now re-raises anything that is not a token clash. |
| 9 | A bar can open its own cancelled or older orders by URL and repeat them (low) | **Declined.** Repeating one's own order is not on the no list, and repeating an order cancelled by mistake is useful. The list stays the last three (D5). |
| 10 | Readability: why routes are in a table, and how a request gets its account | **Fixed.** Two short comments in `app/main.py`. |

**Tests changed, and why.** The `confirm` helper used to post made-up tokens (`"token-1"`, `"same"`, `"a"`), which only worked because the app accepted any token. That was the gap in finding 1, hidden by the tests. The helper now opens the review screen and uses the token the page served, as a phone would, and a new `cancel` helper does the same on the order page. No assertion was loosened.

**Runs.** Before the fixes, with the new tests: `11 failed, 63 passed` (the race test passed already, since that branch worked; it is kept as a guard). After the fixes, one test still failed, and the fault was in the test, not the app: it took a cancel token from an order page that now correctly had no cancel form, so the token was empty and the app refused it for the wrong reason (400, not 409). It now issues a genuine token, so only the time rule can refuse. Final: `74 passed in 1.78s` with warnings as errors; `ruff check` and `ruff format --check` clean.

**Lessons added to AGENTS.md.** Two: an idempotency key is not a security token; drive forms in tests with what the page served.
