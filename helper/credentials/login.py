import typer
import hashlib
import re

def login_user(username):
    password = typer.prompt('Enter password: ')
    encoded_pass = password.encode('utf-8')
    hash_pass = hashlib.md5(encoded_pass)
    file_path = 'user_credentials.txt'
    with open(file_path, 'r') as file:
        content = file.read()
        pattern = f'{username}\n{hash_pass.hexdigest()}'
        match = re.search(pattern, content)
        if match:
            print(f'Welcome {username}')
            return True
        else:
            print("Unknown user")
            return False
