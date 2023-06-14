import os
import typer
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def encrypt_file(file: str, public_key_file: str, output_dir: str):
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

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write the encrypted contents to a new file in the output directory
    encrypted_file = os.path.join(output_dir, f"{os.path.basename(file)}")
    with open(encrypted_file, "wb") as f:
        f.write(encrypted_contents)

    typer.echo(f"File '{file}' encrypted successfully. Encrypted file: '{encrypted_file}'.")


def encrypt_folder(folder: str, public_key_file: str, output_dir: str):
    # Load the public key
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder):
        relative_root = os.path.relpath(root, folder)  # Get the relative path of the current root folder
        output_root = os.path.join(output_dir, relative_root)  # Create the corresponding output directory
        os.makedirs(output_root, exist_ok=True)  # Create the output directory if it doesn't exist

        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, public_key_file, output_root)

    typer.echo(f"Folder '{folder}' encrypted successfully.")
