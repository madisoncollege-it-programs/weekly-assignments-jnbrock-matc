#!/usr/bin/env python3

#Author: Josh Brock

#Week 13 lab: interacting with websites

import requests

ans = input("Enter website URL (ex: 'http://google.com'): ")
hFile = open("my_web_file.html","w")

try:

    response = requests.get(ans)
    response.raise_for_status()
#    for key,value in response.headers.items():
#        hFile.write(f"")
    hFile.write(response.text)
except Exception as excp:
    print(f"An error occured: {excp}")

hFile.close()
