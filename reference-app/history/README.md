# History: the briefs and reviews

Last checked: 2026-09-26.

This is how the reference app was actually built, one step at a time, by a coding agent (Claude) working from the book's method. Each file is the brief for one step, in the six-part form from Chapter 3 (goal, context, constraints, definition of done, verification, questions), written at the start of the step, followed by its review record: what was checked, the evidence (test counts from real runs), what changed after review, and the lessons added to [`../AGENTS.md`](../AGENTS.md).

Nothing here was rewritten to look better. The only later edits: wording that overstated what had been checked was corrected; spelling was made US throughout; brief 06 was set out in the same sections as the others; and dated notes were added to briefs 04, 05 and 06 where a later step changed what they describe (each note says so). The records keep the failed runs, the tests that were wrong, and the facts the first version got wrong, because that is what a build history is for.

| Step | Brief | What happened, in one line |
|---|---|---|
| 1 | [From spec to failing tests](01-brief-spec-to-tests.md) | Spec, instruction file and 58 tests written first; 3 passed on an empty app, so they were given positive controls. |
| 2 | [From failing tests to the feature](02-brief-tests-to-feature.md) | Green in four runs; a threading bug and a framework change found on the way; walking the pages at phone width found three problems the tests could not see. |
| 3 | [Independent review, then fixes](03-brief-review-fixes.md) | A second agent reviewed against the spec and found ten issues, the worst a form token that anyone could invent; eight fixed, one partly fixed, one declined, each with a reason. |
| 4 | [Match the company's own facts sheet](04-brief-relocalize-to-facts-sheet.md) | The first version invented London facts; rebuilt on the Bengaluru facts sheet, with a test that fails if the two drift apart. |
| 5 | [Continuous integration, deployment notes, README](05-brief-ci-and-deploy.md) | Every CI step run locally; the container built, ran, passed its health check and took an order. |
| 6 | [Walk the running app against the acceptance tests](06-brief-live-walk.md) | An independent walk on a fresh install passed every acceptance test and found one gap: after the cancel window, the order page gave no next step. Fixed test-first; 94 tests pass. |
| 7 | [Fixes from the second companion review](07-brief-review-2-fixes.md) | Nineteen findings handled (one, an empty folder, left for deletion): type checks (mypy) added to CI, two facts moved out of the templates into the facts file, CI made to run when the facts sheet changes, the CI file's move recorded; 7 new or changed tests seen failing first; 97 tests pass. |

Two things to know when reading the early files:

- **Steps 1 to 3 describe the first version,** set in London with prices in pounds. Step 4 explains why that was wrong and what replaced it. The early records are left as they were.
- **The spec's decisions were numbered D1 to D12 until step 4,** then renumbered B1 to B15 ("build"), so they cannot be confused with the company decision log's D-numbers. Early records use the old numbers.

The brief format is the one in [`../../briefs/brief-template.md`](../../briefs/brief-template.md).
