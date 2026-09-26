# Ship checklist

*Companion to Chapter 9, "Ship It, Run It", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

The principle: **run the least infrastructure that works, and let agents watch it.** Every change to your product, whether an agent wrote it or you did, travels the same automated path from change to customer. This file is that path as a checklist, the settings to look for on a managed platform, the five things to watch, and how agents fit on call.

## How to use it

- **Once, at setup:** work through "Settings to look for on a managed platform". Tick each one, or write down why you do not need it.
- **Every change:** the six steps. Steps 1, 2, 4, 5 and 6 are automatic once set up. Step 3 is you.
- **Every quarter:** re-check the settings (they drift) and run a backup restore drill.

Settings are described by what they do, not by product name, because the names change. As of late 2026, most managed hosting platforms offer most of these; check your platform's documentation for what it calls each one.

---

## The six steps, for every change

### 1. Automated checks
- [ ] Tests run on their own, including the acceptance tests from the spec.
- [ ] Style and type checks run.
- [ ] Security and secret scans run.
- [ ] If anything fails, the change stops here. No overrides "just this once".

### 2. A preview
- [ ] The platform built the change at its own private address.
- [ ] The preview is identical to the real product except that no customer can see it.

### 3. Your review
- [ ] I opened the preview on a real phone, the kind my customers use.
- [ ] I walked the acceptance tests from the spec myself.
- [ ] I tried to break it: wrong inputs, double taps, a slow connection.
- [ ] For code I did not write and cannot read: a second agent reviewed the change against the spec and I read its list of risks.

### 4. Release
- [ ] I approved the release.
- [ ] For higher-risk changes: released to a small share of customers first, or behind a switch I can turn off without redeploying.

### 5. Watch
- [ ] For the first hour, monitoring compares errors, speed and orders with the hour before.

### 6. Roll back automatically
- [ ] If errors jump or orders stop, the platform returns to the previous version on its own and tells me.

---

## Settings to look for on a managed platform

| Setting | What it does | Set up? |
|---|---|---|
| Connect your code repository | Every change pushed to the repository is built by the platform | [ ] |
| Preview per change | Each proposed change gets its own private address | [ ] |
| Required checks before merge | A change cannot join the main version until tests and scans pass | [ ] |
| Protected main branch | Nobody, agent or human, can push directly to the live version | [ ] |
| One-click rollback | Return to any previous version in one step | [ ] |
| Gradual rollout or feature switches | Release to a share of customers first, or turn a feature off without redeploying | [ ] |
| Automatic rollback on error-rate rise | The platform reverts on its own when errors or failures jump | [ ] |
| Secrets store | Passwords and keys held by the platform, never in code or in files agents read | [ ] |
| Automatic database backups | A managed database backed up on a schedule, with a known restore procedure | [ ] |
| Logs and monitoring | Requests, errors and speed recorded and searchable | [ ] |
| Alerts to your phone | Only for the few conditions in the table below | [ ] |
| Two-factor sign-in | On the platform, and also on email, code host, payment provider and domain registrar | [ ] |
| Separate agent identities | Agents use their own accounts and keys, with read access to logs, not write access to data | [ ] |

> **For the technical founder:** if a managed platform cannot meet your cost, performance, privacy or portability needs, the same six steps apply to a pipeline you build yourself. The [reference app](../reference-app/) shows one.

---

## The five watches

Monitor five things. Alert on very few. Everything else goes into the daily summary.

| Watch | The question | Alert you when |
|---|---|---|
| **Up** | Can customers reach the product? | It has been unreachable for more than a few minutes |
| **Fast** | Is it responding quickly enough? | Key pages are much slower than usual for a sustained period |
| **Errors** | Are requests failing? | Failures rise sharply above the normal rate |
| **Money** | Are orders and payments flowing? | Orders or payments stop at a time they normally arrive |
| **The one number** | Is the product doing its job? | Your key measure (repeat orders, active users) moves far out of its normal range |

Write your own thresholds:

| Watch | My normal | Alert when | Where the alert goes |
|---|---|---|---|
| Up | | | |
| Fast | | | |
| Errors | | | |
| Money | [e.g. about 8 orders in any two hours on a weekday] | [e.g. none in 2 hours, 10 am to 10 pm] | |
| The one number | | | |

---

## Agents on call

Following the [trust ladder](trust-ladder.md):

| When | What the agent does | Rung |
|---|---|---|
| Every morning | Reviews the last day's logs, errors, speed and orders; leaves a short summary: normal, unusual, anything that needs you | 4, autonomous |
| When an alert fires | Investigates immediately: reads logs around the time, checks recent changes, tries to reproduce; sends a summary with its best explanation and the evidence | 3, act and report |
| When the cause is a recent release | Automatic rollback, without waiting | 4 |
| When a fix is needed | Drafts the fix, writes a test that reproduces the problem, opens the change for your review | 2, act with approval |
| Afterward | Drafts the incident account for you to edit ([incident runbook](incident-runbook.md)) | 1, draft |

Two limits stay firmly in place:

- [ ] Operations agents have **read access to logs and monitoring, not write access to your data.**
- [ ] Anything that touches **customers or money stays at rung 2 at most**: the agent prepares the refund or drafts the apology; you send it.

---

## The four-on-Friday test

Would you release a fix at four on a Friday afternoon with the same calm as on a quiet Tuesday morning?

- [ ] Yes, because every step above that could fail by tired hands is automated or checked.
- [ ] Not yet. The step I do not trust is: [___]. Fixing it is next week's first brief.

## Quarterly

- [ ] Restore a backup into a test environment and check it works (an agent can run the drill and report; you read the report).
- [ ] Export customer, order and financial data in plain formats, stored separately from your main provider.
- [ ] Re-check the settings table above.

## Related files

- [Incident runbook](incident-runbook.md)
- [One-page spec](one-page-spec.md)
- [Permission matrix](../stack/permission-matrix.md)
