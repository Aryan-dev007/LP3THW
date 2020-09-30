# this one is like your script with argv
def print_two(*args):                              # *args which is a lot like your argv parameter but for functions. Has to go inside parathesis to work
    arg1 , arg2 = args                            
    print(f"arg1 : {arg1} , arg2 : {arg2}")

# ok that *args is actually pointless , we can just do this
def print_two_again(arg1 , arg2):
    print(f"arg1 : {arg1} , arg2 : {arg2}")
# this one takes only one argument
def print_one(arg1):
    print(f"arg1 : {arg1}")

# this one takes no arguments
def print_none() :
    print("I got nothing.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

