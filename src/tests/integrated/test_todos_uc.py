import pytest
from requests import HTTPError

from business_rules.exceptions import BadGatewayException
from business_rules.todos_use_case import TodosUseCase
from utils import mock_response, validate_dicts
from fixtures import JSON_RAW_DATA


def test_get_filtered_data_error(mocker):
    request = mock_response(
        status_code=404, raise_for_status=HTTPError("Error url")
    )
    mocker.patch("business_rules.todos_use_case.requests.get", return_value=request)

    with pytest.raises(BadGatewayException):
        TodosUseCase().get_filtered_data()


def test_fetch_data_success(mocker):
    expected_result = [
        {'id': 1, 'title': 'delectus aut autem'},
        {'id': 2, 'title': 'quis ut nam facilis et officia qui'},
        {'id': 3, 'title': 'fugiat veniam minus'}
    ]
    request = mock_response(
        status_code=200, json_data=JSON_RAW_DATA
    )
    mocker.patch("business_rules.todos_use_case.requests.get", return_value=request)
    resp = TodosUseCase().get_filtered_data()

    validate_dicts(expected_result, resp)
