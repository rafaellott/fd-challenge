import pytest

from main import app


@pytest.fixture(autouse=True)
def _app():
    """Load the Flask Application."""
    yield app

#
# @pytest.fixture(autouse=True)
# def req_ctx(_app):
#     """Load the Flask Request Context."""
#     with _app.test_request_context() as ctx:
#         yield ctx


@pytest.fixture(scope="function")
def client(_app):
    """Load a Flask test client."""

    with _app.test_client() as _client:
        yield _client
