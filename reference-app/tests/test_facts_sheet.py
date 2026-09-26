"""The app's facts must match the company facts sheet (brief 04).

The facts sheet (context-kit/examples/beverage-company/facts-sheet.md in the
companion repository) is the source of truth for everything the page tells a
customer. facts/facts.toml and the seed prices are the app's copies. This test
reads the sheet and fails if they drift apart. If you use this app as a template
outside the companion repository, point FACTS_SHEET at your own sheet, or the
test is skipped.
"""

import os
import re
from pathlib import Path

import pytest

from app.facts import load_facts
from app.seed import BOTTLE, PRODUCTS, TERMS

DEFAULT_SHEET = (
    Path(__file__).resolve().parents[2]
    / "context-kit"
    / "examples"
    / "beverage-company"
    / "facts-sheet.md"
)
SHEET = Path(os.environ.get("FACTS_SHEET", DEFAULT_SHEET))
NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}


def mismatches(sheet: str, facts, products, terms: str, bottle: str) -> list[str]:
    """Every way the app's facts differ from the sheet's text."""
    found = []

    def expect(label, sheet_value, app_value):
        if sheet_value != app_value:
            found.append(f"{label}: sheet says {sheet_value!r}, app has {app_value!r}")

    def search(pattern):
        match = re.search(pattern, sheet)
        if match is None:
            found.append(f"not found in the sheet: {pattern}")
        return match

    if m := search(r"Weekly cut-off: (\w+ \d+(?::\d\d)? [ap]m)"):
        expect("cut-off", m.group(1), facts.schedule.cutoff_label)
    if m := search(r"cancelled within (\d+) minutes"):
        expect("cancel window", int(m.group(1)), facts.cancel_window.total_seconds() // 60)
    if m := search(r"Sold by the case of (\w+) bottles"):
        expect("bottles per case", NUMBERS.get(m.group(1)), facts.bottles_per_case)
    if m := search(r"free for (\w+) cases or more; otherwise Rs (\d+) per delivery"):
        expect("free delivery from", NUMBERS.get(m.group(1)), facts.free_delivery_from_cases)
        expect("delivery charge", int(m.group(2)) * 100, facts.delivery_charge_paise)
    if m := search(r"All mixers come in a (\d+ ml) glass bottle"):
        expect("bottle", m.group(1), bottle.removesuffix(" bottle"))
    if search(r"We do not offer credit terms") and search(r"payment is due on delivery"):
        expect("payment terms", "Due on delivery", terms)

    areas = {}
    for line in sheet.splitlines():
        row = re.fullmatch(r"\| ([^|]+) \| (Monday|Tuesday|Wednesday|Thursday) \|", line.strip())
        if row:
            for area in row.group(1).split(", "):
                areas[area] = row.group(2)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
    app_areas = {area: days[day] for area, day in facts.schedule.area_days.items()}
    expect("delivery days by area", areas, app_areas)

    prices = {}
    products_section = sheet.split("## Products", 1)[-1].split("\n## ", 1)[0]
    for line in products_section.splitlines():
        row = re.fullmatch(r"\| ([^|]+) \| [^|]* \| Rs (\d+) \|.*", line.strip())
        if row:
            prices[row.group(1)] = int(row.group(2))
    on_sale = {name: rupees for name, rupees, gone in products if not gone}
    expect("products and prices per bottle", prices, on_sale)
    return found


@pytest.mark.skipif(not SHEET.exists(), reason=f"facts sheet not found at {SHEET}")
def test_the_app_matches_the_company_facts_sheet():
    sheet = SHEET.read_text(encoding="utf-8")
    assert mismatches(sheet, load_facts(), PRODUCTS, TERMS, BOTTLE) == []


@pytest.mark.skipif(not SHEET.exists(), reason=f"facts sheet not found at {SHEET}")
def test_the_check_catches_a_drifted_sheet():
    """Positive control: a sheet with a new cut-off and a new price must be caught."""
    sheet = SHEET.read_text(encoding="utf-8")
    drifted = sheet.replace("Sunday 8 pm", "Saturday 6 pm").replace("Rs 540", "Rs 560")
    problems = mismatches(drifted, load_facts(), PRODUCTS, TERMS, BOTTLE)
    assert any("cut-off" in p for p in problems)
    assert any("prices" in p for p in problems)
