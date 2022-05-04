#!/usr/bin/env python3

#Author: Joshua Brock

#Week 13 part 2 script

#========================

import requests

import bs4

hFile = open("my_web_file.html","r")

myWP = hFile.read()
myHTML = bs4.BeautifulSoup(myWP,features="html.parser")

#print(myWP)
#print(f"\n========================================\n")
#print(myHTML.select("li"))

#==== printing out the links ====

print(f"Name of the page:\n")
title = myHTML.select("title")
print(title[0].getText())
print(f"\n=============")

elems = myHTML.select("li")
print(f"List of links on the site:\n")
for i in range(0, len(elems)):
    print(elems[i].getText())

hFile.close()
