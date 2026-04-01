from progetto_etl.etl.api import estrai_prodotti
from progetto_etl.etl.pipeline import esegui_pipeline_api
from unittest.mock import patch

from unittest.mock import patch
from progetto_etl.etl.api import estrai_prodotti


@patch("progetto_etl.etl.api.requests.get")
def test_estrai_prodotti(mock_get):
    # dati finti
    fake_response = {
        "products": [
            {"title": "A", "price": 10, "category": "x"},
            {"title": "B", "price": 20, "category": "y"}
        ]
    }

    # configuro il mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = fake_response

    # eseguo funzione
    risultato = estrai_prodotti()

    # assert
    assert isinstance(risultato, list)
    assert len(risultato) == 2
    assert risultato[0]["title"] == "A"


from unittest.mock import patch
import json


@patch("progetto_etl.etl.pipeline.estrai_prodotti")
def test_esegui_pipeline_api(mock_estrai, tmp_path):

    # dati finti (GIÀ pronti)
    mock_estrai.return_value = [
        {"title": "A", "price": 10, "category": "x"},
        {"title": "B", "price": 20, "category": "x"}
    ]

    output_clean = tmp_path / "clean.json"
    output_report = tmp_path / "report.json"

    # eseguo pipeline
    esegui_pipeline_api(output_clean, output_report)

    # verifica file
    assert output_clean.exists()
    assert output_report.exists()

    # leggo output
    with open(output_report, "r") as f:
        report = json.load(f)

    # assert report
    assert len(report) == 1
    assert report[0]["category"] == "x"
    assert report[0]["numero_prodotti"] == 2
    assert report[0]["prezzo_medio"] == 15