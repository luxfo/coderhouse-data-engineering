import smtplib
from email.message import EmailMessage
from ..config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, MAIL_FROM

def send_mail(p_to, p_subject, p_body):
    try:
        message = EmailMessage()
        message["From"] = "Airflow <" + MAIL_FROM + ">"
        message["To"] = ', '.join(p_to)
        message["Subject"] = p_subject
        message.add_header('Content-Type','text/html')
        message.set_payload(p_body)

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASSWORD)
            smtp.send_message(message)
            smtp.quit()
    except Exception as err:
        raise
