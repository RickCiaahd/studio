import pytest
from esercizi_python.calcolatrice import analizza_lista

def test_analizza_lista():
    numeri = [5, 2, 8, 1, 10]
    risultato = analizza_lista(numeri)
    assert risultato == {
        "min": 1,
        "max": 10,
        "media": 5.2
    }

def test_analizza_lista_vuota():
    with pytest.raises(ValueError):
        analizza_lista([])

@pytest.mark.parametrize(
    "input_lista, risultato_atteso",
    [
        ([1, 2, 3], {"min": 1, "max": 3, "media": 2}),
        ([10, 10, 10], {"min": 10, "max": 10, "media": 10}),
        ([5, 2, 8, 1, 10], {"min": 1, "max": 10, "media": 5.2}),
    ]
)
def test_analizza_lista_parametrico(input_lista, risultato_atteso):
    assert analizza_lista(input_lista) == risultato_atteso