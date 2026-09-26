"""Loads facts/facts.toml, the app's copy of the company facts sheet.

A broken facts file stops the app at start-up with a clear error, rather than
telling a bar the wrong delivery day.
"""

import tomllib
from dataclasses import dataclass
from datetime import time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from app.delivery import WEEKDAYS, DeliverySchedule

DEFAULT_FACTS = Path(__file__).resolve().parent.parent / "facts" / "facts.toml"


@dataclass(frozen=True)
class Facts:
    schedule: DeliverySchedule
    cancel_window: timedelta
    bottles_per_case: int
    delivery_charge_paise: int
    free_delivery_from_cases: int
    max_bottles_per_line: int
    currency: str

    def delivery_charge(self, bottles: int) -> int:
        """Facts sheet: free for two cases or more; otherwise Rs 150 per delivery."""
        cases = bottles // self.bottles_per_case
        return 0 if cases >= self.free_delivery_from_cases else self.delivery_charge_paise


def _weekday(name: str) -> int:
    if name not in WEEKDAYS:
        raise ValueError(f"not a weekday: {name!r} (use one of {', '.join(WEEKDAYS)})")
    return WEEKDAYS.index(name)


def _clock_time(text: str) -> time:
    try:
        return time.fromisoformat(text)
    except ValueError:
        raise ValueError(f"not a 24-hour time like 20:00: {text!r}") from None


def _area_days(days: dict, no_delivery_days: list[str]) -> dict[str, int]:
    area_days = {}
    for day_name, areas in days.items():
        if day_name in no_delivery_days:
            raise ValueError(f"the facts sheet says there are no deliveries on {day_name}")
        for area in areas:
            if area in area_days:
                raise ValueError(f"{area!r} is listed for two delivery days")
            area_days[area] = _weekday(day_name)
    return area_days


def load_facts(path: str | Path = DEFAULT_FACTS) -> Facts:
    with open(path, "rb") as f:
        raw = tomllib.load(f)
    ordering, delivery = raw["ordering"], raw["delivery"]
    try:
        zone = ZoneInfo(ordering["timezone"])
    except ZoneInfoNotFoundError:
        raise ValueError(f"unknown time zone: {ordering['timezone']!r}") from None
    schedule = DeliverySchedule(
        timezone=zone,
        cutoff_weekday=_weekday(ordering["cutoff_weekday"]),
        cutoff_time=_clock_time(ordering["cutoff_time"]),
        area_days=_area_days(delivery["days"], delivery["no_delivery_days"]),
    )
    return Facts(
        schedule=schedule,
        cancel_window=timedelta(minutes=int(ordering["cancel_window_minutes"])),
        bottles_per_case=int(ordering["bottles_per_case"]),
        delivery_charge_paise=int(delivery["charge_rupees"]) * 100,
        free_delivery_from_cases=int(delivery["free_from_cases"]),
        max_bottles_per_line=int(raw["reorder_page"]["max_bottles_per_line"]),
        currency=str(raw["money"]["currency"]),
    )
