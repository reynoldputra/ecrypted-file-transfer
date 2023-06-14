import os
import typer
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from paramiko import SSHClient
import paramiko
from lib.helper.ssh import runCommand
from ..helper.transfer import scp

def init_session(path:str):
    try:
        os.makedirs(path+"/.eft")
        create_key(path)
        username = typer.prompt('username')
        password = typer.prompt('password', hide_input=True)
        sessionname = typer.prompt('session name')
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="localhost", username=username, password=password)
        # runCommand(ssh, f'mkdir /home/{username}/.eft')
        runCommand(ssh, f'mkdir /home/{username}/.eft/{sessionname}')
        runCommand(ssh, f'mkdir /home/{username}/.eft/{sessionname}/.eft')
        runCommand(ssh, f'mkdir /home/{username}/eft')
        runCommand(ssh, f'mkdir /home/{username}/eft/{sessionname}')
        ssh.close()
        scp(path+"/.eft/key.pub" , f'/home/{username}/.eft/{sessionname}/.eft', username=username, password=password)
        typer.echo("Success init session")
    except FileExistsError:
        typer.echo("This folder already have a session")

def save_key_to_file(key_data, file_path):
    with open(file_path, "wb") as file:
        file.write(key_data)

def create_key(path: str):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    save_key_to_file(public_key_pem, path + "/.eft/key.pub")
    save_key_to_file(private_key_pem, path + "/.eft/key.pem")



