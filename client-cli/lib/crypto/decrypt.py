import typer
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def decrypt_file(encrypted_file: str, private_key_file: str):
    # Load the private key
    with open(private_key_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # Read the contents of the encrypted file
    with open(encrypted_file, "rb") as f:
        encrypted_contents = f.read()

    # Decrypt the file contents
    decrypted_contents = private_key.decrypt(
        encrypted_contents,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Write the decrypted contents to a new file
    decrypted_file = f"{encrypted_file}.decrypted"
    with open(decrypted_file, "wb") as f:
        f.write(decrypted_contents)

    typer.echo(f"File '{encrypted_file}' decrypted successfully. Decrypted file: '{decrypted_file}'.")
