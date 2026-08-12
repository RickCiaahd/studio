from decimal import Decimal
from typing import Dict, List, Union

from fastapi import FastAPI

from src.etl.db import get_connection

app = FastAPI(title="Data Engineering Lab API")


@app.get("/products")
def get_products() -> List[Dict[str, Union[str, float]]]:
    """Return products currently stored in PostgreSQL."""
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT title, price, category FROM products ORDER BY id")
            rows = cursor.fetchall()

    return [
        {"title": title, "price": float(Decimal(price)), "category": category}
        for title, price, category in rows
    ]
