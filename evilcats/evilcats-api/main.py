from fastapi import FastAPI, Request, UploadFile, HTTPException, status, Query, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from zipfile import ZipFile
from typing import List, Annotated
import os

#python -m uvicorn main:app --reload 
# to run the server

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Hello World"}    

@app.get("/catpic/", response_class=HTMLResponse)
async def catpic(request: Request):
    images = os.listdir("./static/cats")
    return templates.TemplateResponse("catpic.html.j2",{"request": request, "images":images })

@app.post("/catpics/addpics/")
async def add_cat_pic(file: UploadFile):
    try:
        zip = ZipFile(file.file)
        for sub_file in zip.namelist():
            if sub_file.endswith('.jpg') or sub_file.endswith('.jpeg') or sub_file.endswith('.png'):
                zip.extract(sub_file,'./static/')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Item not found")
    return status.HTTP_201_CREATED