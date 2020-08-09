from typing import List

from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from manage import Manager

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/upload/", response_class=HTMLResponse)
async def create_upload_files(request: Request, files: List[UploadFile] = File(...)):
    filenames = [file.filename for file in files]

    if not filenames[0]:
        raise HTTPException(
            status_code=400, detail="Please select a file to upload!")

    audio = await files[0].read()
    manager = Manager(audio)

    manager.convert_audio()
    manager.denoise_input()
    manager.separate()
    
    transcript = manager.create_transcript()

    return templates.TemplateResponse("index.html",
        {'request': request,
        'en_transcript': transcript["transcriptions"][0]["utf_text_en"],
        'hi_transcript': transcript["transcriptions"][0]["utf_text"]
        })


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

