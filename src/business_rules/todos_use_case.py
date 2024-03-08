import os
import logging

import requests

from .exceptions import BadGatewayException

LOGGER = logging.getLogger("fd_challenge." + __name__)


class TodosUseCase:
    url = os.getenv("FETCH_URL") or "https://jsonplaceholder.typicode.com/todos"

    def _fetch_data(self):
        resp = requests.get(self.url)
        try:
            resp.raise_for_status()
        except requests.exceptions.RequestException:
            LOGGER.error("API Status Code: %s", resp.status_code)
            raise BadGatewayException(message="Gateway not available.")

        LOGGER.info("API Status Code: %s", resp.status_code)
        LOGGER.info("API Result: %s", resp.json())
        return resp.json()

    def get_filtered_data(self, completed=None, title=None, qtd_items=5):
        raw_data = self._fetch_data()
        filter_result = raw_data

        if completed is not None:
            LOGGER.info("Filtering for completed: `%s`", completed)
            filter_result = list(filter(lambda x: x["completed"] == completed, raw_data))

        if title:
            LOGGER.info("Filtering for title: `%s`", title)
            filter_result = list(filter(lambda x: title.lower() in x["title"].lower(), filter_result))

        LOGGER.info("Quantity of items to return: %s", qtd_items)
        return filter_result[:qtd_items]
