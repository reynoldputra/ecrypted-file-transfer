import typer
import hashlib

def register_user(username):
    password = typer.prompt('Enter password: ')
    confirm_password = typer.prompt('Confirm password: ')
    
    if(password != confirm_password):
        typer.echo('Password do not match. User creation failed.')
        return

    encoded_pass = password.encode('utf-8')
    result = hashlib.md5(encoded_pass)
    typer.echo(f'User "{username}" created succesfully.')
    with open('user_credentials.txt', 'a') as file:
        file.write(f'{username}\n{result.hexdigest()}')
