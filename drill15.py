# Q6) what I got
#>>> txt = open("/Users/arx6363/Desktop/hard way/sample_ex15.txt")   use of double quotes , always specify the path of the file.
#>>> print(txt.read())                                                even it is in the same directory.
#It is some stuff that I typed into this file.
#It is really cool stuff.
#It's been a lot of fun being here.
#>>> quit()


# Q3) Use only input to open and read files.

print("Use of input to open the files , type the filename below")     # be in the same directory for convinience
x = open(input(">>"))                                                 # putting open and input in single line and it works
print(x.read())
x.close()
