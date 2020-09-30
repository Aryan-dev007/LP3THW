from sys import argv
from os.path import exists
script, from_file, to_file = argv

in_data = open(from_file).read()
# shorter method for copying files
print(f"Checking whether file exists or not {exists(to_file)}")

open(to_file,'w').write(in_data)

print("Check your files")
