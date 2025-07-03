from unittest.mock import patch

from src.utils import way_to_json


@patch("json.load")
def test_read_json_1(mock_load, utils_1):
    mock_load.return_value = utils_1
    assert way_to_json(mock_load) == utils_1
    mock_load.assert_called()


@patch("json.load")
def test_read_json_2(mock_load, utils_2):
    mock_load.return_value = utils_2
    assert way_to_json(mock_load) == utils_2
    mock_load.assert_called()
