from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def print_message() -> None:
    print("Hello Python World")


with DAG(
    "task_1_dag",
    description="",
    schedule=None,
    start_date=days_ago(1),
    tags=["task_1"],
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
) as dag:
    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="echo Hello Bash World",
    )

    python_task = PythonOperator(
        task_id="python_task",
        python_callable=print_message,
    )


[bash_task, python_task]
