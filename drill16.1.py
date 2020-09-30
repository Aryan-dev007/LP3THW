# this is a short version of ex16
from sys import argv
script , filename = argv

print("Opening the file...")
target = open(filename,'r+')

print("Truncating the file")
target.truncate()

print("Writing lines about yourself")
line1 = input(">")
line2 = input(">")
line3 = input(">")
target.write(f"{line1} \n {line2} \n {line3}")
 
target.seek(0)
print("This is your file : ")
print(target.read())
target.close()
