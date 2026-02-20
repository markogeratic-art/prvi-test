from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="Preprost API", description="Preprost API, ki pošilja statične datoteke s Swagger dokumentacijo")

# API funkcije
@app.get("/api/hello", summary="Pozdrav", tags=["API"])
def hello():
    """
    Vrne pozdravni sporočilo.
    """
    return {"message": "Pozdrav iz FastAPI!"}

# Funkcije za pošiljanje datotek
@app.get("/", summary="Glavna stran", tags=["Datoteke"])
def read_index():
    """
    Vrne HTML datoteko za domačo stran aplikacije.
    """
    return FileResponse("index.html")

@app.get("/script.js", summary="JavaScript datoteka", tags=["Datoteke"])
def read_js():
    """
    Vrne script.js datoteko, ki vsebuje logiko na strani odjemalca.
    """
    return FileResponse("script.js")

@app.get("/style.css", summary="CSS datoteka", tags=["Datoteke"])
def read_css():
    """
    Vrne style.css datoteko za oblikovanje aplikacije.
    """
    return FileResponse("style.css")
