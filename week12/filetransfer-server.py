#!/usr/bin/env python3

#Testing a server listening connection


import socket

LHOST = ''

LPORT = 5000
RCV_DATA = ""

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while(1):

    hFile2 = open("Data_received.txt", "w")
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print(f"Connected by {addr}")
    while 1:
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA: break
        datastr = RCV_DATA.decode()
        print(datastr)
        hFile2.writelines(datastr)
        print("Data was received and written to file: 'Data_received.txt'")
        L_CONN.sendall(RCV_DATA)
    hFile2.close()

    L_CONN.close()
