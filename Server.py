import socket
import paramiko
import threading
import sys
from colorama import Fore

# Login Credentials 
USERNAME = 'Username'
PASSWORD = 'Password'

# Connection Credentials 
KEY_PATH = '~/Path/to/ssh/key'              # SSH RSA Key path for connection.
SERVER_IP = 'IPAddress'                     # Server IP Address.
PORT = 22                                   # Connection port to the server. 
LISTEN = 100                                # Number of connections the server listen to.

host_key = paramiko.RSAKey(filename=KEY_PATH) # Path to SSH RSA_KEY

class Server(paramiko.ServerInterface):
    def __init__(self) -> None:
        self.event = threading.Event()
    
    # Is called in to server when the client requests a connection channel.
    def check_channel_request(self, ban, chan):  
        if ban == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    # Defines if username & password supplied by client is correct during authentication.
    def check_auth_password(self, username, password):
        if (username == USERNAME) and (password == PASSWORD):  
            return paramiko.AUTH_SUCCESFUL
        return paramiko.AUTH_FAILED
    

try:
    # Allowing to bind an IP address that previously connected and left the socket in TIME_WAIT
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER_IP, PORT)) # Server IP adress, Login port
    sock.listen(LISTEN) # Number of connections the server listen to. 
    print(Fore.YELLOW + 'Listening for connection...')
    client, addr = sock.accept()

except Exception:
    print(Fore.RED + 'Listen/bind/accept failed!') # ???
    sys.exit(1)
print(Fore.GREEN + 'Got a connection!')


try:
    test_client = paramiko.Transport(client)
    test_client.load_server_moduli()
except:
    print('ERROR 1 - Failed to load moduli - gex will be unsupported')
    raise KeyError # maybe key error
test_client.add_server_key(host_key)
server = Server()

try:
    test_client.start_server(server=server)
except paramiko.SSHException:
    print(Fore.RED + 'ERROR 2 - SSH negotitation failed!')


try:
    chan = test_client.accept(20)
    print(Fore.GREEN + 'Authenticated!')
    chan.recv(1024) ## Maybe print or return
    chan.send('Yeah I can see tihs..')
except Exception:
    print(Fore.RED + 'ERROR 3 - Caught exception. Authentication timed out!')


try:
    test_client.close
except:
    pass
sys.exit(1)




    

