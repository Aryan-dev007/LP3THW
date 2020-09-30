tabby_cat = "\tI'm tabbed in."        # "\t" gives space 
persian_cat = "I'm split \non a line." # "\n" gives new line 
backslash_cat = "I'm \\ a \\ cat"      # "\\" gives a new line

fat_cat = '''                  
I'll do a list:
\t* Cat food\n\t* Fishes\n\t* Catnip\n\t* Grass
'''
#this all is use of \n and \t don't bother about * it's just bullet points.
print(f"tabbed{tabby_cat}")
print(f"split\t{persian_cat}")
print(f"backslash\t{backslash_cat}")
print(f"list{fat_cat}")

ultimate_format = "{}"       # all I have done is a part of study drills using .format() and f-string to get the output
print(ultimate_format.format(tabby_cat))
print(ultimate_format.format(persian_cat))
print(ultimate_format.format(backslash_cat))
print(ultimate_format.format(fat_cat))