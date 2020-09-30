def add(a,b):
    print(f"ADDING {a} + {b}")
    return a+b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"MUTIPLYING {a} * {b}")
    return a*b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a/b


print("Let's do some maths with just function!")

age = add(30, 5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age} , Height: {height} , Weight: {weight} and IQ: {iq}")


# here is a puzzle for extra credit , type it anyway
print("Here is a puzzle.")

what = add(age, subtract(height,multiply(weight, divide(iq,2))))

print("That becomes : ",what, "Can you do it by hand?")


# study drill question number 3

study = multiply(iq,subtract(weight,add(age,divide(height,3))))

print(f"This is what I got {study}")
