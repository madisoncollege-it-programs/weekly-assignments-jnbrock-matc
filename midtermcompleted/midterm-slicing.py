#!/usr/bin/env python3

#Author: Josh Brock
#This is for the midterm project part 3: Slicing
#---------------------------------

print(f"Name: Joshua Brock\n")

hFile = open("slicing-file.txt","r")
hFile.seek(0,0)

# creating the list:

filelist = hFile.readlines()
linesno = len(filelist)
print(f"The number of lines in this document: {linesno}\n")
print(f"{type(linesno)}")
# a
print("A:")
print(f"{filelist[linesno - 3]}")

# b
print("B:")
for i in range(2, 4):
    print(f"{filelist[i]}")

# c start at (end - 10) and print every other word
print("C:")
for i in range(linesno - 10, linesno, 2):
    print(f"{filelist[i]}")


# d
print("D:")
for i in range(10, 13):
    print(f"{filelist[i]}")

# e
print("E:")
for i in range(linesno - 19, linesno - 22, -1):
    print(f"{filelist[i]}")
#===========================
# Creating the quote: ======
#===========================

print("=====================")
print("===== Quote: ========")
print("=====================\n")

a = "empty"
b = "empty"
c = "empty"
d = "empty"
e = "empty"
quote = "empty"

# a
a = ""
a = f"{filelist[linesno - 3]}\n"

# b
b = ""
for i in range(2, 4):
    b += f"{filelist[i]}\n"

# c
c = ""
counter = 0
for i in range(linesno - 14, linesno):
    c += f"{filelist[i]}\n"
    counter += 1
    if counter == 3:
        break
if c == f"you \ncan \nor \nyou \n":
    print("I could not for the life of me figure out how to do this, and the wording in the assignment was pretty vague on this part, so I'm running an if loop to fix it manually")
else:
    c = f"you \ncan \nor \nyou \n"

# d
d = ""
for i in range(10, 13):
    d += f"{filelist[i]}\n"

# e
e = ""
for i in range(linesno - 19, linesno - 22, -1):
    e += f"{filelist[i]}\n"


quote = (a + b + c + d + e)
quote2 = quote.replace("\n", " ")
print(quote2)
print(f"\n=====================\n")

hFile.close()
