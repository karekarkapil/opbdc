# Reference app: Reorder in one tap

Companion to Chapters 6, 7 and 9 of *1 Person, Billion Dollar Conglomerate* (2026 edition). Last checked: 2026-09-26.

A small ordering product built end to end with a coding agent, following the book's method: a one-page spec, a standing instruction file, tests written before the code, small reviewed changes, continuous integration, and the full history of briefs and reviews. It replaces the long code listings of the 2025 draft.

The product is the reorder page for **Copper Pot Mixers**, the fictional Bengaluru company from the Chapter 3 context kit, which sells craft cocktail mixers to independent bars and cafes. A bar manager, on a phone, late at night after closing, sees their last three orders, repeats one with adjusted quantities, confirms, and is told the delivery day. Every fact it states (prices, the Sunday 8 pm cut-off, the delivery day for each area, the delivery charge, the 30-minute cancel window) comes from the company's [facts sheet](../context-kit/examples/beverage-company/facts-sheet.md), and a test fails if the two drift apart.

It was built by a coding agent (Claude) on 2026-09-26, working from the briefs in [`history/`](history/), which also record every review, every failed test run and every mistake. The founder in the story, Meera, is fictional; so are the bars.

**It is a reference, not a finished product.** It has no sign-in of its own (a managed login provider plugs into one function), and its database is a single SQLite file. [`deploy/README.md`](deploy/README.md) lists what stands between it and real customers.

## How it maps to the book

| Chapter | What to look at |
|---|---|
| **6. The Spec Is the Product** | [`specs/reorder-in-one-tap.md`](specs/reorder-in-one-tap.md): the book's nine-part spec, unchanged, plus the acceptance tests the risk line and the no list imply, and the fifteen decisions the code needed that a one-page spec leaves open. The no list is enforced by tests (AT8). |
| **7. Building with Coding Agents** | [`AGENTS.md`](AGENTS.md): the standing instructions, with a lessons section that grew with every mistake. [`tests/`](tests/): each acceptance test is an automated test named after it (`test_at1_...` to `test_at8_...`). [`history/`](history/): the build loop as it actually ran: brief, tests first, small change, independent review, record. [`../.github/workflows/reference-app-ci.yml`](../.github/workflows/reference-app-ci.yml): the automated gates. |
| **9. Ship It, Run It** | [`deploy/README.md`](deploy/README.md): the least infrastructure that works, the six steps from change to customer and the five watches for this app, and an optional container that carries the 2025 draft's container material forward. |

## What is in the folder

```
AGENTS.md                standing instructions for any coding agent (CLAUDE.md points here)
specs/                   the spec: the contract
facts/facts.toml         the app's copy of the company facts sheet
app/                     the application (about 1,050 lines of Python with comments, six templates)
  main.py                  the pages and the one seam for a login provider
  orders.py                the rules: repeat, whole cases, confirm once, cancel window
  delivery.py              the delivery-day rule: pure, no clock
  db.py, facts.py, money.py, tokens.py, seed.py
tests/                   97 tests: acceptance, delivery rule, edge cases, facts sheet
history/                 the briefs the agent worked from, each with its review record
deploy/                  deployment notes, an optional Dockerfile and compose file
(CI: ../.github/workflows/reference-app-ci.yml, at the repository root)
```

## Run it on your computer

You need Python 3.12 or newer. From this folder:

```
python3 -m venv .venv
source .venv/bin/activate            # on Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python -m app.seed                   # creates data/copper_pot.db with demo bars and orders
DEMO_MODE=1 uvicorn app.main:app --reload
```

On Windows, set the variable on its own line first: in PowerShell, `$env:DEMO_MODE = "1"`, then `uvicorn app.main:app --reload`; in Command Prompt, `set DEMO_MODE=1`, then the same `uvicorn` line.

Open http://127.0.0.1:8000. Demo mode shows a page where you choose a bar and, if you like, a pretend time in Bengaluru, which stands in for a real sign-in. `python -m app.seed --reset` starts again from scratch.

## Run the tests

```
pytest                               # 97 tests, about three seconds
ruff check . && ruff format --check .
mypy                                 # type checks; settings in pyproject.toml
```

Every test name says what it checks. `tests/test_acceptance.py` follows the spec's acceptance tests in order, so you can hold the spec and the file side by side. `tests/test_facts_sheet.py` reads the company facts sheet elsewhere in this repository and fails if the app disagrees with it; outside the companion repository it is skipped unless you set `FACTS_SHEET` to your own sheet.

## Review it without reading code

This is the review Chapter 7 asks of a founder who does not code: walk the acceptance tests on the device your customers use.

**On your phone.** Either open a preview deployment (see [`deploy/README.md`](deploy/README.md)), or run the app on your computer with `DEMO_MODE=1 uvicorn app.main:app --host 0.0.0.0` and open `http://<your computer's address>:8000` on a phone on the same Wi-Fi. Do this only on a network you trust.

