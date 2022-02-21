#!/usr/bin/env python3

#Author: Josh Brock
#This is for the String Formatting Lab in Week 3.

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

print(f"Hello {varName: <0s}")
print(f"{varRed: <0s}-{varGreen: <0s}-{varBlue: <0s}")
print(f"Is this {varGreen.lower(): <0s} or {varBlue.lower(): <0s}?")
print(f"My name is {varName.upper(): <0s}")
print(f"[{varRed:+^7s}]")
print(f"[{varGreen.lower():=<7s}]")
print(f"[{varBlue.lower():*>9s}]")
print(f"{varBlue}" * 10)
print(f"{varLoot}")
print(f"{varLoot: <.1f}")
print(f"I have ${varLoot: <.2f}")
print(f"[{varRed:$^9s}] [{varGreen:$^10s}] [{varBlue:$^10s}]")
print(f"[  deR  ] [{varGreen: ^9s}] [  eulB  ]")
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
