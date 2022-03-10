#!/usr/bin/env python3

#Author: Joshua Brock
#This is for the week 6 lab: flow control.
#-------------------------

print("""You enter a dark room with three doors. 
Do you go through door 1, 2, or 3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("Inside door 1 there is a giant python who is almost done with eating a smaller python.")
    print("What do you do?\n")

    print("1. Run!")
    print("2. Attack, that python must be saved.")

    # == Snake logic ============================
    snake = input("-> ")

    if snake == "1":
        print("You try to escape but the door has suddenly closed behind you. What now?")
        print("1. Attack the bigger python.")
        print("2. Yell for help")
            # == run logic ============================
        run = input("-> ")
        if run == "1":
            print("You attempt to punch and kick the leviathan into submission but are ultimately devoured, along with the other, smaller snake.")
        elif run == "2":
            print("You scream as loudly as you can but no one hears you. Fortunately, your hardy warcry has scared off the bigger snake! Then the smaller python, out of appreciation for being saved, gives you the key to escape.")
    elif snake == "2":
        print("You attempt to punch and kick the python but are tripped by its tail and black out on the cold stone ground. You awake to the feeling of stomach acid burning your flesh.")
    else:
        print(f"N)Well, doing {snake} is probably better.")
        print(f"N)You die of starvation standing in place.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    # == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print("N) The insanity rots your eyes into a pool of muck.")
        print("N) Good job!")
# == Door 3 logic =====================
elif door == "3":
    print("You see a giant wasp getting closer and closer...")
    print("1. Panic, because it looks scary.")
    print("2. Panic, because you're deathly allergic.")
    print("3. Panic, because you're scared of teh color yellow.")
    # == Wasp logic ==========================
    wasp = input("-> ")
    if wasp == "1":
        print("You get stabbed and die")
    elif wasp == "2":
        print("You get stabbed and die")
    elif wasp == "3":
        print("You get stabbed and die")
    else:
        print("You decided not to panic, and get stabbed and die in a peaceful state of acceptance.")
else:
    print("You did not select a door??? Good Call :)")






