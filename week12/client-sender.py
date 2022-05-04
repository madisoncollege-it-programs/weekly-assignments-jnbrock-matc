#!/usr/bin/env python3

#Testing sending data to a listener.

import socket


RHOST    = "127.0.0.1"
RPORT    = 5000
RCV_DATA = ""
SND_DATA = "lol"

#==========================

#IPv4 and TCP version:

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#IPv6 and UDP version:

#C_SOCK = socket.socket(socket.AF_INET6, socket.DGRAM)

#==========================


#Connect to the listener:
C_SOCK.connect((RHOST, RPORT))

#Send data to the listener:
C_SOCK.send(SND_DATA)

#Store any data that was received back:
RCV_DATA = C_SOCK.recv(1024)

#Print any received data to the console:
print(RCV_DATA.decode())

#Close the connection:
C_SOCK.close()


