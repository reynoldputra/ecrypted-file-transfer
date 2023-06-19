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

def create_remote_ssh(username,password):
    try:
        command = f"./create_user.sh {username} {password}"
        process = subprocess.Popen(command, shell=True)
        process.wait()
    except:
        print("Failed create user")

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/register")
def register(registerDTO: RegisterDTO):
    query = "INSERT INTO user (user, password, email) VALUES (?, ?, ?)"
    dbInsert(query, (registerDTO.user, registerDTO.password, registerDTO.email))
    create_remote_ssh(registerDTO.user, registerDTO.password)
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
