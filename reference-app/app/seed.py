"""Create a demo database for Copper Pot Mixers, Bengaluru.

    python -m app.seed            # creates data/copper_pot.db (or $COPPER_POT_DB)
    python -m app.seed --reset    # starts again from scratch

Products and prices come from the company facts sheet (context-kit/examples/
beverage-company/facts-sheet.md); tests/test_facts_sheet.py checks they match.
Past orders are dated relative to today, so the demo always looks current.
Every bar here is fictional.
"""

import argparse
import os
from datetime import UTC, datetime, timedelta
from pathlib import Path

from app import db
from app.delivery import delivery_day
from app.facts import load_facts

BOTTLE = "750 ml bottle"
# (name, price per bottle in rupees, discontinued)
PRODUCTS = [
    ("Roasted Pineapple and Ginger", 540, False),
    ("Kokum and Black Salt", 520, False),
    ("Smoked Chilli and Lime", 520, False),
    ("Tender Coconut and Lemongrass", 560, False),
    ("Jaggery Cola Syrup", 480, False),
    # Listed on the facts sheet as "No longer sold", with no price (the price here is
    # only for old orders). It is here so the demo can show AT4 (a discontinued
    # product is left out, with a note).
    ("Guava and Pink Salt", 520, True),
]
TERMS = "Due on delivery"  # the facts sheet: no credit terms


def seed(path: Path, now: datetime) -> None:
    facts = load_facts()
    conn = db.connect(path)

    lantern = db.add_account(conn, "The Tin Lantern", "Indiranagar", TERMS)  # Mondays
    banyan = db.add_account(conn, "Banyan Street Cafe", "Koramangala", TERMS)  # Tuesdays
    db.add_account(conn, "The Night Owl", "Jayanagar", TERMS)  # Thursdays; no orders yet
    sunbird = db.add_account(conn, "Sunbird Bar", "Whitefield", TERMS)  # no fixed day

    ids = [
        db.add_product(conn, name, BOTTLE, rupees * 100, gone) for name, rupees, gone in PRODUCTS
    ]
    pineapple, kokum, chilli, coconut, cola, guava = ids
    price = {pid: rupees * 100 for pid, (_, rupees, _) in zip(ids, PRODUCTS, strict=True)}

    def past(account: int, area: str, days_ago: int, hour: int, *lines):
        """An order placed `days_ago` days ago at about `hour` o'clock, Bengaluru time."""
        local = now.astimezone(facts.schedule.timezone) - timedelta(days=days_ago)
        placed = local.replace(hour=hour, minute=40, second=0, microsecond=0)
        day = delivery_day(placed, facts.schedule, area)
        bottles = sum(qty for _, qty in lines)
        db.add_order(
            conn, account, placed, [(pid, qty, price[pid]) for pid, qty in lines],
            day.date, day.reason, delivery_charge_paise=facts.delivery_charge(bottles),
        )  # fmt: skip

    # The Tin Lantern: a weekly regular, ordering at 1 am after closing. The newest
    # order includes a flavor that has since been discontinued (AT4).
    past(lantern, "Indiranagar", 34, 1, (pineapple, 6), (kokum, 6))
    past(lantern, "Indiranagar", 27, 1, (pineapple, 6), (kokum, 6))
    past(lantern, "Indiranagar", 20, 1, (pineapple, 6), (chilli, 6))
    past(lantern, "Indiranagar", 13, 1, (kokum, 12))
    past(lantern, "Indiranagar", 6, 1, (pineapple, 6), (coconut, 3), (guava, 3))

    # Banyan Street Cafe: two orders (AT1), one of them a single case (delivery charged).
    past(banyan, "Koramangala", 16, 16, (coconut, 6), (cola, 6))
    past(banyan, "Koramangala", 2, 16, (kokum, 6))

    # Sunbird Bar is outside the scheduled areas: Meera confirms its delivery day.
    past(sunbird, "Whitefield", 9, 23, (cola, 6), (chilli, 6))
    conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--reset", action="store_true", help="delete and recreate the database")
    args = parser.parse_args()
    path = Path(os.environ.get("COPPER_POT_DB", "data/copper_pot.db"))
    if path.exists():
        if not args.reset:
            raise SystemExit(f"{path} already exists. Use --reset to start again.")
        path.unlink()
    path.parent.mkdir(parents=True, exist_ok=True)
    seed(path, datetime.now(UTC))
    print(f"Created {path} with demo data for Copper Pot Mixers.")


if __name__ == "__main__":
    main()
