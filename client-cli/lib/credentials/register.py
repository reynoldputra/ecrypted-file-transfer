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
    # with open('user_credentials.txt', 'a') as file:
    #     file.write(f'{username}\n{result.hexdigest()}')


    # URL to send the JSON payload to
    url = "http://127.0.0.1:8000/register"

    # Create a dictionary with the values
    data = {
        "user": username,
        "password": password,
        "email": email
    }

    # Convert the dictionary to JSON
    json_data = json.dumps(data)

    # Set the appropriate headers
    headers = {
        "Content-Type": "application/json"
    }

    # Send the POST request with the JSON payload
    response = requests.post(url, data=json_data, headers=headers)

    # Check the response
    if response.status_code == 200:
        typer.echo(f'User "{username}" created succesfully.')
    else:
        typer.echo(f"Request failed with status code: {response.status_code}")

    