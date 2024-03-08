import json

RAW_DATA = """
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": true
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": false
  }
]
"""

JSON_RAW_DATA = json.loads(RAW_DATA)


FILTER_RESULT_FULL = [{"id": x.get("id"), "title": x.get("title")} for x in JSON_RAW_DATA]

FILTER_RESULT_COMPLETED_TRUE = list(map(
    lambda d: {'id': d['id'], 'title': d['title']},
    filter(lambda x: x["completed"] is True, JSON_RAW_DATA)
))
