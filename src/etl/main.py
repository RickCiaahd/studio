import logging

from src.etl.db import create_table
from src.etl.extract import extract_products
from src.etl.load import save_to_db
from src.etl.transform import transform_products

LOGGER = logging.getLogger(__name__)


def run_pipeline() -> int:
    """Run the REST API to PostgreSQL ETL pipeline."""
    LOGGER.info("Starting product ETL pipeline")
    products = extract_products()
    transformed_products = transform_products(products)
    create_table()
    inserted_count = save_to_db(transformed_products)
    LOGGER.info("Product ETL pipeline completed")
    return inserted_count


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    run_pipeline()
