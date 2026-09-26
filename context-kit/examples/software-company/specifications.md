# Specifications: Ledgerly

*Companion to Chapters 3 and 6 of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

*Illustration: Ledgerly is a fictional company. Full versions of the software and service specs are worked examples in [`../../../playbooks/one-page-spec.md`](../../../playbooks/one-page-spec.md).*

Last checked: 2026-09-10

| Spec | For | Status | Last updated | File |
|---|---|---|---|---|
| Receipt match | Owners on a phone, after a purchase | live | 2026-02-02 | specs/receipt-match.md |
| Show the source | Anyone reading a report | live | 2026-04-20 | specs/show-the-source.md |
| Bank-feed outage alert | Every customer with a bank connection | built | 2026-08-05 | specs/bank-feed-alert.md |
| Ledgerly Assist (service) | Owners who want the month done | live | 2026-05-15 | specs/assist-service.md |
| Client import for bookkeepers | Bookkeepers moving 10+ clients | draft | 2026-09-08 | specs/client-import.md |

## Retired
| Spec | Retired on | Why | Decision log entry |
|---|---|---|---|
| AI cash-flow prediction | 2026-03-30 | Customers did not trust it; it added support load; the no list said "no forecasts" and we ignored it | D-5 |

---

## Summary: Bank-feed outage alert (software)

1. **The problem:** a bank connection can stop silently. "My bank feed stopped on the 3rd and nobody told me until the 20th."
2. **Who it is for:** any customer with a bank connection, usually checking once a week.
3. **The job:** "Tell me when my numbers stop being complete."
4. **The must-haves:** detect a connection with no new lines for longer than its normal gap; email the customer and show a banner; one button to reconnect.
5. **The no list:** no automatic re-entry of missing lines (they come from the bank or not at all); no alerts for connections the customer paused; no more than one email per connection per day.
6. **Acceptance tests:**
   - *Given* a connection that normally updates daily, *when* 48 hours pass with no new lines, *then* the customer gets one email and sees a banner.
   - *Given* the customer reconnects, *then* the banner clears and missing lines appear with their original dates.
   - *Given* a paused connection, *then* no alert is sent.
7. **Data and connections:** reads connection status and last-line dates; sends email; never changes transactions.
8. **Risks and open questions:** false alarms for quiet accounts (use each connection's own normal gap).
9. **How we will know it worked:** re-contact about "missing transactions" falls by half within eight weeks; check 2026-10-01.

## Summary: Ledgerly Assist (service)

- **Must-haves:** client sends bank access and receipts by the 3rd working day; reconciled books, summary and questions delivered by the 10th working day; every close signed off by a qualified bookkeeper.
- **No list:** no tax filing; no paying bills; no guessing missing receipts; no clients with inventory or payroll above ten staff.
- **Acceptance tests:** three sample months with known right answers (the Assist golden set) reconcile exactly before any new client starts.
- **Worked if:** clients renew after three months, and the founder's checking time is under 45 minutes per client.
