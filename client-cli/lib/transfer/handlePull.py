from lib.crypto.decrypt import decrypt_folder
from lib.helper.cekDir import fileExist
import shutil
import typer
from lib.helper.transfer import scpReverse

def handle_pull(src):
    prv=src+"/.eft/key.pem"
    if not fileExist(prv): 
        return
    
    username = typer.prompt('username')
    password = typer.prompt('password', hide_input=True)
    sessionname = typer.prompt('sessionname')
    scpReverse(f'/home/{username}/eft/{sessionname}/{sessionname}_encrypted', src, username=username, password=password)
    decrypt_folder(f'{src}/{sessionname}_encrypted', prv, src)
    shutil.rmtree(f'{src}/{sessionname}_encrypted')
