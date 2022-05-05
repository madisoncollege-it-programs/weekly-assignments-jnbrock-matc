#!/usr/bin/env python3

#Author: Joshua Brock

#Final Exam script

#==========================================================

#Setup (Imports and variables):

import argparse
import requests
import bs4
import socket
import json


ag = argparse.ArgumentParser(description = "This is the final exam script.")

author = "Joshua Brock; the one and only"
#==========================================================

#Argument Setup:

ag.add_argument("-i", "--ipaddress", dest="ip", help="IP address argument", required=True, metavar="[ipaddress]", type=str, default="172.31.29.252")

ag.add_argument("-f", "--function", dest="fnum", help="Function number argument(1, 2, 3, 4, or 5)", required=True, metavar="[function-number]", type=int, default=1)

args = ag.parse_args()

url = f'http://{args.ip}/q{args.fnum}'



print(f"My name is: {author}")
print(f"The specified URL is: {url}")
print(f"==============")
#==========================================================

#Function 1: get_response

def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.text
    except Exception as excp:
        result = print(f"An error occured: {excp}")
    return result

#==========================================================

#Function 2 (parse_string):


def parse_string(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        baseHTML = response.text
        myHTML = bs4.BeautifulSoup(baseHTML,features="html.parser")

        h3 = myHTML.select("H3")
        h3string = str(h3)
        fstring = f"{h3string[9:26:2]} {author[0:6:]}"
        result = fstring
    except Exception as excp:
        result = f"An error occured: {excp}"

    return result

#==========================================================

#Function 3 (parse_header):

def parse_header(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        baseHTML = response.text

        for key,value in response.headers.items():
            if key == "MATC-HEADER":
                x = value
        result = x
    except Exception as excp:
        result = print(f"Uh oh! An error occured: {excp}")
    return result




#==========================================================

#Function 4 (parse_json):

def parse_json(url):
    rsp = requests.get(url)
    dict = json.loads(rsp.text)
    varmb = dict.get("Music And Books")
    for name in varmb:
        if name.get("title") == "The Shining":
            return name.get("publish_info").get("publisher")


#==========================================================

#Function 5 (socket_client):

def socket_client(ipaddress):
    #x = 0
    RHOST = ipaddress
    RPORTS = range(5000, 6001)
    fails = 0

    for port in RPORTS:

        try:
            #x = 1
            SND_DATA = ("secret")
            #x = 2
            C_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            #x = 3
            C_SOCK.connect((RHOST,port))
            #x = 4            
            C_SOCK.send(SND_DATA.encode())
            #x = 5
            RCV_DATA = C_SOCK.recv(1024)
            #x = 6
            C_SOCK.close()
            #x = 7
            return RCV_DATA.decode()
            break
        
        except Exception as excp:
            C_SOCK.close()
            #print(x)
            #print(excp)
            fails += 1
    return fails
#==========================================================


#    if message == "You Win":
#        return message
#    else:
#        message = "You Win"
#        return message



#==========================================================

#Running the script:

answer = args.fnum

if answer == 1:
    print(f"Running function 1...\n")
    print(f"RESULT: {get_response(url)}")

elif answer == 2:
    print(f"Running function 2...\n")

    print(f"RESULT: {parse_string(url)}")

elif answer == 3:
    print(f"Running function 3...\n")
    print(f"RESULT: {parse_header(url)}")

elif answer == 4:
    print(f"Running function 4...\n")
    print(f"RESULT: {parse_json(url)}")

elif answer == 5:
    print(f"Running function 5...\n")
    print(f"RESULT: {socket_client(ip)}")

else:
    print("Invalid function number.")
