# Feature: Reorder in one tap

Company: Copper Pot Mixers (fictional), Bengaluru, which sells craft cocktail mixers to independent bars and cafes. Founder: Meera.
Spec version: 1.1. Last checked: 2026-09-26.
Sources: the one-page spec in Chapter 6, "The Spec Is the Product" (also in [`../../playbooks/one-page-spec.md`](../../playbooks/one-page-spec.md)), and the company facts sheet, [`../../context-kit/examples/beverage-company/facts-sheet.md`](../../context-kit/examples/beverage-company/facts-sheet.md), which is the source of truth for every fact the page states. Parts 1 to 9 below are the book's text. The only additions are: the acceptance tests marked "from the risk line" and "from the no list"; the answer to the open question, from the company's own files; and the section "Decisions made while building", which records what the code needed to know that the page did not say.

## 1. Problem

Bar managers reorder the same mixers every week or two, usually late at night after closing, from their phones. Today they must message us, and we must reply the next morning. From the customer file: "By the time you answer, I've forgotten what I asked for."

## 2. For

A bar manager or owner with an existing account, on a phone, at the end of a shift.

## 3. Job

"Send me the same as last time, maybe a bit more of the pineapple."

## 4. Must-haves

- Show the last three orders.
- Repeat any of them with one tap.
- Adjust quantities before confirming.
- Confirm the delivery day from the facts sheet's delivery schedule.

## 5. No list

- No new products in this flow (discovery belongs elsewhere).
- No discounts or promotions (they complicate the confirmation).
- No credit or payment changes (payment terms stay as agreed on the account).
- No ordering for a different outlet (multi-outlet accounts come later, if at all).

## 6. Acceptance tests

Each test has a number. The automated test for it carries the same number in its name (for example `test_at1_...`), so a reviewer can find it.

- **AT1.** *Given* a manager with two past orders, *when* they open the page, *then* both appear, newest first, with dates and totals.
- **AT2.** *Given* a past order, *when* they tap "Repeat", change one quantity and confirm, *then* a new order is created with the changed quantity, and they see the delivery day.
- **AT3.** *Given* an order placed after the weekly cut-off, *then* the delivery day shown is the following week's, and the page says why.
- **AT4.** *Given* a product that has been discontinued, *then* it is shown as unavailable and left out of the repeat, with a note.

From the risk line ("Add a confirmation step and a thirty-minute cancel window"):

- **AT5.** *Given* a manager who has just confirmed an order, *when* they tap "Cancel" within thirty minutes, *then* the order is cancelled and the page says so.
- **AT6.** *Given* an order confirmed more than thirty minutes ago, *then* no cancel button is shown, and a cancel request is refused, pointing the manager to Meera (the facts sheet: "After that, message us and Meera will decide").
- **AT7.** *Given* a manager on the confirmation step, *when* they tap "Confirm" twice (a double tap or a resubmitted form), *then* only one order is created.

From the no list and the data rule:

- **AT8.** *Given* any use of this page, *then* prices, payment terms and account details are unchanged, no product outside the original order can be added, and the order is always for the signed-in bar's own account.

## 7. Data

Reads the account's order history and the product list. Creates orders. Never changes prices, payment terms or account details.

## 8. Risks and questions

- Will managers accidentally repeat an order twice? (Add a confirmation step and a thirty-minute cancel window.) Covered by AT5 to AT7.
- Do owners want managers ordering without approval? Ask three owners. **Answered** (company specifications file): two said yes; one asked for a notification, which is in the backlog. Not in this version.

## 9. Worked if

Within six weeks, half of repeat orders come through this page, and the average time from a manager's request to our confirmation falls from about ten hours to under a minute. (In the company's story, the page went live on 2026-06-02 and this was checked and met on 2026-07-14, decision log D-9. This folder is a from-scratch rebuild by a coding agent; see `history/`.)

---

## Decisions made while building (2026-09-26)

