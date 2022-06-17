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
    user  = {}
    message = "User Not Found"
    lengthOfUserData = len(userData)
    for i in range(lengthOfUserData):
        if userData[i].id == userId:
            user = userData[i]
            message = "User Found"
            break


    return {"data": user, "message": message }


@app.post("/search")
def read_item(q: str):
    return {"results": [{}] }    