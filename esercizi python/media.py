"""
Calcolo della media di una lista di numeri
"""


def media(numeri):
    return sum(numeri) / len(numeri)


def main():
    quanti = int(input("Quanti numeri vuoi inserire? 5"))

    numeri = []
    for i in range(quanti):
        n = float(input(f"Inserisci il numero {i+1}: "))
        numeri.append(n)

    risultato = media(numeri)
    print("La media è:", risultato)


if __name__ == "__main__":
    main()
