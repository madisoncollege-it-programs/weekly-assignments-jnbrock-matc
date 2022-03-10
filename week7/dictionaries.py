#!/usr/bin/env python3

#Author: Joshua Brock
#This is for the week 7 lab - Dictionaries
#-----------------------------------------


#1. Make the dictionary:

myDict1 = {
    "server1.testlab.com":"192.168.1.10",
    "server2.testlab.com":"192.168.1.11",
    "server3.testlab.com":"192.168.1.12",
    "server4.testlab.com":"192.168.1.13",
    "server5.testlab.com":"192.168.1.14",
    "server6.testlab.com":"192.168.1.15"
}
#2. List the FQDN's (names):

print(myDict1.keys())

#3. List the IP's:

print(myDict1.values())

#4. List all the records (both names and IP's):

print(myDict1.items())

#5. Add server7 and server8:

myDict1["server7.testlab.com"] = "192.168.1.16"
myDict1["server8.testlab.com"] = "192.168.1.17"

#6. Test for server2:

print(myDict1["server2.testlab.com"])

#7. Test for server10:

print(myDict1["server10.testlab.com"])
