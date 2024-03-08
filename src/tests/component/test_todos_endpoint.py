from fixtures import JSON_RAW_DATA, FILTER_RESULT_FULL
from utils import validate_dicts, mock_response


def test_unauthorized_access_invalid_token(client):
    response = client.get("/todos", headers={"Authorization": "Bearer 123"})
    assert response.status_code == 401
    assert response.json() == {'error': {'reason': 'User does not have permission to access the application.'}}


def test_forbidden_access_for_user(client, mocker):
    mocker.patch("adapters.gateway.security.jwt.decode", return_value={"username": "invalid_user"})

    response = client.get("/todos", headers={"Authorization": "Bearer 123"})
    assert response.status_code == 403


def test_get_todos_success(client, mocker):
    mocker.patch("adapters.gateway.security.jwt.decode", return_value={"username": "frameworkdigital", })

    request = mock_response(status_code=200, json_data=JSON_RAW_DATA)
    mocker.patch("business_rules.todos_use_case.requests.get", return_value=request)

    response = client.get("/todos", headers={"Authorization": "Bearer 123"})

    assert response.status_code == 200
    validate_dicts(FILTER_RESULT_FULL, response.json())

