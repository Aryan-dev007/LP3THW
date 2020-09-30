from os.path import exists
from sys import argv, exit
script, player = argv


def start():

    print("----------------------------------------------------------------------------------------------------------------------------")
    print(f"Hi {player} now you are in parallel universe where lot of things are going on with you.")
    print("\n")
    print("So, you are at home , and is getting ready to go to school.")

    print("How do you want to go to school , you have a cycle or school bus will arrive.")

    choice = input(">> ")

    if "cycle" in choice:                         # cycle()
        print("Fitness for life.")
        cycle()

    elif "bus" in choice:                        # bus()
        print("Bus arrives you get on the bus.")
        bus()

    else:
        print("You stayed on home wasting your time.")


def loser(loser):
    print(loser, "LOSER")
    exit(0)


def bus():
    print("""You got on the bus and you found the guys who bullies everyone in the school.
Unfortunately only one seat is left , the seat beside them.""")
    print("What you will do?")
    bullied = False

    while True:
        choice = input(">> ")

        if "seat" in choice and not bullied:
            print("You got to the seat and is comfortable. What do you do next?")

        elif "stand" in choice:
            loser("They forced you to take the seat beside them and then you were bullied by them. You did'nt went to school because of this .")

        elif "talk" in choice and not bullied:
            print("You make them friends of your. Thanks to your extrovert nature.")
            school()

        else:
            print("You have to do something so they don't bully you.")


def cycle():
    print("You go to your garage and escort for school.")
    print("In the way you spotted the a girl from your school searching for something. Will you help or move on.")

    choice = input(">> ")

    if choice == "help":
        print("You go and asks her about her problem. She tells you that she lost her ring that she lost her ring.")
        print("What are you gonna do?")

        girl = input(">> ")

        if "who" in girl:
            print("The ring was given by her boyfriend.")
            print("You found her ring and you are now friends.")
            school()

        elif "kiss" in girl:
            loser("She kicked you in your balls and she left.")

        else:
            print("Keep searching")

    else:
        school()


def school():
    print("You reached to the school and you have TWO classes today MATHS , LANGUAGES.")
    print("Which class you want to attend first.")

    choice = input(">> ")

    if "maths" in choice:
        maths()
    elif "language" in choice:
        lang()
    else:
        print("You have to chose one of them.")


def maths():
    print("You reached maths classes in time.")
    print("You go and then sit with your friends.")
    print("Today topic is Arthmetic progressions.")

    a = int(input("> First term of series "))
    d = int(input("> Common difference "))
    l = int(input("> Last number "))
    sr = []

    for i in range(a, l+1):
        #print(f"The first number of the series is {a}")
        n = a + (i * d)
        sr.append(n)
        #print("Your next number in series:",n)
        print("Enter the  number of the series.")
        z = int(input("> "))
        if z == n:
            print("You are correct.")
        else:
            print("You were wrong")
            loser("Kicked out of the class.")

            #print("Your list: ",sr)
            #print(f"Now the number is: {a}")
            #print(f"this is d:{d}")
            #print(f"This is i: {i}")

        print("Your arithmetic progression--", sr)

    won()


def lang():

    print("You got language class and languages they were teaching to encode and decode.")
    print("You need to open your language file.")

    filename = input("> ")

    file = open(filename)
    print("What should you do to read your file.")

    enc = input("> ")

    if "encode" in enc:
        print("Congo you encoded the file. Next step is..")
        enc = file.readline().strip().encode()

        dec = input("> ")

        if "decode" in dec:
            print("Well done. Now you can read file.")

            dec = enc.decode()

            print(dec)
            file.close()
            won()

        else:
            print("You failed to read file. Try again")

    else:
        print("You failed to read file. Try again.")


def won():
    print("You completed this game and successfully survived one day in parallel universe.")


start()
