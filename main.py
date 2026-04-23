from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from CORe_algorithm import normalize
from CORe_algorithm import run_projectx
import sqlite3
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#DATABASE CONNECTION

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "projectx.db")

def get_db_connection():
    # Opening in Read-Only mode
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn

# ---APP ROUTES ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, subject_code: str = Form(...)):
    # 1. Run the original algorithm
    raw_output = run_projectx(subject_code.upper())
    
    if not raw_output:
        return templates.TemplateResponse("index.html", {"request": request, "results": None, "subject": subject_code.upper()})

    # 2. RESTORE THRESHOLD: Filter out anything below 1.0
    filtered_output = {}
    for part in ["A", "B", "C"]:
        # Only keep questions where score >= 1.0
        filtered_output[part] = [item for item in raw_output.get(part, []) if item['score'] >= 1.0]
            
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "results": filtered_output, 
        "subject": subject_code.upper()
    })