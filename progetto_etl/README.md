# 📊 Progetto ETL con Python e Pandas

## 📌 Descrizione

Questo progetto implementa una pipeline ETL (Extract, Transform, Load) in Python per l’elaborazione di dati di vendita.

La pipeline:
- legge dati da un file CSV
- valida i dati
- calcola il fatturato
- genera un report aggregato per prodotto
- salva i risultati in formato JSON

---

## ⚙️ Tecnologie utilizzate

- Python 3
- pandas
- pytest
- logging
- GitHub Actions (CI/CD)

---

## 📂 Struttura del progetto

progetto_etl/
├── data/
│ └── vendite.csv
├── etl/
│ ├── pipeline.py
│ └── validazione.py
├── tests/
│ ├── test_pipeline.py
│ └── test_validazione.py
├── requirements.txt
└── README.md


---

## 🔄 Pipeline ETL

### 1. Extract
Lettura dati da CSV tramite pandas

### 2. Transform
- validazione dei dati (quantità e prezzo > 0)
- calcolo del fatturato:
  fatturato = quantità * prezzo_unitario

  
### 3. Load
- salvataggio dati puliti → `dati_clean.json`
- generazione report aggregato → `dati_report.json`

---

## 📊 Esempio output report

```json
[
{
  "prodotto": "pane",
  "quantità_totale": 15,
  "fatturato_totale": 22.5
}
]

🧪 Testing

Il progetto include test automatici con pytest:

test unitari per validazione
test trasformazione dati
test pipeline completa
Eseguire i test

PYTHONPATH=. pytest

🚀 Esecuzione pipeline

python3 -c "from progetto_etl.etl.pipeline import esegui_pipeline_completa; esegui_pipeline_completa('data/vendite.csv', 'dati_clean.json', 'dati_report.json')"

🔁 CI/CD

Il progetto utilizza GitHub Actions per eseguire automaticamente i test ad ogni push.

🎯 Obiettivo del progetto

Dimostrare competenze pratiche in:

Data Engineering di base
progettazione pipeline ETL
manipolazione dati con pandas
testing e qualità del codice
automazione CI/CD