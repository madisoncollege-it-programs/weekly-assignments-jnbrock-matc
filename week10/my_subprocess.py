#!/usr/bin/env python3

#Author: Josh Brock
#Week 10's subprocess lab

import subprocess

myProclist = []

myProc = subprocess.run(["ps","-axco","command"], stdout=subprocess.PIPE)
myProcstr = myProc.stdout.decode()

myProclist = myProc.stdout.decode().split("\n")

for i in myProclist:
    print(i)

num = len(myProclist) - 1
print("Number of processes:")
print(num)
