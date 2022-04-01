import os

from fastapi import FastAPI, UploadFile

app = FastAPI()

content_dir = os.path.join(os.getcwd(), "uploads")
os.makedirs(content_dir, exist_ok=True)


@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    content = file.file.read()
    with open(f"/{content_dir}/{file.filename}", "wb") as f:
        f.write(content)
    return {"filename": file.filename}
