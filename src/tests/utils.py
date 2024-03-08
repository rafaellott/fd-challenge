from unittest import mock


def mock_response(
    status_code: int = 200,
    content: str = "CONTENT",
    json_data: dict = None,
    raise_for_status: Exception = None,
):
    """Dynamically change the Mock Response for each test."""
    mock_resp = mock.Mock()
    # mock raise_for_status call w/optional error
    mock_resp.raise_for_status = mock.Mock()
    if raise_for_status:
        mock_resp.raise_for_status.side_effect = raise_for_status
    # set status code and content
    mock_resp.status_code = status_code
    mock_resp.content = content
    # add json data if provided
    if json_data:
        mock_resp.json = mock.Mock(return_value=json_data)
    return mock_resp


def validate_dicts(expected, result, parent=""):
    """Validate dynamically the elements: dict, list and set."""
    if isinstance(expected, dict) and isinstance(result, dict):
        for key, value in expected.items():
            if key not in result:
                raise AssertionError(f"result does not have key '{key}'")
            validate_dicts(expected[key], result[key], f"{parent}/{key}")

    elif isinstance(expected, (tuple, list, set)) and isinstance(result, (tuple, list, set)):
        assert len(expected) == len(
            result
        ), f"expected len {len(expected)}, but got {len(result)} # In '{parent}'"
        for value_expected, value_result in zip(expected, result):
            validate_dicts(value_expected, value_result, f"{parent}")
    else:
        assert expected == result, f"Expected '{expected}', got '{result}' # In '{parent}''"
