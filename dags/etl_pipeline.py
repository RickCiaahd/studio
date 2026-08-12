from datetime import datetime, timezone

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.etl.main import run_pipeline


with DAG(
    dag_id="product_etl_pipeline",
    description="Extract products from a REST API and load them into PostgreSQL",
    start_date=datetime(2024, 1, 1, tzinfo=timezone.utc),
    schedule="@daily",
    catchup=False,
    tags=["etl", "learning-lab"],
) as dag:
    run_etl = PythonOperator(task_id="run_etl", python_callable=run_pipeline)
