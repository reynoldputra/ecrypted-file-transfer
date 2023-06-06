import typer
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def encrypt_file(file: str, public_key_file: str):
    # Load the public key
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    # Read the contents of the file
    with open(file, "rb") as f:
        contents = f.read()

    # Encrypt the file contents
    encrypted_contents = public_key.encrypt(
        contents,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Write the encrypted contents to a new file
    encrypted_file = f"{file}.encrypted"
    with open(encrypted_file, "wb") as f:
        f.write(encrypted_contents)

    typer.echo(f"File '{file}' encrypted successfully. Encrypted file: '{encrypted_file}'.")
