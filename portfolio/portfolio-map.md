# Portfolio map

*Companion to Chapter 17, "The Holding Company Machine", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

A one-page map of your conglomerate in three layers: **the holding layer** (you), **shared services** (built once, used by all), and **each company** (its own identity). It rests on one rule:

> **Share know-how. Separate data and money.**

Know-how (procedures, skills, templates, checklists, the design-system structure, the security baseline, the operating rhythm, reference code) gets better the more places it is used, so it lives once, at the portfolio level. Customer data, bank and payment accounts, credentials, contracts and agent permissions belong to one company each, for four reasons: **law, trust, security and sale.**

## How to use it

1. Draw the map now, even with one company. It shows what to build as shared and what to keep separate from the first day.
2. Update it whenever you add, close or restructure a company, or add a shared service.
3. Review it at the quarterly portfolio strategy review ([weekly-review.md](../playbooks/weekly-review.md) has the portfolio rhythm).

---

## The map

Last checked: [YYYY-MM-DD]

### Layer 1: The holding layer (you)

| Item | Where it lives | Last reviewed |
|---|---|---|
| Portfolio mission (one sentence, Chapter 1) | [file] | [date] |
| Portfolio context: principles, standards every company meets | [file] | [date] |
| Portfolio disclosure policy (Chapter 11) | [file] | [date] |
| Portfolio dashboard, one line per company | [file or tool] | [date] |
| Weekly portfolio review (time and day) | [calendar] | |
| Holding company, if your lawyer and accountant advise one | [entity name, jurisdiction] | [date] |
| Advisers: lawyer, accountant, senior engineer, peers | [names] | |

### Layer 2: Shared services (built once, used by all)

| Service | What is shared (know-how) | What stays per company (data and money) | Owner of the shared version | Companies using it |
|---|---|---|---|---|
| **Back office: finance** | The [finance stack](../playbooks/finance-stack.md) pattern, the [monthly close](../playbooks/monthly-close.md) checklist, the finance agent's instruction file | Each company's books, bank account, payment account, close and sign-off | [you] | [list] |
| **Back office: compliance** | The [compliance calendar](../playbooks/compliance-calendar.md) format, the compliance agent's brief | Each entity's filings, deadlines, registrations | [you] | [list] |
| **Platform** (software companies) | The reference app, the pipeline, monitoring setup, [incident runbook](../playbooks/incident-runbook.md) | Each product's code repository, hosting account, database, secrets | [you or contract engineer] | [list] |
| **Design and voice structures** | The [design-system template](../context-kit/design-system.md) and [voice-guide template](../context-kit/voice-guide.md) | Each company's filled-in design system and voice | [you] | [list] |
| **Skills library** | Every procedure written as a skill, versioned, in one place | Company-specific facts referenced by each skill | [you] | [list] |
| **Security standards** | The [permission matrix](../stack/permission-matrix.md) format, the [audit](../playbooks/permission-audit.md) schedule, the kill-switch procedure | Each company's keys, accounts, agent identities and matrix | [you] | [list] |

### Layer 3: Each company (its own identity)

Copy this block once per company.

