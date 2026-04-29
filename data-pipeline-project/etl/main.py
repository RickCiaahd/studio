from etl.extract import extract_products
from etl.transform import transform_products
from etl.load import save_to_db
from etl.db import create_table


def run_pipeline():
    products = extract_products()
    transformed = transform_products(products)

    create_table()
    save_to_db(transformed)


if __name__ == "__main__":
    run_pipeline()