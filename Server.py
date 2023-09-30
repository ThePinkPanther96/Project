import socket
import paramiko
import threading
import sys
from colorama import Fore

print(Fore.YELLOW + f"Starting Script...")

# Login Credentials (Replace with actual values)
USERNAME = 'username'
PASSWORD = 'password'

# Connection Credentials (Replace with actual values)
KEY_PATH = '/etc/ssh/ssh_host_rsa_key'     # SSH RSA Key path for connection.
SERVER_IP = 'IP Address'                   # Server IP Address.
PORT = 22                                  # Connection port to the server.
LISTEN = 5                                 # Number of connections the server listens to.

host_key = paramiko.RSAKey(filename=KEY_PATH)  # Path to SSH RSA_KEY

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == USERNAME and password == PASSWORD:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

try:
    # Create a socket and bind to the server address and port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER_IP, PORT))
    sock.listen(LISTEN)
    print(Fore.YELLOW + 'Listening for connections...')
    client, addr = sock.accept()
except Exception as e:
    print(Fore.RED + f'Listen/bind/accept failed: {str(e)}')
    sys.exit(1)

print(Fore.GREEN + 'Got a connection!')

try:
    transport = paramiko.Transport(client)
    transport.load_server_moduli()
    transport.add_server_key(host_key)
    server = Server()

    transport.start_server(server=server)

    # Accept an SSH channel within a timeout.
    chan = transport.accept(20)
    if chan:
        print(Fore.GREEN + 'Authenticated!')
        data = chan.recv(1024).decode('utf-8')
        print(Fore.WHITE + f'Received data from client: {data}')
        chan.send(Fore.GREEN + f'Yeah, I can see this...'.encode('utf-8'))
        chan.close()
    else:
        print(Fore.RED + 'Authentication timed out!')
except paramiko.SSHException as e:
    print(Fore.RED + f'SSH negotiation failed: {str(e)}')
finally:
    try:
        transport.close()
    except Exception:
        pass
    sys.exit(0)
