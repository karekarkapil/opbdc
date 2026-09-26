"""Shared test fixtures: a small world of Bengaluru bars, products and past orders.

Facts from the company's facts sheet: prices per 750 ml bottle, orders in whole
cases of six (flavours can be mixed), cut-off Sunday 8 pm, a fixed delivery day
by area, Monday to Thursday. Money is in paise (Rs 540 is 54000).

The clock is fake and starts on Saturday 26 September 2026 at 10:00 in Bengaluru,
before the Sunday 27 September 8 pm cut-off.
"""

import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest
from fastapi.testclient import TestClient

from app import db
from app.main import create_app

IST = ZoneInfo("Asia/Kolkata")


def ist(year, month, day, hour=0, minute=0, second=0) -> datetime:
    """A moment in Bengaluru time."""
    return datetime(year, month, day, hour, minute, second, tzinfo=IST)


class FakeClock:
    def __init__(self, now: datetime):
        self.now = now

    def __call__(self) -> datetime:
        return self.now

    def advance(self, **kwargs) -> None:
        self.now += timedelta(**kwargs)


@dataclass
class World:
    db_path: Path
    # accounts
    lantern: int  # The Tin Lantern, Indiranagar (Monday): five past orders
    banyan: int  # Banyan Street Cafe, Koramangala (Tuesday): two past orders
    owl: int  # The Night Owl, Jayanagar (Thursday): no orders yet
    # products, per bottle
    pineapple: int  # Roasted Pineapple and Ginger, Rs 540
    kokum: int  # Kokum and Black Salt, Rs 520
    chilli: int  # Smoked Chilli and Lime, Rs 520
    coconut: int  # Tender Coconut and Lemongrass, Rs 560 (was Rs 520 before July)
    cola: int  # Jaggery Cola Syrup, Rs 480
    guava: int  # Guava and Pink Salt: discontinued, for AT4
    # orders, oldest first
    lantern_orders: list[int]
    banyan_orders: list[int]


@pytest.fixture
def world(tmp_path) -> World:
    path = tmp_path / "test.db"
    conn = db.connect(path)
    terms = "Due on delivery"  # no credit terms (facts sheet)
    lantern = db.add_account(conn, "The Tin Lantern", "Indiranagar", terms)
    banyan = db.add_account(conn, "Banyan Street Cafe", "Koramangala", terms)
    owl = db.add_account(conn, "The Night Owl", "Jayanagar", terms)

    bottle = "750 ml bottle"
    pineapple = db.add_product(conn, "Roasted Pineapple and Ginger", bottle, 54000)
    kokum = db.add_product(conn, "Kokum and Black Salt", bottle, 52000)
    chilli = db.add_product(conn, "Smoked Chilli and Lime", bottle, 52000)
    coconut = db.add_product(conn, "Tender Coconut and Lemongrass", bottle, 56000)
    cola = db.add_product(conn, "Jaggery Cola Syrup", bottle, 48000)
    guava = db.add_product(conn, "Guava and Pink Salt", bottle, 52000, discontinued=True)

    def order(account, when, *lines, charge=0):
        return db.add_order(conn, account, when, list(lines), delivery_charge_paise=charge)

    lantern_orders = [
        order(lantern, ist(2026, 8, 24, 1, 40), (pineapple, 6, 54000), (kokum, 6, 52000)),
        order(lantern, ist(2026, 8, 31, 1, 10), (pineapple, 6, 54000), (kokum, 6, 52000)),
        order(lantern, ist(2026, 9, 7, 0, 55), (pineapple, 6, 54000), (chilli, 6, 52000)),
        order(lantern, ist(2026, 9, 14, 1, 30), (kokum, 12, 52000)),
        order(
            lantern,
            ist(2026, 9, 21, 0, 30),
            (pineapple, 6, 54000),
            (coconut, 3, 56000),
            (guava, 3, 52000),
        ),
    ]
    banyan_orders = [
        order(banyan, ist(2026, 9, 10, 16, 40), (coconut, 6, 56000), (cola, 6, 48000)),
        order(banyan, ist(2026, 9, 24, 16, 30), (kokum, 6, 52000), charge=15000),
    ]
    conn.close()
    return World(
        path, lantern, banyan, owl, pineapple, kokum, chilli, coconut, cola, guava,
        lantern_orders, banyan_orders,
    )  # fmt: skip


@pytest.fixture
def clock() -> FakeClock:
    return FakeClock(ist(2026, 9, 26, 10, 0))


@pytest.fixture
def app(world, clock):
    application = create_app(world.db_path, demo_mode=True)
    application.state.clock = clock
    return application


@pytest.fixture
def client(app):
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def conn(world):
    connection = sqlite3.connect(world.db_path)
    connection.row_factory = sqlite3.Row
    yield connection
    connection.close()


# ---- helpers ------------------------------------------------------------------


def sign_in(client, account_id: int) -> None:
    """Demo mode stands in for a managed login provider (spec B11)."""
    client.cookies.set("demo_account", str(account_id))


def order_ids_in(html: str) -> list[int]:
    """Order ids in the order they appear on the page."""
    return [int(x) for x in re.findall(r'data-order-id="(\d+)"', html)]


def form_token(html: str) -> str:
    """The token the server put in a form on this page ("" if there is no form)."""
    found = re.search(r'name="token" value="([^"]+)"', html)
    return found.group(1) if found else ""


def review_token(client, order_id: int) -> str:
    """Open the review screen, as a manager would, and take its token."""
    return form_token(client.get(f"/repeat/{order_id}").text)


def confirm(client, order_id: int, quantities: dict[int, int], token=None, extra=None):
    """Confirm a repeat of `order_id` from its review screen.

    Without `token`, the token is taken from the review screen, as a phone would.
    Pass `token` to replay one, or to test a forged one.
    """
    form = {f"qty-{pid}": str(qty) for pid, qty in quantities.items()}
    form["token"] = review_token(client, order_id) if token is None else token
    form.update(extra or {})
    return client.post(f"/repeat/{order_id}", data=form)


def cancel_token(client, order_id: int) -> str:
    return form_token(client.get(f"/orders/{order_id}").text)


def cancel(client, order_id: int, token=None):
    """Tap "Cancel this order" on the order page."""
    token = cancel_token(client, order_id) if token is None else token
    return client.post(f"/orders/{order_id}/cancel", data={"token": token})


def newest_order(conn, account_id: int):
    return conn.execute(
        "SELECT * FROM orders WHERE account_id = ? ORDER BY id DESC LIMIT 1", (account_id,)
    ).fetchone()


def lines_of(conn, order_id: int) -> dict[int, tuple[int, int]]:
    """{product_id: (bottles, unit_price_paise)} for an order."""
    rows = conn.execute(
        "SELECT product_id, quantity, unit_price_paise FROM order_lines WHERE order_id = ?",
        (order_id,),
    ).fetchall()
    return {r["product_id"]: (r["quantity"], r["unit_price_paise"]) for r in rows}


def count_orders(conn) -> int:
    return conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]


def add_account(world, name: str, area: str) -> int:
    connection = db.connect(world.db_path)
    try:
        return db.add_account(connection, name, area, "Due on delivery")
    finally:
        connection.close()