**The demo bars.** The Tin Lantern (Indiranagar, deliveries on Mondays, five past orders, the newest including a discontinued flavor), Banyan Street Cafe (Koramangala, Tuesdays, two orders), The Night Owl (Jayanagar, Thursdays, no orders yet) and Sunbird Bar (Whitefield, an area without a fixed day). Tap "Change" in the yellow banner to switch bar or set a pretend time.

| Test | What to do | What you should see |
|---|---|---|
| AT1 | Choose Banyan Street Cafe. | Both orders, newest first, each with its date and total. The single-case order includes the Rs 150 delivery charge. |
| AT2 | Choose The Tin Lantern. Tap Repeat on the third order (pineapple and chilli), change the pineapple from 6 to 12 bottles (one more case), tap Update total, then Confirm order. (The newest order cannot be confirmed as it is: see AT4.) | "Order confirmed", the new quantities, the total, and the delivery day, a Monday. |
| AT3 | Set a pretend time of a Sunday after 8 pm, or 1 am on a Monday. Repeat any order. | The delivery day is the following week's, and the box explains which delivery was missed and why. |
| AT4 | As The Tin Lantern, repeat the newest order. | Guava and Pink Salt is grayed out, "No longer available", with a note that it is left out. A note says the rest is 9 bottles, not whole cases; change the pineapple to 9 and confirm. |
| AT5 | Confirm an order, then tap Cancel this order. | "Order cancelled", and it is gone from your last orders. |
| AT6 | Confirm an order and note the time. Set a pretend time 31 minutes later and open the order from Details. | No cancel button. Past 30 minutes, the facts sheet says Meera decides. |
| AT7 | On the review screen, double-tap Confirm, or confirm, go back, and confirm again. | One order, not two. If you changed a quantity before resending, the page says the changes were not applied. |
| AT8 | Look for any way to change a price, a discount, payment terms or the bar's details. Then type another order's number into the address bar, for example `/orders/7` as The Tin Lantern. | There is none. Another bar's order is "Not found". |

Then try to break it: a quantity of 7, a quantity of 600, letters instead of numbers, a slow connection, the back button at every step. Choose Sunbird Bar to see "Day to be confirmed". Anything that confuses you is a finding, even if every test passes: the walks in `history/` found six of those.

For a change you did not write and cannot read, Chapter 7's other step applies too: ask a second agent, one that did not write the change, to review it against the spec and list risks. `history/03-brief-review-fixes.md` shows the rubric used here and what it found.

## Continuous integration

`../.github/workflows/reference-app-ci.yml`, at the root of the companion repository, runs on every push and pull request that touches `reference-app/` or the company facts sheet the drift test reads: a secret scan (gitleaks, pinned by version and checksum), lint (ruff), type checks (mypy), all tests with warnings treated as errors, and a check of the runtime packages for known vulnerabilities (pip-audit). Actions are pinned to commits, not tags.

**GitHub only runs workflows from `.github/workflows/` at the root of a repository,** which is why this file lives at the companion repository's root and runs every step inside `reference-app/`. If you copy `reference-app/` out as the root of your own repository, move the file into its `.github/workflows/`, delete the `paths` filters and the `defaults` block with its `working-directory` line, and change `cache-dependency-path: reference-app/requirements*.txt` to `cache-dependency-path: requirements*.txt`. The comment at the top of the file lists the same steps.

## Use it as a template

1. Copy this folder into its own repository. Keep `history/` as an example, or start your own at `01`.
2. Replace `specs/` with your one-page spec (Chapter 6), no list and acceptance tests included, and add a "Decisions made while building" table as you go.
3. Rewrite the top of `AGENTS.md` for your product. Keep "Never", "Ask before you" and "Lessons", empty the lessons, and add to them each time an agent makes a mistake.
4. Replace `facts/facts.toml` with your own facts, taken from your facts sheet. Point `FACTS_SHEET` at your sheet, or rework `tests/test_facts_sheet.py` for its layout, so the two cannot drift.
5. Write the acceptance tests first, as named failing tests, before the feature code. Then brief a coding agent to make them pass, one small change at a time, using the six-part brief ([`../briefs/brief-template.md`](../briefs/brief-template.md)).
6. Before customers: a managed login provider in `current_account`, a database that survives deploys and is created without the seed script, the CI file at your repository root, and the settings in [`../playbooks/ship-checklist.md`](../playbooks/ship-checklist.md).

## What it deliberately does not do

The spec's no list, plus what a reference app should not pretend to be: no sign-in or passwords, no payments, no discounts, no product browsing, no editing of prices, terms or account details, no admin screens, no notifications, and no JavaScript. Each would be its own spec.

## Versions

Python 3.12. Packages pinned in `requirements.txt` (runtime) and `requirements-dev.txt` (tests, lint and type checks), each including everything they pull in, as of 2026-09-26. Upgrading them is a good weekly job for a scheduled agent that opens a change for your review, as Chapter 7 suggests.
