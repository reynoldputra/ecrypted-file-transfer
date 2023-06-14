import os
import typer
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def decrypt_file(encrypted_file: str, private_key_file: str, output_dir: str):
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

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write the decrypted contents to a new file in the output directory
    decrypted_file = os.path.join(output_dir, f"{os.path.basename(encrypted_file)}")
    with open(decrypted_file, "wb") as f:
        f.write(decrypted_contents)



def decrypt_folder(encrypted_folder: str, private_key_file: str, output_dir: str):
    # Load the private key
    with open(private_key_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all files in the encrypted folder
    for root, dirs, files in os.walk(encrypted_folder):
        relative_root = os.path.relpath(root, encrypted_folder)  # Get the relative path of the current root folder
        output_root = os.path.join(output_dir, relative_root)  # Create the corresponding output directory
        os.makedirs(output_root, exist_ok=True)  # Create the output directory if it doesn't exist

        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, private_key_file, output_root)

    typer.echo(f"Folder '{encrypted_folder}' decrypted successfully.")

