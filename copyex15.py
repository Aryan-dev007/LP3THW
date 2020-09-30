from sys import argv     # from a module import a function 

script , filename = argv    # passing argument variables
x = open(filename)
print(x.read())           # one way to open the file , make sure that both are in same directory i.e. script and the file to be opened
x.close()                                      # printing the file that python read

print("Type the filename again:")     # simple string 
file_again = open(input("> "))              # it's not another way to open a file it's just the way round
# It's just that we have taken input of the files and now we need to open that file which we have done in line 13 and then printing done in line 15                                      
      # this is to show that python does'nt have the problem to show the file again that was once being opened

print(file_again.read())

file_again.close()                    # it is important to close the file