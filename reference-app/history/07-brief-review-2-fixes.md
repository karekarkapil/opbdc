# Brief 07: fixes from the second companion review

Date: 2026-09-26. Written by the coding agent (Claude) from the plan it made at the start of the step, and written down at the end of it, so the review record below says what actually happened in the order it happened.

## Goal

Close every finding the second independent review of the companion repository (kept with the book's manuscript, not in this repository) raised against the reference app: nine "should fix" items and ten nits. Why: readers arrive here from Chapters 6, 7 and 9, and every place where the app, its CI or its notes say something untrue, or stop checking something they claim to check, teaches the opposite of the book.

## Context

- The review's findings for the reference app: a stale CI path in the deploy notes and brief 05; CI not triggered by the facts sheet the drift test reads; copy-out steps that miss the cache path; type checks promised by Chapter 7 (and Chapter 9 and the ship checklist) but never run; two customer-facing facts typed into templates; a README walk that fails on the newest order; a "plan" step no history file contains; a missing-database message that suggests the demo seed script on a live site; `AGENTS.md` forbidding edits outside the folder while the CI file lives outside it.
- The nits: "five problems" should be six; the spec's list of additions is incomplete; British spellings; unpinned packages pulled in by the dev tools; a total shown for quantities that cannot be placed; the CI concurrency group; no Windows form of `DEMO_MODE=1`; an empty `.github/workflows/` folder left in this folder; brief 06 laid out differently from briefs 01 to 05; the two facts-sheet questions left open in brief 04.
- `AGENTS.md`, the spec, the facts sheet, and briefs 01 to 06.

## Constraints

- Tests first for every change in behavior: the failing test, seen failing, then the code.
- The full suite stays green; no test is weakened.
- Type checks with a pinned mypy in `requirements-dev.txt`, configured in `pyproject.toml`, run in CI, and the code made to pass; only if that proved unreasonable, reword the claims instead.
- The virtual environments live outside the repository. No git commands. Files that must be deleted are listed, not deleted.
- History is not rewritten: corrections to earlier briefs are dated notes.
- No em-dash or en-dash characters, no Cyrillic characters, in any file.

## Definition of done

- Every finding fixed, or recorded below with the reason it was handled differently.
- `pytest -W error`, `ruff check`, `ruff format --check`, `mypy` and `pip-audit -r requirements.txt` pass.
- A clean install of both requirement files matches the pins exactly.
- The changed pages walked on a running server.

## Verification

- The red run and the green run, with counts.
- The first mypy run on the code as it stood, and the last.
- A `pip freeze` from a fresh environment compared with the pins.
- A search for the old CI path, and for British spellings.

## Questions

- Stop and ask if a fix would change what a customer is promised, or change a fact rather than where a fact is read from.

---

## Review record (2026-09-26)

**Tests written first.** Three new tests and three changed ones, all in `tests/test_orders.py` and `tests/test_facts_sheet.py`:
- `test_the_pages_take_the_cutoff_and_free_delivery_from_the_facts_file`: runs the app on the real facts file (the control) and on a copy with a Saturday 6 pm cut-off and free delivery from three cases, and requires the list and the review screen to follow.
- `test_a_missing_database_suggests_the_seed_script_only_in_demo_mode`: the demo still says `python -m app.seed` (the control); a live app says the database is missing and never mentions the seed script.
- `test_no_total_is_shown_for_quantities_that_cannot_be_placed`: the newest Tin Lantern order (9 bottles once the discontinued guava is left out) shows the "Before you confirm" note and no total; the third order (two whole cases) still shows one.
- The whole-cases and over-the-limit tests now also check the US spelling of their messages ("flavors can be mixed", "bottles of each flavor").
- The facts-sheet guard now also compares the time zone and the list of products no longer sold, and its positive control now drifts both.

**Red run.** `7 failed, 90 passed`: the five tests above that check page text or behavior, and both facts-sheet tests, which could not find a time zone or a "No longer sold" line in the sheet. The new facts-file test failed on its second pass, after passing its control.

**Type checks.** mypy 2.3.1, pinned, with its settings in `pyproject.toml`: every function body is checked, annotated or not (`check_untyped_defs`), with strict equality and unreachable-code warnings; not strict mode, so annotations are not required everywhere. The first run on the code as it stood: `Found 5 errors in 4 files`. Two were in the app: an empty list in `app/money.py` with no element type, and the `ROUTES` table in `app/main.py`, inferred as a list of plain functions. Three were in the tests: a delivery date that may be `None`, and a route's `methods` that may be `None`. The test fixes add a check (`assert result.date is not None`) or an empty fallback that would make the route test fail, not pass, so neither loosens a test. Last run: `Success: no issues found in 15 source files`. CI runs `mypy` between lint and tests.

**What changed, finding by finding.**

| Finding | Outcome |
|---|---|
| Stale CI path | **Fixed.** `deploy/README.md` links the file at the repository root; brief 05 has a dated note. The move itself is recorded here: after brief 05, the CI file went from `reference-app/.github/workflows/ci.yml` to the companion repository's root as `.github/workflows/reference-app-ci.yml`, because GitHub runs workflows only from there. No history file had recorded it. A search now finds the old path only in brief 05's original text and in the notes that describe the move. |
| CI misses the facts sheet | **Fixed.** Both `paths` filters include `context-kit/examples/beverage-company/facts-sheet.md`, with a comment saying why. |
| Copy-out steps miss the cache path | **Fixed** in the workflow's opening comment and the README. |
| Type checks promised, not run | **Fixed** as above. The workflow's header no longer claims "the order Chapter 7 lists them"; it names the checks Chapter 7 lists and the order they run in. |
| Facts typed into templates | **Fixed, test first.** The cut-off on the list, "free from two cases" on the review screen, and the cut-off and cancel window in the demo page's hint are rendered from the facts file. The number is written in words, as the sheet writes it. |
| README AT2 walk fails on the newest order | **Fixed, differently from the review's wording.** The review suggested "the second or third order". Walking it found that the second order is kokum only, so it has no pineapple box to change: the spec's no list forbids adding a product. The walk now names the third order (pineapple and chilli), was run against the server, and confirmed 12 pineapple and 6 chilli for Monday 28 September 2026, Rs 9,600. |
| "plan" step in the README | **Dropped.** No brief has a separate plan. |
| Seed suggested outside demo mode | **Fixed, test first.** Outside demo mode the page says only "The database has not been created." `deploy/README.md` now lists five things before real customers, the new one being a live database created without the seed script, with the one-line command that creates an empty database (checked: it creates the four tables and nothing else). |
| `AGENTS.md` and the file outside the folder | **Fixed.** Layout names the two files outside this folder that belong to it (the CI file and the facts sheet); "Never" allows editing them only after asking; "Ask before you" lists them. |
| "five problems" | **Fixed:** six (three in brief 02, two in brief 04, one in brief 06). |
| Spec additions list | **Fixed:** it now also names the AT1 to AT4 numbers and part 6's sentence about them, part 8's note on AT5 to AT7, and part 9's note in brackets. |
| British spellings | **Fixed.** The pages now say "flavor" (the review screen's hint and two error messages), with the matching test strings; the rest of this folder, specs and history included, now uses US spelling too (flavor, grayed, honor, behavior, labeled). |
| Unpinned dev packages | **Fixed.** The ten packages pulled in by pytest, httpx2 and mypy are pinned, each with what needs it. |
| Total shown for an unplaceable repeat | **Fixed, test first.** |
| CI concurrency group | **Fixed:** `${{ github.workflow }}-${{ github.ref }}`. |
| No Windows form of `DEMO_MODE=1` | **Fixed:** PowerShell and Command Prompt, each setting the variable on its own line (a `set X=1 && ...` one-liner would include a trailing space, and the app requires exactly `1`). |
| Empty `.github/workflows/` in this folder | **Not deleted here** (this agent cannot delete files). It holds no files, so git does not track it; delete the folder locally. |
| Brief 06 layout | **Fixed:** set out in the same sections as briefs 01 to 05, with a dated note; content unchanged apart from spelling. |
| Brief 04's open questions | **Answered on the facts sheet,** which now states that its times are Bengaluru time (Asia/Kolkata) and lists Guava and Pink Salt as no longer sold, with a change-history row. The drift test checks both. `facts/facts.toml` changed only in comments. Brief 04 has a dated note. |

**Other changes.** `.mypy_cache/` added to `.gitignore` and `.dockerignore`; the seed's comment on the discontinued flavor now points at the sheet; README test counts (97) and the line count of `app/` (about 1,050) updated; the history index's note on later edits now lists the dated notes and the spelling change.

**Clean install.** New virtual environments outside the repository, Python 3.12.4 and 3.13.13, `pip install -r requirements-dev.txt`: 31 packages, `pip check` clean, and `pip freeze` identical to the pins in the two files.

**Walking the changed pages.** The app ran on a throwaway database outside the repository, seeded with `python -m app.seed --reset`. The demo page, the list and the review of the newest order were rendered at 375 pixels wide in a headless browser: the cut-off in the hints read "Sunday 8 pm", and the newest order showed the "Before you confirm" note and no total, with nothing out of place. Over HTTP: Banyan Street Cafe's one-case review showed "Rs 150 (free from two cases)"; with no database, the live app answered 503 "The database has not been created." and the demo app added "Run: python -m app.seed". The AT2 walk is described above.

**Final runs.** Python 3.12.4: `97 passed in 2.36s` with warnings as errors; Python 3.13.13: `97 passed in 2.02s`. `ruff check`: all checks passed; `ruff format --check`: 27 files already formatted; `mypy`: no issues in 15 source files; `pip-audit -r requirements.txt`: no known vulnerabilities found. The secret scan was not run locally (gitleaks is not installed on this machine); CI runs it first on every change. The workflow file was parsed to confirm its triggers, concurrency group and step order.

**Lessons added to AGENTS.md.** Three: a fact typed into a template is invisible to the drift test; when a file moves, search every file for its old path and record the move; a claim about the checks is checked like code (CI must watch every file the tests read and run every check the docs promise).

**Questions raised.** None needed stopping for. Stating the time zone and the discontinued flavor on the facts sheet writes down what the app already assumed; no fact a customer is told changed.
