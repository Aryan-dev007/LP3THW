from sys import argv 

script , filename = argv                       # argument variables
 
print(f"We're going to erase {filename}.")                 # f string
print("If you don't want that, hit CTRL - C(^C).")           
print("If you do want that , hit RETURN,")
 
input("?")                # just a trick see above two lines

print("Opening the file...")
target = open(filename,'r+')         # this r+ is for reading and writing the files

print("Truncating the file. Goodbye!")       # emptying the file 
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1 :  ")
line2 = input("line2 :  ")                 #input to files
line3 = input("line3 :  ")

print("I'm going to write these to file.")

target.write(line1)
target.write("\n")
target.write(line2)               
target.write("\n")                
target.write(line3)          # question 2 answered in this script
target.write("\n")
target.write(input('>>'))       # an easy to do file input from this we don't need to write line 19 ,20 and 21

target.seek(0)                   # once file is opened and we write in it we need to take the pointer back to zero for new lines to read so we use seek(0)
print("Let me show your file once.",)
print("\n")
print(target.read())                  # printing the file 
print("And finally, we close it.")
target.close()
# don't forget to close the file .

#this whole code is not as per ex16 its a bit modified to see new file output as well.