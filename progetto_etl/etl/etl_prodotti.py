import csv
import json


def estrai_da_csv(nome_file):
    with open(nome_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [
            {"prodotto": r["prodotto"], "prezzo": float(r["prezzo"])} for r in reader
        ]


def trasforma_dati(prodotti):
    return [p for p in prodotti if p["prezzo"] > 2.0]


def carica_su_json(nome_file, dati):
    with open(nome_file, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    dati_csv = estrai_da_csv("prodotti.csv")
    dati_filtrati = trasforma_dati(dati_csv)
    carica_su_json("prodotti_filtrati.json", dati_filtrati)
    print("Pipeline completata.")
