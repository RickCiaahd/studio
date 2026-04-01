import json
from progetto_etl.etl.pipeline import esegui_etl, valida_prezzo_positivo


def test_esegui_etl(tmp_path):
    # 📄 1. Crea il file CSV di input
    input_path = tmp_path / "input.csv"
    input_path.write_text("prodotto,prezzo\npane,2.5\nlatte,-3.0\nuova,1.8")

    # 📄 2. Definisci il path del file JSON di output
    output_path = tmp_path / "output.json"

    # 🚀 3. Esegui la funzione
    esegui_etl(input_path, output_path, valida_prezzo_positivo)

    # 📦 4. Verifica che il file JSON sia stato creato
    assert output_path.exists()

    # 🧐 5. Leggi il contenuto del file JSON
    contenuto = json.loads(output_path.read_text())

    # ✅ 6. Verifica che solo le righe valide siano presenti
    assert len(contenuto) == 2
    assert contenuto[0]["prodotto"] == "pane"
    assert contenuto[1]["prodotto"] == "uova"


import json
from progetto_etl.etl.pipeline import esegui_etl, valida_prezzo_positivo

def test_esegui_etl_tutti_dati_invalidi(tmp_path):
    # 📄 1. Crea un CSV con TUTTI dati non validi
    input_path = tmp_path / "input.csv"
    input_path.write_text("prodotto,prezzo\nlatte,-1\ncaffè,-2")

    # 📄 2. Output path
    output_path = tmp_path / "output.json"

    # 🚀 3. Esegui l’ETL
    esegui_etl(input_path, output_path, valida_prezzo_positivo)

    # ✅ 4. Verifica che il file esista ma sia vuoto
    assert output_path.exists()

    contenuto = json.loads(output_path.read_text())
    assert contenuto == []


from progetto_etl.etl.pipeline import calcola_fatturato

def test_calcola_fatturato(tmp_path):
    file_csv = tmp_path / "vendite.csv"

    file_csv.write_text(
        "prodotto,quantità,prezzo_unitario\n"
        "pane,10,1.5\n"
        "latte,-2,0.9\n"
        "caffè,5,2.0\n",
        encoding="utf-8"
    )

    risultato = calcola_fatturato(file_csv)

    assert len(risultato) == 2

    # qui controlla almeno una riga
    assert risultato[0]["prodotto"] == "pane"
    assert risultato[0]["fatturato"] == 15.0


from progetto_etl.etl.pipeline import genera_report

def test_genera_report(tmp_path):
    dati=[
            {"prodotto": "pane", "quantità": 10, "fatturato": 15},
            {"prodotto": "pane", "quantità": 5, "fatturato": 7.5}
         ]

    risultato = genera_report(dati)

    assert len(risultato) == 1

    # qui controlla almeno una riga
    assert risultato[0]["prodotto"] == "pane"
    assert risultato[0]["quantità_totale"] == 15.0
    assert risultato[0]["fatturato_totale"] == 22.5
    assert isinstance(risultato, list)
    assert "quantità_totale" in risultato[0]

from progetto_etl.etl.pipeline import esegui_pipeline_completa

def test_esegui_pipeline_completa(tmp_path):
    input_file = tmp_path / "vendite.csv"

    input_file.write_text(
        "prodotto,quantità,prezzo_unitario\n"
        "pane,10,1.5\n"
        "latte,3,0.9\n"
        "caffè,5,2.0\n"
        "latte,4,0.9\n"
        "pane,5,1.5\n"
        "caffè,6,2.0\n",
        encoding="utf-8"
    )

    output_clean = tmp_path / "dati_clean.json"
    output_report = tmp_path / "dati_report.json"

    esegui_pipeline_completa(input_file, output_clean, output_report)

    with open(output_clean, "r", encoding="utf-8") as f:
        dati_clean = json.load(f)

    with open(output_report, "r", encoding="utf-8") as f:
        dati_report = json.load(f)

    assert output_clean.exists()
    assert output_report.exists()
    assert len(dati_clean) == 6
    assert len(dati_report) == 3
    assert dati_clean[0]["prodotto"] == "pane"
    assert dati_clean[0]["fatturato"] == 15.0
    assert any(
    r["prodotto"] == "pane" 
    and r["quantità_totale"] == 15 
    and r["fatturato_totale"] == 22.5
    for r in dati_report
    ) 