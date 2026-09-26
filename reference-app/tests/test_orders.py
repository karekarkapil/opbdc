"""Edge cases around the rules, from the decisions in the spec (B4 to B15)."""

from tests.conftest import (
    add_account,
    cancel,
    cancel_token,
    confirm,
    count_orders,
    ist,
    lines_of,
    newest_order,
    order_ids_in,
    review_token,
    sign_in,
)


def _add_order(world, account, lines, when=None, charge=0):
    from app import db

    conn = db.connect(world.db_path)
    try:
        when = when or ist(2026, 9, 1, 1, 0)
        return db.add_order(conn, account, when, lines, delivery_charge_paise=charge)
    finally:
        conn.close()


# ---- the list ------------------------------------------------------------------


def test_cancelled_orders_are_not_among_the_last_three(client, world, conn):
    """B5."""
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    cancel(client, newest_order(conn, world.lantern)["id"])
    assert order_ids_in(client.get("/").text) == list(reversed(world.lantern_orders))[:3]


def test_a_bar_with_no_orders_sees_a_helpful_empty_page(client, world):
    sign_in(client, world.owl)
    page = client.get("/")
    assert page.status_code == 200
    assert order_ids_in(page.text) == []
    assert "No orders yet" in page.text


def test_the_list_marks_discontinued_products(client, world):
    """Found in review (brief 03)."""
    sign_in(client, world.lantern)
    assert "Guava and Pink Salt (no longer available)" in client.get("/").text


# ---- the review screen, prices and cases -----------------------------------------


def test_repeat_uses_todays_prices_and_says_so(client, world, conn):
    """B6: Tender Coconut was Rs 520 a bottle before 1 July 2026 and is Rs 560 now."""
    june = _add_order(world, world.lantern, [(world.coconut, 6, 52000)], ist(2026, 6, 15, 1, 0))
    sign_in(client, world.lantern)
    review = client.get(f"/repeat/{june}")
    assert "Rs 560" in review.text
    assert "today's prices" in review.text
    confirm(client, june, {world.coconut: 6})
    assert lines_of(conn, newest_order(conn, world.lantern)["id"]) == {world.coconut: (6, 56000)}


def test_a_zero_quantity_leaves_the_line_out(client, world, conn):
    """B7."""
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[2], {world.pineapple: 0, world.chilli: 6})
    assert lines_of(conn, newest_order(conn, world.lantern)["id"]) == {world.chilli: (6, 52000)}


def test_all_zero_quantities_are_refused(client, world, conn):
    sign_in(client, world.lantern)
    before = count_orders(conn)
    response = confirm(client, world.lantern_orders[2], {world.pineapple: 0, world.chilli: 0})
    assert response.status_code == 400
    assert "Add at least one case" in response.text
    assert count_orders(conn) == before


def test_orders_go_out_in_whole_cases(client, world, conn):
    """B8: the facts sheet sells by the case of six; flavors can be mixed."""
    sign_in(client, world.lantern)
    before = count_orders(conn)
    # The discontinued guava is left out, so repeating as it was leaves 9 bottles.
    response = confirm(client, world.lantern_orders[4], {world.pineapple: 6, world.coconut: 3})
    assert response.status_code == 400
    assert "whole cases of 6" in response.text
    assert "flavors can be mixed" in response.text
    assert "9 bottles" in response.text
    assert count_orders(conn) == before
    # A mixed case is fine.
    confirm(client, world.lantern_orders[4], {world.pineapple: 3, world.coconut: 3})
    assert count_orders(conn) == before + 1


def test_a_quantity_over_the_limit_is_refused(client, world, conn):
    sign_in(client, world.lantern)
    before = count_orders(conn)
    response = confirm(client, world.lantern_orders[2], {world.pineapple: 600, world.chilli: 6})
    assert response.status_code == 400
    assert "60" in response.text
    assert "bottles of each flavor" in response.text
    assert count_orders(conn) == before


