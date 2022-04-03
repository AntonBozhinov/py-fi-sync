import os

from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from mail import send_mail, gmail_user

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
async def upload_file(file: UploadFile):
    content = file.file.read()
    with open(f"/{content_dir}/{file.filename}", "wb") as f:
        f.write(content)

    send_mail(gmail_user, "File Uploaded", f"{file.filename}")
    return {"filename": file.filename}
