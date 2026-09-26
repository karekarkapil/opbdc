# Glossary (template)

*Companion to Chapter 3, "Context Is the Company", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

Every term with a special meaning in your company or your industry. Agents confidently misread jargon: "covers" means guests served in an evening, not bottle caps. A short glossary prevents a whole class of fluent, wrong answers.

## How to use it

- Add a term the first time an agent misreads it, or the first time a customer uses a word you had to ask about.
- Give the meaning **in your company**, not the dictionary meaning.
- Where a word has a common meaning that is wrong for you, say so.
- Include internal names: product nicknames, plan names, the names of your agents and playbooks.
- Keep it alphabetical so agents and people can scan it.

See filled-in versions: [beverage company](examples/beverage-company/glossary.md), [software company](examples/software-company/glossary.md).

---

## Template

```markdown
# Glossary: [Company name]

Last checked: [YYYY-MM-DD]
Rule for agents: when a term here appears in a message or document, use this meaning.

## Industry terms
| Term | What it means here | Not to be confused with | Example in a sentence |
|---|---|---|---|
| [term] | [meaning] | [common wrong reading] | "[customer's sentence using it]" |

## Our internal terms
| Term | What it means | Where it is defined |
|---|---|---|
| [product nickname] | [the full product name] | [facts sheet] |
| [plan or offer name] | [what it includes] | [facts sheet] |
| [agent or playbook name] | [what it does] | [playbooks index] |

## Abbreviations
| Abbreviation | Stands for | Meaning here |
|---|---|---|
| [ ] | [ ] | [ ] |

## Words we avoid
| Word | Why | Use instead |
|---|---|---|
| [ ] | [ ] | [ ] |
```

---

## Starter terms from the book

These appear across the companion repo. Keep the ones you use.

| Term | Meaning |
|---|---|
| Agent | Software that takes a goal, plans, uses tools and checks its work, for minutes or hours at a time |
| Brief | What you give an agent for one job: goal, context, constraints, done, verification, questions |
| Context kit | The ten files that tell agents what your company is |
| Escalate | Stop and hand a decision to the founder |
| Facts sheet | The single source of truth for anything an agent tells a customer |
| Golden set | A handful of past examples with known right answers, used to test an agent before you trust a change |
| Skill | A folder of written instructions (and sometimes scripts) that an agent loads when a task calls for it |
| Trust ladder | The five rungs of supervision, from 0 Manual to 4 Autonomous within guardrails |

## Guidance notes

- **One meaning per term.** If a word means two things in your company, rename one of them.
- **Customer words first.** If customers say "restock" and you say "reorder", agents should understand both and reply with the customer's word.

## Where this breaks

- **Defined once, used differently.** If the facts sheet uses a plan name the glossary does not know, fix one of them.
- **Too long.** A glossary of 200 common words hides the ten that matter. List only terms an agent could plausibly get wrong.