def test_nonsense_quantities_are_refused(client, world, conn):
    sign_in(client, world.lantern)
    before = count_orders(conn)
    for bad in ["-1", "two", "2.5", ""]:
        token = review_token(client, world.lantern_orders[3])
        response = client.post(
            f"/repeat/{world.lantern_orders[3]}",
            data={f"qty-{world.kokum}": bad, "token": token},
        )
        assert response.status_code == 400, bad
    assert count_orders(conn) == before


def test_delivery_charge_under_two_cases_and_free_from_two(client, world, conn):
    """Facts sheet: free for two cases or more; otherwise Rs 150 per delivery."""
    sign_in(client, world.lantern)
    one_case = confirm(client, world.lantern_orders[2], {world.pineapple: 6, world.chilli: 0})
    assert newest_order(conn, world.lantern)["delivery_charge_paise"] == 15000
    assert "Rs 150" in one_case.text
    assert "Rs 3,390" in one_case.text  # 6 x Rs 540 + Rs 150
    two_cases = confirm(client, world.lantern_orders[2], {world.pineapple: 6, world.chilli: 6})
    assert newest_order(conn, world.lantern)["delivery_charge_paise"] == 0
    assert "Free" in two_cases.text


def test_the_review_screen_shows_the_total_and_can_update_it(client, world, conn):
    """Found in review (brief 03): the total was only seen after confirming."""
    sign_in(client, world.lantern)
    order = world.lantern_orders[2]  # 6 pineapple at Rs 540, 6 chilli at Rs 520
    assert "Rs 6,360" in client.get(f"/repeat/{order}").text
    before = count_orders(conn)
    updated = client.post(
        f"/repeat/{order}",
        data={
            f"qty-{world.pineapple}": "12",
            f"qty-{world.chilli}": "6",
            "token": review_token(client, order),
            "action": "update",
        },
    )
    assert updated.status_code == 200
    assert "Rs 9,600" in updated.text
    assert count_orders(conn) == before


def test_no_total_is_shown_for_quantities_that_cannot_be_placed(client, world):
    """Found in review 2: leaving out the discontinued guava makes 9 bottles, which cannot
    be confirmed, yet the review screen showed a total for them."""
    sign_in(client, world.lantern)
    placeable = client.get(f"/repeat/{world.lantern_orders[2]}")  # control: two whole cases
    assert "Total at these quantities" in placeable.text
    review = client.get(f"/repeat/{world.lantern_orders[4]}")
    assert "Before you confirm" in review.text
    assert "Total at these quantities" not in review.text


def test_the_pages_take_the_cutoff_and_free_delivery_from_the_facts_file(world, clock, tmp_path):
    """Found in review 2: the cut-off on the list and "free from two cases" on the review
    screen were typed into the templates, where the facts-sheet guard cannot see them.
    Change both in a copy of the facts file, and the pages must follow."""
    from fastapi.testclient import TestClient

    from app.facts import DEFAULT_FACTS
    from app.main import create_app

    text = DEFAULT_FACTS.read_text(encoding="utf-8")
    changed = (
        text.replace('cutoff_weekday = "Sunday"', 'cutoff_weekday = "Saturday"')
        .replace('cutoff_time = "20:00"', 'cutoff_time = "18:00"')
        .replace("free_from_cases = 2", "free_from_cases = 3")
    )
    for new_value in ['"Saturday"\n', '"18:00"', "free_from_cases = 3"]:
        assert new_value in changed  # the copy really differs
    copy = tmp_path / "facts.toml"
    copy.write_text(changed, encoding="utf-8")

    # The real facts file first, as a control, then the changed copy.
    for facts_path, cutoff, free_from in [
        (DEFAULT_FACTS, "Sunday 8 pm", "two"),
        (copy, "Saturday 6 pm", "three"),
    ]:
        application = create_app(world.db_path, facts_path=facts_path, demo_mode=True)
        application.state.clock = clock
        with TestClient(application) as browser:
            sign_in(browser, world.banyan)
            assert f"Order by {cutoff} for delivery that week" in browser.get("/").text
            one_case = browser.get(f"/repeat/{world.banyan_orders[1]}")  # delivery charged
            assert f"free from {free_from} cases" in one_case.text


