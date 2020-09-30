from sys import argv
script , yourname , age = argv             #commenting out some useful lines for expt
#prompt = "_/\_"
prompt = 1

print(f"I wanted to say hello    {prompt}   to my companion {yourname} and age is lem'me guess {age}. ")
print(f"By the I am the script {script} talking to you.")
print("Please enter you reaction on my namste.")
hello = input(f"{prompt}------> ")
print("Your reactions are valuable to me so I'll show you some magic.")
print("\n")
print("\n")                      # we need to specify age as int or otherwise python will treat this a str error
print(hello)                                #it works hurrah
new_age = int(age) + prompt +1               #we can add any number as well as it reads prompt=1 
print(f"I will be there for you to say 'Happy Bithday' as you {age} +1 you will be {new_age}")
print(f"Bye {yourname} I'll have to go see u soon at end of the book {prompt}")


