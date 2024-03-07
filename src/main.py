"""Main app."""
import logging
from flask import Flask

LOGGER = logging.getLogger(__name__)
app = Flask(__name__)


if __name__ == "__main__":
    LOGGER.info("Starting application")
    app.run(port=8080, server="gevent", debug=True)
