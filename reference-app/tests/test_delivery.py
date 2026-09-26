"""Unit tests for the delivery-day rule (spec B1 to B3) and the facts file.

Facts sheet: "Weekly cut-off: Sunday 8 pm for delivery that week." Each area has a
fixed delivery day, Monday to Thursday. Bengaluru is on India Standard Time
(UTC+5:30, no daylight saving).

Calendar used below (2026): Sat 26 Sep, Sun 27 Sep, Mon 28 Sep, Thu 1 Oct,
Sat 3 Oct, Mon 5 Oct, Tue 6 Oct, Thu 8 Oct.
"""

from datetime import UTC, date, datetime, time, timedelta
from zoneinfo import ZoneInfo

import pytest

from app.delivery import DeliverySchedule, delivery_day
from app.facts import load_facts
from tests.conftest import ist

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, SUNDAY = 0, 1, 2, 3, 6
AREAS = {"Indiranagar": MONDAY, "Koramangala": TUESDAY, "MG Road": WEDNESDAY, "Jayanagar": THURSDAY}
SCHEDULE = DeliverySchedule(ZoneInfo("Asia/Kolkata"), SUNDAY, time(20, 0), AREAS)


@pytest.mark.parametrize(
    ("area", "placed_at", "expected", "after"),
    [
        # Indiranagar delivers on Mondays.
        ("Indiranagar", ist(2026, 9, 26, 10, 0), date(2026, 9, 28), False),  # Saturday
        ("Indiranagar", ist(2026, 9, 27, 19, 59, 59), date(2026, 9, 28), False),  # a second early
        ("Indiranagar", ist(2026, 9, 27, 20, 0, 0), date(2026, 10, 5), True),  # exactly 8 pm (B2)
        ("Indiranagar", ist(2026, 9, 27, 23, 30), date(2026, 10, 5), True),  # Sunday night
        ("Indiranagar", ist(2026, 9, 28, 1, 0), date(2026, 10, 5), True),  # 1 am, after closing
        ("Indiranagar", ist(2026, 9, 28, 15, 0), date(2026, 10, 5), True),  # on delivery day
        ("Indiranagar", ist(2026, 9, 29, 10, 0), date(2026, 10, 5), False),  # Tuesday: next Monday
        ("Indiranagar", ist(2026, 10, 3, 10, 0), date(2026, 10, 5), False),  # Saturday again
        # Jayanagar delivers on Thursdays.
        ("Jayanagar", ist(2026, 9, 26, 10, 0), date(2026, 10, 1), False),
        ("Jayanagar", ist(2026, 9, 28, 10, 0), date(2026, 10, 8), True),  # missed Sunday's cut-off
        ("Jayanagar", ist(2026, 10, 1, 9, 0), date(2026, 10, 8), True),
        ("Jayanagar", ist(2026, 10, 2, 9, 0), date(2026, 10, 8), False),  # Friday: next Thursday
        # Koramangala (Tuesday) and MG Road (Wednesday).
        ("Koramangala", ist(2026, 9, 27, 21, 0), date(2026, 10, 6), True),
        ("MG Road", ist(2026, 9, 26, 10, 0), date(2026, 9, 30), False),
    ],
)
def test_delivery_day_by_area_around_the_sunday_cutoff(area, placed_at, expected, after):
    result = delivery_day(placed_at, SCHEDULE, area)
    assert result.date == expected
    assert result.after_cutoff is after


def test_the_cutoff_is_judged_in_india_time_not_server_time():
    # 14:29:59 UTC is 19:59:59 in Bengaluru (UTC+5:30): just in time.
    in_time = datetime(2026, 9, 27, 14, 29, 59, tzinfo=UTC)
    assert delivery_day(in_time, SCHEDULE, "Indiranagar").date == date(2026, 9, 28)
    # 14:30 UTC is 20:00 in Bengaluru: the cut-off.
    too_late = datetime(2026, 9, 27, 14, 30, tzinfo=UTC)
    assert delivery_day(too_late, SCHEDULE, "Indiranagar").date == date(2026, 10, 5)


def test_a_server_still_on_sunday_while_bengaluru_is_on_monday():
    # 19:00 UTC on Sunday is 00:30 on Monday in Bengaluru: today's delivery is already missed.
    placed = datetime(2026, 9, 27, 19, 0, tzinfo=UTC)
    result = delivery_day(placed, SCHEDULE, "Indiranagar")
    assert result.date == date(2026, 10, 5)
    assert result.after_cutoff


