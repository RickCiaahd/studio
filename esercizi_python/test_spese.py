from esercizio import *

def test_calcolo_totale():
    lista_mock = [
        {"descrizione": "pane", "importo": 2},
        {"descrizione": "latte", "importo": 1},
        {"descrizione": "caffè", "importo": 3}
    ]
    assert calcolo_totale(lista_mock) == 6

def test_calcolo_media():
    lista_mock = [
        {"descrizione": "pane", "importo": 4},
        {"descrizione": "latte", "importo": 2},
        {"descrizione": "caffè", "importo": 4}
    ]
    media = calcolo_media(lista_mock)
    assert media == 10 /3 

def test_importo_massimo():
    lista_mock = [
        {"descrizione": "pane", "importo": 2},
        {"descrizione": "latte", "importo": 5},
        {"descrizione": "caffè", "importo": 3}
    ]
    massimo = importo_massimo(lista_mock)
    assert massimo == 5

def test_importo_massimo_lista_vuota():
    lista_mock = []
    massimo = importo_massimo(lista_mock)
    assert massimo == 0

def test_spesa_massima():
    lista_mock = [
        {"descrizione": "pane", "importo": 2},
        {"descrizione": "latte", "importo": 5},
        {"descrizione": "caffè", "importo": 3}
    ]
    risultato = spesa_massima(lista_mock)
    assert risultato == {"descrizione": "latte", "importo": 5}

def test_spesa_massima_lista_vuota():
    lista_mock = []
    risultato = spesa_massima(lista_mock)
    assert risultato is None
