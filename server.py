from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
