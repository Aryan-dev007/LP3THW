print("""You enter a dark room with two doors.
Do you go throught door #1 or door #2 or #3""")
print("""
1. You hear Roars.
2. It's quiet there.
3. You hear a beautiful voice singing.""")

door = input("> ")

if door == "1":
    print("There's a gaint bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Throws a wooden block at another corner.")


    bear = input("> ")

    if bear == "1":
        print("The bear wats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
    else:
        print("Bears looks at you and rest is history.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothepins.")
    print("3. Understanding revolver yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif door == "3":
    print("You see a beautiful girl in a room with dim lights.")
    print("1. You go talk to her about how to get out of the here.")
    print("2. You ask her 'Is she stuck here?")
    print("3. You try to kiss her.")

    girl = input("> ")

    if girl == "1":
        print("The girl attacks you and you discovered that she was a Zombie.You die")
    elif girl == "2":
        print("She tell's you a story how she came here and then , you get frieghtened and you try to run but was killed by the girl.")
    elif girl =="3":
        print("The girl kisses you and sucks your organs into in her by the time you discovered that she was Zombie you were dead.")
    else:
        print("You return back to the doors.")
        
else:
    print("You stumble around and fall on a knife and die. Good job!")
