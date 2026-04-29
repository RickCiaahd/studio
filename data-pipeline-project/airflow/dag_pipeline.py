import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.main import run_pipeline


def run_etl():
    run_pipeline()


with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )

    etl_task