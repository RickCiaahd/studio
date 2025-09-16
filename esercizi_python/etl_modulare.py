import csv
import json
import logging

logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def valida_prezzo_positivo(riga):
    try:
        prodotto = riga["prodotto"].strip()
        prezzo = float(riga["prezzo"])
        if prezzo < 0:
            raise ValueError("Prezzo negativo")
        return {"prodotto": prodotto, "prezzo": prezzo}
    except (KeyError, ValueError) as e:
        logging.warning(f"Riga scartata: {riga} → {e}")
        return None


def estrai_e_valida(nome_file, validatore):
    validi = []
    with open(nome_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for riga in reader:
            prodotto = validatore(riga)
            if prodotto:
                validi.append(prodotto)
    return validi


def carica_su_json(nome_file, dati):
    with open(nome_file, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)
    logging.info(f"Salvati {len(dati)} elementi in {nome_file}")


def esegui_etl(file_input, file_output, validatore):
    logging.info(f"Avvio ETL: {file_input} → {file_output}")
    dati_validi = estrai_e_valida(file_input, validatore)
    carica_su_json(file_output, dati_validi)
    print("ETL completato.")


if __name__ == "__main__":
    esegui_etl("prodotti.csv", "prodotti_filtrati.json", valida_prezzo_positivo)
