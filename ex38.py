ten_things = "Apples Oranges Crows Telephones Light Sugar"

print("Wait there are not 10 things in that list , let's fix that.")

stuff = ten_things.split(' ')          #
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn" , "Banana" , "Girl", "Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()           # see line 22 for explanation that line occurs till the condition is not met.
    stuff.append(next_one)
    print("Adding: ",next_one)
    print(f"There are {len(stuff)} items now.")


print("There we go: ",stuff)        # There we go:  ['Apples', 'Oranges', 'Crows', 'Telephones', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']

print("Let's do some things with stuff.")

print(stuff[1])         # print(stuff , oranges)
print(stuff[-1])              # print(stuff , corn)
print(stuff.pop())                # pop(stuff , corn)
print(" ".join(stuff))            # Apples Oranges Crows Telephone Light Sugar Boy Girl Banana  >> convert it from list to just a simple sentence.
print("#".join(stuff[3:5]))         # including index 3 and excluding index 5

# line 22 means pop on last element in stuff and  until a parameter (index) is given.
# line 23 and 24 meaning joining the stuff with space in line 23 with spaces means breaking their list format.
# in line 24 joining with # but specified elements since the indexes are mentioned.

stuff.remove("")
