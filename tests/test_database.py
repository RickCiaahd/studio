from decimal import Decimal
from unittest.mock import MagicMock, patch

from src.etl.db import connection_settings
from src.etl.load import save_to_db


def test_connection_settings_uses_environment(monkeypatch):
    monkeypatch.setenv("POSTGRES_HOST", "db")
    monkeypatch.setenv("POSTGRES_PORT", "5433")
    monkeypatch.setenv("POSTGRES_DB", "lab")
    monkeypatch.setenv("POSTGRES_USER", "user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "secret")

    assert connection_settings() == {
        "host": "db", "port": 5433, "dbname": "lab", "user": "user", "password": "secret"
    }


@patch("src.etl.load.get_connection")
@patch("src.etl.load.execute_batch")
def test_save_to_db_batches_rows(mock_execute_batch, mock_connection):
    connection_context = MagicMock()
    connection = MagicMock()
    cursor = MagicMock()
    mock_connection.return_value = connection_context
    connection_context.__enter__.return_value = connection
    connection.cursor.return_value.__enter__.return_value = cursor
    products = [{"title": "A", "price": Decimal("2.50"), "category": "x"}]

    assert save_to_db(products) == 1
    mock_execute_batch.assert_called_once()
    assert mock_execute_batch.call_args[0][2] == [("A", Decimal("2.50"), "x")]
