"""Web routes for the reorder page. Thin: each route reads the request, calls a
rule in app/orders.py, and renders a template.

Run it:  DEMO_MODE=1 uvicorn app.main:app --reload
"""

import os
import re
import secrets
import sqlite3
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi import Path as UrlPart
from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from app import db, orders, tokens
from app.delivery import delivery_day, long_date
from app.facts import DEFAULT_FACTS, load_facts
from app.money import format_money

HERE = Path(__file__).resolve().parent
ID = re.compile(r"[0-9]{1,9}")  # plain ASCII digits only; "²" and 30-digit ids are refused


# ---- sign-in, clock and database ------------------------------------------------
#
# How a request gets its account: FastAPI sees `account: Account` in a route's
# arguments, calls current_account() first (which itself gets a database
# connection from get_conn()), and passes the result in. If current_account()
# raises, the route never runs.


class SignInNotConnected(Exception):
    pass


class ChooseDemoBar(Exception):
    pass


def get_conn(request: Request):
    path = request.app.state.db_path
    if not path.exists():
        raise HTTPException(503, "The database has not been created. Run: python -m app.seed")
    conn = db.connect(path)
    try:
        yield conn
    finally:
        conn.close()


Conn = Annotated[sqlite3.Connection, Depends(get_conn)]


def current_account(request: Request, conn: Conn):
    """The signed-in bar. THE ONE SEAM FOR A LOGIN PROVIDER (spec B11).

    In production, replace the body with a lookup of the account id from your
    managed login provider's session. Never build passwords here. Keep the
    provider's session cookie SameSite=Lax or Strict. In demo mode, a cookie
    set on /demo stands in for the session.
    """
    if not request.app.state.demo_mode:
        raise SignInNotConnected()
    raw = request.cookies.get("demo_account", "")
    account = db.get_account(conn, int(raw)) if ID.fullmatch(raw) else None
    if account is None:
        raise ChooseDemoBar()
    return account


Account = Annotated[sqlite3.Row, Depends(current_account)]
OrderId = Annotated[int, UrlPart(ge=1, le=999_999_999)]


def now(request: Request) -> datetime:
    """The current time. In demo mode, a pretend time set on /demo wins."""
    state = request.app.state
    pretend = _pretend_time(request.cookies.get("demo_now", ""), state.facts)
    if state.demo_mode and pretend is not None:
        return pretend
    return state.clock()


def _pretend_time(text: str, facts) -> datetime | None:
    """A local date and time like 2026-09-29T23:30, or None if it is not one."""
    try:
        naive = datetime.fromisoformat(text)
    except ValueError:
        return None
    if naive.tzinfo is not None:
        return None
    return naive.replace(tzinfo=facts.schedule.timezone)


def _short_date(moment: datetime) -> str:
    """Tue 22 Sep 2026."""
    return f"{moment:%a} {moment.day} {moment:%b %Y}"


def render(request: Request, template: str, status_code=200, **context):
    state = request.app.state
    tz = state.facts.schedule.timezone
    currency = state.facts.currency
    context.update(
        demo_mode=state.demo_mode,
        pretend_now=request.cookies.get("demo_now", "") if state.demo_mode else "",
        money=lambda paise: format_money(paise, currency),
        long_date=long_date,
        short_date=lambda text: _short_date(db.from_utc_text(text).astimezone(tz)),
        clock_time=lambda moment: f"{moment.astimezone(tz):%H:%M}",
        day_label=lambda moment: (
            f"{moment.astimezone(tz):%a} {moment.astimezone(tz).day} {moment.astimezone(tz):%b}"
        ),
        placed_time=lambda text: f"{db.from_utc_text(text).astimezone(tz):%H:%M}",
    )
    return state.templates.TemplateResponse(request, template, context, status_code=status_code)


# ---- the pages ---------------------------------------------------------------------


def home(request: Request, account: Account, conn: Conn):
    """AT1: the last three orders, newest first, with dates and totals."""
    recent = db.recent_orders(conn, account["id"], limit=3)
    lines = {o["id"]: db.order_lines(conn, o["id"]) for o in recent}
    return render(request, "home.html", account=account, orders=recent, lines=lines)


def review(order_id: OrderId, request: Request, account: Account, conn: Conn):
    """The confirmation step: quantities to adjust, and the delivery day if confirmed now."""
    plan = orders.repeat_plan(conn, account["id"], order_id)
    if plan is None:
        raise HTTPException(404)
    quantities = {line.product_id: line.quantity for line in plan.lines}
    # Say up front if the old quantities cannot be confirmed as they are (for example,
    # leaving out a discontinued flavour breaks a whole case), not after Confirm.
    notice = ""
    if plan.lines:
        prefilled = {f"qty-{pid}": str(qty) for pid, qty in quantities.items()}
        try:
            orders.parse_quantities(prefilled, plan, request.app.state.facts)
        except orders.OrderError as problem:
            notice = str(problem)
    return _review_page(request, account, plan, quantities, notice=notice)


