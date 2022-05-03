#!/usr/bin/env python3

#Author Josh Brock

#Week 9 main function lab


import c2f
import f2c


print("Input a temperature below:")
temp_num = input(">")
print("Temperature type? (F/C):")
temp_type = input(">")

if temp_type == "F":
    print(f2c.f2cfunc(temp_num))
elif temp_type == "C":
    print(c2f.c2ffunc(temp_num))
else:
    print("Please enter a valid temperature type.")
