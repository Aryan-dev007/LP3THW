types_of_people = 10
# assignment of a variable
x = (f"There are {types_of_people} types of people.")  # string inside string 1
# use of format string
binary = "binary"  # assignment of variable
do_not = "don't"   # same as above
# string inside string 2
y = (f"Those who know {binary} and those who {do_not}.")
# use of f-strings to put string inside string
print(x)  # printing of a variable
print(y)  # printing of a variable
print(f"I said: {x}")  # string inside string 3
# use off-string and printing of varible with out single quotes
print(f"I also said: '{y}' ")  # string inside string 4
# use of f-string and printing of variable with single quotes
hilarious = False
# variable assignment and it is a boolean condition
joke_evaluation = "Is that joke funny?!{}"
# varible assignment with space left to use .format() method , it is used when string is already there and we need to assign something to it.
print(joke_evaluation.format(hilarious))
# using .format() method keep and eye on brakt
w = "This is the left side of ..."   # two variable assigned having string in it
e = "a string with a right side."
print(w + e)   # this shows that we are printing variables that are having strings in it
# adding two variable assigned with strings , we can add variables to make a longer string
# but we can't substract the string

