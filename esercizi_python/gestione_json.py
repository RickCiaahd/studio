import json


def scrivi_json(nome_file, dati):
    with open(nome_file, "w", encoding="utf-8") as file:
        json.dump(dati, file, indent=4, ensure_ascii=False)
    print("File JSON scritto correttamente.")


def leggi_json(nome_file):
    with open(nome_file, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    prodotti = [
        {"prodotto": "biscotti", "prezzo": 2.5},
        {"prodotto": "yogurt", "prezzo": 1.3},
        {"prodotto": "miele", "prezzo": 4.0},
    ]

    scrivi_json("prodotti.json", prodotti)

    prodotti_letti = leggi_json("prodotti.json")
    for p in prodotti_letti:
        print(f"{p['prodotto'].capitalize()}: €{p['prezzo']:.2f}")
