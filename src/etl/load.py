import logging
from typing import Any, Dict, Iterable

from psycopg2.extras import execute_batch

from src.etl.db import get_connection

LOGGER = logging.getLogger(__name__)


def save_to_db(products: Iterable[Dict[str, Any]]) -> int:
    """Insert transformed products in one database transaction."""
    rows = [(p["title"], p["price"], p["category"]) for p in products]
    if not rows:
        LOGGER.info("No products to insert")
        return 0

    with get_connection() as connection:
        with connection.cursor() as cursor:
            execute_batch(
                cursor,
                "INSERT INTO products (title, price, category) VALUES (%s, %s, %s)",
                rows,
            )

    LOGGER.info("Inserted %d products into PostgreSQL", len(rows))
    return len(rows)
