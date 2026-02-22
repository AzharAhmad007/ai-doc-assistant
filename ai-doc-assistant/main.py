# main.py

import os
import shutil
from fastapi import FastAPI, UploadFile, File
from rag_pipeline import create_vector_store, ask_question

app = FastAPI()

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    message = create_vector_store(file_path)

    return {"message": message}


@app.get("/ask")
async def ask(query: str):
    answer = ask_question(query)
    return {"answer": answer}