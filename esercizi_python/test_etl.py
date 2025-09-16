from esercizi_python.etl_prodotti import trasforma_dati


def test_filtra_prodotti_maggiori_di_due_euro():
    input_mock = [
        {"prodotto": "pane", "prezzo": 1.5},
        {"prodotto": "latte", "prezzo": 2.0},
        {"prodotto": "caffè", "prezzo": 3.5},
    ]

    atteso = [{"prodotto": "caffè", "prezzo": 3.5}]

    assert trasforma_dati(input_mock) == atteso
