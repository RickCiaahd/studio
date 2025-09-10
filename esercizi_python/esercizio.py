"""
Costruire un piccolo menù interattivo con più opzioni e logica strutturata in funzioni.
"""

import os


def carica_da_file():
    lista_spesa = []
    if os.path.exists("spese.txt"):
        with open("spese.txt", "r") as f:
            for riga in f:
                dati = riga.strip().split(",")
                if len(dati) == 2:
                    descrizione = dati[0]
                    try:
                        importo = int(dati[1])
                        lista_spesa.append(
                            {"descrizione": descrizione, "importo": importo}
                        )
                    except ValueError:
                        print(f"Valore non valido per importo: {dati[1]}")
    else:
        print("Nessun file di spese trovato.")
    return lista_spesa


def popola_spesa(spese):
    descrizione = input("Inserisci descrizione: ")
    importo = int(input("Inserisci importo: "))
    spesa = {
        "descrizione": descrizione,
        "importo": importo,
    }
    spese.append(spesa)


def popola_lista():
    spese = []
    numspese = int(input("Quante spese vuoi aggiungere? "))
    for i in range(numspese):
        popola_spesa(spese)
    return spese


def calcolo_totale(lista_spesa):
    totale = 0
    if len(lista_spesa) == 0:
        print("La lista è vuota, inserisci degli elementi con il comando 1")
        return 0
    for spesa in lista_spesa:
        totale = totale + spesa["importo"]
    return totale


def calcolo_media(lista_spesa):
    if len(lista_spesa) == 0:
        print("La lista è vuota, inserisci degli elementi con il comando 1")
        return 0
    return calcolo_totale(lista_spesa) / len(lista_spesa)


def mostra_lista(lista_spesa):
    if len(lista_spesa) == 0:
        print("La lista è vuota, inserisci degli elementi con il comando 1")
    else:
        for spesa in lista_spesa:
            print(f"Descrizione: {spesa['descrizione']} | Importo: €{spesa['importo']}")


def menu(comando, lista_spesa):
    if comando == 1:
        lista_spesa = popola_lista()
    elif comando == 2:
        mostra_lista(lista_spesa)
    elif comando == 3:
        print(f"Il totale delle spese è: €{calcolo_totale(lista_spesa):.2f}")
    elif comando == 4:
        print(f"La media delle spese è: €{calcolo_media(lista_spesa):.2f}")
    elif comando == 5:
        salva_su_file(lista_spesa)
    elif comando == 6:
        print("Uscita dal programma.")
        exit()
    else:
        print("Comando non valido.")
    return lista_spesa


def salva_su_file(lista_spesa):
    with open("spese.txt", "w") as f:
        for spesa in lista_spesa:
            descrizione = spesa["descrizione"]
            importo = spesa["importo"]
            f.write(f"{descrizione},{importo}\n")
    print("Spese salvate su file.")


def importo_massimo(lista_spesa):
    if not lista_spesa:
        return 0
    return max(spesa["importo"] for spesa in lista_spesa)


def spesa_massima(lista_spesa):
    if not lista_spesa:
        return None
    return max(lista_spesa, key=lambda spesa: spesa["importo"])



def main():
    lista_spesa = carica_da_file()

    while True:
        comando = int(
            input(
                "Inserisci comando:"
                + "\n"
                + "1. Aggiungi spesa"
                + "\n"
                + "2. Mostra tutte le spese"
                + "\n"
                + "3. Calcola totale"
                + "\n"
                + "4. Calcola media"
                + "\n"
                + "5. Salva spese su file"
                + "\n"
                + "6. Esci"
                + "\n"
            )
        )
        lista_spesa = menu(comando, lista_spesa)


if __name__ == "__main__":
    main()
