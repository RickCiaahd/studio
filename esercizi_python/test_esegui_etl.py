import json
from esercizi_python.etl_modulare import esegui_etl, valida_prezzo_positivo


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
from esercizi_python.etl_modulare import esegui_etl, valida_prezzo_positivo


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
