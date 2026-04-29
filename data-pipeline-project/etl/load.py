from etl.db import get_connection


def save_to_db(products):
    conn = get_connection()
    cur = conn.cursor()

    for p in products:
        cur.execute("""
            INSERT INTO products (title, price, category)
            VALUES (%s, %s, %s);
        """, (
            p["title"],
            p["price"],
            p["category"]
        ))

    conn.commit()
    cur.close()
    conn.close()

    print(f"Inserted {len(products)} records into PostgreSQL")