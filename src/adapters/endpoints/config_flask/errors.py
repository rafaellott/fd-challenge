import logging
import traceback
import json
from dataclasses import dataclass

from connexion.lifecycle import ConnexionResponse, ConnexionRequest
from werkzeug.exceptions import HTTPException as wHTTPException
from starlette.exceptions import HTTPException as sHTTPException

from business_rules.exceptions import BaseFdChallengeException

LOGGER = logging.getLogger("fd_challenge." + __name__)


@dataclass
class ErrorMapping:
    """Class of errors mapped."""

    status_code: int
    message: str = "An error occurred in the system."

    def __str__(self):
        """Representation as string."""
        return self.message


ERROR_CODE_MAPPING = {
    # 400s
    "UnauthorizedException": ErrorMapping(
        401, "User does not have permission to access the application.",
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


def setup_error_handling(app) -> None:
    """Configure error handling."""

    app.add_error_handler(Exception, _configure_exception_response)
    app.add_error_handler(400, _configure_exception_response)
    app.add_error_handler(404, _configure_exception_response)
    app.add_error_handler(405, _configure_exception_response)


def _configure_exception_response(request: ConnexionRequest, exc: Exception) -> ConnexionResponse:
    """Generate a response for exceptions."""

    class_name = type(exc).__name__
    exception_mapping = ERROR_CODE_MAPPING.get(class_name) or ERROR_CODE_MAPPING["Exception"]
    detail = None

    code = exception_mapping.status_code
    if isinstance(exc, (wHTTPException, sHTTPException)):
        code = getattr(exc, "code", getattr(exc, "status_code", 500))

    if not isinstance(exc, BaseFdChallengeException):
        message = str(exc)
    else:
        message = exception_mapping.message
        detail = exc.message

    if code != 403:
        LOGGER.error("Exception: %s", message)
        LOGGER.error("Exception Detail: %s", detail)
        if code >= 400:
            LOGGER.error(traceback.format_exc())

    return ConnexionResponse(
        status_code=code,
        content_type="application/json",
        body=json.dumps({
            "error": {
                "reason": message,
            }
        })
    )
