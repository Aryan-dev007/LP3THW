from sys import argv 
from os.path import exists
script , from_file , to_file = argv

# opening file using with

with open(from_file) as in_file:
    in_data = in_file.read()

print(f"Does the output file exists {exists(to_file)} ")

open(to_file,'w').write(in_data)

print("Check your files")