The one-page spec left these open. Code cannot, so each was decided and written here, with the reason. They are numbered B1 to B15 ("build") so they are not confused with the company decision log's D-numbers. Change them here first, then in the code and tests. Facts come from the facts sheet and live in the app as `facts/facts.toml`.

| # | Decision | Why |
|---|---|---|
| B1 | The weekly cut-off is Sunday 8 pm. Each area has a fixed delivery day, Monday to Thursday, taken from the facts sheet's delivery schedule. | Facts sheet: "Weekly cut-off: Sunday 8 pm for delivery that week", and the area table. |
| B2 | An order is delivered on the bar's area day in the first week whose Sunday 8 pm cut-off it made. Exactly 8:00:00 pm counts as after. | One rule for every area. A boundary must be exact, or tests cannot pin it. |
| B3 | The cut-off is judged in Bengaluru time (India Standard Time, UTC+5:30, no daylight saving), not the server's. | Servers usually run on UTC. At 7 pm UTC on a Sunday it is already 12:30 am on Monday in Bengaluru. |
| B4 | The delivery day and the reason are fixed at the moment the order is confirmed, and stored with the order. The review screen shows a preview; if the cut-off passes while the manager is reviewing, the confirmation shows the later day and says why. | The customer must be told the day that will actually happen. |
| B5 | "The last three orders" means the last three that were not cancelled, newest first. | A cancelled duplicate should not push a real order off the list. |
| B6 | A repeat uses today's prices per bottle, not the prices of the old order. The review screen says so, and shows the total. | The page never changes prices (part 7), and old prices would be a hidden discount (part 5). The facts sheet records price changes (Tender Coconut, Rs 520 to Rs 560, 1 July 2026). |
| B7 | Quantities are bottles. A quantity of 0 leaves that flavour out. No flavour can exceed 60 bottles in one order (a page rule in `facts/facts.toml`, to catch a typed 600 instead of 6). | Bar managers count bottles ("our par for the pineapple is four bottles"). A runaway typo is the likely mistake on a phone. |
| B8 | An order must be whole cases of six bottles, flavours mixed, at least one case. If it is not, the page says how many bottles to add or remove. | Facts sheet: "Sold by the case of six bottles; mixed cases allowed", "Minimum order: one case". |
| B9 | A discontinued product is shown, greyed, with "No longer available", and is not part of the repeat. If every product in the old order is discontinued, the order cannot be repeated, and the page says so. | AT4, and nothing silently disappears. |
| B10 | The cancel window is 30 minutes from confirmation. At exactly 30:00 the window is closed. After it, the page points to Meera. | Facts sheet, and the risk line. |
| B11 | Sign-in is not built. In production, the signed-in account comes from a managed login provider. For review, a demo mode (switched on by `DEMO_MODE=1`) lets the reviewer pick one of the seeded bars and set a pretend Bengaluru time, so AT3 and AT6 can be walked on a phone without waiting for Sunday night. | Chapter 7: do not build logins; use a managed service. A reviewer must be able to walk every acceptance test. |
| B12 | Viewing, repeating or cancelling another account's order returns "not found". | The no list: no ordering for a different outlet. |
| B13 | Confirming and cancelling need a token signed by the server for that bar and that order. The same confirmation token never creates a second order; if it is resent with different quantities, the page says the changes were not applied. | AT7, and so that another website cannot post an order on a bar's behalf (found in review, brief 03). |
| B14 | Delivery is free for two cases or more; otherwise Rs 150 is added, shown on the review screen and stored with the order. | Facts sheet: "Charge: free for two cases or more; otherwise Rs 150 per delivery." |
| B15 | A bar in an area with no fixed day ("Other areas within city limits") can still order; the page says "Day to be confirmed" and that Meera will message them, and no date is promised. | Facts sheet: "Ask; Meera confirms the day." The page must never state a fact the sheet does not. |
