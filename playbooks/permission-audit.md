# Permission audit

*Companion to Chapter 14, "Law, Trust and Safety", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

A quarterly procedure for checking every agent, connector, key and skill your company uses: what each can read, write and delete, and whether it still needs that access. It also carries the six agent-safety practices from Chapter 14 as a checklist, including the kill-switch drill and the incident log.

## How to use it

1. Once a quarter, brief the audit agent (brief at the end). **It lists; you decide and revoke.**
2. Go through the inventory table row by row. For each row, choose: keep, reduce, revoke.
3. Make the changes yourself, then update your [permission matrix](../stack/permission-matrix.md).
4. Run the six-practice checklist, including the kill-switch drill.
5. File the signed table in your compliance evidence folder, and tick it off on the [compliance calendar](compliance-calendar.md).

Allow about an hour for a single company.

---

## The procedure

- [ ] **1. Inventory.** The agent lists everything with access: every agent, connector, API key, skill, agent card and scheduled job.
- [ ] **2. Compare** each item's actual access with the permission matrix. Mark every difference.
- [ ] **3. Check use.** When was each item last used? Anything unused for [90] days is a revocation candidate.
- [ ] **4. Check sources.** Is each connector from the system's own maker? Is each skill one you have read? Is each version pinned?
- [ ] **5. Check separation.** Does any agent that reads untrusted content (web, email, customer messages) also hold keys to money or sensitive data?
- [ ] **6. Decide.** Keep, reduce or revoke, row by row.
- [ ] **7. Act.** You make the changes. The agent does not revoke its own or anyone else's access.
- [ ] **8. Record.** Update the permission matrix; add anything surprising to the lessons log.

## The inventory table

| Item | Type (agent, connector, key, skill, card, job) | Can read | Can write | Can delete | Source and pinned version | Last used | Still needed? | Action (keep, reduce, revoke) |
|---|---|---|---|---|---|---|---|---|
| [Support agent] | agent | [orders, delivery status, facts sheet] | [address before dispatch; capped goodwill credit, logged] | [nothing] | [provider] | [date] | [yes/no] | [action] |
| [Accounting connector] | connector | [books, bank feed] | [categories, drafts] | [nothing] | [maker, version] | [date] | [yes/no] | [action] |
| [Monthly-close skill] | skill | not applicable | not applicable | not applicable | [author, version, read on date] | [date] | [yes/no] | [action] |
| [Agent card] | card | not applicable | [purchases up to limit] | not applicable | [provider] | [date] | [yes/no] | [action] |
| [Hosting API key] | key | [logs, monitoring] | [none] | [none] | [platform] | [date] | [yes/no] | [action] |

Signed off: [founder], [date]. Items revoked: [N]. Items reduced: [N].

---

## The six agent-safety practices (Chapter 14)

### 1. A quarterly permission audit
- [ ] This file, completed and signed this quarter.

### 2. An audit trail
- [ ] Every agent action that touches customers, money, data or the outside world leaves a record you can read later.
- [ ] You know where each agent's log lives, and you skimmed it this week (Chapter 2's seventh rule).
- [ ] Logs are kept for at least [period agreed with your lawyer].

### 3. Known sources only
- [ ] Connectors installed from the systems' own makers.
- [ ] Every third-party skill read before installation, the way you would read a contract.
- [ ] Versions pinned, so an update cannot change behavior silently.
- [ ] Agent configuration kept under version control, so any change to it is visible.

### 4. Separation of reading and power
- [ ] No agent that reads the web, email or customer messages can also move money or reach sensitive data. The only exception worth allowing is a small, capped power on the customer's own account, such as a goodwill credit, and even that is logged. Check the log and the cap this quarter.
- [ ] Customer-facing agents see only the records of the customer they are helping.

### 5. A kill switch
- [ ] One written, practiced way to disable all agent access quickly: revoke keys, pause schedules, disconnect connectors.
- [ ] Written down at: [location], reachable from your phone.
- [ ] **Drill this quarter.** Start a timer. From your phone only, stop every agent and scheduled job. Target: two minutes.

| Drill date | Time taken | What was slow or missing | Fix |
|---|---|---|---|
| [date] | [mm:ss] | [note] | [change made] |

- [ ] After the drill, restore access and confirm each agent works again.

### 6. An incident log
- [ ] Every agent mistake, near miss or suspected attack is written down, with what you changed.

**Incident log template**

| Date | Agent or tool | What happened | Harm (none, near miss, actual) | How detected | What we changed | Lesson added to lessons log? |
|---|---|---|---|---|---|---|
| [date] | [agent] | [e.g. supplier email asked finance agent to change bank details] | [near miss] | [agent escalated] | [none needed; rule confirmed] | [yes] |

Serious incidents follow the [incident runbook](incident-runbook.md). Every incident feeds the [lessons log](../context-kit/lessons-log.md), and moves the affected job down the [trust ladder](trust-ladder.md) until the cause is fixed.

---

## Brief for the audit agent

> **Goal:** Prepare this quarter's permission audit so the founder can decide on every item in about an hour.
>
> **Context:** Read the permission matrix, last quarter's audit, the incident log, and the admin or settings pages of each connected system you have read access to.
>
> **Constraints:** Read and list only. Never change, grant or revoke any permission, key or connection, including your own. Never copy a key or secret into the report; name it only.
>
> **Done:** The inventory table filled for every item, with differences from the permission matrix marked, unused items marked, unpinned or unknown-source items marked, and any reading-and-power overlap highlighted at the top.
>
> **Verification:** For each row, name where you found the information (which settings page, which log). List anything you could not inspect, so the founder checks it by hand.
>
> **Questions:** Ask if you find access you cannot explain, a key with no owner, or a connector or skill from a source you cannot identify. Report these first.

## Related files
- [Permission matrix](../stack/permission-matrix.md)
- [Compliance calendar](compliance-calendar.md)
- [Incident runbook](incident-runbook.md)
- [Legal starter](legal-starter.md)
