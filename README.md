# 1 Person, Billion Dollar Conglomerate: companion repository

The working files for the book **1 Person, Billion Dollar Conglomerate** (2026 edition) by Kapil Karekar: a playbook for founders, technical and non-technical, who run a company with a staff of AI agents, and then replicate that machine into a portfolio of companies.

The book teaches the durable patterns: how to brief, check and trust agents, how to write your company down, how to build, ship, sell and run it, and how to start the next company from the first. This repository holds the parts you fill in and use: templates, checklists, agent briefs, worked examples and a small reference app. Every "In the repo" link in the book points to a file here.

Last reviewed: September 2026.

## How to use it with the book

1. **Read the chapter first.** Each file here assumes you know the idea behind it; the chapter explains why it works and where it breaks.
2. **Copy the template, then make it yours.** Copy a file into your own company's folder (a shared folder, or a repository next to your code) and fill it in for your company. Plain Markdown works with every agent tool, today and next year.
3. **Point your agents at your filled-in copies,** never at the examples. The examples are there to show what "good" looks like.
4. **Keep dates on everything.** Every file that holds facts, meaning the ten context files and the design system, in both the templates and the examples, has a "Last checked" line. Add one to every register, log and checklist you copy and fill in. A fact without a date cannot be judged stale.
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
| **1. The One-Person Conglomerate** | [playbooks/founder-start.md](playbooks/founder-start.md): the mission statement, the full-stack self-assessment, the first machine sketch<br>Start the decision log: [context-kit/decision-log.md](context-kit/decision-log.md) |
| **2. Your Agent Stack** | [stack/permission-matrix.md](stack/permission-matrix.md): what each agent and connector may read, write and delete, and what needs your approval<br>[stack/cost-worksheet.md](stack/cost-worksheet.md): cost per task, cost per customer, the ten-times test<br>[stack/local/](stack/local/README.md): when local models make sense, a general setup path, and how to point the same instruction files at a local model |
| **3. Context Is the Company** | [context-kit/](context-kit/README.md): the ten files every company needs, as templates, with filled-in examples for a [beverage company](context-kit/examples/beverage-company/) and a [software company](context-kit/examples/software-company/)<br>[briefs/brief-template.md](briefs/brief-template.md): the six-part brief, with [example briefs](briefs/examples/) for research, writing, design, code, support and finance, plus an extra for supplier email |
| **4. Managing Agents** | [briefs/agent-brief-card.md](briefs/agent-brief-card.md): the delegation loop on one card<br>[playbooks/verification-checklist.md](playbooks/verification-checklist.md), with [golden sets](playbooks/golden-sets/) for support, finance and content<br>[playbooks/trust-ladder.md](playbooks/trust-ladder.md): every recurring job on the ladder, with promotion and demotion rules |
| **5. A Problem Worth Solving** | [briefs/research-agent.md](briefs/research-agent.md): with variants for consumer, small-business and professional markets<br>[playbooks/customer-conversations.md](playbooks/customer-conversations.md): question guide, outreach template, summary format<br>[playbooks/validation-scorecard.md](playbooks/validation-scorecard.md): the nine questions, with a worked example |
| **6. The Spec Is the Product** | [playbooks/one-page-spec.md](playbooks/one-page-spec.md): the nine-part template and three full examples |
| **7. Building with Coding Agents** | [reference-app/](reference-app/): a small ordering product built end to end with coding agents |
| **8. Design Without a Designer** | [context-kit/design-system.md](context-kit/design-system.md): the six-part design system, with a filled-in example<br>[playbooks/five-person-test.md](playbooks/five-person-test.md): three prototypes, five real people, tasks and silence |
| **9. Ship It, Run It** | [playbooks/ship-checklist.md](playbooks/ship-checklist.md): the six steps from change to customer<br>[reference-app/deploy/](reference-app/deploy/): the six steps and five watches applied to the reference app, with an optional container<br>[playbooks/incident-runbook.md](playbooks/incident-runbook.md): the five steps, customer message templates and the incident account |
| **10. The Launch Nobody Noticed** | [playbooks/first-ten.md](playbooks/first-ten.md): list-building brief, note template, tracking sheet<br>[playbooks/getting-paid.md](playbooks/getting-paid.md): hosted checkout, your customers' payment methods, paid pilots, money actions on the trust ladder |
| **11. Marketing When Everyone Has AI** | [playbooks/pillar-and-spoke.md](playbooks/pillar-and-spoke.md): the workflow with the edit pass, and a voice-file template |
| **12. Sales and Support Agents** | [briefs/support-agent.md](briefs/support-agent.md): a complete support agent instruction file |
| **13. The AI CFO** | [playbooks/finance-stack.md](playbooks/finance-stack.md): setup checklist and the finance agent's instructions and permissions<br>[playbooks/monthly-close.md](playbooks/monthly-close.md): the agent's checklist, the flag list and the summary template |
| **14. Law, Trust and Safety** | [playbooks/legal-starter.md](playbooks/legal-starter.md): questions for a lawyer by the five areas, with [template terms and policies](playbooks/legal-templates/) for review (goods, and a subscription variant)<br>[playbooks/compliance-calendar.md](playbooks/compliance-calendar.md)<br>[playbooks/permission-audit.md](playbooks/permission-audit.md) |
| **15. The Operating Rhythm** | [playbooks/weekly-review.md](playbooks/weekly-review.md): the agenda and the preparing agent's brief<br>[playbooks/ceo-dashboard.md](playbooks/ceo-dashboard.md): the one-screen layout, thresholds and compiling agent's brief |
| **16. The Second Company** | [portfolio/company-template/](portfolio/company-template/README.md): a guide to packaging your first company's machine as a template: copy as is, keep but adapt (with the placeholders to mark), earn fresh, the readiness test and a ninety-day plan |
| **17. The Holding Company Machine** | [portfolio/portfolio-map.md](portfolio/portfolio-map.md): the three-layer map<br>[portfolio/shared-services-checklist.md](portfolio/shared-services-checklist.md) |
| **18. Moats in an Age of Abundance** | [playbooks/moat-audit.md](playbooks/moat-audit.md): the questions, a scoring sheet and a worked example |
| **19. Building for Value** | [portfolio/company-template/data-room-checklist.md](portfolio/company-template/data-room-checklist.md): everything a buyer will ask for, and the agent that keeps it current |
| **21. The First Step** | The ninety-day plan, week by week:<br>Week 1: [founder-start.md](playbooks/founder-start.md), [permission-matrix.md](stack/permission-matrix.md), [cost-worksheet.md](stack/cost-worksheet.md), [company-brief.md](context-kit/company-brief.md), [facts-sheet.md](context-kit/facts-sheet.md), [agent-instructions.md](context-kit/agent-instructions.md)<br>Week 2: [research-agent.md](briefs/research-agent.md), [verification-checklist.md](playbooks/verification-checklist.md), the outreach template in [customer-conversations.md](playbooks/customer-conversations.md)<br>Week 3: [customer-conversations.md](playbooks/customer-conversations.md), [customer-file.md](context-kit/customer-file.md), [validation-scorecard.md](playbooks/validation-scorecard.md)<br>Week 4: [one-page-spec.md](playbooks/one-page-spec.md), [specifications.md](context-kit/specifications.md)<br>Week 5: [agent-instructions.md](context-kit/agent-instructions.md) (see the [code-project example](context-kit/examples/software-company/agent-instructions.md)), [the code brief](briefs/examples/code.md), [reference-app/](reference-app/)<br>Week 6: [design-system.md](context-kit/design-system.md), [the design brief](briefs/examples/design.md), [five-person-test.md](playbooks/five-person-test.md)<br>Week 7: [ship-checklist.md](playbooks/ship-checklist.md), [incident-runbook.md](playbooks/incident-runbook.md)<br>Week 8: [getting-paid.md](playbooks/getting-paid.md), the disclosure policy in [pillar-and-spoke.md](playbooks/pillar-and-spoke.md) and [voice-guide.md](context-kit/voice-guide.md)<br>Week 9: [first-ten.md](playbooks/first-ten.md)<br>Week 10: [support-agent.md](briefs/support-agent.md), [the support golden set](playbooks/golden-sets/support.md), [finance-stack.md](playbooks/finance-stack.md)<br>Week 11: [monthly-close.md](playbooks/monthly-close.md), the AI disclosure notice in [legal-starter.md](playbooks/legal-starter.md), [permission-audit.md](playbooks/permission-audit.md)<br>Week 12: [weekly-review.md](playbooks/weekly-review.md), [ceo-dashboard.md](playbooks/ceo-dashboard.md), and, for later, the [readiness test](portfolio/company-template/readiness-test.md) that decides when "Company two: ideas" becomes a company |

