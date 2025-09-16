import csv
import json
import logging

# Imposta il logging
logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def valida_riga(riga):
    try:
        prodotto = riga["prodotto"].strip()
        prezzo = float(riga["prezzo"])
        if prezzo < 0:
            raise ValueError("Prezzo negativo")
        return {"prodotto": prodotto, "prezzo": prezzo}
    except (KeyError, ValueError) as e:
        logging.warning(f"Riga scartata: {riga} → {e}")
        return None


def estrai_e_valida(nome_file_csv):
    prodotti_validi = []
    with open(nome_file_csv, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for riga in reader:
            prodotto_valido = valida_riga(riga)
            if prodotto_valido:
                prodotti_validi.append(prodotto_valido)
    return prodotti_validi


def carica_su_json(nome_file, dati):
    with open(nome_file, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)
    logging.info(f"Salvati {len(dati)} prodotti in {nome_file}")


if __name__ == "__main__":
    dati = estrai_e_valida("prodotti.csv")
    carica_su_json("prodotti_validati.json", dati)
    print("ETL completato. Controlla etl.log.")