def test_an_order_of_only_discontinued_products_cannot_be_repeated(client, world, conn):
    """B9."""
    guava_only = _add_order(world, world.lantern, [(world.guava, 6, 52000)])
    sign_in(client, world.lantern)
    review = client.get(f"/repeat/{guava_only}")
    assert "cannot be repeated" in review.text
    assert "Confirm order" not in review.text
    before = count_orders(conn)
    assert confirm(client, guava_only, {world.guava: 6}, token="x").status_code == 400
    assert count_orders(conn) == before


# ---- the delivery day ---------------------------------------------------------------


def test_cutoff_passing_during_review_moves_the_day_and_says_why(client, world, clock):
    """B4: reviewed at 7:58 pm on Sunday, confirmed at 8:01 pm."""
    clock.now = ist(2026, 9, 27, 19, 58)
    sign_in(client, world.lantern)
    token = review_token(client, world.lantern_orders[3])
    assert "Monday 28 September 2026" in client.get(f"/repeat/{world.lantern_orders[3]}").text
    clock.now = ist(2026, 9, 27, 20, 1)
    done = confirm(client, world.lantern_orders[3], {world.kokum: 12}, token=token)
    assert "Monday 5 October 2026" in done.text
    assert "had passed" in done.text


def test_the_delivery_day_is_stored_with_the_order(client, world, conn, clock):
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    new = newest_order(conn, world.lantern)
    assert new["delivery_date"] == "2026-09-28"
    # Viewing it later, after the cut-off, does not change it.
    clock.now = ist(2026, 9, 27, 21, 0)
    assert "Monday 28 September 2026" in client.get(f"/orders/{new['id']}").text


def test_each_bar_gets_its_areas_day(client, world, conn):
    """Koramangala delivers on Tuesdays."""
    sign_in(client, world.banyan)
    done = confirm(client, world.banyan_orders[1], {world.kokum: 6})
    assert "Tuesday 29 September 2026" in done.text


def test_a_bar_in_an_area_without_a_fixed_day_is_told_meera_will_confirm(client, world, conn):
    """Facts sheet: "Other areas within city limits: Ask; Meera confirms the day"."""
    sunbird = add_account(world, "Sunbird Bar", "Whitefield")
    past = _add_order(world, sunbird, [(world.cola, 6, 48000)])
    sign_in(client, sunbird)
    assert "Meera" in client.get(f"/repeat/{past}").text
    done = confirm(client, past, {world.cola: 6})
    assert done.status_code == 200
    assert newest_order(conn, sunbird)["delivery_date"] is None
    assert "Meera" in done.text


def test_the_confirmation_shows_the_time_it_was_placed(client, world):
    """Found by walking the pages (brief 02)."""
    sign_in(client, world.lantern)
    assert "at 10:00" in confirm(client, world.lantern_orders[3], {world.kokum: 12}).text


def test_an_old_order_is_not_described_in_the_future(client, world):
    """Found by walking the pages (brief 02)."""
    from datetime import date

    from app import db

    conn = db.connect(world.db_path)
    old = db.add_order(
        conn,
        world.lantern,
        ist(2026, 8, 30, 1, 0),
        [(world.kokum, 6, 52000)],
        date(2026, 8, 31),
        "Ordered before the Sunday 8 pm cut-off, so it arrives on ...",
    )
    conn.close()
    sign_in(client, world.lantern)
    page = client.get(f"/orders/{old}")
    assert "Monday 31 August 2026" in page.text
    assert "arrives on" not in page.text
    assert "Order confirmed" not in page.text
    assert "Past order" in page.text


# ---- cancelling --------------------------------------------------------------------


def test_cancel_window_boundary(client, world, conn, clock):
    """B10: open at 29:59, closed at exactly 30:00."""
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    first = newest_order(conn, world.lantern)["id"]
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    second = newest_order(conn, world.lantern)["id"]
    second_token = cancel_token(client, second)

    clock.advance(minutes=29, seconds=59)
    assert cancel(client, first).status_code == 200
    clock.advance(seconds=1)
    assert cancel(client, second, token=second_token).status_code == 409


