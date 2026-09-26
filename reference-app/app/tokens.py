"""Signed form tokens: proof that a form came from a page this app served.

The review screen and the order page each put a token in their form. The token
is signed with the server's secret over who it was for and what it may do, so
a made-up token, or one copied from another order's page, is refused. That
stops another website from posting an order or a cancel on a bar's behalf.
The repeat token also makes confirming safe to repeat (spec B13).
"""

import hashlib
import hmac
import secrets


def issue(secret: bytes, purpose: str, account_id: int, order_id: int) -> str:
    nonce = secrets.token_urlsafe(12)
    return f"{nonce}.{_sign(secret, purpose, account_id, order_id, nonce)}"


def is_valid(secret: bytes, token: str, purpose: str, account_id: int, order_id: int) -> bool:
    nonce, _, signature = token.partition(".")
    expected = _sign(secret, purpose, account_id, order_id, nonce)
    return bool(nonce) and hmac.compare_digest(signature, expected)


def _sign(secret: bytes, purpose: str, account_id: int, order_id: int, nonce: str) -> str:
    message = f"{purpose}:{account_id}:{order_id}:{nonce}".encode()
    return hmac.new(secret, message, hashlib.sha256).hexdigest()
