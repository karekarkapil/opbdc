"""The acceptance tests from specs/reorder-in-one-tap.md, one or more per test.

Each test name starts with the acceptance test's number (at1 to at8), so a
reviewer can put the spec and this file side by side.
"""

import re

from fastapi.routing import APIRoute

from tests.conftest import (
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

# ---- AT1: the last orders, newest first, with dates and totals ----------------


def test_at1_two_past_orders_appear_newest_first_with_dates_and_totals(client, world):
    sign_in(client, world.banyan)
    page = client.get("/")
    assert page.status_code == 200
    older, newer = world.banyan_orders
    assert order_ids_in(page.text) == [newer, older]
    assert "Thu 24 Sep 2026" in page.text and "Thu 10 Sep 2026" in page.text
    assert "Rs 3,270" in page.text  # 6 x Rs 520, plus Rs 150 delivery for one case
    assert "Rs 6,240" in page.text  # 6 x Rs 560 + 6 x Rs 480, two cases deliver free


def test_at1_each_order_has_a_one_tap_repeat_button(client, world):
    sign_in(client, world.banyan)
    page = client.get("/")
    for order_id in world.banyan_orders:
        assert f'href="/repeat/{order_id}"' in page.text


def test_at1_only_the_last_three_orders_are_shown(client, world):
    sign_in(client, world.lantern)
    page = client.get("/")
    assert order_ids_in(page.text) == list(reversed(world.lantern_orders))[:3]


# ---- AT2: repeat with a changed quantity, and see the delivery day ------------


def test_at2_repeat_with_one_changed_quantity_creates_the_order(client, world, conn):
    sign_in(client, world.lantern)
    order = world.lantern_orders[2]  # 6 pineapple, 6 chilli

    review = client.get(f"/repeat/{order}")
    assert review.status_code == 200
    assert re.search(rf'name="qty-{world.pineapple}"[^>]*value="6"', review.text)
    assert re.search(rf'name="qty-{world.chilli}"[^>]*value="6"', review.text)

    # "Send me the same as last time, maybe a bit more of the pineapple."
    done = confirm(client, order, {world.pineapple: 12, world.chilli: 6})
    assert done.status_code == 200
    new = newest_order(conn, world.lantern)
    assert new["id"] not in world.lantern_orders
    assert {pid: qty for pid, (qty, _) in lines_of(conn, new["id"]).items()} == {
        world.pineapple: 12,
        world.chilli: 6,
    }
    assert "Order confirmed" in done.text
    assert "Monday 28 September 2026" in done.text  # Indiranagar delivers on Mondays


def test_at2_the_new_order_tops_the_list(client, world, conn):
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[2], {world.pineapple: 12, world.chilli: 6})
    new = newest_order(conn, world.lantern)
    assert order_ids_in(client.get("/").text)[0] == new["id"]


# ---- AT3: after the weekly cut-off, next week's day, and why ------------------


def test_at3_after_the_cutoff_the_delivery_is_next_week_and_the_page_says_why(client, world, clock):
    clock.now = ist(2026, 9, 27, 21, 15)  # Sunday, after the 8 pm cut-off
    sign_in(client, world.lantern)
    done = confirm(client, world.lantern_orders[2], {world.pineapple: 6, world.chilli: 6})
    assert "Monday 5 October 2026" in done.text
    assert "cut-off" in done.text and "Sunday 8 pm" in done.text and "had passed" in done.text


def test_at3_the_review_screen_warns_before_confirming(client, world, clock):
    clock.now = ist(2026, 9, 28, 1, 0)  # 1 am Monday, after closing: too late for today
    sign_in(client, world.lantern)
    review = client.get(f"/repeat/{world.lantern_orders[2]}")
    assert "Monday 5 October 2026" in review.text
    assert "Sunday 8 pm" in review.text and "had passed" in review.text


def test_at3_before_the_cutoff_there_is_no_warning(client, world):
    sign_in(client, world.lantern)
    assert "had passed" not in client.get(f"/repeat/{world.lantern_orders[2]}").text
    done = confirm(client, world.lantern_orders[2], {world.pineapple: 6, world.chilli: 6})
    assert "Monday 28 September 2026" in done.text
    assert "had passed" not in done.text


