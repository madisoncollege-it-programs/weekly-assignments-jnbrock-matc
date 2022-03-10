#!/usr/bin/env python3

#Author: Josh Brock
#This is for the week 5 lab: "File Data Interactions".
#--------------------------

#Opening and reading the passwd file:
hFile = open("/etc/passwd","r")
passwdstr = hFile.read()

#1, A-D:
print(f"passwdstr")
print(f"Amount of objects contained in the specified file: ")
print(f"len(passwdstr)")
print(f"Using the 'read()' function over another type of read function is preferable here because it saves as a string.")


hFile.close()

