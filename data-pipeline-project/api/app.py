from fastapi import FastAPI
from etl.db import get_connection

app = FastAPI()


@app.get("/products")
def get_products():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT title, price, category FROM products;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    result = []
    for r in rows:
        result.append({
            "title": r[0],
            "price": float(r[1]),
            "category": r[2]
        })

    return result