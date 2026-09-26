# 1 Person, Billion Dollar Conglomerate: companion repository

The working files for the book **1 Person, Billion Dollar Conglomerate** (2026 edition) by Kapil Karekar: a playbook for founders, technical and non-technical, who run a company with a staff of AI agents, and then replicate that machine into a portfolio of companies.

The book teaches the durable patterns: how to brief, check and trust agents, how to write your company down, how to build, ship, sell and run it, and how to start the next company from the first. This repository holds the parts you fill in and use: templates, checklists, agent briefs, worked examples and a small reference app. Every "In the repo" link in the book points to a file here.

Last reviewed: September 2026.

## How to use it with the book

1. **Read the chapter first.** Each file here assumes you know the idea behind it; the chapter explains why it works and where it breaks.
2. **Copy the template, then make it yours.** Copy a file into your own company's folder (a shared folder, or a repository next to your code) and fill it in for your company. Plain Markdown works with every agent tool, today and next year.
3. **Point your agents at your filled-in copies,** never at the examples. The examples are there to show what "good" looks like.
4. **Keep dates on everything.** Every template has a "Last checked" line. A fact without a date cannot be judged stale.
5. **Come back for updates.** The book ages slowly; this repository moves with the tools. Volatile details (tools, prices, setup steps) are dated "as of late 2026" and reviewed for each printing.

If you do not code, you never need to run anything here except, optionally, the reference app. Everything else is documents you read and fill in.

## Conventions

- **Fill-in fields** look like `[Company name]` or `[YYYY-MM-DD]`. Checklists use `- [ ]` boxes.
- **Fictional examples.** Worked examples use two invented companies: **Copper Pot Mixers**, a small Bengaluru business selling craft cocktail mixers to independent bars and cafes, and **Ledgerly**, a small bookkeeping-software company for micro businesses and their bookkeepers. Any resemblance to a real business is unintended. Figures in examples are illustrations, not data.
- **Book terms are exact.** The six-part brief, the five-rung trust ladder, the nine-part spec and the rest use the same names and order as the chapters.
- **Not professional advice.** Files touching law, tax or finance say so and tell you when to consult a qualified lawyer or accountant where you operate. The legal templates are starting points that require a lawyer's review.
- **No secrets.** Nothing here needs a password, key or real customer data, and nothing you fill in for an agent to read should contain them.

## Contents by chapter

