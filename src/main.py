"""Main app."""
import logging
from flask import Flask

LOGGER = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    LOGGER.info("Starting application")
    app.run(port=8080, server="gevent", debug=True)
