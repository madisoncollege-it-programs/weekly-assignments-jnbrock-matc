#!/usr/bin/env python3

#Author: Joshua Brock

#Week 14 lab: JSON

#=====================================

import sys
import requests
import argparse
import json


ag = argparse.ArgumentParser(description="Week 14 script: JSON")

ag.add_argument("-i", "--ipaddress", dest="ip", help="Enter an IP address", metavar="[ipaddress]", type=str, required=True)

args = ag.parse_args()

url = f"http://ipinfo.io/{args.ip}/json"

jsonderulo = requests.get(url)

myDict = json.loads(jsonderulo.text)

for i in myDict:
    print(f"{i} : {myDict[i]}")
