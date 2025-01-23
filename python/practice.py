# Check if port is open on a given domain

"""

import socket

domain = input('Enter domain: ')
port = int(input('Enter port: '))

def port_open(domain, port):
    # chech if a port is open on a given host
    try:
        sock = socket.create_connection((domain, port), timeout=5)
        sock.close()
        return True
    except (socket.error, socket.timeout):
        return False
    
print(port_open(domain, port))

"""


# Get your public IP address

"""

import requests
#url = input('Enter domain: ')  # example: api.ipify.org
def get_public_ip():
    # get the public IP address of a domain
    try:
        ip = requests.get(f"https://api.ipify.org?format=json")
        ip.raise_for_status()
        return ip.json()["ip"]
    except requests.exceptions.RequestException as e:
        print(f"Error getting Ip: {e}")
        return None
    
print(get_public_ip())

"""


# Find files with a given extension in a directory

import os

