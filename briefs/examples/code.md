# Example brief: code

*Companion to Chapters 3, 6 and 7, "Context Is the Company", "The Spec Is the Product" and "Building with Coding Agents", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Ledgerly is a fictional company used for illustration.* Ledgerly's customers asked for a way to see which bank lines still have no receipt attached. The founder wrote a one-page spec for "Missing receipts list" before briefing a coding agent. The project's agent instruction file already says how the code is organized, how to run the tests and what never to touch.

## The brief

> **Goal:** Build the "Missing receipts list" feature from the spec, so a small-business owner can see, in one place, every bank line over the receipt threshold that has no receipt attached. Customers tell us they spend Sunday nights matching receipts to bank lines by hand.
>
> **Context:** Read the one-page spec at `specs/missing-receipts.md` (listed in the specifications index; must-haves, no list, acceptance tests) and the project's agent instruction file. The receipt threshold is a per-business setting that already exists in the settings model; do not create a new one.
>
> **Constraints:** Tests first: turn the five acceptance tests in the spec into automated tests, run them, and show me them failing before you write the feature. Keep the change small: this feature only, no refactoring of unrelated code, no new dependencies without asking. Read-only on bank data: this feature must not change, delete or re-categorize any transaction. Work on its own branch. Do not touch the billing, login or bank-feed code.
>
> **Done:** A pull request on its own branch with the tests and the feature, a preview link, and a plain-language description: what changed, why, what you did not do, and what could go wrong.
>
> **Verification:** Show the test run failing before the feature and passing after. Run the full test suite, the type checks, the linter and the secret scan, and paste the results. Include a screenshot of the list at phone width with the sample data. State whether this change stores, sends or displays any personal or payment information, and where.
>
> **Questions:** Ask before changing any existing test, any database schema, or anything outside the feature's folder. If an approach to a failing test has already failed, stop and tell me rather than repeating it.

**Plan first:** before writing code, send me your plan: the files you will change or add, the tests, and the risks. Wait for my reply.

## Why this brief works

- The **spec is the brief**. Its acceptance tests become automated tests, which gives the agent a way to verify its own work and gives you evidence.
- **Showing the tests failing first** proves they test something real.
- **Small change, own branch, no unrelated edits** keeps the result reviewable in minutes.
- The **"ask before changing any existing test"** rule guards against an agent under pressure changing the test instead of the code.

## What to check when it comes back

- [ ] Read the diff, not only the summary. The description is a claim; the diff is the evidence.
- [ ] Did any existing test change? If so, why?
- [ ] Open the preview on a phone and walk each acceptance test yourself, including the edge cases (no bank lines, all receipts attached, a line exactly at the threshold).
- [ ] Ask a second agent, one that did not write the code, to review the change against the spec and list risks. Read the risks.
- [ ] New dependencies: none, or each one reviewed and pinned.
- [ ] Record: any mistake you corrected becomes one line in the project's agent instruction file.

If you don't code: you can still do every step above except reading the diff line by line. Walk the tests on the preview, try to break it, ask for a plain-language explanation, and use a second agent as reviewer. See the [agent instructions template](../../context-kit/agent-instructions.md).
