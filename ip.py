"""
To validate the IP address we should follow these steps
Tokenize the string (IP address) using the dot “.” delimiter
If the sub strings are containing any non-numeric character, then return false
If the number in each token is not in range 0 to 255, then return false
If there are exactly three dots and four parts then it is a valid IP address

"""
addr = '127.0.0.1'
addr = '527.0.0.1'
addr = '127.1.0'
addr = '999.999.999.999'


import socket

def is_valid_ip(addr):
    try:
        socket.inet_aton(addr)
        return True
    except ValueError:
        return False


print(is_valid_ip(addr))

########################

import ipaddress

def is_valid_ip(addr):
    try:
        ipaddress.ip_address(addr)
        return True
    except ValueError:
        return False

print(is_valid_ip(addr))

#########################
import re

def is_valid_ip(addr):
    try:
        m = re.match(r"^(\d{1,3}\.){3}\d{1,3}$", addr)
        return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))
    except ValueError:
        return False


print(is_valid_ip(addr))
