from unittest.mock import Mock, patch

import pytest

from src.etl.extract import extract_products


@patch("src.etl.extract.requests.get")
def test_extract_products_validates_response(mock_get, monkeypatch):
    monkeypatch.setenv("HTTP_TIMEOUT_SECONDS", "3")
    response = Mock()
    response.json.return_value = {"products": [{"title": "A"}]}
    mock_get.return_value = response

    assert extract_products() == [{"title": "A"}]
    mock_get.assert_called_once_with("https://dummyjson.com/products", timeout=3.0)
    response.raise_for_status.assert_called_once_with()


@patch("src.etl.extract.requests.get")
def test_extract_products_rejects_unexpected_payload(mock_get):
    mock_get.return_value.json.return_value = {"items": []}

    with pytest.raises(ValueError, match="products"):
        extract_products()
