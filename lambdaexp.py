def square(num):
    return num**2

my_num = [1,3,4,5,6]
#1st way
for i in map(square,my_num):
    print(i)
# 2nd way
print(list(map(square,my_num)))

mynums = [2,53,54,63,17,65]

def even(num):
    return num%2 == 0

print(list(filter(even,mynums)))

# lambda function

#a = input("> ")
hello = (lambda a: a ** 4)       # ek baar ka use ke liye
print(hello(4))

    
