people = 91                  # variable assignment
cars = 15
trucks = 19


if cars > people or trucks < cars:                           # conditional statement if this cond is true then line 7 will be executed.
    print("We should take the cars.")         
elif cars < people:                           # call it as elseif if true line 9 will be executed.
    print("We should not take the cars.")
else:
    print("We can't decide.")                  # if none of the statements are correct then this statement will be executed.

if trucks > cars and cars > people:              # This statement can be used as with 'and' & 'or' to vary results.
    print("That's too many trucks.")
elif not trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take  the trucks.")
else:
    print("Fine, let's stay home then.")
# if multiple elif blocks are true then python starts at the top and runs the first block.
# Running only first one.