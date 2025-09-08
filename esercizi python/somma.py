"""
Programma di esempio con funzione somma.
"""

def somma(a, b):
    """Restituisce la somma di due numeri."""
    return a + b

def main():
    numero1 = int(input("Inserisci il primo numero: "))
    numero2 = int(input("Inserisci il secondo numero: "))

    # Calcola la somma
    risultato = somma(numero1, numero2)
    print("La somma è:", risultato)

if __name__ == "__main__":
    main()