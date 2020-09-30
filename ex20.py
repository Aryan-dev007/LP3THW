from sys import argv                 # from module sys importing function argv (argument variable)

script , input_file = argv          # passing argument variable in terminal

def print_all(f):                   # defining function and function variable is f.
    print(f.read())                   # This function is defined for reading the files.

def rewind(f):                        # defining function f , we can use same variable when defining different function but we can't use same variable in same function.
    f.seek(0)                         # seek(0) takes pointer back to 0 byte.

def print_a_line(line_count,f):                  # defining a function with two function variables.
        print(line_count , f.readline(),end='')    # super error wrote readlines() notice 's' at last and got all print_a_line output in one line only.
                                                            # this end='' avoids adding double \n to every line.
current_file = open(input_file)                 # since the readline() returns the \n that's in the file at the end of every line.

print("First let's print the whole file:\n")

print_all(current_file)                     #  line14 opening the file and in this line using defined function print_all to print the  current_file.
                                          # remember we can use global variable like current_file in the defined function and that's normal.
print("Now let's rewind , kind of like tape.")      

rewind(current_file)            # using rewind function 

print("Let's print three lines:")

current_line = 1                  # this current line only shows the current line number the file is in just by simple maths and has no relation with readline()
print_a_line(current_line , current_file)        

current_line += 1 
print_a_line( current_line , current_file)                # current_line have no relation with the line count and it's was just confusing me , if the readlines depend on line count and
                                               # and the answer is NO , it's just that readlines() reads as line 1 then line 2 then line 3.
current_line += 1          
print_a_line(current_line , current_file)

current_file.close()        # always use close() even the author ignored it.


# a += b ------> a = a+b