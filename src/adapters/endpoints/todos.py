"""
Endpoints mapping file.

In this file you will find all code related to each endpoint.
It's responsibility are to receive the parameters from request,call the Use Case
to process than receive the data and convert to a valid JSON format.
"""

from business_rules.todos_use_case import TodosUseCase
from entities.todos import TodoSchema


def get_todos(completed=None, title=None, qtd_items=5):
    if qtd_items > 20:
        qtd_items = 20

    todos_uc = TodosUseCase()
    data = todos_uc.get_filtered_data(completed, title, qtd_items)

    r = TodoSchema(many=True).load(data)
    return r
