import typer
from helper.crypto.decrypt import decrypt_file
from helper.crypto.encrypt import encrypt_file

app = typer.Typer()

@app.command()
def encrypt(file: str, public_key_file: str):
    encrypt_file(file, public_key_file)

@app.command()
def decrypt(file: str, private_key_file: str):
    decrypt_file(file, private_key_file)

if __name__ == "__main__":
    app()