async def confirm(order_id: OrderId, request: Request, account: Account, conn: Conn):
    """AT2 and AT7: create the order from the review screen, once.

    The same form also has an "Update total" button, which shows the new total
    without placing anything.
    """
    plan = orders.repeat_plan(conn, account["id"], order_id)
    if plan is None:
        raise HTTPException(404)
    form = await request.form()
    state = request.app.state
    token = str(form.get("token", ""))
    if not tokens.is_valid(state.secret, token, "repeat", account["id"], order_id):
        message = "This page has expired. Open the order again and confirm from there."
        return _review_page(request, account, plan, None, error=message, entered=form)
    try:
        quantities = orders.parse_quantities(form, plan, state.facts)
    except orders.OrderError as problem:
        return _review_page(request, account, plan, None, error=str(problem), entered=form)
    if form.get("action") == "update":
        return _review_page(request, account, plan, quantities, entered=form)

    new_id, already = orders.place_repeat(
        conn, account, plan, quantities, token, now(request), state.facts
    )
    if already and not orders.same_quantities(conn, new_id, quantities):
        return RedirectResponse(f"/orders/{new_id}?resent=changed", status_code=303)
    return RedirectResponse(f"/orders/{new_id}", status_code=303)


def _review_page(request, account, plan, quantities, error="", entered=None, notice=""):
    state = request.app.state
    subtotal = orders.subtotal_paise(plan, quantities) if quantities else None
    charge = state.facts.delivery_charge(sum(quantities.values())) if quantities else None
    return render(
        request,
        "repeat.html",
        status_code=400 if error else 200,
        account=account,
        plan=plan,
        subtotal=subtotal,
        charge=charge,
        preview=delivery_day(now(request), state.facts.schedule, account["area"]),
        token=tokens.issue(state.secret, "repeat", account["id"], plan.source["id"]),
        max_quantity=state.facts.max_bottles_per_line,
        bottles_per_case=state.facts.bottles_per_case,
        error=error,
        notice=notice,
        entered=entered or {},
    )


def order_page(order_id: OrderId, request: Request, account: Account, conn: Conn):
    """The confirmation: delivery day, lines, total, and the cancel button while it is open."""
    order = db.get_order(conn, order_id, account["id"])
    if order is None:
        raise HTTPException(404)
    # A fixed notice chosen by a flag, never text taken from the URL.
    resent = request.query_params.get("resent") == "changed"
    return _order_view(request, account, conn, order, resent=resent)


async def cancel(order_id: OrderId, request: Request, account: Account, conn: Conn):
    """AT5 and AT6: cancel within the window; refuse after it."""
    order = db.get_order(conn, order_id, account["id"])
    if order is None:
        raise HTTPException(404)
    state = request.app.state
    token = str((await request.form()).get("token", ""))
    if not tokens.is_valid(state.secret, token, "cancel", account["id"], order_id):
        raise HTTPException(400, "This page has expired. Open the order again to cancel it.")
    if orders.cancel(conn, order, now(request), state.facts):
        return RedirectResponse(f"/orders/{order_id}", status_code=303)
    message = _window_closed_message(state.facts)
    return _order_view(request, account, conn, order, status_code=409, message=message)


