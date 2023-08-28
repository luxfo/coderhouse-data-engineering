from airflow.decorators import dag, task
from airflow.utils.email import send_email_smtp
from airflow.utils.state import State
from airflow.configuration import conf
from urllib.parse import quote
from datetime import datetime, timedelta
from etl_nba.src.etl import extract_data, transform_data, load_data
from etl_nba.src.config import MAIL_TO
from etl_nba.src.utils import send_mail

default_args = {
    'owner': 'lucianofodrini',
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
}

# Email notification for success or failed dag/task
def notify_email(context):
    ti = context['ti']
    dag_run = context['dag_run']
    var = context['var']['json']
    params = context['params']
    recipient_emails = MAIL_TO

    subject = ""
    body = ""

    if dag_run._state == State.SUCCESS: # Success email
        subject = f"""Airflow: "{dag_run.dag_id}" succeed"""
        body = """
            <p style='color:green'>DAG "{dag_id}" run successfully</p>
            """.format(dag_id=dag_run.dag_id)
    else:
        if ti.state == State.FAILED: # Failed email
            logs_link = '{}/log?dag_id={}&task_id={}&execution_date={}'.format(conf.get("webserver", "base_url"), ti.dag_id, ti.task_id, quote(str(ti.execution_date)))
            subject = f"""Airflow alert: "{dag_run.dag_id}" failed on "{ti.task_id}" """
            body = """
            <p style='color:red'>Task "{task_id}" failed.</p>
            <p>Log: {log_link}</p>
            """.format(task_id=ti.task_id, log_link=logs_link)

    send_mail(p_to=recipient_emails, p_subject=subject, p_body=body)

# Dag
'''
    start_date: date will start being scheduled.
    schedule_interval: how the dag have to run. In this case, daily.
    catchup: if the dag starts processing including past intervals.
    on_success_callback: function to call when dag finish successfully.
'''
@dag(
    dag_id="dag_etl_nba",
    description="procesamiento de datos de la nba (ETL)",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2023, 8, 10),
    catchup=False,
    on_success_callback=notify_email
)
# Flow task of dag
def task_flow_nba():
    # Task to extract data from api
    @task(on_failure_callback=notify_email)
    def get_data():
        data = extract_data()
        return data

    # Task to transform data
    @task(on_failure_callback=notify_email)
    def process_data(p_data):
        dfs = transform_data(p_data)
        return dfs

    # Task to load data to database
    @task(on_failure_callback=notify_email)
    def save_data(p_dfs):
        load_data(p_dfs)

    # Pipeline task dependencies
    data = get_data()
    dfs = process_data(data)
    save_data(dfs)

task_flow_nba()
