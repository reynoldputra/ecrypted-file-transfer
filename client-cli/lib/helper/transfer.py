from scp import SCPClient
import typer
from paramiko import SSHClient
import paramiko

def scp(src, dest, username=None, password=None):
    hostname = 'localhost'
    if username is None:
        username = typer.prompt('username')
    if password is None:
        password = typer.prompt('password', hide_input=True)

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)

    scp = SCPClient(ssh.get_transport())
    scp.put(src, recursive=True, remote_path=dest)
    scp.close()

def scpReverse(src, dest, username=None, password=None):
    hostname = 'localhost'
    if username is None:
        username = typer.prompt('username')
    if password is None:
        password = typer.prompt('password', hide_input=True)

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)

    scp = SCPClient(ssh.get_transport())
    scp.get(local_path=dest, recursive=True, remote_path=src)
    scp.close()
