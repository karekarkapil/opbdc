# Deploying the reorder page

Companion to Chapter 9, "Ship It, Run It". Last checked: 2026-09-26.

The principle from the chapter: **run the least infrastructure that works, and let agents watch it.** For this app that means a managed platform that runs Python web apps straight from your repository. You do not need the container in this folder unless your platform asks for one, or you have a reason (cost, privacy, portability) to run it yourself.

No platform is named here, on purpose: names, features and prices change. Look for the settings in [`../../playbooks/ship-checklist.md`](../../playbooks/ship-checklist.md).

## What the platform needs to know

| Setting | Value |
|---|---|
| Runtime | Python 3.12 |
| Install command | `pip install -r requirements.txt` |
| Start command | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` (use the port variable your platform provides) |
| Health check path | `/healthz` (answers `{"status": "ok"}` when the app can reach its database) |

Environment variables:

| Variable | What it is | Where it goes |
|---|---|---|
| `COPPER_POT_SECRET` | A long random string that signs the confirm and cancel forms (spec B13). Make one with `python3 -c "import secrets; print(secrets.token_hex(32))"`. | The platform's **secrets store**. Never in code, never in a file an agent reads. Without it, the app makes a random one at start-up and open pages expire on every restart. |
| `COPPER_POT_DB` | Where the SQLite file lives, for example `/data/copper_pot.db`. | Ordinary setting. |
| `DEMO_MODE` | `1` switches on the demo sign-in and pretend clock. | **Previews only.** Never on the live site. |

## Before real customers

This is a reference app. Four things stand between it and a real bar's orders:

1. **Sign-in.** Connect a managed login provider in `current_account` in `app/main.py`, the one seam for it (spec B11). Do not build passwords. Keep its session cookie `SameSite=Lax` or `Strict`.
2. **Demo mode off** on the live site. Without a login provider and without demo mode, every page says sign-in is not connected (a 503), which is the safe failure.
3. **A disk that survives deploys.** SQLite is a single file. Many managed platforms wipe the app's own disk on every deploy, which would lose every order. Either attach a persistent volume and point `COPPER_POT_DB` at it, or move to the platform's managed database with automatic backups. Moving means changing `app/db.py`, the only file that talks to the database, and running the same tests: a good brief for a coding agent.
4. **Backups you have restored.** Chapter 9: a backup you have never restored is a hope. Once a quarter, restore into a test copy and open the reorder page against it.

## The six steps, for this app

| Step (Chapter 9) | Here |
|---|---|
| 1. Automated checks | `.github/workflows/ci.yml`: secret scan, lint, all tests including every acceptance test, known vulnerabilities in dependencies. Copy it to the repository root's `.github/workflows/` to switch it on. Make it a required check before merging. |
| 2. A preview | Turn on the platform's preview for each change. Previews run with `DEMO_MODE=1` and their own database, seeded with `python -m app.seed`, never a copy of real orders. |
| 3. Your review | Open the preview on a phone and walk the acceptance tests (the README says how). For a change to the delivery rule or the facts, walk AT3 at a pretend Sunday 9 pm. |
| 4. Release | You approve. Riskier changes (the delivery rule, `facts/facts.toml`, the database) go out early in the week, not before the Sunday 8 pm cut-off, when most orders arrive. |
| 5. Watch | The five watches, below. |
| 6. Roll back automatically | Turn on the platform's automatic rollback. One catch: rolling back code does not roll back the database. Keep database changes additive (add a column, never rename or drop one in the same release), so the previous version still works with the new data. |

## The five watches, for this app

| Watch | For the reorder page | Alert when |
|---|---|---|
| Up | The platform's check of `/healthz` | It fails for more than a few minutes |
| Fast | Time to load `/` and `/repeat/...` | Much slower than usual for a sustained period |
| Errors | Responses of 500 and above | They rise above the normal rate. A 400 (a bad quantity) or 409 (a closed cancel window) is the page doing its job, not an error. |
| Money | New orders | None on a Sunday evening before the cut-off, when they normally arrive. Orders cluster late at night and on Sunday, so compare with the same hours last week, not the last hour. |
| The one number | Share of repeat orders placed through the page (spec part 9) | It falls well below its normal range. A weekly summary, not an alert. |

## The container, if you want it

Verified on 2026-09-26 with Docker Engine 29.8.0: the image built, ran as a non-root user, passed its health check, and took an order.

```
# from the reference-app folder
export COPPER_POT_SECRET=$(python3 -c "import secrets; print(secrets.token_hex(32))")
docker compose -f deploy/compose.yaml up --build -d        # PORT=8080 to use another port
docker compose -f deploy/compose.yaml exec app python -m app.seed
# open http://localhost:8000
docker compose -f deploy/compose.yaml down                 # add -v to delete the orders volume
```

`Dockerfile` pins the base image to a digest and installs only the pinned runtime packages. `compose.yaml` runs one service in demo mode with a named volume for the database.

## What happened to the 2025 material

The 2025 draft built this machinery by hand. It still works; most founders no longer need to start there.

| 2025 | Here, updated |
|---|---|
| A multi-stage Dockerfile for the backend, another for a separate frontend served by Nginx | One single-stage Dockerfile: the pages are rendered by the app itself, and nothing is compiled, so there is no build stage and no second server. Base image pinned to a digest; non-root user kept. |
| Docker Compose with backend, frontend and a database server | One service and a volume. SQLite needs no server. |
| A pipeline that tested and then deployed | `ci.yml` does the checks. Deploying, previews and rollback are the platform's job. |
| Visual regression tests that compared screenshots | Walking the acceptance tests on a phone at each review. Screenshot comparison is worth adding once the pages change often enough to justify it. |
| Monitoring you assembled yourself | The platform's logs and alerts, the five watches above, and an agent that reads them each morning with read-only access. |
