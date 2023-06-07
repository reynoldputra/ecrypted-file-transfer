import typer
import hashlib
import requests
import json



def login_user(username):
    password = typer.prompt('Enter password: ')
    encoded_pass = password.encode('utf-8')
    hash_pass = hashlib.md5(encoded_pass)
    file_path = 'user_credentials.txt'
    # with open(file_path, 'r') as file:
    #     content = file.read()
    #     pattern = f'{username}\n{hash_pass.hexdigest()}'
    #     match = re.search(pattern, content)
    #     if match:
    #         print(f'Welcome {username}')
    #         return True
    #     else:
    #         print("Unknown user")
    #         return False

    url = "http://127.0.0.1:8000/login"

    # Create a dictionary with the values
    data = {
        "user": username,
        "password": password
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
        typer.echo(f'User "{username}" login succesfully.')
    else:
        typer.echo(f"Request failed with status code: {response.status_code}")

    