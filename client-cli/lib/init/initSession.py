import os
import typer

def init_session(path:str):
    try:
        os.makedirs(path+"/.eft")
        typer.echo("Success init session")
    except FileExistsError:
        typer.echo("This folder already have a session")

