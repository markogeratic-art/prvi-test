from fastapi import FastAPI
from fastapi.responses import FileResponse

# Ustvarimo FastAPI aplikacijo, ki vsebuje naslov in opis za dokumentacijo
app = FastAPI(title="Preprost API", description="Preprost API, ki pošilja statične datoteke s Swagger dokumentacijo")

# Deklariramo končno točko za GET zahtevo na poti "/", z povzetkom funkcije in oznakami za skupine v dokumentaciji
# V našem primeru prikazujemo vse funkcije v skupini "Datoteke"
@app.get("/", summary="Glavna stran", tags=["Datoteke"])
def read_index():
    # Dokumentacija funkcije, ki se prikaže, ko uporabnik klikne na to funkcijo
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