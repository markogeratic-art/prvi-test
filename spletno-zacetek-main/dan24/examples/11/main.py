from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Preprost API", description="Preprost API, ki omogoča vpis in pošilja statične datoteke s Swagger dokumentacijo")

# Modeli za zahtevo in odgovor
class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    return_code: int
    message: str

# API funkcije
# Ta primer prikazuje POST zahtevo za prijavo z uporabo Pydantic modelov za validacijo
# Modeli zagotavljajo avtomatsko validacijo vhodnih podatkov in strukturo odgovora
@app.post("/api/login", summary="Prijava", tags=["API"], response_model=LoginResponse)
def login(request: LoginRequest) -> LoginResponse:
    """
    Preveri prijavo uporabnika in vrne status.

    - **request**: Podatki za prijavo (username in password)
    """
    # Preprosta preveritev uporabniškega imena in gesla (v resničnem svetu se uporablja SQL baza in varno shranjevanje gesel)
    if request.username == "admin" and request.password == "secret":
        return LoginResponse(return_code=0, message=f"Logged in successfully. Hello {request.username}!")
    else:
        return LoginResponse(return_code=1, message="Invalid username or password.")

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