# ---- AT4: discontinued products are shown as unavailable and left out ---------


def test_at4_discontinued_product_is_shown_unavailable_with_a_note(client, world):
    sign_in(client, world.lantern)
    review = client.get(f"/repeat/{world.lantern_orders[4]}")
    assert "Guava and Pink Salt" in review.text
    assert "No longer available" in review.text
    assert "left out" in review.text
    assert f'name="qty-{world.guava}"' not in review.text


def test_at4_discontinued_product_is_left_out_of_the_repeat(client, world, conn):
    sign_in(client, world.lantern)
    # Even if the form is tampered with to include it.
    confirm(
        client,
        world.lantern_orders[4],
        {world.pineapple: 6, world.coconut: 6, world.guava: 3},
    )
    new = newest_order(conn, world.lantern)
    assert set(lines_of(conn, new["id"])) == {world.pineapple, world.coconut}


# ---- AT5: cancel within thirty minutes ----------------------------------------


def test_at5_cancel_within_thirty_minutes(client, world, conn, clock):
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    new = newest_order(conn, world.lantern)

    clock.advance(minutes=10)
    page = client.get(f"/orders/{new['id']}")
    assert f'action="/orders/{new["id"]}/cancel"' in page.text
    assert "You can cancel until 10:30" in page.text

    cancelled = cancel(client, new["id"])
    assert cancelled.status_code == 200
    assert "Order cancelled" in cancelled.text
    assert newest_order(conn, world.lantern)["status"] == "cancelled"
    assert new["id"] not in order_ids_in(client.get("/").text)


# ---- AT6: after thirty minutes, no cancelling ---------------------------------


def test_at6_no_cancel_after_thirty_minutes(client, world, conn, clock):
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    new = newest_order(conn, world.lantern)
    token = cancel_token(client, new["id"])  # taken while the window was open

    clock.advance(minutes=31)
    page = client.get(f"/orders/{new['id']}")
    assert "/cancel" not in page.text

    refused = cancel(client, new["id"], token=token)
    assert refused.status_code == 409
    assert "Meera" in refused.text  # facts sheet: after 30 minutes, Meera decides
    assert newest_order(conn, world.lantern)["status"] == "placed"


def test_at6_order_page_says_how_to_change_after_window(client, world, conn, clock):
    """Found in a live walk of the running app: after the window closed, the order page
    dropped the cancel button but gave no way forward. It must say who decides now."""
    sign_in(client, world.lantern)
    confirm(client, world.lantern_orders[3], {world.kokum: 12})
    new = newest_order(conn, world.lantern)

    clock.advance(minutes=31)
    page = client.get(f"/orders/{new['id']}")
    assert page.status_code == 200
    assert "window to cancel has closed" in page.text
    assert "Meera will decide" in page.text


# ---- AT7: a double tap creates one order --------------------------------------


def test_at7_double_tap_creates_one_order(client, world, conn):
    sign_in(client, world.lantern)
    before = count_orders(conn)
    token = review_token(client, world.lantern_orders[3])
    first = confirm(client, world.lantern_orders[3], {world.kokum: 12}, token=token)
    second = confirm(client, world.lantern_orders[3], {world.kokum: 12}, token=token)
    assert count_orders(conn) == before + 1
    assert first.url == second.url


def test_at7_resending_with_changed_quantities_says_the_changes_were_not_applied(
    client, world, conn
):
    """Found in review (brief 03): the second post was silently ignored."""
    sign_in(client, world.lantern)
    before = count_orders(conn)
    token = review_token(client, world.lantern_orders[3])
    confirm(client, world.lantern_orders[3], {world.kokum: 12}, token=token)
    again = confirm(client, world.lantern_orders[3], {world.kokum: 18}, token=token)
    assert count_orders(conn) == before + 1
    assert lines_of(conn, newest_order(conn, world.lantern)["id"])[world.kokum][0] == 12
    assert "changes were not applied" in again.text


def test_at7_confirming_requires_the_confirmation_step(client, world, conn):
    sign_in(client, world.lantern)
    before = count_orders(conn)
    response = client.post(f"/repeat/{world.lantern_orders[3]}", data={f"qty-{world.kokum}": "12"})
    assert response.status_code == 400
    assert count_orders(conn) == before


