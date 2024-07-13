import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from celery_config import celery


@celery.task
def send_email(email):
    # Email content
    msg = MIMEText('This is a test email.')
    msg['Subject'] = 'Test Email'
    msg['From'] = 'princesamuel619@gmail.com'
    msg['To'] = email

    # Gmail SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'princesamuel619@gmail.com'
    smtp_password = 'mwcj crms uefj ljsc'

    # Sending email using Gmail's SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(smtp_user, smtp_password)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

@celery.task
def log_time():
    try:
        with open('/var/log/messaging_system.log', 'a') as log_file:
            log_file.write(f"{datetime.now()}\n")
    except Exception as e:
        print(f"Error logging time: {e}")