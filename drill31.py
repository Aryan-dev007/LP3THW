print("Welcome to the game")
print("--------------\tCHOICES\t--------------------")
print("You are in middle of something in this game and you have to make choice for it.")
print("\n\n")

print("You are having 3 three girlfriends Lola , Lizzy and Lily.")
print("Whom do you wanna take to date?")
print("1.Lola is a horny one and Is thinking that you are cheating on her, she gets angry quickly.")
print("2.Lizzy is calm nature but she has habit of asking silly questions in public and you feel embarassed about it.")
print("3.Lily is nerd but has a great figure to play with.")

date = int(input("> "))

if date == 1:
    print("You saw Lizzy's car parked at the side of the restaurant where you two were going.")
    print("""
    What would you do ?
    1. Convince Lola to go to other place.
    2. Make a moment and tell her to go home with you.
    3. Ask her what she wanna do?""")

    lola = int(input("> "))

    if lola == 1:
        print("Lola did'nt give shit to your words and walks in the restaurant where she finds yours truth.")
        print("Kicks in your balls.")
        print("You lost all your girlfriends. Ps: They checked your phone") 
    elif lola == 2:
        print("She critizes you for being materialistic and leaves you.")
    elif lola == 3:
        print("You go to her home and GHAPA GHAP occurs.")
        print("Good evening spent")
    else:
        print("You did nothing evening is wasted.")


if date == 2:
    print("Lizzy calls you to pick her from her home.")
    print("You get her home and finds that she is not in her room.") 
    print("You walk to the bathroom. \nShe is in bathroom.")
    print("""What would you do.
    1. Knock on the door.
    2. Directly get inside the bathroom.
    3. Ask her why is she not ready yet.""")

    lizzy = int(input("> "))

    if lizzy == 1:
        print("She told you to wait at living room and then you two spend a well time together in malls and pubs.")
    
    elif lizzy == 2:
        print("You get kicked in you balls and she thorws you out of her house.")
        print("Your relationship is over.")
    elif lizzy == 3:
        print("She pulls you inside the bathroom and tells that she was waiting for you to come here.")
        print("GHAPA GHAP")
    else:
        print("You did nothing your evening is wasted.")


if date == 3:
    print("""Lily is at library and she calls you she found something strange there
          ,when you reached there she said it was just a trick to meet you.
          You were never interested in this girl.""")
    print("""What would you do?
    1. Tell her that she wasted you time.
    2. Tell her that you did'nt liked her joke.
    3. Tell her to give you tour of the library.""")

    lily = int(input("> "))

    if lily == 1:
        print("She cries in library and everyone in the library is staring at you.")
        print("This news got famous in whole college and your other girlfriends comes to know that. ")
        print("You lost all your girlfriends.")
    
    elif lily == 2:
        print("She critices for not giving her time and broke up with you.")
    
    elif lily == 3:
        print("You saw book of KAMASUTRA  and asked her to explain it.")
        print("In return she give you a physical explanation, GHAPA GHAP")
    else:
        print("You did nothing your evening is wasted.")

elif 4 <= date < 10:
    print("You got a new girlfriend.")
else:
    ("You stayed at home watched netflix.")
    