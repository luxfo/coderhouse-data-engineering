from airflow.decorators import dag, task
from airflow.utils.email import send_email_smtp
from airflow.utils.state import State
from airflow.configuration import conf
from urllib.parse import quote
from datetime import datetime, timedelta
from etl_nba.src.etl import extract_data, transform_data, load_data
from etl_nba.src.config import MAIL_TO
from etl_nba.src.utils import send_mail

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
        subject = f"""Airflow OK: "{dag_run.dag_id}" finished successfully"""
        body = """
            <h2>Mail message from Airflow</h2>
            <hr />
            <p>
                DAG: {dag_id}<br>
                Date: {dag_date}<br>
                State: <span style='color:green'>Success</span><br>
            </p>
            """.format(dag_id=dag_run.dag_id, dag_date=dag_run.execution_date)
    else:
        if ti.state == State.FAILED: # Failed email
            logs_link = '{}/log?dag_id={}&task_id={}&execution_date={}'.format(conf.get("webserver", "base_url"), ti.dag_id, ti.task_id, quote(str(ti.execution_date)))
            subject = f"""Airflow ERROR: "{dag_run.dag_id}" failed on "{ti.task_id}" """
            body = """
                <h2>Mail message from Airflow</h2>
                <hr />
                <p>
                    DAG: {dag_id}<br>
                    Task: {task_id}<br>
                    Date: {task_date}<br>
                    State: <span style='color:red'>Failed</span><br>
                    Log: {log_link}
                </p>
                """.format(dag_id=dag_run.dag_id, task_date=ti.execution_date, task_id=ti.task_id, log_link=logs_link)

    send_mail(p_to=recipient_emails, p_subject=subject, p_body=body)

# Dag
''' Default args
    ------------
    owner: creator of de dag.
    retries: number of retries.
    retry_delay: time to try again.
    on_failure_callback: function will be applied to all failed task.
'''
default_args = {
    'owner': 'lucianofodrini',
    'retries': 5,
    'retry_delay': timedelta(seconds=30),
    'on_failure_callback': notify_email
}
''' Parameters
    ----------
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
    @task()
    def get_data():
        data = extract_data()
        return data

    # Task to transform data
    @task()
    def process_data(p_data):
        dfs = transform_data(p_data)
        return dfs

    # Task to load data to database
    @task()
    def save_data(p_dfs):
        load_data(p_dfs)

    # Pipeline task dependencies
    data = get_data()
    dfs = process_data(data)
    save_data(dfs)

task_flow_nba()
