from fastapi import FastAPI
from pydantic import BaseModel
from database.database import dbCreate, dbGet, dbInsert,dbGetColumn
import sqlite3


app = FastAPI()
class LoginDTO(BaseModel):
    user: str;
    password: str;

class RegisterDTO(BaseModel):
    user: str;
    password: str;
    email: str;

class InviteDTO(BaseModel):
    fromUser: str;
    toUser: str;
    password: str;

connection = sqlite3.connect("db.sqlite3")

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/register")
def register(registerDTO: RegisterDTO):
    query = "INSERT INTO user (user, password, email) VALUES (?, ?, ?)"
    dbInsert(query, (registerDTO.user, registerDTO.password, registerDTO.email))
    return {"message": "User registered successfully"}

@app.post("/login")
def login(loginDTO: LoginDTO):
    query = "SELECT * FROM user WHERE user = ? AND password = ?"
    rows = dbGetColumn(query, (loginDTO.user, loginDTO.password))
    user = rows[0] if rows else None
    if user:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}

@app.post("/invite/add")
def createInvitatioin(inviteDTO : InviteDTO):
    return {"Hello": "World"}

@app.get("/invite")
def getInvitation():
    return {"Hello": "World"}

@app.post("/invite/accept")
def acceptInvitation():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
