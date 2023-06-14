from paramiko import SSHClient
import paramiko
from scp import SCPClient
import typer
from lib.crypto.decrypt import decrypt_file
from lib.crypto.encrypt import encrypt_file
from lib.credentials.register import register_user
from lib.credentials.login import login_user

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
def send():
    hostname = '172.31.0.4'
    username = 'root'
    password = 'password'
    # local_path = './requirements.txt'
    # remote_path = '/home/requirements.txt'
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)

    scp = SCPClient(ssh.get_transport())
    scp.put('requirements.txt', recursive=True, remote_path='/home')
    scp.close()

if __name__ == "__main__":
    app()