def test_cancelling_twice_is_harmless(client, world, conn):
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    new = newest_order(conn, world.lantern)["id"]
    token = cancel_token(client, new)
    assert cancel(client, new, token=token).status_code == 200
    again = cancel(client, new, token=token)
    assert again.status_code == 200
    assert "Order cancelled" in again.text


def test_cancelling_needs_the_token_from_the_order_page(client, world, conn):
    """Found in review (brief 03)."""
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    new = newest_order(conn, world.lantern)["id"]
    assert cancel(client, new, token="").status_code == 400
    assert cancel(client, new, token="made-up").status_code == 400
    assert newest_order(conn, world.lantern)["status"] == "placed"
    assert cancel(client, new).status_code == 200  # control: the real button works


def test_the_cancel_deadline_names_the_day(client, world, clock):
    """Found in review (brief 03): "until 00:20" did not say which day."""
    clock.now = ist(2026, 9, 26, 23, 50)
    sign_in(client, world.lantern)
    done = confirm(client, world.lantern_orders[3], {world.kokum: 12})
    assert "You can cancel until 00:20 on Sun 27 Sep" in done.text


def test_two_taps_at_the_same_instant_still_make_one_order(client, world, conn, monkeypatch):
    """The database's unique token catches a race that the first lookup misses."""
    from app import db

    sign_in(client, world.lantern)
    token = review_token(client, world.lantern_orders[3])
    confirm(client, world.lantern_orders[3], {world.kokum: 12}, token=token)
    before = count_orders(conn)

    real_find = db.find_order_by_token
    calls = []

    def miss_once(*args):
        calls.append(args)
        return None if len(calls) == 1 else real_find(*args)

    monkeypatch.setattr(db, "find_order_by_token", miss_once)
    response = confirm(client, world.lantern_orders[3], {world.kokum: 12}, token=token)
    assert response.status_code == 200
    assert count_orders(conn) == before
    assert len(calls) == 2


def test_unknown_orders_are_not_found(client, world):
    sign_in(client, world.lantern)
    assert client.get(f"/repeat/{world.lantern_orders[0]}").status_code == 200  # control
    assert client.get("/repeat/99999").status_code == 404
    assert client.get("/orders/99999").status_code == 404


def test_odd_ids_are_not_found_rather_than_crashing(client, world):
    """Found in review (brief 03)."""
    sign_in(client, world.lantern)
    for path in ["/repeat/abc", "/repeat/99999999999999999999999999", "/orders/-1"]:
        response = client.get(path)
        assert response.status_code == 404, path
        assert "Not found" in response.text


# ---- sign-in and demo mode (B11) -------------------------------------------------


def test_without_demo_mode_the_app_asks_for_a_real_login_provider(world):
    from fastapi.testclient import TestClient

    from app.main import create_app

    with TestClient(create_app(world.db_path, demo_mode=False)) as plain:
        plain.cookies.set("demo_account", str(world.lantern))
        page = plain.get("/")
        assert page.status_code == 503
        assert "sign-in" in page.text.lower()
        assert plain.get("/demo").status_code == 404


def test_a_missing_database_suggests_the_seed_script_only_in_demo_mode(tmp_path):
    """Found in review 2: outside demo mode, the error pointed at the script that fills
    the database with fictional bars."""
    from fastapi.testclient import TestClient

    from app.main import create_app

    missing = tmp_path / "missing.db"
    with TestClient(create_app(missing, demo_mode=True)) as demo:
        page = demo.get("/healthz")
        assert page.status_code == 503
        assert "python -m app.seed" in page.text  # control: the demo still says how
    with TestClient(create_app(missing, demo_mode=False)) as live:
        page = live.get("/healthz")
        assert page.status_code == 503
        assert "database" in page.text
        assert "seed" not in page.text
    assert not missing.exists()


def test_demo_mode_without_a_chosen_bar_goes_to_the_demo_page(client):
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] == "/demo"


