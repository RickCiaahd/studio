from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Iterable, List


def transform_products(products: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Select and validate the product fields stored by this project."""
    transformed = []

    for index, product in enumerate(products):
        try:
            title = str(product["title"]).strip()
            category = str(product["category"]).strip()
            price = Decimal(str(product["price"]))
        except (KeyError, InvalidOperation, TypeError, ValueError) as exc:
            raise ValueError("Invalid product at index {}".format(index)) from exc

        if not title or not category or price < 0:
            raise ValueError("Invalid product at index {}".format(index))

        transformed.append({"title": title, "price": price, "category": category})

    return transformed
