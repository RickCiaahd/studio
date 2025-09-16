import csv


def scrivi_prodotti(nome_file, lista_prodotti):
    with open(nome_file, mode="w", newline="", encoding="utf-8") as file:
        intestazioni = ["prodotto", "prezzo"]
        writer = csv.DictWriter(file, fieldnames=intestazioni)
        writer.writeheader()
        for prodotto in lista_prodotti:
            writer.writerow(prodotto)


if __name__ == "__main__":
    prodotti = [
        {"prodotto": "biscotti", "prezzo": 2.5},
        {"prodotto": "yogurt", "prezzo": 1.3},
        {"prodotto": "miele", "prezzo": 4.0},
    ]
    scrivi_prodotti("nuovi_prodotti.csv", prodotti)
    print("File CSV scritto correttamente.")
