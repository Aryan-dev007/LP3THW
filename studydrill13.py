# we used sys module's function argv
from sys import argv
# here scriptname = filename & greetings = next word & name = third word
scriptname, greetings, name, college, sem, bye = argv
# if ur not understanding what is next word see ex13.py (poor memory)
print("script name will be displayed here:", scriptname)
print("I am saying", greetings)
print("My name is ", name)
print("I am a student at ", college)
print("I am in sem ", sem)
print("Time to go bro ", bye)  # well done no mistakes in executing program

