from decimal import Decimal
from unittest.mock import MagicMock, patch

from src.api.app import get_products


@patch("src.api.app.get_connection")
def test_get_products_serializes_database_rows(mock_connection):
    connection = MagicMock()
    cursor = MagicMock()
    mock_connection.return_value.__enter__.return_value = connection
    connection.cursor.return_value.__enter__.return_value = cursor
    cursor.fetchall.return_value = [("Phone", Decimal("99.50"), "mobile")]

    assert get_products() == [{"title": "Phone", "price": 99.5, "category": "mobile"}]
