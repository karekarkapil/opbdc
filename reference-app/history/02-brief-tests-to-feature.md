# Brief 02: from failing tests to the feature

Date: 2026-09-26. Written by the coding agent at the start of the step. Carried out as written; the review record at the end says what actually happened.

## Goal

Make all 58 tests from brief 01 pass with the smallest readable code that does what the spec says, so a bar manager can repeat an order from a phone, see the delivery day, and cancel within thirty minutes. The code should be readable by a founder in an hour.

## Context

- `specs/reorder-in-one-tap.md`, especially decisions D1 to D12.
- `AGENTS.md`: layout, conventions, the never list, the lessons.
- The tests in `tests/`, which are the contract. `app/db.py` already holds the schema and queries.

## Constraints

- Do not change any test to make it pass. If a test looks wrong, stop and say which and why.
- Keep the rules (`app/orders.py`, `app/delivery.py`) free of web code, and the delivery rule free of the clock, so they can be tested alone.
- Server-rendered HTML, no JavaScript, readable and tappable on a small phone.
- No new dependencies beyond brief 01.
- No route beyond the eight the AT8 route test lists.
- A seed script with believable demo data for Copper Pot Mixers.

## Definition of done

- `pytest` passes: 58 tests, 0 failures, no warnings.
- `ruff check .` and `ruff format --check .` pass.
- `python -m app.seed` creates a demo database, and the app starts with `DEMO_MODE=1 uvicorn app.main:app`.
- Each page checked by hand in a phone-sized browser window.

## Verification

- Paste the test summary line.
- Start the app on the seeded data and walk AT1 to AT7 by hand in a narrow window, as a non-coder reviewer would. Report anything that passes the tests but looks wrong to a person.

## Questions

- Stop and ask if a test and the spec disagree.
- Stop and ask if passing a test seems to need a route, a table or a dependency not already allowed.

---

## Review record (2026-09-26)

**What was built.** `app/delivery.py` (the rule, about 40 lines of logic), `app/facts.py` (loads and checks the facts file), `app/orders.py` (repeat, quantities, confirm once, cancel window), `app/main.py` (eight routes in one table, the sign-in seam, demo mode), five templates, one stylesheet, and `app/seed.py`.

**How the tests went from red to green.**
1. Delivery rule and facts loader first: the 22 unit tests passed on the first run.
2. With the pages in place: `25 failed, 33 passed`. Every failure was the same error: `SQLite objects created in a thread can only be used in that same thread`. FastAPI runs plain dependencies in a worker thread and `async` routes on the main loop, so a request's connection crossed threads. Each request has its own connection and uses it one step at a time, so the fix was `check_same_thread=False` in `db.connect`, with a comment saying why.
3. Then `1 failed, 57 passed`: the AT8 route test found no routes at all. The installed FastAPI (0.141.1) wraps an included router in a private `_IncludedRouter` object instead of copying its routes into the app. The brief says not to bend a test, and the test's intent (the app serves exactly these eight routes) was right. The code changed instead: the routes are now one explicit table, `ROUTES` in `app/main.py`, registered directly on the app. It also reads better.
4. `58 passed`, also with warnings turned into errors (`pytest -W error`).

**Caught on self-review before the first run.** The GET route for an order page first had extra `status_code` and `message` parameters, so the cancel route could reuse it. In FastAPI every parameter of a route function becomes something the URL can set: anyone could have sent a bar a link that printed any message on a genuine order page. Split into a private `_order_view` helper that no URL reaches.

**Lint.** `ruff` flagged `Depends(...)` in argument defaults (rule B008) on every route. Rewritten in the current FastAPI style with two type aliases, `Conn` and `Account`, which also made the signatures short enough to drop the formatter overrides.

**Walking the pages.** The seeded app was run with `DEMO_MODE=1` and each screen was rendered at 375 pixels wide (a common phone width) in headless Chrome, inside a 375-pixel frame, because headless Chrome will not open a window that narrow and silently crops a wider one. The walk covered AT1 (list), AT4 (review with a discontinued product), AT2 (confirmation), the all-zero error, and AT3 (pretend time Tuesday 23:30). Three things passed every test but were wrong to a person (the first and third seen on the rendered screens, the second found by reading the template behind the Details button during the walk):
- The quantity boxes were different widths when a product name wrapped to two lines. Fixed in CSS.
- The Details page of a month-old order would have said "Order confirmed" and "so it arrives on Thursday 27 August", in the future tense. Now titled "Past order", and the reason is only shown for upcoming deliveries.
- The confirmation gave the date placed but not the time, while offering a cancel deadline by the clock. It now says "Placed Sat 26 Sep 2026 at 10:55."

Each got a failing test first (2 failed, 59 passed), then the fix. A test for the seed script was added at the same time, as a guard for the demo data.

**Final run.** `61 passed in 1.13s`, `ruff check` clean, `ruff format --check` clean.

**Lessons added to AGENTS.md.** Four: SQLite and FastAPI threads; route parameters are URL inputs; check the installed framework's behavior instead of assuming it; walk the pages at phone width, because tests do not see what a person sees.

**Questions raised.** None needed stopping for.
