import csv
import json
import logging
import pandas as pd


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


def valida_riga(riga):
    try:
        prodotto = riga["prodotto"].strip()
        prezzo = float(riga["prezzo"])
        quantità = float(riga["quantità"])
        if prezzo <= 0 or  quantità <=0: 
            raise ValueError("Prezzo negativo")
        return {"prodotto": prodotto, "prezzo": prezzo, quantità : "quantità"}
    except (KeyError, ValueError) as e:
        logging.warning(f"Riga scartata: {riga} → {e}")
        return None

def filtra_righe_valide_per_calcoli(nome_file_csv):
    df = pd.read_csv(nome_file_csv)
    scartati = df[(df["quantità"] <= 0) | (df["prezzo_unitario"] <= 0)]
    logging.warning(f"Scartate {len(scartati)} righe non valide")
    df_validi = df[(df["quantità"] > 0) & (df["prezzo_unitario"] > 0)]
    return df_validi

def calcola_fatturato (nome_file_csv):
    df_validi = filtra_righe_valide_per_calcoli(nome_file_csv)
    df_validi["fatturato"] = df_validi["quantità"] * df_validi["prezzo_unitario"]
    return df_validi.to_dict(orient="records")

def genera_report(dati):
    df = pd.DataFrame(dati)

    df_report = (
        df.groupby("prodotto")[["quantità", "fatturato"]]
        .sum()
        .reset_index()
    )

    df_report = df_report.rename(columns={
        "quantità": "quantità_totale",
        "fatturato": "fatturato_totale"
    })

    logging.info(f"Generato report con {len(df_report)} prodotti")

    return df_report.to_dict(orient="records")

def carica_su_json(output_file, dati):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)
    logging.info(f"Salvati {len(dati)} elementi in {output_file}")

def esegui_pipeline_completa(input_file, output_clean, output_report):
    dati = calcola_fatturato (input_file)

    report = genera_report(dati)

    carica_su_json(output_clean, dati)
    carica_su_json(output_report, report)

def esegui_etl(file_input, file_output, validatore):
    logging.info(f"Avvio ETL: {file_input} → {file_output}")
    dati_validi = estrai_e_valida(file_input, validatore)
    carica_su_json(file_output, dati_validi)
    print("ETL completato.")

from progetto_etl.etl.api import estrai_prodotti, genera_report_categorie

def esegui_pipeline_api(output_clean, output_report):
    df = pd.DataFrame(estrai_prodotti())

    if df.empty:
        raise Exception("Nessun dato estratto dalla API")
    
    df = df[["title","price", "category"]]

    logging.info(f"Estratti {len(df)} prodotti dalla API")

    report = genera_report_categorie(df)

    logging.info(f"Generato report con {len(report)} categorie")

    df.to_json(output_clean, orient="records")
    report.to_json(output_report, orient="records")

if __name__ == "__main__":
    esegui_etl("prodotti.csv", "prodotti_filtrati.json", valida_prezzo_positivo)
