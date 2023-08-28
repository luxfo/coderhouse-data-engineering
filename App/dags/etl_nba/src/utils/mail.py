import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, SMTP_MAIL_FROM

def send_mail(p_to, p_subject, p_body):
    message = MIMEMultipart()
    message["From"] = SMTP_MAIL_FROM
    message["Subject"] = p_subject
    message.attach(MIMEText(p_body, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.sendmail(SMTP_MAIL_FROM, p_to, str(message))
        smtp.quit()
