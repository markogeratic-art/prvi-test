from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# Serve index.html
@app.get("/")
def read_index():
    return FileResponse("index.html")

# Serve JavaScript
@app.get("/scripts.js")
def read_js():
    return FileResponse("scripts.js")

# Serve CSS
@app.get("/style.css")
def read_css():
    return FileResponse("style.css")