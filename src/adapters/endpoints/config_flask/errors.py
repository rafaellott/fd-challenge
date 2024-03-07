import logging
import traceback
from dataclasses import dataclass
from typing import Tuple

from flask import jsonify, Response
from flask.app import Flask

from business_rules.exceptions import BaseFdChallengeException

LOGGER = logging.getLogger(__name__)


@dataclass
class ErrorMapping:
    """Class of errors mapped."""

    status_code: int
    message: str = "An error occurred in the system."


ERROR_CODE_MAPPING = {
    # 400s
    "UnauthorizedException": ErrorMapping(
        401, "User '{username}' does not have permission to access the application.",
    ),
    "ForbiddenException": ErrorMapping(
        403, "You do not have access to this page.",
    ),
    "ResourceNotFoundException": ErrorMapping(
        404, "Entity not found."
    ),
    "BadRequestException": ErrorMapping(422, "Request format invalid."),

    # 500s
    "Exception": ErrorMapping(500),
    "BaseFdChallengeException": ErrorMapping(500),
    "BadGatewayException": ErrorMapping(502),
}


def setup_error_handling(app: Flask) -> None:
    """Configure error handling."""

    @app.errorhandler(Exception)
    def configure_default_error(exception: Exception) -> Tuple[Response, int]:
        """Generate a response for internal server errors."""
        return _configure_exception_response(exception)


def _configure_exception_response(exception: Exception) -> Tuple[Response, int]:
    """Generate a response for exceptions."""
    class_name = type(exception).__name__
    exception_mapping = ERROR_CODE_MAPPING.get(class_name) or ERROR_CODE_MAPPING["Exception"]

    code = exception_mapping.status_code
    message = str(exception)
    if not isinstance(exception, BaseFdChallengeException):
        message = exception_mapping.message

    if code != 403:
        LOGGER.error("Exception '%s'", exception)
        if code >= 400:
            LOGGER.error(traceback.format_exc())

    return (
        jsonify({
            "error": {
                "reason": message,
            }
        }),
        code,
    )
