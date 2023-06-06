from fastapi import FastAPI
from pydantic import BaseModel

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

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/register")
def register(registerDTO : RegisterDTO):
    return {"Hello": "World"}

@app.post("/login")
def login(loginDTO : LoginDTO):
    return {"Hello": "World"}

@app.post("/invite/add")
def createInvitatioin(inviteDTO : InviteDTO):
    return {"Hello": "World"}

@app.get("/invite")
def getInvitation():
    return {"Hello": "World"}

@app.post("/invite/accept")
def acceptInvitation():
    return {"Hello": "World"}