| Field | [Company name] |
|---|---|
| Legal entity and jurisdiction | [name, form, where registered] |
| Path (Chapter 19): cash flow, asset, or held in the portfolio | [choice, date decided] |
| Quarterly verdict: grow, keep steady, fix, or close | [verdict, date] |
| Brand, voice and design system | [link to its filled-in files] |
| Context kit | [link: facts sheet, customer file, decision log, lessons log] |
| Bank account and payment account | [in the company's name: yes / no] |
| Customer data held | [what, where] |
| Front-office agents (belong to this company only) | [support, sales, marketing] |
| Back-office agents serving it, with their per-company permissions | [finance, compliance] |
| Status on the portfolio dashboard | [green / amber / red] |
| Share of your weekly attention | [percent or hours] |

---

## Agents across the portfolio

| Agent type | May serve several companies? | Condition |
|---|---|---|
| Finance, compliance (back office) | Yes, carefully | A separate, limited set of permissions per company; a separate close for each company; never one set of keys to everything |
| Support, sales, marketing (front office) | No | One company each: its voice, its facts, its customers |
| Coding, operations | Per product | Access only to that product's repository, hosting and logs |
| Research | Yes | Public sources only; no access to any company's data or money |

**Improvements travel as proposals.** A better skill found in one company updates the shared version in the skills library; each company adopts it through its own weekly review, never automatically. Use the proposal form in the [shared-services checklist](shared-services-checklist.md).

## Legal structure: questions for your lawyer and accountant

> This is not legal, tax or financial advice. Structures, taxes and obligations vary widely by country and change. Decide with a qualified lawyer and accountant where you operate, and decide early: restructuring after the fact costs far more.

- [ ] Should each company be its own legal entity with limited liability? (The general pattern: yes.)
- [ ] Should a holding company own the operating companies, and should it provide the shared services, charging each company under a simple written agreement?
- [ ] Which lighter form suits a new, unproven company here, and when should it convert to a fuller one?
- [ ] What records must each entity keep separately, and what may be shared?
- [ ] If companies sit in different countries, who advises on each?

---

## Worked example

*Illustration, and a thought experiment: the founder, Copper Pot Mixers and Ledgerly are fictional. Everywhere else in this repository the two are separate companies with separate founders, both started in late 2025 (Meera runs Copper Pot; Ledgerly's founder is a bookkeeper). Here we imagine one founder holding both, as if Ledgerly had been started later, as "same machine, new customer" (Chapter 16), only after Copper Pot had passed the readiness test. Copper Pot sells craft cocktail mixers to bars and cafes in Bengaluru; Ledgerly is a small bookkeeping-software company selling to micro businesses in the US and UK.*

**Holding layer.** Mission: "Small companies that do one useful thing very well, run by one founder and a machine that keeps its promises." One weekly portfolio review, Monday 9 to 10:30 am. A holding company is under discussion with a lawyer and an accountant in each country, because the two companies are in different jurisdictions.

**Shared services.**

| Service | Shared | Separate |
|---|---|---|
| Finance | One close checklist and one finance-agent instruction file | Two sets of books, two bank accounts, two closes, two accountants |
| Compliance | One calendar format, one compliance agent | Separate permissions per entity; separate filings in India and abroad |
| Platform | Pipeline, monitoring and runbook patterns | Separate code repositories, hosting accounts and databases |
| Design and voice | The template structure | Copper Pot: warm, bar-floor plain speech. Ledgerly: calm, precise, never casual about money |
| Skills library | 23 skills, versioned; the escalation rules and the monthly-close checks are shared | Each skill points to the company's own facts sheet |
| Security | Matrix format, quarterly audit, kill switch | Separate agent identities and keys per company |

**Each company.**

| Field | Copper Pot Mixers | Ledgerly |
|---|---|---|
| Path | Cash flow | Asset (built to be sellable) |
| Quarterly verdict | Keep steady | Grow |
| Front-office agents | Support, sales (proposal drafts), marketing drafts, as in its company brief | Support (chat and email), as in its company brief |
| Back-office agents | Finance, purchasing and compliance, Copper Pot permissions only | Finance (its own close and Assist preparation) and compliance, Ledgerly permissions only; coding and operations agents reach only Ledgerly's product |
| Dashboard status | Green | Amber (re-contact rate rising) |
| Weekly attention | About 30 percent | About 70 percent |

What the map made obvious: an early version shared one support inbox across both companies. It moved to the "separate" column and was split the same week.

## Related files

- [Shared-services checklist](shared-services-checklist.md)
- [Company template](company-template/README.md), to start the next company from the machine
- [CEO dashboard](../playbooks/ceo-dashboard.md), including the one-line-per-company portfolio view
- [Moat audit](../playbooks/moat-audit.md), for the moats a portfolio can share
