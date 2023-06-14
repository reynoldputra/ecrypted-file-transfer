from lib.helper.cekDir import fileExist
from lib.crypto.encrypt import encrypt_folder
import os
import shutil
import typer
from lib.helper.transfer import scp

def handle_push(src):
    prv=src+"/.eft/key.pub"
    if not fileExist(prv): 
        return
    
    username = typer.prompt('username')
    password = typer.prompt('password', hide_input=True)
    sessionname = typer.prompt('sessionname')
    temp = os.path.join(os.path.abspath(src), f'../{sessionname}_encrypted')
    encrypt_folder(src, prv, temp)
    scp(temp, f'/home/{username}/eft/{sessionname}', username=username, password=password)
    shutil.rmtree(temp)
