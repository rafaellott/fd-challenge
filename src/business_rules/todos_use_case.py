import os

import requests

from .exceptions import BadGatewayException


class TodosUseCase:
    url = os.getenv("FETCH_URL") or "https://jsonplaceholder.typicode.com/todos"

    def _fetch_data(self):
        resp = requests.get(self.url)
        try:
            resp.raise_for_status()
        except requests.exceptions.RequestException:
            raise BadGatewayException(message="Gateway not available.")

        return resp.json()

    def get_filtered_data(self, completed=None, title=None, qtd_items=5):
        raw_data = self._fetch_data()
        filter_result = raw_data

        if completed is not None:
            filter_result = list(filter(lambda x: x["completed"] == completed, raw_data))

        if title:
            filter_result = list(filter(lambda x: title.lower() in x["title"].lower(), raw_data))

        return filter_result[:qtd_items]
