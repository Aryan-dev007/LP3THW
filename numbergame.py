from sys import argv
script , user_name = argv
print("Hello I am ",script)
print("Welcome to world of NUMBERS.",user_name)
print("Today we will be learning a trick to trick people.")

choices = 10,30,50,70,90
arrow = ">>>"
print("Select a number for the numbers given below.")
print(choices)
selected = input(arrow)
print("Now that you have selected your number I will teach you a trick")
print(f"Adding two to you number , I want to tell again you that {script} doesn't know your number")
mod1 = int(selected) + 2 
print(mod1)
print("Now multiply two to your number")
mod2 = int(mod1) * 2
print(mod2)
print("Substracting two from the number")
mod3 = int(mod2) - 2
print(mod3)
print("Patience! Last step , dividing the number by two")
mod4 = int(mod3) / 2
print("Just one step more , subtracting one from your number")
mod5 = int(mod4) - 1
print(f"Is this the number you thought of *************{mod5}*************")
print(f"""
*Selection of number
*Adding 2 {mod1}
*Multiply 2 {mod2}
*Subtract 2 {mod3}
*Divide 2 {mod4}
*Subtract 1 {mod5}
""")

print(f"So this script {script} teaches a number trick.")


# This is my first fully created script in python. Ha ' that works
