import logging

LOGGER = logging.getLogger("fd_challenge")
LOGGER.setLevel(logging.INFO)

# Custom formatter for stream output
fmt = "[%(levelname)s]: %(message)s"
# Get the built-in StreamHandler
handler = logging.StreamHandler()
# Set the handler formatter
handler.setFormatter(logging.Formatter(fmt=fmt))
handler.setLevel(logging.INFO)

LOGGER.addHandler(handler)
