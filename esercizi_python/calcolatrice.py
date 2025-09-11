def analizza_lista(numeri):
    if not numeri:
        raise ValueError("La lista è vuota.")

    minimo = min(numeri)
    massimo = max(numeri)
    media = sum(numeri) / len(numeri)
    
    return {
        "min": minimo,
        "max": massimo,
        "media": media
    }
