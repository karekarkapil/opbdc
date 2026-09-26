"""SQLite storage: the schema and every query the app makes.

Money is integer paise (Rs 540 is 54000). Times are stored as UTC ISO 8601 strings.
Every query uses parameters (?), never string formatting.
"""

import sqlite3
from datetime import UTC, date, datetime
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS accounts (
    id            INTEGER PRIMARY KEY,
    name          TEXT NOT NULL,
    area          TEXT NOT NULL,  -- sets the delivery day (facts/facts.toml)
    payment_terms TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS products (
    id           INTEGER PRIMARY KEY,
    name         TEXT NOT NULL,
    pack         TEXT NOT NULL,
    price_paise  INTEGER NOT NULL CHECK (price_paise >= 0),  -- per bottle
    discontinued INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS orders (
    id              INTEGER PRIMARY KEY,
    account_id      INTEGER NOT NULL REFERENCES accounts(id),
    created_at      TEXT NOT NULL,
    status          TEXT NOT NULL DEFAULT 'placed' CHECK (status IN ('placed', 'cancelled')),
    delivery_date   TEXT,
    delivery_reason TEXT NOT NULL DEFAULT '',
    delivery_charge_paise INTEGER NOT NULL DEFAULT 0,
    request_token   TEXT,
    UNIQUE (account_id, request_token)
);
CREATE TABLE IF NOT EXISTS order_lines (
    order_id         INTEGER NOT NULL REFERENCES orders(id),
    product_id       INTEGER NOT NULL REFERENCES products(id),
    quantity         INTEGER NOT NULL CHECK (quantity > 0),  -- bottles
    unit_price_paise INTEGER NOT NULL CHECK (unit_price_paise >= 0),
    PRIMARY KEY (order_id, product_id)
);
"""


def connect(path: str | Path) -> sqlite3.Connection:
    # One connection per request, used by one step at a time. FastAPI may hand the
    # request between threads, so SQLite's same-thread check must be off.
    conn = sqlite3.connect(path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    return conn


def to_utc_text(moment: datetime) -> str:
    if moment.tzinfo is None:
        raise ValueError("times must be timezone-aware")
    return moment.astimezone(UTC).isoformat()


def from_utc_text(text: str) -> datetime:
    return datetime.fromisoformat(text)


# ---- writes used by the seed script and the tests ----------------------------


def add_account(conn, name: str, area: str, payment_terms: str) -> int:
    cur = conn.execute(
        "INSERT INTO accounts (name, area, payment_terms) VALUES (?, ?, ?)",
        (name, area, payment_terms),
    )
    conn.commit()
    return cur.lastrowid


def add_product(conn, name: str, pack: str, price_paise: int, discontinued=False) -> int:
    cur = conn.execute(
        "INSERT INTO products (name, pack, price_paise, discontinued) VALUES (?, ?, ?, ?)",
        (name, pack, price_paise, int(discontinued)),
    )
    conn.commit()
    return cur.lastrowid


def add_order(
    conn,
    account_id: int,
    created_at: datetime,
    lines: list[tuple[int, int, int]],
    delivery_date: date | None = None,
    delivery_reason: str = "",
    status: str = "placed",
    request_token: str | None = None,
    delivery_charge_paise: int = 0,
) -> int:
    """Insert an order and its lines in one transaction.

    `lines` is a list of (product_id, bottles, unit_price_paise).
    """
    with conn:
        cur = conn.execute(
            "INSERT INTO orders (account_id, created_at, status, delivery_date,"
            " delivery_reason, delivery_charge_paise, request_token)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                account_id,
                to_utc_text(created_at),
                status,
                delivery_date.isoformat() if delivery_date else None,
                delivery_reason,
                delivery_charge_paise,
                request_token,
            ),
        )
        order_id = cur.lastrowid
        conn.executemany(
            "INSERT INTO order_lines (order_id, product_id, quantity, unit_price_paise)"
            " VALUES (?, ?, ?, ?)",
            [(order_id, pid, qty, price) for pid, qty, price in lines],
        )
    return order_id


# ---- reads -------------------------------------------------------------------


def get_account(conn, account_id: int):
    return conn.execute("SELECT * FROM accounts WHERE id = ?", (account_id,)).fetchone()


def list_accounts(conn):
    return conn.execute("SELECT * FROM accounts ORDER BY id").fetchall()


def recent_orders(conn, account_id: int, limit: int):
    """The newest orders that were not cancelled, with their totals (delivery included)."""
    return conn.execute(
        "SELECT o.*, SUM(l.quantity * l.unit_price_paise) + o.delivery_charge_paise AS total_paise"
        " FROM orders o JOIN order_lines l ON l.order_id = o.id"
        " WHERE o.account_id = ? AND o.status = 'placed'"
        " GROUP BY o.id ORDER BY o.created_at DESC, o.id DESC LIMIT ?",
        (account_id, limit),
    ).fetchall()


def get_order(conn, order_id: int, account_id: int):
    """One order, only if it belongs to this account."""
    return conn.execute(
        "SELECT * FROM orders WHERE id = ? AND account_id = ?", (order_id, account_id)
    ).fetchone()


def find_order_by_token(conn, account_id: int, token: str):
    return conn.execute(
        "SELECT * FROM orders WHERE account_id = ? AND request_token = ?", (account_id, token)
    ).fetchone()


def order_lines(conn, order_id: int):
    """The lines of an order, joined with today's product details."""
    return conn.execute(
        "SELECT l.product_id, l.quantity, l.unit_price_paise, p.name, p.pack,"
        " p.price_paise AS current_price_paise, p.discontinued"
        " FROM order_lines l JOIN products p ON p.id = l.product_id"
        " WHERE l.order_id = ? ORDER BY p.name",
        (order_id,),
    ).fetchall()


def cancel_order(conn, order_id: int) -> None:
    with conn:
        conn.execute("UPDATE orders SET status = 'cancelled' WHERE id = ?", (order_id,))
