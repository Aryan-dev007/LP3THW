from sys import argv
print("Hello World")
script , one , two , three = argv
print("Name of the script  ",script)
print("I am second in the line but name after first ",one)
print("I am third in the line but named after second ,",two)
print("I am fourth in the line but named after third ",three)
input("Which line I will be? ")
int(input("This information is false put any try putting a alphabet here"))   # revised or learned to use int(input())
int(input("put the number on which b comes "))                        # shows an error on terminal if intergers are not entered
print(f"What comes after A is {two}")              #okay after this exercise I get know that we use f string 
print(f"hello {one} {three}")                                                   # on variable which i have assigned in argv
# if i use this
# input("intenional error ",one)        get this -> TypeError: input expected at most 1 arguments, got 2
# this is because first input from input() and second one from argv