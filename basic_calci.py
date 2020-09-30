def add(a,b):                                 # defining functions
    print("Adding the two numbers.")
    return a+b                           # first add then return


def subtract(a,b):
    print("Subtracting your two numbers.")
    return a-b


def multiply(a,b):
    print("Multiplying the two numbers.")
    return a*b


def divide(a,b):
    print("Dividing the two numbers.")
    return a/b


print("Applying all the operator one by one")

a = int(input())
b = int(input())                    # always define the type of input in this it showed error because on default input is taken as string

adding = add(a,b)
subtracting = subtract(a,b)
multiplying = multiply(a,b)                  # in these four lines there will be only the print statement of the def function
dividing = divide(a,b)                        # as return performs first add then return

print(f"""
Additon is {adding}
Substraction is {subtracting}
Multiplication is {multiplying}
Division is {dividing}
""")

# in this part final values are shown return results are printed here only.