## Layout

```
stack/          the agent stack: permissions, costs, local models (ch2)
context-kit/    the ten files of company context, the design system, two filled-in examples (ch3, ch8)
briefs/         the brief template, example briefs, standing agent instruction files (ch3 to ch5, ch12)
playbooks/      checklists and runbooks for starting, building, shipping, selling and running the company (ch1, ch4 to ch18, ch21)
portfolio/      the portfolio map, shared services and the company template (ch16, ch17, ch19)
reference-app/  a small product built with coding agents (ch7, ch9)
```

## Keeping it current

Tools, prices and setup steps change faster than books. Anything volatile here is dated "as of late 2026", and tools are named only as examples of a category. If a link, a tool or an instruction has gone stale, please open an issue with the file path and what changed.

The book links to files here by path, so files are not renamed or moved without updating the book.

## License

Everything in this repository, the templates, briefs, playbooks and the reference app, is released under the [MIT License](LICENSE). Use it, adapt it and build your own companies with it; keep the copyright notice in copies of the repository.

Two cautions that the license does not change. The legal templates in `playbooks/legal-templates/` are starting points only and must be reviewed by a qualified lawyer where you operate before you use them. And the example companies, Copper Pot Mixers and Ledgerly, are inventions for teaching: any resemblance to a real business is a coincidence.
