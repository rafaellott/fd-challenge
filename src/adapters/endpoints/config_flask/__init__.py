"""Customize Flask."""
from .errors import setup_error_handling


def customize_flask(app):
    """All custom methods."""
    setup_error_handling(app)
