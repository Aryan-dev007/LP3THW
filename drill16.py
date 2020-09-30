from sys import argv
script , filename = argv                # argument variables

print("Opening the file...")
target = open(filename,'r+')               # opening file with write command

print("Not going to truncate file.")

target.write(input(f"""
Hello I am the new line .
Nice to meet you .
My script is {script}.
Tell me your name about yourself in three lines
>>>"""))

print("Just printing the output")
target.seek(0)
print(target.read())

print("Closing the file")
target.close()

