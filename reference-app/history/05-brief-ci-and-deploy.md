# Brief 05: continuous integration, deployment notes, README

Date: 2026-09-26. Written by the coding agent. The CI file was drafted earlier, while the independent review of brief 03 was running, because it touches no file the reviewer was reading; this brief covers finishing and checking it, and the rest of the step. The review record at the end says what actually happened.

*Note added 2026-09-26 (brief 07): after this step, the CI file was moved out of this folder, from `reference-app/.github/workflows/ci.yml` to the companion repository's root as `.github/workflows/reference-app-ci.yml`, where GitHub runs it. Where this brief says `.github/workflows/ci.yml`, or that the file lives inside `reference-app/` where GitHub will not run it, read the new location. The move itself is recorded in brief 07. The text below is otherwise left as it was.*

## Goal

Give the app the path from change to customer that Chapter 9 describes: automated checks on every change (Chapter 7's gates: tests, lint, secret scan, known vulnerabilities), an optional container for founders whose managed platform wants one, a short note on deploying with the least infrastructure that works, and a README that lets a founder run, test, review and reuse the app.

## Context

- Chapter 7, the workshop box: automated gates, pinned dependencies, supply-chain care.
- Chapter 9: the six-step path (checks, preview, review, release, watch, roll back), the five watches, "run the least infrastructure that works".
- `playbooks/ship-checklist.md` in the companion repository: the same steps as a checklist.
- The 2025 draft's container material (Chapter 8 there: a multi-stage Dockerfile, a non-root user, Docker Compose), which the 2026 book says lives on here, updated.

## Constraints

- The CI file lives in `reference-app/.github/workflows/`, where GitHub will not run it. Write it to run from the repository root with `reference-app` as its working directory, and say plainly in the file and the README that it must be copied to the root to run.
- Pin everything: actions by commit, the secret scanner by version and checksum, Python packages by version.
- No tool prices, no platform recommendations by name, no claims that cannot be checked from here.
- The deploy notes must be honest about SQLite: a file on a disk that a platform may wipe on each deploy.

## Definition of done

- `.github/workflows/ci.yml`, `deploy/Dockerfile`, `deploy/compose.yaml`, `deploy/README.md`, `.dockerignore`, `README.md`, and `history/README.md` as an index.
- Every CI command run locally and passing.
- The container built and run locally, with the health check answering.

## Verification

- The output of each CI step run locally.
- `docker build` and a request to the running container's `/healthz` and `/demo`.
- A scan of the whole folder for em-dash, en-dash and Cyrillic characters.

## Questions

- Stop and ask before recommending any specific hosting company.

---

## Review record (2026-09-26)

**CI file.** Pinned before writing: `actions/checkout` v7.0.1 and `actions/setup-python` v7.0.0 by full commit (looked up from GitHub's API on the day), gitleaks 8.30.1 by version and by the SHA-256 in the release's checksums file. Permissions are read-only. It could not be run on GitHub from here (it lives inside `reference-app/`, and no git commands were run), so each step was run locally instead, in the same order:
- Secret scan: `gitleaks dir . --no-banner --redact` found no leaks. It scanned about 309 KB, far less than the 71 MB `.venv`, so the reason was checked rather than guessed: gitleaks does not honor `.gitignore` in a plain folder (a planted key in an ignored folder was still found), but its default rules skip `site-packages` folders (a planted key there was not). In CI the scan runs before anything is installed, so this does not matter there. To check the scan works at all, a fake key was planted in a scratch folder outside the app: gitleaks found it and exited with 1, which fails a CI step.
- Lint: `ruff check .` clean; `ruff format --check .` clean.
- Tests: `pytest -W error`, `93 passed`.
- Known vulnerabilities: `pip-audit -r requirements.txt`, "No known vulnerabilities found".
- The YAML was parsed to confirm the steps and triggers.

**Found while checking.**
- `requirements.txt` pinned only the five direct packages, so every install could pull different versions of the twelve packages they depend on. All seventeen are now pinned. A clean virtual environment installed both requirement files with `pip check` reporting no conflicts, and the tests still passed.
- The container's first run failed: port 8000 was already taken on this machine by something unrelated. The compose file now takes `PORT` from the environment (default 8000). It was a real snag a founder could hit, not a fault in the app.

**Container.** Built from `deploy/Dockerfile` (base image `python:3.12-slim` pinned to its multi-architecture digest; Python 3.12.14 inside; the Asia/Kolkata time zone resolves). Run with `deploy/compose.yaml` on port 8790:
- `/healthz` answered `{"status":"ok"}`, and Docker reported the container `healthy`;
- the process ran as `uid=10001(app)`, not root;
- seeded inside the container, the first bar's page showed three orders;
- an order confirmed through the review form redirected to "Order confirmed", Monday 28 September 2026.

The container, its volume and the image were then removed.

**Deployment notes and README.** `deploy/README.md` names no hosting company and quotes no price, as the brief required. It lists the four things between this app and real customers, maps the six steps and five watches to this app, and states plainly what SQLite needs (a disk that survives deploys). `README.md` covers what the app is, how it maps to Chapters 6, 7 and 9, how to run it and its tests in a few commands, an eight-row walk of the acceptance tests for a reviewer who does not code, CI, and how to use the folder as a template. Its counts were checked against the files (1,005 lines of Python in `app/`, six templates, 93 tests), and two wrong first guesses were corrected.

**Character scan.** Every file in the folder, outside `.venv`, was scanned for em-dash, en-dash and Cyrillic characters. None were found.

**Lessons added to AGENTS.md.** One: pin what your pins pull in.
