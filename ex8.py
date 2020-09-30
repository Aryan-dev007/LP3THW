formatter = "{} {} {} {} {}"
# formatter is a variable and assigned with string although the string is empty we can use .format() to fill it
print(formatter.format(1, 2, 3, 4, 5))
# there was so much to learn in these things
print(formatter.format("one", "two", "three", "four", 5))
# here i made a mistake in putting double quotes
print(formatter.format(True, False, False, True, True))
print(formatter.format(formatter, formatter, formatter, formatter, formatter))
print(formatter.format(        # we need to give 5 inputs so as to satisfy condition of line 1
    # five {} means five input should be give otherwise it will show an error
    "hello",
    "world",                    # be careful about commas and double quotes
    "have to write five things here",
    "Bye",
    "saying hello again"
))

# whats happening here is we specified a variable "formatter" it is a string with {} so that we can assign it using .format() method
# in all the lines  using print function we assign 5 values (arguments) to them matching with their five {}
# experimenting a short way of executing all of this program using f-strings

print(f"{1,2,3,4,5}")
print(f"{'one','two','three','four','five'}")
print(f"{True,False,True,False,False}")
print(f"{formatter,formatter,formatter,formatter,formatter}")
print(f"""
       hello world!
""")


# ('{} {} {} {} {}', '{} {} {} {} {}', '{} {} {} {} {}', '{} {} {} {} {}', '{} {} {} {} {}') output for f string
# {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}       output for .format()

# 1 2 3 4 5 output for .format()
# (1, 2, 3, 4, 5) output for f string           # same happens with true and false cond brackets are present