def _window_closed_message(facts):
    """One wording for 'too late to cancel', on the order page and after a late cancel."""
    minutes = int(facts.cancel_window.total_seconds() // 60)
    return (
        f"The {minutes}-minute window to cancel has closed. "
        "Message us on WhatsApp or at hello@copperpot.example, and Meera will decide."
    )


def _order_view(request, account, conn, order, status_code=200, message="", resent=False):
    state = request.app.state
    today = now(request).astimezone(state.facts.schedule.timezone).date()
    can_cancel = orders.can_cancel(order, now(request), state.facts)
    upcoming = (order["delivery_date"] or "9999") >= today.isoformat()
    # Once the window closes, say how to ask for a change (unless the same words are
    # already on the page as the error for a late cancel).
    window_closed = (
        _window_closed_message(state.facts)
        if order["status"] == "placed" and upcoming and not can_cancel and not message
        else ""
    )
    return render(
        request,
        "order.html",
        status_code=status_code,
        account=account,
        order=order,
        lines=db.order_lines(conn, order["id"]),
        can_cancel=can_cancel,
        deadline=orders.cancel_deadline(order, state.facts),
        token=tokens.issue(state.secret, "cancel", account["id"], order["id"]),
        # No date yet (Meera confirms it) counts as upcoming.
        upcoming=upcoming,
        window_closed=window_closed,
        message=message,
        resent=resent,
    )


def demo_page(request: Request, conn: Conn):
    """Demo mode only: pick a bar and a pretend time, to walk the acceptance tests."""
    if not request.app.state.demo_mode:
        raise HTTPException(404)
    chosen = request.cookies.get("demo_account", "")
    return render(request, "demo.html", accounts=db.list_accounts(conn), chosen=chosen)


async def demo_choose(request: Request, conn: Conn):
    state = request.app.state
    if not state.demo_mode:
        raise HTTPException(404)
    form = await request.form()
    account_id = str(form.get("account_id", ""))
    if not ID.fullmatch(account_id) or db.get_account(conn, int(account_id)) is None:
        raise HTTPException(400, "Choose one of the bars.")
    pretend = str(form.get("pretend_now", "")).strip()
    if pretend and _pretend_time(pretend, state.facts) is None:
        raise HTTPException(400, "Pick the pretend time with the date and time picker.")
    response = RedirectResponse("/", status_code=303)
    response.set_cookie("demo_account", account_id, httponly=True, samesite="lax")
    if pretend:
        response.set_cookie("demo_now", pretend, httponly=True, samesite="lax")
    else:
        response.delete_cookie("demo_now")
    return response


def health(conn: Conn):
    """For the platform's uptime check (Chapter 9, the "Up" watch)."""
    conn.execute("SELECT 1")
    return {"status": "ok"}


# ---- the app ------------------------------------------------------------------------

# Every page the app serves. test_at8_only_the_expected_routes_exist holds the same
# list, so a new route is a decision recorded in the spec, not a side effect.
# (Routes are listed here rather than with decorators so the whole app fits in one view.)
ROUTES = [
    ("GET", "/", home),
    ("GET", "/repeat/{order_id}", review),
    ("POST", "/repeat/{order_id}", confirm),
    ("GET", "/orders/{order_id}", order_page),
    ("POST", "/orders/{order_id}/cancel", cancel),
    ("GET", "/demo", demo_page),
    ("POST", "/demo", demo_choose),
    ("GET", "/healthz", health),
]


def create_app(
    db_path: str | Path,
    facts_path: str | Path = DEFAULT_FACTS,
    demo_mode=False,
    secret: bytes | None = None,
):
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
    app.state.db_path = Path(db_path)
    app.state.facts = load_facts(facts_path)  # a broken facts file stops start-up
    app.state.demo_mode = demo_mode
    # Signs form tokens. Set COPPER_POT_SECRET in the platform's secrets store; without
    # it, a random secret is made at start-up and open pages expire on each restart.
    app.state.secret = secret or secrets.token_bytes(32)
    app.state.clock = lambda: datetime.now(UTC)
    app.state.templates = Jinja2Templates(directory=HERE / "templates")
    app.state.templates.env.filters["as_date"] = date.fromisoformat
    app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
    for method, path, endpoint in ROUTES:
        app.add_api_route(path, endpoint, methods=[method])

    @app.exception_handler(SignInNotConnected)
    def sign_in_not_connected(request, exc):
        return render(
            request,
            "message.html",
            status_code=503,
            title="Sign-in is not connected",
            text="This reference app has no sign-in of its own. Connect a managed login "
            "provider in current_account (app/main.py), or run it with DEMO_MODE=1.",
        )

    @app.exception_handler(ChooseDemoBar)
    def choose_demo_bar(request, exc):
        return RedirectResponse("/demo", status_code=303)

    @app.exception_handler(RequestValidationError)
    def bad_address(request, exc):
        # Only order ids are validated this way, so a bad one is simply not found.
        return render(
            request,
            "message.html",
            status_code=404,
            title="Not found",
            text="There is nothing here.",
        )

    @app.exception_handler(StarletteHTTPException)
    def friendly_error(request, exc):
        titles = {404: "Not found", 400: "Something is missing", 503: "Not available"}
        text = exc.detail if exc.status_code != 404 else "There is nothing here."
        return render(
            request,
            "message.html",
            status_code=exc.status_code,
            title=titles.get(exc.status_code, "Something went wrong"),
            text=text,
        )

    return app


_secret = os.environ.get("COPPER_POT_SECRET")
app = create_app(
    os.environ.get("COPPER_POT_DB", "data/copper_pot.db"),
    demo_mode=os.environ.get("DEMO_MODE") == "1",
    secret=_secret.encode() if _secret else None,
)