def test_reason_after_the_cutoff_says_which_delivery_was_missed_and_why():
    result = delivery_day(ist(2026, 9, 28, 1, 0), SCHEDULE, "Indiranagar")
    assert "Sunday 8 pm" in result.reason
    assert "had passed" in result.reason
    assert "Monday 28 September" in result.reason  # the delivery that was missed
    assert "Monday 5 October 2026" in result.reason  # the one it goes on


def test_reason_before_the_cutoff_says_it_is_in_time():
    result = delivery_day(ist(2026, 9, 26, 10, 0), SCHEDULE, "Indiranagar")
    assert "had passed" not in result.reason
    assert "Sunday 8 pm" in result.reason
    assert "Monday 28 September 2026" in result.reason


def test_an_area_without_a_fixed_day_is_confirmed_by_meera():
    """Facts sheet: "Other areas within city limits: Ask; Meera confirms the day"."""
    result = delivery_day(ist(2026, 9, 26, 10, 0), SCHEDULE, "Whitefield")
    assert result.date is None
    assert "Meera" in result.reason


def test_naive_times_are_refused():
    with pytest.raises(ValueError):
        delivery_day(datetime(2026, 9, 26, 10, 0), SCHEDULE, "Indiranagar")


def test_delivery_is_always_monday_to_thursday_on_the_area_day_and_after_the_order():
    start = ist(2026, 9, 21, 0, 0)
    for area, weekday in AREAS.items():
        for hour in range(0, 24 * 14):
            moment = start + timedelta(hours=hour)
            result = delivery_day(moment, SCHEDULE, area)
            assert result.date is not None  # every area here has a fixed day
            assert result.date.weekday() == weekday <= THURSDAY
            assert result.date > moment.date()


@pytest.mark.parametrize(
    ("clock", "label"),
    [(time(20, 0), "Sunday 8 pm"), (time(20, 30), "Sunday 8:30 pm"), (time(0, 0), "Sunday 12 am"),
     (time(12, 0), "Sunday 12 pm")],
)  # fmt: skip
def test_the_cutoff_is_written_the_way_the_facts_sheet_writes_it(clock, label):
    assert DeliverySchedule(ZoneInfo("Asia/Kolkata"), SUNDAY, clock, AREAS).cutoff_label == label


# ---- the facts file -------------------------------------------------------------


def test_the_real_facts_file_loads():
    facts = load_facts()
    assert AREAS.items() <= facts.schedule.area_days.items()
    assert facts.schedule.timezone == ZoneInfo("Asia/Kolkata")
    assert facts.schedule.cutoff_label == "Sunday 8 pm"
    assert facts.schedule.area_days["Indiranagar"] == MONDAY
    assert facts.schedule.area_days["Basavanagudi"] == THURSDAY
    assert len(facts.schedule.area_days) == 12
    assert facts.cancel_window == timedelta(minutes=30)
    assert facts.bottles_per_case == 6
    assert facts.delivery_charge_paise == 15000
    assert facts.free_delivery_from_cases == 2
    assert facts.max_bottles_per_line == 60
    assert facts.currency == "Rs"


FACTS_TEMPLATE = """
[ordering]
timezone = "Asia/Kolkata"
cutoff_weekday = "{cutoff_day}"
cutoff_time = "{cutoff_time}"
bottles_per_case = 6
cancel_window_minutes = 30

[delivery]
charge_rupees = 150
free_from_cases = 2
no_delivery_days = ["Friday", "Saturday", "Sunday"]

[delivery.days]
Monday = ["Indiranagar"]
{extra_day} = {extra_areas}

[money]
currency = "Rs"

[reorder_page]
max_bottles_per_line = 60
"""


@pytest.mark.parametrize(
    ("cutoff_day", "cutoff_time", "extra_day", "extra_areas"),
    [
        ("Sundy", "20:00", "Tuesday", '["Koramangala"]'),  # misspelled day
        ("Sunday", "25:00", "Tuesday", '["Koramangala"]'),  # impossible time
        ("Sunday", "8pm", "Tuesday", '["Koramangala"]'),  # not a 24-hour time
        ("Sunday", "20:00", "Friday", '["Koramangala"]'),  # no Friday deliveries
        ("Sunday", "20:00", "Tuesday", '["Indiranagar"]'),  # one area, two days
        ("Tuesday", "20:00", "Tuesday", '["Koramangala"]'),  # cut-off on a delivery day
    ],
)
def test_a_broken_facts_file_is_refused(tmp_path, cutoff_day, cutoff_time, extra_day, extra_areas):
    path = tmp_path / "facts.toml"
    path.write_text(
        FACTS_TEMPLATE.format(
            cutoff_day=cutoff_day,
            cutoff_time=cutoff_time,
            extra_day=extra_day,
            extra_areas=extra_areas,
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError):
        load_facts(path)
