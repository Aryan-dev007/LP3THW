from sys import argv 
from os.path import exists             # it returns true or false if a file exists or not

script , from_file , to_file = argv # argument variable

print(f"Copying from {from_file} to {to_file}")

in_file_data = open(from_file).read()    # this is something new     # opening of file

print(f"The input of file is {len(in_file_data)} bytes long")
print(f"Does the output file exist?{exists(to_file)}")              
print("Ready to hit ENTER to continue , CTRL+C to ABORT")
input()                                

out_file = open(to_file,'w')       # opening file in writing mode
out_file.write(in_file_data)             # this step involves overwriting of data which we called copying

print("Alright ! done")

out_file.close()
#in_file_data.close()          # don't know why error is there
# got the ans why I can't close in_file_data.close() it is string variable since I have added the command .read()
# difference between object and string , it will be automatically closed as soon as session ends.