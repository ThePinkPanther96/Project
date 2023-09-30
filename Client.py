import paramiko
from colorama import Fore

server_ip = 'ip address'  # Server IP address
user = 'username'
passwd = 'password'

print(Fore.YELLOW + f"Starting Script...")

client = paramiko.SSHClient()
user
# Automatically adds the hostname and server host key to the local ‘HostKeys’.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the SSH server.
    client.connect(server_ip, username=user, password=passwd)

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
