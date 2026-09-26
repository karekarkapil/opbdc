# AGENTS.md: standing instructions for this project

Last checked: 2026-09-26. Read this before every task. Keep it under two pages; detail belongs in `specs/` and `history/`.

## What this is

The reorder page for Copper Pot Mixers (fictional), Bengaluru, which sells craft cocktail mixers to independent bars and cafes. The founder is Meera. A bar manager, on a phone, late at night, sees their last three orders, repeats one with adjusted quantities, confirms, and is told the delivery day. That is the whole product. The spec is `specs/reorder-in-one-tap.md`; if the code and the spec disagree, the spec wins, and you ask.

## Layout

- `specs/`: one spec per feature. The acceptance tests there are the contract.
- `facts/facts.toml`: the app's copy of the company facts sheet (`../context-kit/examples/beverage-company/facts-sheet.md`): cut-off, delivery days by area, time zone, cases, delivery charge, cancel window, currency. The sheet is the source of truth; `tests/test_facts_sheet.py` fails if the two disagree.
- `app/main.py`: the web routes. `app/orders.py`: the rules (last three, repeat, confirm, cancel). `app/tokens.py`: signed form tokens. `app/delivery.py`: the delivery-day calculation, pure and clock-free. `app/db.py`: SQLite schema and queries. `app/facts.py`: loads the facts file. `app/money.py`: rupees, written the Indian way. `app/seed.py`: demo data, with prices from the facts sheet. `app/templates/`, `app/static/`: the pages.
- `tests/`: `test_acceptance.py` (one or more tests per acceptance test, named `test_atN_...`), `test_delivery.py`, `test_orders.py`, `test_facts_sheet.py`.
- `history/`: the brief for each step and its review record. Add one for every change you make.
- `deploy/`: optional Dockerfile and deployment notes.
- Outside this folder, two files belong to it: `../.github/workflows/reference-app-ci.yml`, its CI (GitHub runs workflows only from the repository root), and the facts sheet above, which `tests/test_facts_sheet.py` reads.

## Commands

```
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements-dev.txt
python -m app.seed                 # creates data/copper_pot.db with demo data
DEMO_MODE=1 uvicorn app.main:app --reload
pytest                             # must pass before you hand anything back
ruff check . && ruff format --check .
mypy                               # type checks; settings in pyproject.toml
```

## Conventions

- Tests first. For a new behavior, write the failing test, show it failing, then write the code.
- Money is integer paise (Rs 540 is 54000). Never floats. Quantities are bottles; orders are whole cases of six.
- Times are timezone-aware. Store UTC; judge the cut-off in Bengaluru time (Asia/Kolkata), from the facts file.
- Anything a customer is told as a fact (a day, a time, a price, a charge) comes from the facts sheet, through `facts/facts.toml` or the seed. If the sheet does not say it, the page does not say it: hand it to Meera.
- The clock is injected (`app.state.clock`), never read directly in the rules, so tests can set the time.
- SQL uses parameters, never string formatting. Templates are autoescaped; do not mark user data safe.
- Server-rendered HTML that works without JavaScript on a small phone screen. Tap targets at least 44 pixels high.
- Small changes: one behavior per change, reviewable in a few minutes.

## Never

- Never add a way to change prices, payment terms, discounts or account details. The spec's data rule forbids it, and `test_at8_only_the_expected_routes_exist` will fail.
- Never take the account, the price or the product list from the form. The account comes from the session; prices and products come from the database.
- Never build sign-in, passwords or payments. Those are managed services. `current_account_id` in `app/main.py` is the one seam where a login provider plugs in.
- Never weaken, skip or delete a test to make it pass. If a test looks wrong, stop and ask.
- Never add a dependency without pinning it in `requirements.txt` or `requirements-dev.txt` and saying why in your hand-back.
- Never put secrets in code, facts or history. There are none in this project, and there should stay none.
- Never edit files outside this folder, except the two listed under Layout, and those only after asking.

## Ask before you

- change anything in `specs/` or `facts/facts.toml` (a fact changes in the facts sheet first);
- edit the CI file or the facts sheet, the two files outside this folder;
- change what a customer is shown about delivery days or cancelling;
- add a page, a route or a table.

## Hand-back checklist

Tests pass (paste the summary line), lint and type checks pass, the relevant `history/` brief has its review record, and any lesson learned is added below.

## Lessons

(Each line is a mistake made once, so it is not made twice. Add to it.)

- A "must not" test passes on an app that does nothing. Give it a positive control in the same test: show the allowed case works before asserting the forbidden one fails. (Brief 01: 3 of 58 tests passed on the empty skeleton.)
- Read the warnings in a test run, not just the summary line. They are early notice. (Brief 01: the test client wanted `httpx2`.)
- SQLite connections refuse to cross threads, and FastAPI moves a request between threads (sync dependencies, async routes). Open one connection per request with `check_same_thread=False`. (Brief 02: 25 tests failed on this.)
- Every parameter of a FastAPI route function can be set from the URL. Put shared rendering in a private helper, never in extra route parameters. (Brief 02: nearly let a link print any message on an order page.)
- Check what the pinned version actually does before relying on how a framework used to work. (Brief 02: FastAPI 0.141 nests included routers, which emptied the route list.)
- Walk every changed page at phone width before handing back. Tests do not see layout or tense. (Brief 02: three problems passed all 58 tests.)
- A key that stops double submits is not a security token. Anything a form sends back that the server must trust is signed (`app/tokens.py`). (Brief 03: any made-up token placed an order.)
- In tests, submit forms with the token the page served, not an invented one. Invented inputs hid the gap above. (Brief 03.)
- Read the company's own files before inventing a fact. The app was first built with London times, pounds and credit terms the company does not offer, because the facts sheet was never read. (Brief 04.)
- Parse only the section of a document you mean. The sheet's change-history table looked like a price list. (Brief 04.)
- Pin what your pins pull in. Five pinned packages brought twelve unpinned ones. (Brief 05.)
- Walk the running app against the acceptance tests, not only the test suite, and check the states between steps. After the cancel window closed, the order page dropped the cancel button but said nothing about what to do next; no test looked at that page in that state. (Brief 06.)
- A fact typed into a template is invisible to the drift test. Render every fact a customer is told from the facts file, and test that changing the file changes the page. (Brief 07: the cut-off on the list and "free from two cases" on the review screen.)
- When a file moves, search every file for its old path, history included, and record the move. (Brief 07: the CI file moved and five references went stale.)
- A claim about the checks is checked like code. CI must watch every file the tests read, and run every check the docs promise. (Brief 07: the facts sheet did not trigger CI, and the promised type checks never ran.)
