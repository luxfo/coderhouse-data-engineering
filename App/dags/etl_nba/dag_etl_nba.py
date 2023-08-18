from airflow.decorators import dag, task
from datetime import datetime, timedelta
from etl_nba.src.etl import extract_data, transform_data, load_data

default_args = {
    'owner': 'lucianofodrini',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

@dag(
    dag_id= "dag_etl_nba",
    description= "procesamiento de datos de la nba (ETL)",
    default_args= default_args,
    schedule_interval= "@daily",
    start_date= datetime(2023, 8, 10),
    catchup= False,
)
def task_flow_nba():
    @task()
    def get_data():
        data = extract_data()
        return data

    @task()
    def process_data(p_data):
        dfs = transform_data(p_data)
        return dfs

    @task()
    def save_data(p_dfs):
        load_data(p_dfs)

    data = get_data()
    dfs = process_data(data)
    save_data(dfs)

task_flow_nba()
