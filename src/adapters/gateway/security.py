import logging
import jwt

from business_rules.exceptions import UnauthorizedException, ForbiddenException

LOGGER = logging.getLogger(__name__)

AUTHORIZED_USERS = {"frameworkdigital", }


def decode_token(token: str):
    LOGGER.info("Decoding token...")
    print("Decoding token...")

    try:
        decoded = jwt.decode(token, "secret_word", algorithms=["HS256"])
        username = decoded.get("username")
    except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.DecodeError):
        raise UnauthorizedException()

    if not username:
        raise UnauthorizedException()

    if username not in AUTHORIZED_USERS:
        raise ForbiddenException()

    return {
        "username": decoded["username"],
        "sub": decoded["username"],
    }
