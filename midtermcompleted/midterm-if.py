#!/usr/bin/env python3

#Author: Josh Brock
#This is for the Midterm-if project (project 1).

print("Name: Joshua Brock")

Total = 0

hFile = open("Midterm-if.txt","r")
listLines = hFile.readlines()
lineno = 0

str1 = "gmeach18@ed.gov"
str2 = "248.253.63.149"
str3 = "Whiteland"
str4 = "80.222.19.190"
str5 = "Kayley"
str6 = "dcassyqw@microsoft.com"



Total = 0
linenolist = 0
linenostr = 0
joinstr = ""


for line in listLines:

    if str1 in line:
        linenolist = line.split(",")
        linenostr = joinstr.join(linenolist[0])
        linenoint = int(linenostr)
        Total += linenoint
    elif str2 in line:
        linenolist = line.split(",")
        linenostr = joinstr.join(linenolist[0])
        linenoint = int(linenostr)
        Total += linenoint
    elif str3 in line:
        linenolist = line.split(",")
        linenostr = joinstr.join(linenolist[0])
        linenoint = int(linenostr)
        Total += linenoint
    elif str4 in line:
        linenolist = line.split(",")
        linenostr = joinstr.join(linenolist[0])
        linenoint = int(linenostr)
        Total += linenoint
    elif str5 in line:
        linenolist = line.split(",")
        linenostr = joinstr.join(linenolist[0])
        linenoint = int(linenostr)
        Total += linenoint
    elif str6 in line:
        linenolist = line.split(",")
        linenostr = joinstr.join(linenolist[0])
        linenoint = int(linenostr)
        Total += linenoint

print(f"The total is: {Total}")

hFile.close()
