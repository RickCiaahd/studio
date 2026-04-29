import requests

def extract_products():
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    data = response.json()
    return data["products"]