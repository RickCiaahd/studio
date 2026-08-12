import os
from typing import Any, Dict

import psycopg2


def connection_settings() -> Dict[str, Any]:
    """Build PostgreSQL connection settings from environment variables."""
    return {
        "host": os.getenv("POSTGRES_HOST", "localhost"),
        "port": int(os.getenv("POSTGRES_PORT", "5432")),
        "dbname": os.getenv("POSTGRES_DB", "products_db"),
        "user": os.getenv("POSTGRES_USER", "postgres"),
        "password": os.getenv("POSTGRES_PASSWORD", "postgres"),
    }


def get_connection():
    """Open a PostgreSQL connection using environment-based configuration."""
    return psycopg2.connect(**connection_settings())


def create_table() -> None:
    """Create the destination table when it does not already exist."""
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    price NUMERIC NOT NULL CHECK (price >= 0),
                    category TEXT NOT NULL
                );
                """
            )
