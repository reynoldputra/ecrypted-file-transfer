import typer
from paramiko import SSHClient
import paramiko

from lib.helper.transfer import scpReverse

def get_session(path):
    username = typer.prompt('username')
    password = typer.prompt('password', hide_input=True)
    sessionname = typer.prompt('session name')
    scpReverse(f'/home/{username}/.eft/{sessionname}', path, username=username, password=password)
