#!/usr/bin/env python3

#Author: Josh Brock
#This is for the week 4 Data Types lab.

varString="Here is a nice string to slice"
varList="Here","is","a","nice","list","to","slice"

print(varString[3:30])
print(varString[0:3])
print(varString[3:10])
print(varString[0:30:2])
print(varString[::-1])

print(varList[::-1])
print(varList[2::-1])
print(varList[2:4])
print(varList[0::3])
print(varList[1:])

for i in varString:
    print(i)
for i in varList:
    print(i)


