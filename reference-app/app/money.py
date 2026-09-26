"""Money is stored as integer paise and written the Indian way: Rs 1,40,000."""


def format_money(paise: int, currency: str) -> str:
    rupees, rest = divmod(paise, 100)
    digits = str(rupees)
    # Indian grouping: the last three digits, then groups of two (1,40,000).
    head, tail = digits[:-3], digits[-3:]
    groups: list[str] = []
    while len(head) > 2:
        head, groups = head[:-2], [head[-2:], *groups]
    grouped = ",".join([g for g in [head, *groups] if g] + [tail])
    return f"{currency} {grouped}" + (f".{rest:02d}" if rest else "")
