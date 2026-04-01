import requests
import pandas as pd

def estrai_prodotti():

    response = requests.get("https://dummyjson.com/products", timeout=5)
    if response.status_code != 200:
        raise Exception(f"Errore API: {response.status_code} - {response.text[:100]}")
    
    try:
        return response.json()["products"]
    except ValueError:
        raise Exception("Risposta non valida (non JSON)")

def genera_report_categorie(df):
    df_report = df.groupby('category') \
       .agg({'title':'size', 'price':'mean'}) \
       .rename(columns={'title':'numero_prodotti','price':'prezzo_medio'}) \
       .reset_index()
    
    return df_report


if __name__ == "__main__":
    df = pd.DataFrame(estrai_prodotti())
    df = df[["title","price", "category"]]
    df_report = genera_report_categorie(df)
    print(df_report)