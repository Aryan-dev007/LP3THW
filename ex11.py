#print("How old are you?",end='')    # use of end function to not end the line there 
#age = input()                        # use of input function to take input
# more easy way of input
age = input("How old are you?")
#print("How tall are you?",end='')    # next four lines exp same as above
#height = input()
height = input("How tall are you?")
#print("How much do you weight?",end='')
#weight = input()                                  ###made a mistake in first attempt of the new format in syntax of the lines.
weight = input("How much do you weight?")            ## variable = input("Data needed")

print(f"So, you're {age} old, {height} tall and {weight} heavy")       # use of f string as usual

# i think i figured out another way of input

length = input("length of the house?")


print("How old are you?",input())     #if print this type it will first take the input then prints the following in the double quotes
# therefore it is not preffered.