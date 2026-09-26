# Specifications: Copper Pot Mixers

*Companion to Chapters 3 and 6 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Illustration: Copper Pot Mixers is a fictional company.*

Last checked: 2026-09-10

| Spec | For | Status | Last updated | File |
|---|---|---|---|---|
| Reorder in one tap | Bar managers with an existing account, on a phone | live | 2026-06-02 | specs/reorder-in-one-tap.md |
| Staff recipe card | Bar and cafe staff, behind the bar | live | 2026-02-05 | specs/staff-recipe-card.md |
| Onboarding a new bar (process) | New accounts, first order | agreed | 2026-04-10 | specs/onboarding-new-bar.md |
| New flavor: Mango and Kashmiri Chilli (physical product) | Bars running a summer menu | draft | 2026-09-10 | specs/new-flavor-mango-chilli.md |

## Retired
| Spec | Retired on | Why | Decision log entry |
|---|---|---|---|
| Subscription delivery | 2026-02-20 | Customers order to their own stock levels; no one wanted a fixed schedule | D-6 |

---

## Summary: Reorder in one tap

The full nine-part spec, as written before building, is the worked example in [`../../../playbooks/one-page-spec.md`](../../../playbooks/one-page-spec.md). In short:

1. **The problem:** managers reorder the same mixers every week or two, late at night, from their phones, and wait until morning for a reply. "By the time you answer, I've forgotten what I asked for."
2. **Who it is for:** a bar manager or owner with an existing account, on a phone, at the end of a shift.
3. **The job:** "Send me the same as last time, maybe a bit more of the pineapple."
4. **The must-haves:** show the last three orders; repeat any with one tap; adjust quantities before confirming; confirm the delivery day from the facts sheet's schedule.
5. **The no list:** no new products in this flow; no discounts or promotions; no credit or payment changes; no ordering for a different outlet.
6. **Acceptance tests:** past orders newest first; repeat with a changed quantity; after the weekly cut-off the following week's day is shown with the reason; discontinued products left out with a note.
7. **Data and connections:** reads order history and the product list; creates orders; never changes prices, payment terms or account details.
8. **Risks and open questions:** accidental double orders (a confirmation step and a 30-minute cancel window); do owners want managers ordering without approval? (asked three owners: two said yes, one asked for a notification, now in the backlog).
9. **How we will know it worked:** within six weeks, half of repeat orders through the page, and time from request to confirmation down from about ten hours to under a minute. Checked 2026-07-14: met (see decision log D-9).

## Summary: New flavor, Mango and Kashmiri Chilli (draft)

- **Must-haves:** shelf life of at least 9 months unopened; cost per serve within our current range; needs only a jigger and shaker.
- **No list:** no ingredients that need refrigeration before opening; no flavor that only works in one cocktail.
- **Tests:** three bars make it on a busy night, and reorder.
- **Open question:** can we source Kashmiri chilli at a steady price all year? (supplier research brief queued)
