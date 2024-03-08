"""Main app."""
import logging
import connexion

from adapters.endpoints.config_flask import customize_flask

LOGGER = logging.getLogger("fd_challenge." + __name__)
app = connexion.App(__name__)
application = app.app
application.url_map.strict_slashes = False

customize_flask(app)

app.add_api('openapi.yaml')


if __name__ == "__main__":
    LOGGER.info("Starting application")
    app.run("main:app", port=8080)
