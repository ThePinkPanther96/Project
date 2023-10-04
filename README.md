# Creating a custom SSH backdoor in Python
## Introduction
During my time as a System Administrator, I was also in charge of hardening and maintaining the organizational security infrastructure. In an effort to raise cybersecurity awareness among my co-workers and combat phishing and malware attempts, I decided to write two simple scripts in Python, utilizing the Paramiko module. These two scripts, the server and client, establish an SSH connection between them. When the server-side script is executed, it begins listening for SSH connections as configured in both scripts. Once the client script is executed, it instantly connects to the server, opening an SSH backdoor that allows an attacker to execute commands on the victim's machine. I used these scripts within the organizational network, running 10-15 server scripts simultaneously, and sending the client scripts disguised as PDF files from non-organizational email addresses to random email accounts within the company, to see who downloaded the file and would attempt to open it.

## Environment
### Attack Server
- IP Address: 192.168.1.50
- OS: Ubuntu Server 22.04 LTS
- Python Version: 3.11
- PInstalled libraries: Pramiko, Colorama

### Victim Machine
- IP Address: 192.168.1.113
- OS: Windows 10 Pro

## Attack Server Side
1. If Python 3 isn't installed, install it:
   ```
    apt-get install -y python3
   ```
2. Install pip3:
   ```
   sudo apt-get update -y
   apt-get install -y python3-pip
   ```
3. Install Paramiko and Colorama libraries:
   ```
   pip3 install colorama paramiko
   ```
4. Create a user and password to be used for the backdoor SSH connection:
   ```
   useradd <username>
   passwd <unsername>
   ```
5. Set SSH password authentication for the new user:
   ```
   ssh -o PasswordAuthentication=yes <username>@<IP address>
   ```
6. Create a new Python file and upload the server script:
   ```
   vi python.py
   ```
7. Fill in the following parameters according to your specifications:
   ```
   # Login Credentials (Replace with actual values)
   USERNAME = 'username'
   PASSWORD = 'password'
   
   # Connection Credentials (Replace with actual values)
   KEY_PATH = '/etc/ssh/ssh_host_rsa_key'  # SSH RSA Keypath for connection.
   SERVER_IP = 'ip address'                # Server IP Address.
   PORT = 22                               # Connection port to the server.
   LISTEN = 5                              # Number of connections the server listens to.
   ```
   *NOTE!* To avoid occupying port 22 use a different port. In my case, I used port 2222.
   If you get this error when executing the server script:
   ```sh
   Listen/bind/accept failed: [Errno 98] Address already in use
   ```
   
   Restart the sshd service:
   ```
   service ssh restart
   ```
   
   If you do want to use port 22 you can try stopping the sshd service:
   ```
   service sshd stop
   ```
8. 
