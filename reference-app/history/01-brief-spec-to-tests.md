# Brief 01: from spec to failing tests

Date: 2026-09-26. Written by the coding agent at the start of the step, from the founder's request for a reference app. Carried out as written; the review record at the end says what actually happened.

## Goal

Turn the "Reorder in one tap" spec from Chapter 6 into three things the rest of the build can stand on: a spec file precise enough to build from, a standing instruction file for the project, and automated tests for every acceptance test, shown failing before any feature code exists. Why: the tests are the contract. If they are written after the feature, they tend to describe what was built rather than what was promised.

## Context

- Chapter 6, the one-page spec for Copper Pot Mixers, which sells craft cocktail mixers to bars and cafes. Its four acceptance tests, its no list, and its risk line ("a confirmation step and a thirty-minute cancel window").
- Chapter 3, what a facts sheet and an agent instruction file contain.
- Chapter 7, the build loop and the workshop box.
- The spec in Chapter 6 leaves several things open that code cannot leave open: the cut-off day and time, the time zone, whether cancelled orders count among the "last three", which price a repeat uses, what happens on a double tap, and how the bar is identified.

## Constraints

- Everything stays inside `reference-app/`. No git commands.
- The spec's must-haves and no list are not to be widened. Where a decision is needed, record it in the spec under "Decisions made while building", with the reason.
- Facts a customer might be told (cut-off, delivery day, cancel window) live in one facts file, never in code.
- No login system. Sign-in is a managed service's job (Chapter 7); the reference app gets a clearly labelled demo mode instead.
- Pinned dependencies only; as few as will do the job.
- No em-dash or en-dash characters, no Cyrillic characters, in any file.

## Definition of done

- `specs/reorder-in-one-tap.md`: the nine parts, the four acceptance tests from the book, the extra tests the risk line implies, and the decisions.
- `AGENTS.md` (and `CLAUDE.md` pointing to it) on one to two pages.
- `facts/facts.toml` with the delivery schedule and order limits.
- A test suite with one or more tests per acceptance test, unit tests for the delivery-day logic, and edge cases.
- A skeleton app with no feature code, so the tests fail on behavior, not on missing files.

## Verification

- Run the suite and show it failing, with the counts.
- Check that every acceptance test in the spec has a test whose name carries its number.

## Questions

- Stop and ask if the spec seems to require a login system, payments, or anything on the no list.
- Stop and ask if a decision would change what the customer is promised (for example, moving the cut-off).

---

## Review record (2026-09-26)

**What was produced.** `specs/reorder-in-one-tap.md` (the book's nine parts unchanged, AT5 to AT8 added from the risk line, the no list and the data rule, and twelve decisions D1 to D12 with reasons); `AGENTS.md` and `CLAUDE.md`; `facts/facts.toml`; pinned `requirements.txt` and `requirements-dev.txt`; `app/db.py` in full (the test fixtures need a schema to put data in); stubs for `app/delivery.py`, `app/facts.py` and `app/main.py` that raise or have no routes.

**Tests written.** 58 in all: 18 acceptance tests (AT1: 3, AT2: 2, AT3: 3, AT4: 2, AT5: 1, AT6: 1, AT7: 2, AT8: 4), 22 delivery-day and facts-file tests, 18 edge-case tests for the decisions.

**First red run.** `55 failed, 3 passed`. Three tests passed on an app that did nothing: the cross-account test (everything was 404, as it expected), the unknown-order test (same), and the "prices and accounts unchanged" test (nothing happened, so nothing changed). A test that passes before the feature exists proves nothing. Each was given a positive control in the same test: the same request must succeed for the bar's own order, and the flow must actually create and cancel an order before "unchanged" is checked.

**Second red run.** `58 failed in 1.71s`. Every test now fails for a reason the feature will fix (404, `NotImplementedError`, a missing page), not because of a broken import.

**Other changes after review.**
- The test run printed a deprecation warning: this Starlette version wants `httpx2` for its test client instead of `httpx`. Checked the package on PyPI (maintained under the pydantic organization, and Starlette's own code imports it first) and swapped the pin.
- `ruff` flagged four long lines in the fixtures; rewritten with a small helper.

**Checks.** Every acceptance test number in the spec has at least one test named for it. `ruff check` and `ruff format --check` pass.

**Lessons added to AGENTS.md.** Two: positive controls for "must not" tests; read the warnings in a test run.

**Questions raised.** None needed stopping for. The spec's open question (do owners want approval?) stays open and unbuilt.
