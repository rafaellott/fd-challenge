import logging
import jwt
from business_rules.exceptions import UnauthorizedException

LOGGER = logging.getLogger(__name__)

AUTHORIZED_USERS = {"frameworkdigital", }


def decode_token(token: str):
    LOGGER.info("Decoding token...")

    decoded = jwt.decode(token, "secret_word", algorithms=["HS256"])
    username = decoded.get("username")

    if not username or username not in AUTHORIZED_USERS:
        raise UnauthorizedException()

    return {
        "username": decoded["username"],
        "sub": decoded["username"],
    }
