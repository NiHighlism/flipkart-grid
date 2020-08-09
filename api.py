from typing import List

from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from manage import Manager

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/upload/")
async def create_upload_files(files: List[UploadFile] = File(...)):
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

    return {"transcripts": transcript}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})
