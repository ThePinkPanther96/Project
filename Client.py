import paramiko
from colorama import Fore
import threading

SERVER_IP = 'IPAddress' # Server IP address
USERNAME = 'root'
PASSWORD = 'Gr24091996*'

client = paramiko.SSHClient()

# Automatically adds the hostname and server host key to the local ‘HostKeys’.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # maybe no nedd for ()

# Requests a new channel of type ‘session’ from the server (
client.connect(str(SERVER_IP, username=USERNAME, password=PASSWORD))

chan = client.get_transport().open_session()
chan.send(Fore.GREEN + 'Hey I`m connected 🙂')
chan.recv(1024)

client.close()