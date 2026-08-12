import os
from typing import Any, Dict, List

import requests

DEFAULT_API_URL = "https://dummyjson.com/products"
DEFAULT_TIMEOUT_SECONDS = 10.0


def extract_products() -> List[Dict[str, Any]]:
    """Fetch product records from the configured REST API."""
    url = os.getenv("PRODUCTS_API_URL", DEFAULT_API_URL)
    timeout = float(os.getenv("HTTP_TIMEOUT_SECONDS", DEFAULT_TIMEOUT_SECONDS))

    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    payload = response.json()

    products = payload.get("products")
    if not isinstance(products, list):
        raise ValueError("API response does not contain a 'products' list")

    return products
