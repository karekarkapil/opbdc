# Keep, but adapt

*Companion to Chapter 16, "The Second Company", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

The files whose **structure** carries across to a new company, and whose **content** must be rewritten. For each file, the placeholders below mark exactly what changes. Use the convention from the [README](README.md): `[ADAPT: ...]` for anything you rewrite, `[EARN: ...]` for anything that can only come from the new company's own customers and decisions.

## How to use it

Copy each file into the new company's folder, insert the markers listed below at the matching places, then replace them one by one. A file is done when it contains no markers.

---

## 1. Design system

Source: [../../context-kit/design-system.md](../../context-kit/design-system.md). Same six parts, new colors, new type, new imagery.

| Part | Keep | Placeholders |
|---|---|---|
| Our customers' real conditions | The section and its four lines (device, connection, where and when, the design rule that follows) | `[EARN: the new customers' real devices, connections and moments of use, observed, not assumed]` |
| Foundations | The named token structure (action, warning, error, success, text, background), the spacing scale approach | `[ADAPT: color values]`, `[ADAPT: fonts and sizes]`, `[ADAPT: corner and shadow style]` |
| Components | The list of standard components and the "when to use" format | `[ADAPT: how each component looks]` |
| Layout rules | "The two or three things customers come for are always one tap away" | `[EARN: the two or three things THIS customer comes for]` |
| Imagery | The rules: real product, no generated customers, examples you love and would never use | `[ADAPT: photographic style, light, backgrounds, people and places]` |
| Interface words | The four rules (no distress, truthful, pleasant and beneficial, no tricks) | `[ADAPT: sample error, confirmation and empty-screen messages in the new voice]` |
| Accessibility | Minimum sizes, contrast, screen reader labels, slow connections, the review routine | `[ADAPT: the minimums, checked against the real conditions above]` |

## 2. Voice guide

Source: [../../context-kit/voice-guide.md](../../context-kit/voice-guide.md). Same principles, new voice.

- Keep: the section structure of the [voice-guide template](../../context-kit/voice-guide.md), the format of "a reply you love, a reply you hate, and why", the disclosure policy structure.
- "In one sentence": `[ADAPT: who the company sounds like, for the new customer]`
- "Principles": `[ADAPT: three to five principles, each with an example in the new voice]`
- "Words we use / words we avoid": `[EARN: the words the new customers use, and the words to avoid in this industry]`
- "A reply we love" and "A reply we hate": `[EARN: real replies to the new customers, one you approved unchanged and one you rejected, with why]`
- "By channel": `[EARN: the channels where the new customers actually are]`
- "Things we never say": `[ADAPT: the new company's claims it must never make]`
- "Our disclosure policy": `[ADAPT: wording, if the new company uses AI differently]`
- "Rejection log": start it empty.

## 3. Support, sales and marketing playbooks

Same patterns, new facts, new offers.

| File | Keep | Placeholders |
|---|---|---|
| [../../briefs/support-agent.md](../../briefs/support-agent.md) | Disclosure first, grounding rule, escalation rules, handover format, character, protection rules | `[ADAPT: company name and what it sells]`, `[ADAPT: tools and their limits, including the goodwill credit amount]`, `[ADAPT: sample replies]`, `[EARN: the key customers who always go to the founder]` |
| [../../playbooks/first-ten.md](../../playbooks/first-ten.md) | The method: agents prepare, you rewrite and send | `[EARN: who the ideal customer is, from the new ten conversations]`, `[ADAPT: note template in the new voice]` |
| [../../playbooks/pillar-and-spoke.md](../../playbooks/pillar-and-spoke.md) | The workflow, the edit pass, the volume cap | `[EARN: the two or three channels where these customers actually are]`, `[ADAPT: volume cap]` |
| [../../briefs/research-agent.md](../../briefs/research-agent.md) | The rules: pain, quotes with links, money and workarounds, untrusted reading | `[ADAPT: market variant and sources]` |
| Your first company's proposal playbook (the "Drafting a proposal or quote" line in the [playbooks index template](../../context-kit/playbooks.md); Copper Pot's is "Proposal for a multi-outlet account" in its [index](../../context-kit/examples/beverage-company/playbooks.md)), and the paid-pilot template in [first-ten.md](../../playbooks/first-ten.md) | Agents draft, you send; pricing is yours; first-order quantities start small | `[EARN: prices and offers]`, `[ADAPT: the proposal's sections for the new product]` |

## 4. Golden sets and evals

Same method, new examples. Sources: [../../playbooks/golden-sets/support.md](../../playbooks/golden-sets/support.md), [../../playbooks/golden-sets/finance.md](../../playbooks/golden-sets/finance.md), [../../playbooks/golden-sets/content.md](../../playbooks/golden-sets/content.md).

- Keep: the format, the run log, the rule to rerun on every change of instructions or tools.
- `[EARN: five to ten real past cases from the new company, with the answers you approved]`
- Until the new company has real cases, its agents stay at rung 1 (draft) for that job.

## 5. Agent instructions

Source: [../../context-kit/agent-instructions.md](../../context-kit/agent-instructions.md).

- Keep: the one-to-two-page shape, the always/never/when-to-ask sections, the escalation rules.
- `[ADAPT: where things are]`, `[ADAPT: commands, for software]`, `[ADAPT: industry-specific never rules]`

## 6. Glossary and playbooks index

- Glossary: keep general business terms; `[EARN: the new industry's jargon, as customers use it]`.
- Playbooks index ([../../context-kit/playbooks.md](../../context-kit/playbooks.md)): keep the skill format; `[ADAPT: the new company's recurring jobs]`.

## Final check

- [ ] Search the new company's folder for `[ADAPT:`: zero results.
- [ ] Search for `[EARN:`: zero results in any file an agent reads.
- [ ] Search for company one's name, domain, product names and prices: zero results.
