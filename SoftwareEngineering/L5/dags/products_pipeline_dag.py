import json
from datetime import timedelta

import pandas as pd
import requests

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook


API_URL = "https://fakestoreapi.com/products"
LOCAL_FILE_PATH = "/opt/airflow/data/products_data.json"
PARQUET_FILE_PATH = "/opt/airflow/data/products.parquet"


class FailedToGetData(Exception): ...


def get_data_from_api() -> None:
    """Get data from FakeProducts"""

    response = requests.get(API_URL)
    if response.status_code == 200:
        products_data = response.json()
        with open(LOCAL_FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(products_data, file)
    else:
        raise FailedToGetData(f"Error fetching data from FakeProducts API: {response.status_code}")


def save_data() -> None:
    """Save data to parquet-file"""

    processed_df = pd.read_json(LOCAL_FILE_PATH)
    processed_df.to_parquet(PARQUET_FILE_PATH)


def insert_data_to_postgres() -> None:
    """Save data to Postgres"""

    df = pd.read_json(LOCAL_FILE_PATH)

    hook = PostgresHook(postgres_conn_id="pg_products")
    conn = hook.get_conn()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            f"""
            INSERT INTO products
            (id, title, description, price, reviews_count, rating)
            VALUES (
                {row["id"]},
                '{row["title"].replace("'", "`")}',
                '{row["description"].replace("'", "`")}',
                {row["price"]},
                {row["rating"]["count"]},
                {row["rating"]["rate"]}
            );
        """
        )

    conn.commit()
    cursor.close()
    conn.close()


with DAG(
    "products_pipeline_dag",
    default_args={
        "depends_on_past": False,
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=2),
        "start_date": days_ago(1),
    },
    description="A products data pipeline from FakeProducts API",
    # schedule_interval="@daily",
    # schedule_interval="0 0 * * *",
    schedule_interval="0 21 * * *",
    catchup=False,
    tags=["products"],
) as dag:
    get_data_from_api_task = PythonOperator(task_id="get_data_from_api", python_callable=get_data_from_api)
    save_data_task = PythonOperator(task_id="save_data", python_callable=save_data)
    insert_to_db_task = PythonOperator(task_id="insert_to_db", python_callable=insert_data_to_postgres)
    create_products_table_task = PostgresOperator(
        task_id="create_products_table",
        postgres_conn_id="pg_products",
        sql="""
            CREATE TABLE IF NOT EXISTS products (
                id INT,
                title VARCHAR(256),
                description VARCHAR(2048),
                price DECIMAL(10, 2),
                reviews_count INT,
                rating DECIMAL(10, 2)
            );
        """,
    )

[get_data_from_api_task, create_products_table_task] >> save_data_task >> insert_to_db_task
