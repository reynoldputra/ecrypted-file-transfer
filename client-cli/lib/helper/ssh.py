def runCommand(ssh, command):
    # Execute the mkdir command to create a new directory
    stdin, stdout, stderr = ssh.exec_command(command)

    # Check the output for any errors
    error = stderr.read().decode().strip()
    if error:
        print(f"Error occurred : {error}")
    else:
        print(f"Command success")

