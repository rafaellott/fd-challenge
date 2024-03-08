import logging
import jwt

from business_rules.exceptions import UnauthorizedException, ForbiddenException

LOGGER = logging.getLogger("fd_challenge." + __name__)

AUTHORIZED_USERS = {"frameworkdigital", }


def decode_token(token: str):
    LOGGER.info("Decoding token...")

    try:
        decoded = jwt.decode(token, "secret_word", algorithms=["HS256"])
        username = decoded.get("username")
        LOGGER.info("Token decoded!")
    except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.DecodeError) as e:
        raise UnauthorizedException(message=f"Error whiling decoding token: {e}") from e

    if not username:
        raise UnauthorizedException(message="ola vc. vc e eu")

    if username not in AUTHORIZED_USERS:
        raise ForbiddenException()

    return {
        "username": decoded["username"],
        "sub": decoded["username"],
    }
