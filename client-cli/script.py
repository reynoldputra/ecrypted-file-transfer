from paramiko import SSHClient
import paramiko
from lib.init.initSession import init_session
from scp import SCPClient
import typer
from lib.crypto.decrypt import decrypt_file
from lib.crypto.encrypt import encrypt_file
from lib.credentials.register import register_user
from lib.credentials.login import login_user
from lib.init.initSession import init_session
from lib.init.createKey import create_key
from lib.helper.transfer import scp

app = typer.Typer()

@app.command()
def register(username:str, email:str): 
    register_user(username,email)

@app.command()
def login(username:str):
    login_user(username)

@app.command()
def encrypt(file:str, public_key_file:str):
    encrypt_file(file, public_key_file)

@app.command()
def decrypt(file:str, private_key_file:str):
    decrypt_file(file, private_key_file)

@app.command()
def init(path:str):
    init_session(path)

@app.command()
def generate(path:str):
    create_key(path)

@app.command()
def push(src:str, dest:str):
    scp(src, dest)
if __name__ == "__main__":
    app()