def test_at7_a_made_up_token_is_refused(client, world, conn):
    """Found in review (brief 03): any non-empty token used to be accepted."""
    sign_in(client, world.lantern)
    before = count_orders(conn)
    response = confirm(client, world.lantern_orders[3], {world.kokum: 12}, token="made-up")
    assert response.status_code == 400
    assert count_orders(conn) == before


def test_at7_a_token_from_another_orders_review_is_refused(client, world, conn):
    sign_in(client, world.lantern)
    before = count_orders(conn)
    other = review_token(client, world.lantern_orders[2])
    response = confirm(client, world.lantern_orders[3], {world.kokum: 12}, token=other)
    assert response.status_code == 400
    assert count_orders(conn) == before


# ---- AT8: the no list and the data rule ---------------------------------------


def test_at8_only_the_expected_routes_exist(app):
    """Adding a route is a decision for the spec, not a side effect."""
    routes = {
        (method, route.path)
        for route in app.routes
        if isinstance(route, APIRoute)
        for method in route.methods or ()
    }
    assert routes == {
        ("GET", "/"),
        ("GET", "/repeat/{order_id}"),
        ("POST", "/repeat/{order_id}"),
        ("GET", "/orders/{order_id}"),
        ("POST", "/orders/{order_id}/cancel"),
        ("GET", "/demo"),
        ("POST", "/demo"),
        ("GET", "/healthz"),
    }


def test_at8_the_form_cannot_set_prices_accounts_or_add_products(client, world, conn):
    sign_in(client, world.lantern)
    confirm(
        client,
        world.lantern_orders[2],  # pineapple and chilli only
        {world.pineapple: 6, world.chilli: 6, world.cola: 6},
        extra={
            f"price-{world.pineapple}": "1",
            "unit_price_paise": "1",
            "delivery_charge_paise": "1",
            "account_id": str(world.banyan),
            "discount": "50",
        },
    )
    new = newest_order(conn, world.lantern)
    assert new["account_id"] == world.lantern
    assert lines_of(conn, new["id"]) == {world.pineapple: (6, 54000), world.chilli: (6, 52000)}
    assert new["delivery_charge_paise"] == 0  # two cases: free, as the facts sheet says


def test_at8_prices_payment_terms_and_accounts_are_never_changed(client, world, conn, clock):
    def snapshot():
        products = conn.execute("SELECT * FROM products ORDER BY id").fetchall()
        accounts = conn.execute("SELECT * FROM accounts ORDER BY id").fetchall()
        history = conn.execute(
            "SELECT * FROM order_lines WHERE order_id <= ? ORDER BY order_id, product_id",
            (max(world.lantern_orders + world.banyan_orders),),
        ).fetchall()
        return [[tuple(r) for r in rows] for rows in (products, accounts, history)]

    before = snapshot()
    sign_in(client, world.lantern)
    orders_before = count_orders(conn)
    assert client.get("/").status_code == 200
    assert client.get(f"/repeat/{world.lantern_orders[4]}").status_code == 200
    placed = confirm(client, world.lantern_orders[4], {world.pineapple: 6, world.coconut: 6})
    assert placed.is_success
    # Positive control: the flow really ran, so "unchanged" means something.
    assert count_orders(conn) == orders_before + 1
    clock.advance(minutes=5)
    cancelled = cancel(client, newest_order(conn, world.lantern)["id"])
    assert cancelled.status_code == 200
    assert snapshot() == before


def test_at8_a_bar_cannot_repeat_or_see_another_bars_order(client, world, conn):
    sign_in(client, world.lantern)
    # Positive control: the same requests work for the bar's own order.
    assert client.get(f"/repeat/{world.lantern_orders[0]}").status_code == 200
    assert client.get(f"/orders/{world.lantern_orders[0]}").status_code == 200
    theirs = world.banyan_orders[0]
    before = count_orders(conn)
    assert client.get(f"/repeat/{theirs}").status_code == 404
    assert confirm(client, theirs, {world.coconut: 6, world.cola: 6}).status_code == 404
    assert client.get(f"/orders/{theirs}").status_code == 404
    assert cancel(client, theirs, token="x").status_code == 404
    assert count_orders(conn) == before
