#!/usr/bin/env python3

#Author: Josh Brock
#This is for the week 5 lab: "File Data Interactions".

hFile = open("/etc/passwd","r")
passwdstr = hFile.read()
print(f"{passwdstr}\n")
print(f"{len(passwdstr)}\n")

print(f"The len function is counting the amount of objects stored in the passwdstr string.\n")
print(f"Using this read function instead of readlines or readx is necessary to save the file as a string.\n")

hFile.close()

hFile = open("/etc/passwd","r")
passwdlist = hFile.readlines()
print(f"{passwdlist}\n")
print(f"{len(passwdlist)}\n")
hFile.close()

print(f"The len function here is counting \n")
print(f"Using this read function stores the read lines into a list, making it easier to access and parse through individual lines.\n")

hFile = open("/etc/passwd","r")
loopno = 0
passwdloopstr = "empty"
for i in hFile:
        loopno += len(i)
        print(i)
print(f"{loopno}\n")

print(f"This format of reading a file is better for huge files that would otherwise take a very long time to read to a variable.\n")

hFile.close

