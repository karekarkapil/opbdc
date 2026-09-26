"""The rules of the reorder page: repeat, confirm, cancel.

No web code here. Every function takes the database connection, the account
and, where time matters, `now`, so the tests can drive each rule directly.
Quantities are bottles; orders go out in whole cases of six, flavours mixed.
"""

import re
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime

from app import db
from app.delivery import delivery_day
from app.facts import Facts


class OrderError(Exception):
    """A problem the manager can fix; the message is shown to them as written."""


@dataclass
class Line:
    product_id: int
    name: str
    pack: str
    quantity: int  # bottles
    price_paise: int  # today's price per bottle (B6)


@dataclass
class RepeatPlan:
    source: sqlite3.Row
    lines: list[Line] = field(default_factory=list)  # what can be repeated
    unavailable: list[Line] = field(default_factory=list)  # discontinued (B9)


def repeat_plan(conn, account_id: int, order_id: int) -> RepeatPlan | None:
    """What repeating this order would contain, or None if it is not this bar's."""
    source = db.get_order(conn, order_id, account_id)
    if source is None:
        return None
    plan = RepeatPlan(source)
    for row in db.order_lines(conn, order_id):
        line = Line(
            row["product_id"], row["name"], row["pack"], row["quantity"], row["current_price_paise"]
        )
        (plan.unavailable if row["discontinued"] else plan.lines).append(line)
    return plan


def parse_quantities(form, plan: RepeatPlan, facts: Facts) -> dict[int, int]:
    """Read the bottles typed on the review screen (B7, B8).

    Only products in the plan are read, so a form cannot add a product,
    and nothing else in the form (prices, account, discounts) is looked at.
    """
    if not plan.lines:
        raise OrderError(
            "None of the products in this order are still available, so it cannot be repeated."
        )
    most, case = facts.max_bottles_per_line, facts.bottles_per_case
    quantities = {}
    for line in plan.lines:
        raw = str(form.get(f"qty-{line.product_id}", "0")).strip()
        if not re.fullmatch(r"[0-9]{1,4}", raw):
            raise OrderError(f"Bottles must be whole numbers from 0 to {most}.")
        quantity = int(raw)
        if quantity > most:
            raise OrderError(
                f"Up to {most} bottles of each flavour per order. For more, message us."
            )
        if quantity > 0:
            quantities[line.product_id] = quantity
    bottles = sum(quantities.values())
    if bottles == 0:
        raise OrderError(f"Add at least one case ({case} bottles), or go back to your orders.")
    if bottles % case:
        short, over = case - bottles % case, bottles % case
        raise OrderError(
            f"Orders go out in whole cases of {case} bottles, and flavours can be mixed. "
            f"You have {bottles} bottles: add {short} more, or remove {over}."
        )
    return quantities


def subtotal_paise(plan: RepeatPlan, quantities: dict[int, int]) -> int:
    """What these bottles cost at today's prices, before delivery."""
    prices = {line.product_id: line.price_paise for line in plan.lines}
    return sum(prices[pid] * qty for pid, qty in quantities.items())


def place_repeat(
    conn,
    account,
    plan: RepeatPlan,
    quantities: dict[int, int],
    token: str,
    now: datetime,
    facts: Facts,
) -> tuple[int, bool]:
    """Create the order and fix its delivery day and charge (B4, B14).

    Returns (order id, already placed). The token comes from the review screen
    and has been checked by the caller. The same token never creates a second
    order, so a double tap or a resent form is harmless (B13).
    """
    existing = db.find_order_by_token(conn, account["id"], token)
    if existing is not None:
        return existing["id"], True

    day = delivery_day(now, facts.schedule, account["area"])
    prices = {line.product_id: line.price_paise for line in plan.lines}
    lines = [(pid, qty, prices[pid]) for pid, qty in quantities.items()]
    charge = facts.delivery_charge(sum(quantities.values()))
    try:
        new_id = db.add_order(
            conn, account["id"], now, lines, day.date, day.reason,
            request_token=token, delivery_charge_paise=charge,
        )  # fmt: skip
        return new_id, False
    except sqlite3.IntegrityError:
        # Two taps arrived at the same instant, and the database kept one.
        existing = db.find_order_by_token(conn, account["id"], token)
        if existing is None:
            raise  # a different integrity problem: do not hide it
        return existing["id"], True


def same_quantities(conn, order_id: int, quantities: dict[int, int]) -> bool:
    placed = {row["product_id"]: row["quantity"] for row in db.order_lines(conn, order_id)}
    return placed == quantities


def cancel_deadline(order, facts: Facts) -> datetime:
    return db.from_utc_text(order["created_at"]) + facts.cancel_window


def can_cancel(order, now: datetime, facts: Facts) -> bool:
    """Open for 30 minutes after confirming; closed at exactly 30:00 (B10).

    Never open before the order was placed (a demo pretend clock can go back in time).
    """
    placed_at = db.from_utc_text(order["created_at"])
    return order["status"] == "placed" and placed_at <= now < cancel_deadline(order, facts)


def cancel(conn, order, now: datetime, facts: Facts) -> bool:
    """Cancel if the window is open. Cancelling twice is harmless. Returns success."""
    if order["status"] == "cancelled":
        return True
    if not can_cancel(order, now, facts):
        return False
    db.cancel_order(conn, order["id"])
    return True