| Chapter | Files |
|---|---|
| **1. The One-Person Conglomerate** | Start the decision log: [context-kit/decision-log.md](context-kit/decision-log.md) |
| **2. Your Agent Stack** | [stack/permission-matrix.md](stack/permission-matrix.md): what each agent and connector may read, write and delete, and what needs your approval<br>[stack/cost-worksheet.md](stack/cost-worksheet.md): cost per task, cost per customer, the ten-times test<br>[stack/local/](stack/local/README.md): when local models make sense, a general setup path, and how to point the same instruction files at a local model |
| **3. Context Is the Company** | [context-kit/](context-kit/README.md): the ten files every company needs, as templates, with filled-in examples for a [beverage company](context-kit/examples/beverage-company/) and a [software company](context-kit/examples/software-company/)<br>[briefs/brief-template.md](briefs/brief-template.md): the six-part brief, with [example briefs](briefs/examples/) for research, writing, design, code, support and finance |
| **4. Managing Agents** | [briefs/agent-brief-card.md](briefs/agent-brief-card.md): the delegation loop on one card<br>[playbooks/verification-checklist.md](playbooks/verification-checklist.md), with [golden sets](playbooks/golden-sets/) for support, finance and content<br>[playbooks/trust-ladder.md](playbooks/trust-ladder.md): every recurring job on the ladder, with promotion and demotion rules |
| **5. A Problem Worth Solving** | [briefs/research-agent.md](briefs/research-agent.md): with variants for consumer, small-business and professional markets<br>[playbooks/customer-conversations.md](playbooks/customer-conversations.md): question guide, outreach template, summary format<br>[playbooks/validation-scorecard.md](playbooks/validation-scorecard.md): the nine questions, with a worked example |
| **6. The Spec Is the Product** | [playbooks/one-page-spec.md](playbooks/one-page-spec.md): the nine-part template and three full examples |
| **7. Building with Coding Agents** | [reference-app/](reference-app/): a small ordering product built end to end with coding agents |
| **8. Design Without a Designer** | [context-kit/design-system.md](context-kit/design-system.md): the six-part design system, with a filled-in example |
| **9. Ship It, Run It** | [playbooks/ship-checklist.md](playbooks/ship-checklist.md): the six steps from change to customer<br>[playbooks/incident-runbook.md](playbooks/incident-runbook.md): the five steps, customer message templates and the incident account |
| **10. The Launch Nobody Noticed** | [playbooks/first-ten.md](playbooks/first-ten.md): list-building brief, note template, tracking sheet |
| **11. Marketing When Everyone Has AI** | [playbooks/pillar-and-spoke.md](playbooks/pillar-and-spoke.md): the workflow with the edit pass, and a voice-file template |
| **12. Sales and Support Agents** | [briefs/support-agent.md](briefs/support-agent.md): a complete support agent instruction file |
| **13. The AI CFO** | [playbooks/finance-stack.md](playbooks/finance-stack.md): setup checklist and the finance agent's instructions and permissions<br>[playbooks/monthly-close.md](playbooks/monthly-close.md): the agent's checklist, the flag list and the summary template |
| **14. Law, Trust and Safety** | [playbooks/legal-starter.md](playbooks/legal-starter.md): questions for a lawyer by the five areas, with [template terms and policies](playbooks/legal-templates/) for review<br>[playbooks/compliance-calendar.md](playbooks/compliance-calendar.md)<br>[playbooks/permission-audit.md](playbooks/permission-audit.md) |
| **15. The Operating Rhythm** | [playbooks/weekly-review.md](playbooks/weekly-review.md): the agenda and the preparing agent's brief<br>[playbooks/ceo-dashboard.md](playbooks/ceo-dashboard.md): the one-screen layout, thresholds and compiling agent's brief |
| **16. The Second Company** | [portfolio/company-template/](portfolio/company-template/README.md): copy as is, keep but adapt, earn fresh, and the readiness test |
| **17. The Holding Company Machine** | [portfolio/portfolio-map.md](portfolio/portfolio-map.md): the three-layer map<br>[portfolio/shared-services-checklist.md](portfolio/shared-services-checklist.md) |
| **18. Moats in an Age of Abundance** | [playbooks/moat-audit.md](playbooks/moat-audit.md): the questions, a scoring sheet and a worked example |
| **19. Building for Value** | [portfolio/company-template/data-room-checklist.md](portfolio/company-template/data-room-checklist.md): everything a buyer will ask for, and the agent that keeps it current |

## Layout

```
stack/          the agent stack: permissions, costs, local models (ch2)
context-kit/    the ten files of company context, the design system, two filled-in examples (ch3, ch8)
briefs/         the brief template, example briefs, standing agent instruction files (ch3 to ch5, ch12)
playbooks/      checklists and runbooks for building, shipping, selling and running the company (ch4 to ch18)
portfolio/      the portfolio map, shared services and the company template (ch16, ch17, ch19)
reference-app/  a small product built with coding agents (ch7, ch9)
```

## Keeping it current

Tools, prices and setup steps change faster than books. Anything volatile here is dated "as of late 2026", and tools are named only as examples of a category. If a link, a tool or an instruction has gone stale, please open an issue with the file path and what changed.

The book links to files here by path, so files are not renamed or moved without updating the book.

## License

LICENSE: to be chosen by the author.

Until a license file is published in this repository, no license is granted beyond reading and personal use alongside the book. The example companies are inventions for teaching.
