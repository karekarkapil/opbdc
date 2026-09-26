# Shared-services checklist

*Companion to Chapter 17, "The Holding Company Machine", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

The checks that keep a portfolio's shared services useful and safe: every shared resource sorted into **know-how (share)** or **data and money (separate)**, each shared service checked against that rule, a form for moving an improvement from one company to the others as a **proposal**, and the checklist for harvesting the machine when a company closes.

## How to use it

- **Now:** fill in Part 1, the inventory, even with one company. Fix anything in the wrong column.
- **Before adding a company:** run Part 2 for each shared service it will use.
- **Whenever one company improves a shared skill:** use Part 3.
- **Quarterly:** rerun Part 1 and Part 2 with the [permission audit](../playbooks/permission-audit.md).
- **When closing a company:** use Part 4.

---

## Part 1: Inventory of shared resources

Last checked: [YYYY-MM-DD]

List everything that more than one company touches today.

| Resource | Used by | Know-how or data/money? | Correct column? | Action if wrong | Done |
|---|---|---|---|---|---|
| [e.g. support inbox] | [companies] | [know-how / data / money / credential / contract / agent permission] | [yes / no] | [split, move, revoke] | [ ] |
| | | | | | [ ] |

**Always separate, never shared:** customer data, customer lists, bank accounts, payment accounts, credentials and keys, contracts, agent permissions, email inboxes that customers write to, domains and trademarks (each owned by its company).

**Share freely:** procedures and skills, templates, checklists, the design-system and voice-guide structures, the security baseline, the operating rhythm, the brief templates, reference code.

## Part 2: Checks for each shared service

Run this block for each service: back office (finance, compliance), platform, design and voice structures, skills library, security standards.

**Service:** [name]  **Companies using it:** [list]

- [ ] The shared part is know-how only: instructions, templates, checklists, code patterns.
- [ ] Each company's data, money and credentials stay in that company's own accounts.
- [ ] Any agent that serves several companies has a **separate, limited set of permissions per company**, listed in each company's [permission matrix](../stack/permission-matrix.md).
- [ ] The agent works on one company at a time and produces separate outputs per company (for finance: a separate close for each set of books).
- [ ] No front-office agent (support, sales, marketing) is shared. Each belongs to one company.
- [ ] If one company's keys were stolen or one of its agents manipulated, the damage would stop at that company's walls. Write how: [answer].
- [ ] If this company were sold tomorrow, it could be lifted out cleanly. Write what would need untangling: [answer].
- [ ] If the holding company provides this service, there is a simple written agreement and each company is charged fairly for it. (Ask your accountant and lawyer how; this is not tax or legal advice.)
- [ ] The shared version has one owner, one location and a version number or date.

### Service-specific checks

**Back office: finance**
- [ ] One close checklist, one finance-agent instruction file, versioned.
- [ ] Separate books, bank account, payment account, close and sign-off per company.
- [ ] The finance agent has no payment authority in any company.

**Back office: compliance**
- [ ] One calendar covering every entity's obligations, with an entity column.
- [ ] Filing dates come from each entity's accountant, not from a template.

**Platform (software companies)**
- [ ] Pipeline, monitoring and runbook patterns shared; code repositories, hosting accounts, databases and secrets separate.
- [ ] Operations agents read only their own product's logs.

**Design and voice structures**
- [ ] The six-part design-system template and the voice-guide template shared; each company fills in its own.
- [ ] No company's brand assets or voice samples appear in another's files.

**Skills library**
- [ ] Every skill is versioned and lives in one place.
- [ ] Skills point to each company's own facts sheet; no company-specific fact is written inside a shared skill.

**Security standards**
- [ ] One matrix format, one audit schedule, one kill-switch procedure.
- [ ] A kill switch per company, and one for everything, both tested.

## Part 3: Improvement proposal

Improvements travel as proposals, never automatically. What is right for one company is usually right for the others, but not always.

| Field | Entry |
|---|---|
| Date | [YYYY-MM-DD] |
| Skill or shared file | [name, current version] |
| Found in | [company] |
| What happened | [the incident, near miss or better approach] |
| Proposed change | [the exact new wording or step] |
| New version | [number or date] |
| Adopted by [company A] | [yes / no / adapted], at the weekly review of [date], reason: [..] |
| Adopted by [company B] | [yes / no / adapted], at the weekly review of [date], reason: [..] |

## Part 4: Closing a company well

- [ ] The decision was made on evidence, at a quarterly review, not in a bad week. Recorded in the decision log.
- [ ] Customers told early and honestly, given time, and helped to an alternative where possible.
- [ ] Customer data returned or deleted as the privacy policy and the law require. Record what was done: [..]
- [ ] Every obligation met: contracts, suppliers, taxes, filings. Accountant and lawyer consulted.
- [ ] All agents' access revoked; keys rotated; schedules stopped; the company's rows removed from shared agents' permissions.
- [ ] **Harvest the machine:** every useful skill, template, golden set and lesson moved into the shared library, stripped of the closed company's customer data.
- [ ] The portfolio map updated.

## Related files

- [Portfolio map](portfolio-map.md)
- [Company template](company-template/README.md)
- [Permission audit](../playbooks/permission-audit.md)
