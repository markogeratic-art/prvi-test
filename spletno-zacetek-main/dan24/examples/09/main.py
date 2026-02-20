from fastapi import FastAPI, Body, Form
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI(title="Preprost API", description="Preprost API, ki omogoča vpis in pošilja statične datoteke s Swagger dokumentacijo")

# API funkcije
# Ta primer prikazuje POST zahtevo za prijavo, ki sprejme podatke v telesu zahteve
# Uporabljamo Form() za posamezne parametre namesto modela
@app.post("/api/login", summary="Prijava", tags=["API"])
def login(username: str = Form(...), password: str = Form(...)):
    """
    Preveri prijavo uporabnika in vrne status.

    - **username**: Uporabniško ime
    - **password**: Geslo
    """
    # Preprosta preveritev uporabniškega imena in gesla (v resničnem svetu se uporablja SQL baza in varno shranjevanje gesel)
    if username == "admin" and password == "secret":
        color = "green"
        message = f"Logged in successfully. Hello {username}!"
    else:
        color = "red"
        message =  "Invalid username or password."

    return HTMLResponse(content=f"""
    <html>
    <head><title>Rezultat prijave</title></head>
    <body>
    <p style="color: {color};">{message}</p>
    <a href="/">Nazaj</a>
    </body>
    </html>
    """)

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
