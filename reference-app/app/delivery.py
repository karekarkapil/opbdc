"""The delivery-day rule (spec B1 to B3).

Facts sheet: "Weekly cut-off: Sunday 8 pm for delivery that week. Orders after
the cut-off are delivered the following week." Each area has a fixed delivery
day, Monday to Thursday.

Pure: it takes the moment an order is placed, the schedule from the facts file
and the bar's area, and returns the delivery date with a sentence explaining it.
It never reads the clock, so tests can ask it about any moment.
"""

from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


@dataclass(frozen=True)
class DeliverySchedule:
    timezone: ZoneInfo
    cutoff_weekday: int  # Monday is 0, Sunday is 6
    cutoff_time: time
    area_days: dict[str, int] = field(hash=False)  # area name -> weekday

    def __post_init__(self):
        if self.cutoff_weekday in self.area_days.values():
            # "Cut-off Tuesday 8 pm, delivery Tuesday" could mean today or next week.
            raise ValueError("the cut-off cannot fall on a delivery day")

    @property
    def cutoff_label(self) -> str:
        """Written the way the facts sheet writes it: Sunday 8 pm."""
        hour = self.cutoff_time.hour % 12 or 12
        minutes = f":{self.cutoff_time.minute:02d}" if self.cutoff_time.minute else ""
        half = "am" if self.cutoff_time.hour < 12 else "pm"
        return f"{WEEKDAYS[self.cutoff_weekday]} {hour}{minutes} {half}"


@dataclass(frozen=True)
class DeliveryDay:
    date: date | None  # None: the area has no fixed day, and Meera confirms it
    after_cutoff: bool
    reason: str


def long_date(day: date) -> str:
    """Monday 28 September 2026."""
    return f"{day:%A} {day.day} {day:%B %Y}"


def delivery_day(placed_at: datetime, schedule: DeliverySchedule, area: str) -> DeliveryDay:
    if placed_at.tzinfo is None:
        raise ValueError("placed_at must be timezone-aware")
    if area not in schedule.area_days:
        reason = "Your area has no fixed delivery day. Meera will message you to confirm the day."
        return DeliveryDay(None, False, reason)
    weekday = schedule.area_days[area]

    # Judge the cut-off in Bengaluru time, not the server's (B3).
    local = placed_at.astimezone(schedule.timezone)
    week_start = local.date() - timedelta(days=local.weekday())
    cutoff_date = week_start + timedelta(days=schedule.cutoff_weekday)
    cutoff = datetime.combine(cutoff_date, schedule.cutoff_time, tzinfo=schedule.timezone)
    if local >= cutoff:  # exactly at the cut-off counts as after it (B2)
        cutoff_date += timedelta(weeks=1)

    # The first delivery day for this area after the cut-off this order makes.
    delivery = cutoff_date + timedelta(days=(weekday - cutoff_date.weekday()) % 7)

    # The soonest day the area is ever served, today included. If the order goes
    # later than that, it missed a cut-off, and the page must say why (AT3).
    soonest = local.date() + timedelta(days=(weekday - local.weekday()) % 7)
    after_cutoff = delivery > soonest
    if after_cutoff:
        reason = (
            f"The weekly cut-off is {schedule.cutoff_label}. The cut-off for the delivery on "
            f"{soonest:%A} {soonest.day} {soonest:%B} had passed, so this order goes on the "
            f"following week's delivery, {long_date(delivery)}."
        )
    else:
        reason = (
            f"Ordered before the {schedule.cutoff_label} cut-off, "
            f"so it arrives on {long_date(delivery)}."
        )
    return DeliveryDay(delivery, after_cutoff, reason)