def test_demo_page_picks_a_bar_and_a_pretend_time(client, world):
    page = client.get("/demo")
    assert "Banyan Street Cafe" in page.text
    client.post("/demo", data={"account_id": str(world.banyan), "pretend_now": "2026-09-27T21:30"})
    home = client.get("/")
    assert order_ids_in(home.text) == list(reversed(world.banyan_orders))
    done = confirm(client, world.banyan_orders[1], {world.kokum: 6})
    assert "Tuesday 6 October 2026" in done.text


def test_every_page_says_it_is_in_demo_mode(client, world):
    sign_in(client, world.lantern)
    assert "Demo mode" in client.get("/").text


def test_odd_demo_account_values_do_not_crash(client, world):
    """Found in review (brief 03). Cookies carry only ASCII, so "²" is tried in the form."""
    for odd in ["99999999999999999999999", "-1", "abc"]:
        client.cookies.set("demo_account", odd)
        assert client.get("/", follow_redirects=False).status_code == 303, odd
    for odd in ["²", "99999999999999999999999", "-1", "abc"]:
        assert client.post("/demo", data={"account_id": odd}).status_code == 400, odd


def test_bad_pretend_times_are_refused(client, world):
    for bad in ["tomorrow", "2026-09-27T21:30+05:30"]:
        response = client.post("/demo", data={"account_id": str(world.lantern), "pretend_now": bad})
        assert response.status_code == 400, bad


def test_a_pretend_time_before_the_order_cannot_cancel_it(app, client, world):
    """Found in review: a pretend clock set in the past reopened old cancel windows."""
    from app import tokens

    sign_in(client, world.lantern)
    order = world.lantern_orders[4]  # placed 21 September
    # A genuine token, so only the time rule can refuse the cancel.
    token = tokens.issue(app.state.secret, "cancel", world.lantern, order)
    client.cookies.set("demo_now", "2026-09-20T12:00")
    assert "/cancel" not in client.get(f"/orders/{order}").text
    assert cancel(client, order, token=token).status_code == 409


def test_pretend_time_is_ignored_outside_demo_mode(world):
    from starlette.requests import Request

    from app.main import create_app, now

    app = create_app(world.db_path, demo_mode=False)
    real = ist(2026, 9, 26, 10, 0)
    app.state.clock = lambda: real
    request = Request(
        {"type": "http", "app": app, "headers": [(b"cookie", b"demo_now=2020-01-01T00:00")]}
    )
    assert now(request) == real


def test_health_check(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_the_seed_script_builds_a_working_demo(tmp_path):
    from datetime import UTC, datetime

    from fastapi.testclient import TestClient

    from app.main import create_app
    from app.seed import seed

    path = tmp_path / "demo.db"
    seed(path, datetime(2026, 9, 26, 12, 0, tzinfo=UTC))
    with TestClient(create_app(path, demo_mode=True)) as demo:
        sign_in(demo, 1)
        assert len(order_ids_in(demo.get("/").text)) == 3
        sign_in(demo, 2)
        assert len(order_ids_in(demo.get("/").text)) == 2


# ---- money --------------------------------------------------------------------------


def test_rupees_are_written_the_indian_way():
    from app.money import format_money

    assert format_money(54000, "Rs") == "Rs 540"
    assert format_money(636000, "Rs") == "Rs 6,360"
    assert format_money(14000000, "Rs") == "Rs 1,40,000"  # one lakh forty thousand
    assert format_money(12345, "Rs") == "Rs 123.45"
    assert format_money(0, "Rs") == "Rs 0"


# ---- found by walking the re-localized pages (brief 04) ------------------------------


def test_the_review_screen_warns_up_front_when_the_repeat_is_not_whole_cases(client, world):
    """Leaving out the discontinued guava makes 9 bottles: say so before Confirm is tapped."""
    sign_in(client, world.lantern)
    review = client.get(f"/repeat/{world.lantern_orders[4]}")
    assert review.status_code == 200
    assert "add 3 more, or remove 3" in review.text
    assert "Order confirmed" not in review.text


def test_a_whole_case_repeat_has_no_case_warning(client, world):
    sign_in(client, world.lantern)
    assert (
        "whole cases of 6 bottles, and" not in client.get(f"/repeat/{world.lantern_orders[2]}").text
    )
