from decimal import Decimal

import pytest

from src.etl.transform import transform_products


def test_transform_products_selects_expected_fields():
    products = [{"title": " Phone ", "price": 99.5, "category": " mobile ", "stock": 4}]

    assert transform_products(products) == [
        {"title": "Phone", "price": Decimal("99.5"), "category": "mobile"}
    ]


def test_transform_products_rejects_invalid_record():
    with pytest.raises(ValueError, match="index 0"):
        transform_products([{"title": "Missing fields"}])
