print("Let's practice everything you know.")
print('You \'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
 The lovely world 
with logic so firmly planted 
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("------------")

five = 10 - 2 + 3 - 6
print(f"This should be five:{five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100               # inside the function variable is temporary . When you return it then it can be assigned to a variable for later.
    return jelly_beans , jars , crates


start_point = 10000
beans , jars , crates = secret_formula(start_point)

#remember this another way to format strings.
print("With a starting point of:".format(start_point))
#it's just like f"" strings.
print(f"We'd have {beans} beans , {jars} jars and {crates} crates.")

start_point = start_point / 10

print("We can also do it this way:")
formula = secret_formula(start_point)
#this is the easy way to apply format to string.
print("We'd have {} beans , {} jars , {} crates".format(*formula)) #how does it does that?


