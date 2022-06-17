from typing import Union, Optional

from fastapi import FastAPI

from model.data import userData

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/version")
def version():
    return {"version":"one"}

@app.get("/users")
def getUsers():
    return{"data":userData}

@app.get("/user/{userId}")
def getSpecificUser(userId: int):
    return {"data":{} }


@app.post("/search")
def read_item(q: str):
    return {"results": [{}] }    