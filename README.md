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
    apt install python3
   ```
   
