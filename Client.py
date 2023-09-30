import paramiko
from colorama import Fore

SERVER_IP = '192.168.1.50'  # Server IP address
USERNAME = 'ubuntu'
PASSWORD = 'Gr24091996*'
PORT = 2224

print(Fore.YELLOW + f"Starting Script...")

client = paramiko.SSHClient()

# Automatically adds the hostname and server host key to the local ‘HostKeys’.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the SSH server.
    client.connect(SERVER_IP, port=PORT, username=USERNAME, password=PASSWORD)

    # Open a session channel.
    chan = client.get_transport().open_session()

    # Send a message to the server.
    chan.send(Fore.GREEN + 'Hey I`m connected 🙂')

    # Receive data from the server and print it.
    data = chan.recv(1024)
    print(data.decode('utf-8'))
    
finally:
    # Close the SSH client.
    client.close()
