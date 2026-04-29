def transform_products(products):
    risultato = []

    for p in products:
        nuovo = {
        "title": p["title"],
        "price": p["price"],
        "category": p["category"]
        }
        risultato.append(nuovo)
        pass

    return risultato