from esercizi_python.etl_modulare import valida_prezzo_positivo


def test_valida_prezzo_valido():
    riga = {"prodotto": "latte", "prezzo": "2.5"}
    risultato = valida_prezzo_positivo(riga)
    assert risultato == {"prodotto": "latte", "prezzo": 2.5}


def test_valida_prezzo_negativo():
    riga = {"prodotto": "uova", "prezzo": "-3"}
    risultato = valida_prezzo_positivo(riga)
    assert risultato is None


def test_valida_prezzo_non_numerico():
    riga = {"prodotto": "pane", "prezzo": "abc"}
    risultato = valida_prezzo_positivo(riga)
    assert risultato is None


def test_valida_prezzo_mancante():
    riga = {"prodotto": "caffè"}
    risultato = valida_prezzo_positivo(riga)
    assert risultato is None


def test_valida_prodotto_mancante():
    riga = {"prezzo": "1.0"}
    risultato = valida_prezzo_positivo(riga)
    assert risultato is None


def test_log_prezzo_negativo(caplog):
    riga = {"prodotto": "uova", "prezzo": "-3"}

    with caplog.at_level("WARNING"):
        risultato = valida_prezzo_positivo(riga)

    assert risultato is None
    assert "Riga scartata" in caplog.text
    assert "Prezzo negativo" in caplog.text
