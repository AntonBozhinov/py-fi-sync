import os
import smtplib

from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from email.message import EmailMessage

gmail_user = os.environ.get("GMAIL_USER")
gmail_password = os.environ.get("GMAIL_PASSWORD")


def has_mail_enabled():
    return gmail_user and gmail_password


if has_mail_enabled():
    mail_session = smtplib.SMTP('smtp.gmail.com', 587)
    mail_session.helo()
    mail_session.ehlo()
    mail_session.starttls()
    mail_session.login(gmail_user, gmail_password)

app = FastAPI()
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
templates = Jinja2Templates(directory="templates")

content_dir = os.path.join(os.getcwd(), "uploads")
os.makedirs(content_dir, exist_ok=True)


@app.get("/")
async def root(request: Request):
    file_list = os.listdir(content_dir)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "file_list": file_list
    })


@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    content = file.file.read()
    with open(f"/{content_dir}/{file.filename}", "wb") as f:
        f.write(content)

    if has_mail_enabled():
        msg = EmailMessage()

        msg['Subject'] = 'Pwngotchi Upload'
        msg['From'] = gmail_user
        msg['To'] = gmail_user

        msg.set_content(f"File {file.filename} uploaded")
        mail_session.send_message(msg)
    return {"filename": file.filename}
