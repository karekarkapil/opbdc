# Product specifications (template)

*Companion to Chapters 3 and 6, "Context Is the Company" and "The Spec Is the Product", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

The index of what each product or feature does, why, and how you know it works. Each entry is a one-page spec in nine parts. When agents build from your words, the spec is the source code: what they build from, what they test against, what you review against, and what future agents read before they change anything.

## How to use it

- Keep one short spec per feature, service or process, in a `specs/` folder next to this file (or in your code repository).
- List every spec in the index below, with its status and date.
- Update the spec **in the same change** as the product. A spec that drifts from the product misleads the next agent.
- The full method, the ch6 reorder example and two more examples live in [`../playbooks/one-page-spec.md`](../playbooks/one-page-spec.md).

See filled-in versions: [beverage company](examples/beverage-company/specifications.md), [software company](examples/software-company/specifications.md).

---

## Template: the index

```markdown
# Specifications: [Company name]

Last checked: [YYYY-MM-DD]

| Spec | For | Status | Last updated | File |
|---|---|---|---|---|
| [Feature name] | [customer type] | [draft / agreed / built / live / retired] | [YYYY-MM-DD] | [specs/feature-name.md] |

## Retired
| Spec | Retired on | Why | Decision log entry |
|---|---|---|---|
| [ ] | [YYYY-MM-DD] | [ ] | [link] |
```

## Template: one spec (nine parts)

```markdown
# Spec: [Feature name]

Last checked: [YYYY-MM-DD]
Status: [draft / agreed / built / live]

1. **The problem:** [Two or three sentences, with at least one verbatim customer quote from the customer file.]
2. **Who it is for:** [The specific customer and the situation they are in when they use it.]
3. **The job:** "[What the customer is trying to get done, in their words.]"
4. **The must-haves:**
   - [Smallest set of capabilities that does the job. Each traces back to the problem.]
5. **The no list:**
   - No [thing], because [reason].
   - No [thing], because [reason].
6. **Acceptance tests:**
   - *Given* [situation], *when* [the customer does something], *then* [this happens].
   - *Given* [an error or edge case], *then* [this happens].
7. **Data and connections:** Reads [ ]. Creates or changes [ ]. Never touches [ ].
8. **Risks and open questions:**
   - [Risk] (mitigation: [ ])
   - [Question] (how we will find out: [ ])
9. **How we will know it worked:** [One or two measures], checked on [YYYY-MM-DD].
```

---

## Guidance notes

- **The no list is the most important section.** It is usually longer than the must-haves, and it is what stops an agent from "improving" things you never asked for.
- **Acceptance tests become automated tests.** Write at least one for an error or an edge case.
- **Specs are not only for software.** A service, a process or a physical product can be specified in the same nine parts (Chapter 6).
- **Link, don't copy.** Prices and policies in a spec point to the facts sheet.

## Where this breaks

- **A spec without acceptance tests** is a wish, and agents grant wishes in their own way.
- **Specs that drift.** Product changed, spec did not. The next agent builds from an outdated description.
- **Spec as wish list.** If a must-have does not trace to a customer quote or a measure, move it to the backlog.
