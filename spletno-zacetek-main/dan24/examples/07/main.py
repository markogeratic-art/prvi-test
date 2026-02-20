from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="Preprost API", description="Preprost API, ki pošilja statične datoteke s Swagger dokumentacijo")

# API funkcije
# Ta končna točka prikazuje mešanje parametrov poti (name) in parametrov poizvedbe (greeting)
@app.get("/api/hello/{name}", summary="Sporočilo", tags=["API"])
# Name je obvezen parameter iz poti, medtem ko je greeting opcijski parameter poizvedbe z privzeto vrednostjo praznega niza
def hello(name: str, greeting: str = ""):
    """
    Vrne sporočilo z imenom iz poti in opcijskim dodatkom iz poizvedbe.

    - **name**: Ime osebe (iz poti, obvezno)
    - **greeting**: Dodatni tekst sporočila (iz poizvedbe, privzeto prazno)
    """
    return {"message": f"Zdravo, {name}. {greeting}"}

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
