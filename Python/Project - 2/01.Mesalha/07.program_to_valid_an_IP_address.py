#NABEGHEHA.COM

import socket
addr = '127.0.0.256'
try:
    socket.inet_aton(addr)
    print("valid iP")
except socket.error:
    print("invalid iP")