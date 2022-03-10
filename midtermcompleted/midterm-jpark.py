#!/usr/bin/env python3
#Author: Joshua Brock
#Midterm part 2: Jurassic Park project

#--------------------

print(f"Name: Joshua Brock")

#--------------------
#Making the password dictionary:

password_database = {
    "Username":"dnedry",
    "Password":"please"
}

#--------------------
#Making the command dictionary:

command_database = {
    "reboot":"OK. I will reboot the system.",
    "shutdown":"OK. I will shut down all park systems.",
    "done":"I love all this hacker stuff."
}

#--------------------
#Creating the two objects (white rabbit and counter):

white_rabbit_object = 0
counter = 0

#--------------------
#Creating the while loop:

uname = 0
pword = 0
cuname = "Josh"
cpword = "lol"

while 1 == 1:
    uname = input("Enter username: ")
    pword = input("Enter password: ")
    if pword == cpword and uname == cuname:
        print("Hi, Josh. You're stil the best coder in Python Park.")
        print(f"Your available commands are: ")
        print(command_database.keys())
        #command processing after successful login:
        while 1 == 1:

            command = input("Enter your command: ")
            if command == "reboot":
                print(f"{command_database['reboot']}")
            elif command == "shutdown":
                print(f"{command_database['shutdown']}")
            elif command == "done":
                print(f"{command_database['done']}")
                break
            else:
                print(f"The Lysine Contingency has been put into effect.")
    else:
        counter += 1
        print(f"Wrong username/password: {counter}.")
    if counter == 3:
        i = 0
        while i != 25:
            print(f"You didn't say the magic word\n")
            i += 1
        counter = 0
        break

