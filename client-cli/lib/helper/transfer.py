from scp import SCPClient
import typer
from paramiko import SSHClient
import paramiko

def scp(src, dest):
    hostname = 'localhost'
    username = typer.prompt('username')
    password = typer.prompt('password', hide_input=True)

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    scp = SCPClient(ssh.get_transport())
    scp.put(src, recursive=True, remote_path=dest)
    scp.close()
