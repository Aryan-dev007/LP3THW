def add(a,b):
    print(f"Adding {a} + {b}")
    return a+b


def subs(a,b):
    print(f"Subtracting {a} - {b}")
    return a-b


def multiply(a,b):
    print(f"Multiplying {a} * {b}")
    return a*b


def divide(a,b):
    print(f"Dividng {a} - {b}")
    return a/b


print("In this script we are going to perform operations on various number.")
print("If you want to quit anytime just press CTRL + C.")
print("\n")


print("We are going to perform addition first.")
add1 = int(input(">"))
add2 = int(input(">"))

addition = add(add1,add2)
print(f"Addition of two numbers are {addition}.")


print("This is for substraction.")
subs1 = int(input(">"))
subs2 = int(input(">"))

subtraction = subs(subs1,subs2)
print(f"Subtraction of the two numbers are {subtraction}.")


print("This is for Multiplication.")
mul1 = int(input(">"))
mul2 = int(input(">"))

multiplication = multiply(mul1,mul2)
print(f"Multiplication of the two numbers are {multiplication}")     
      

print("This is for Dividing.")
div1 = int(input(">"))
div2 = int(input(">"))

division = divide(div1,div2)
print(f"Division for the two numbers is {division}")

# i need to learn if , else ,elif and how to identify character in python
