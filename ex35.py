from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    #choice = int(input("> "))
    how_much = int(input('>> '))                                      #'0' in choice or '1' in choice
                                                                    #else:
                                                                         #  dead("Man, learn to type.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)

    elif how_much > 50:
        dead("You greedy bastard! DEAD.")

    else:
        dead("Man, lear to type")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("the fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("the bear looks at you then slaps your face.")

        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True

        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")

        elif choice == "open door" and bear_moved:
            gold_room()

        else:
            print("I got no idea what it means.")


def cthulhu_room():
    print("Here you see the great evil CTHULHU.")
    print("He, it , whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head.")

    choice = input("> ")

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("Well that was tasty!")

    else:
        cthulhu_room()


def dead(why):
    print(why,"Good job!")
    exit(0)

def snake_room():
    print("""You came across a room full of snakes.
    Your childhood fears were snakes.
    You need to scare snakes to make them go away.""")
    print("Let's test how much you know about snakes.")
    print("You have three things lying there which are Wood , Flashlight and Lighter.")

    choices = input("> ")

    if "wood" in choices:
        dead("You are unable to scare snake.")

    elif "Flashlight" in choices:
        dead("You can see a whole lot of snakes.")

    elif "lighter" in choices:
        dead("Flame is too low to scare snake.")

    elif "lightood" in choices:
        print("You need to kill snakes by this")
        print("How many combinations you can make?")
        print("Enter the number of wood and lighter.")
        wood = int(input("> "))
        lighter = int(input("> "))
        combo = wood * lighter / 2
        snake_killed = combo * 4
        print("snake killed :",snake_killed)

        if snake_killed > 100:
            print("You finally found gold room.")
            gold_room()


        else:
            dead("You did not killed enough snakes , so they were able bite you.")

    else:
        dead("Snakes biten you.")


def start():
    print("You are in a dark chamber.")
    print("There is a door to your right , left and straight.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()

    elif choice == "right":
        cthulhu_room()

    elif choice == "straight":
        snake_room()

    else:
        dead("You stumble around a room until you starve.")

start()
