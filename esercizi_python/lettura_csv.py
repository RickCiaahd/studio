import csv

def leggi_prodotti(nome_file):
    with open(nome_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        prodotti = []
        for riga in reader:
            prodotti.append({
                "prodotto": riga["prodotto"],
                "prezzo": float(riga["prezzo"])
            })
        return prodotti

if __name__ == "__main__":
    lista_prodotti = leggi_prodotti("prodotti.csv")
    for p in lista_prodotti:
        print(f"{p['prodotto'].capitalize()}: €{p['prezzo']:.2f}")
