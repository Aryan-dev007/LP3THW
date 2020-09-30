import random
from collections import Counter

somewords = """ apple banana mango strawberry
 orange  grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon"""

somewords = somewords.split(' ')

word = random.choice(somewords)

if __name__ == "__main__":
    print("Guess the word! HINT: word is a name of a fruit.")

    for i in word:
        # For printing the empty spaces for letters of the words
        print("_", end=" ")

    print()

    playing = True
    # list for storing the letters guessed by the player.
    letterGuessed = ""
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        # flog is update when the word is correctly guessed.
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input("Enter a letter to guess: "))

            except:
                print("Enter only a letter!")
                continue

            # Validation of guess
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only an SINGLE letter.")
                continue
            elif guess in letterGuessed:
                print("You have guessed that letter.")
                continue

            # If letter is guessed
            if guess in word:
                k = word.count(guess)

                for _ in range(k):
                    # the guess letter is added as many times as it occus.
                    letterGuessed += guess
            # print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):

                    print(char, end=" ")
                    correct += 1

                # Once the correct word is guessed fully.
                elif (Counter(letterGuessed) == Counter(word)):
                    # the game ends even if the chances remains
                    print("The word is :  ", end=" ")
                    print(word)
                    flag = 1
                    print("Congratulation , YOU WON")
                    break  # To break out of the for loop
                    break  # To break out of the while loop

                else:
                    print("_", end=" ")

            if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print("You lost ! Try again..")
                print("The word was {}".format(word))

    except KeyboardInterrupt:

        print()
        print("Bye ! Try again.")
        exit()
