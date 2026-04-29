import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="products_db",
        user="postgres",
        password="postgres"
    )


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            price NUMERIC,
            category TEXT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()