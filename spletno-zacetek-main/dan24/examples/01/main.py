from fastapi import FastAPI
import random
from pydantic import StrictInt, StrictFloat
from typing import Union


app = FastAPI()

@app.get("/random")
def sarma(min: int = 0, max: int = 100):
    return{"random" : random.randint(min,max)}


@app.get("/podvoji/")
def podvoji(stevilo: Union[int, float]):
    # FastAPI bo samodejno zavrnil stringe in vrnil 422 Error
    rezultat = stevilo * 2
    return {
        "vnos": stevilo,
        "rezultat": rezultat,
        "tip": type(stevilo).__name__
    }


app = FastAPI()

@app.get("/podvoji/{stevilo}")
def podvoji(stevilo: int):
    return {"rezultat": stevilo * 2}


def read_root():
    return {"message": "Pozdrav iz FastAPI!"}