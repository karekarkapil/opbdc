# Permission matrix

*Companion to Chapter 2, "Your Agent Stack", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Chapters 14, 16, 17 and 19 refer back to it. Last reviewed: September 2026.*

## What this is

A one-page table listing, for every agent and every connector your company uses, what it may **read**, **write** and **delete**, and which actions need **your approval**. It is the working form of the security baseline in Chapter 2, and it doubles as your privacy map (Chapter 14): if you want to know what customer data an agent can see, the answer is here.

## How to use it

1. List every agent (support, finance, coding, research, marketing, operations) and every connector, key or skill it uses.
2. For each row, write the smallest permission that does the job. Read before write. Write before delete. Nothing gets delete unless it must.
3. Mark every irreversible action as **needs approval**. These never go above rung 2 of the [trust ladder](../playbooks/trust-ladder.md): money out, signing or changing a contract, deleting data, public statements, changing terms for existing customers.
4. Enforce it in the tools (separate accounts, scoped keys, spending caps), not only in the instructions. An instruction is a request; a permission is a wall.
5. Review it every quarter in the [permission audit](../playbooks/permission-audit.md), and whenever you add an agent, a connector or a new power.

---

## The matrix

Last checked: [YYYY-MM-DD] by [name]

| Agent | Connector / system | Identity used | Read | Write | Delete | Needs your approval | Spend cap | Trust rung | Notes |
|---|---|---|---|---|---|---|---|---|---|
| [Agent name] | [System, and source of connector] | [Its own account or key, never yours] | [What it may read] | [What it may create or change] | [Usually: nothing] | [Actions that stop and wait for you] | [Amount per day or month] | [0 to 4] | [Pinned version, date added] |
| | | | | | | | | | |
| | | | | | | | | | |

**Column guide**

- **Identity used:** every agent gets its own account or key (baseline rule 2), so you can see what it did and switch it off without locking yourself out.
- **Read:** be specific. "Orders for the customer in the current conversation" is a permission. "The order database" is a hope.
- **Write:** creating a draft is different from sending it. Say which.
- **Delete:** leave blank unless the job truly requires it, and then say exactly what, and why.
- **Needs your approval:** the gate. Anything here is prepared by the agent and executed only after you say yes.
- **Spend cap:** every agent that spends money, or runs on per-use pricing, has a cap and an alert.
- **Notes:** the connector's source (official, from the system's own maker, or a third party you have read), its pinned version, and the date you last checked it.

## Rules the matrix must satisfy

- [ ] No agent uses the founder's personal account, password or main card.
- [ ] No agent that reads untrusted content (the web, email, customer messages, supplier documents) also holds the keys to money or sensitive data. This is "separation of reading and power" (Chapter 14). The one exception worth allowing (Chapters 2, 10, 12 and 14): a small, capped credit on the customer's own account, such as a support agent's goodwill credit, and even that is logged. Never a refund, a card or a payment out.
- [ ] No secret (password, key, card number) appears in any instruction file, prompt or context file. Secrets live in a secrets store.
- [ ] Every connector comes from the system's own maker, or from a source you have read and pinned.
- [ ] Every row with a write permission leaves a log you can read later.
- [ ] Front-office agents (support, sales, marketing) can reach only their own company's systems (Chapter 17).
- [ ] Back-office agents that serve several companies have a separate, limited set of permissions per company, not one set of keys to everything.
- [ ] You know how to revoke every row in two minutes, from your phone (the kill switch, Chapter 14).

---

## Worked example: Copper Pot Mixers

*Illustration: Copper Pot Mixers is a fictional company, a small Bengaluru business selling craft cocktail mixers to independent bars and cafes. The rungs match the trust-ladder example in Chapter 4.*

Last checked: 2026-09-01 by the founder

| Agent | Connector / system | Identity used | Read | Write | Delete | Needs your approval | Spend cap | Trust rung | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Inbox agent | Company email (official connector) | Its own mailbox delegate, orders address only | Incoming mail to the orders address | Labels and folders only | Nothing | Nothing (sorting only) | Model usage cap per month | 4 | Official connector, pinned 2026-05-02 |
| Support agent | Order system | Its own support account | Orders and delivery status for the customer in the conversation only | Address change before dispatch; draft replacement order for a damaged-product report (held); goodwill credit up to Rs 300 per customer per month, on that customer's own account, for our own mistake, logged in "credits-2026" | Nothing | Every replacement; any refund; any credit above Rs 300 or outside the rule; any exception to the facts sheet | Model usage cap per month; credits capped in the order system at Rs 300 per customer per month | 3 | The one money power any agent holds (see the rule on separation above); decision D-8 |
| Support agent | Facts sheet and policies (read-only folder) | Its own support account | All | Nothing | Nothing | Not applicable | | 3 | |
| Sales agent | Customer file, facts sheet, chat transcripts | Its own account | Leads' conversations, the facts sheet, past proposals | Draft proposals only, in the proposals folder | Nothing | Every proposal (prices and promises); Meera sends it | Model usage cap per month | 2 | |
| Finance agent | Accounting software | Its own accounting user, no payment role | All ledgers and reports | Categorize, match, send routine invoices at dispatch and one routine reminder; draft everything else | Nothing | Any reminder to a top-ten account; any other message; any payment (the agent has no payment authority at all) | None needed: it cannot spend | 1 to 3 by job | |
| Finance agent | Bank feed | Read-only feed token | Transactions, read-only | Nothing | Nothing | Not applicable | | 2 | |
| Purchasing agent | Supplier email and portal | Its own account, no payment details | Supplier quotes, stock levels | Draft purchase orders only | Nothing | Every purchase order; Meera pays every supplier herself | None needed: it holds no card and cannot pay | 2 | Reads untrusted supplier email, so it holds no money power |
| Marketing agent | Social scheduling tool | Its own editor account, no publish right | Past posts and analytics | Drafts only | Nothing | Every post (brand voice still being refined; decision D-10) | Media generation cap | 1 | |
| Research agent | Web browser | A separate browser profile, signed in to nothing | Public web only | Report files in the research folder | Nothing | Widening scope; contacting anyone (it may not) | Model usage cap per task | 1 | |
| Coding agent | Code host and hosting platform | Its own code-host account and scoped token | The product's code, test results, preview builds | Branches and proposed changes | Nothing | Merging to the live product; any change to payments, login or data storage | Model usage cap per month | 2 | |
| Operations agent | Monitoring and logs | Read-only monitoring key | Logs, errors, speed, order counts | Morning summary; draft incident account | Nothing | Anything that touches customer data or money | Model usage cap per month | 3 to 4 | |

Note what is absent. No agent can pay a supplier, change bank details, change wholesale prices, delete a customer record or publish a post without the founder. No agent holds a card. The only money power in the whole matrix is the support agent's capped goodwill credit on a customer's own account, logged. The research agent, which reads the open web, has no access to email, money or accounts at all.

---

## A shorter version for your first week

If the full matrix feels like too much, start with three questions per connector, from Chapter 2:

| Connector | Is there an official connector from the system's own maker? | What is the smallest set of permissions the agent needs? | What should the agent never be able to do through it? |
|---|---|---|---|
| [System] | [Yes / no, source] | [Permissions] | [Forbidden actions] |

Then grow it into the full matrix before any agent talks to a customer or touches money.

## Related files

- [Cost worksheet](cost-worksheet.md), for the spend caps.
- [Trust ladder](../playbooks/trust-ladder.md), for the rung column.
- [Permission audit](../playbooks/permission-audit.md), the quarterly review of this table.
- [Agent instructions template](../context-kit/agent-instructions.md), where the same limits are written as standing rules.
