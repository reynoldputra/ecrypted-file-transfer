import typer
import hashlib
import requests
import json


def register_user(username,email):
    password = typer.prompt('Enter password: ')
    confirm_password = typer.prompt('Confirm password: ')
    
    if(password != confirm_password):
        typer.echo('Password do not match. User creation failed.')
        return

    encoded_pass = password.encode('utf-8')
    result = hashlib.md5(encoded_pass)
    
    url = "http://127.0.0.1:8000/register"

    data = {
        "user": username,
        "password": password,
        "email": email
    }

    json_data = json.dumps(data)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json_data, headers=headers)
    if response.status_code == 200:
        typer.echo(f'User "{username}" created succesfully.')
    else:
        typer.echo(f"Request failed with status code: {response.status_code}")

    
