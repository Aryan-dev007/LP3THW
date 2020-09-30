import random

min = 1
max = 6

roll_again = "y"

while roll_again == "y":
    print("Rolling the dices")
    print("The values are")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input(">>Want to roll again ")
