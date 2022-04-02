import os
import smtplib

gmail_user = os.environ.get("GMAIL_USER")
gmail_password = os.environ.get("GMAIL_PASSWORD")


def has_mail_enabled():
    return gmail_user and gmail_password


def connect():
    if has_mail_enabled():
        mail_session = smtplib.SMTP('smtp.gmail.com', 587)
        mail_session.helo()
        mail_session.ehlo()
        mail_session.starttls()
        mail_session.login(gmail_user, gmail_password)
        return mail_session


def send_mail(to, subject, body):
    mail_session = connect()
    if mail_session:
        mail_session.sendmail(gmail_user, to, 'Subject: {}\n\n{}'.format(subject, body))
        mail_session.quit()
