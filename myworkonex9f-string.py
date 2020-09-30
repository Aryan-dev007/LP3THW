days = "Mon Tue Wed"
months = "Jan Feb Mar"
print(f"Here are the {days}")
print(f"Here are the {months}")  # here I have nothing but another way to concatenate string using f-strings 
# using f-strings in ex8 will be more complicated since the formatter is already assigned , there we will be putting values each time
# I will show you an example
print("\n")
to_put = "Hello World"
formatter = (f"example{to_put}")
print(formatter)

# problem ye h ki f-string me baar baar put variable assign krke put krna padega jabki .format() me ek baar "formatter" ko assign
# krdo aur fir input dete raho kya likhna h kya nahi

# new lead 
print(f"example\t{'hello', 'mine',True,4}")   # Like .format() method we can put either a pre assigned variable or assign it any string.
# shocking it is that we can use it with that ease.
# if main string is enclosed in double quotes use single quotes inside the {} otherwise it will show syntax error.