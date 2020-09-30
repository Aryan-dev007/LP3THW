def cheese_and_crackers(cheese_count , boxes_of_crackers):             # defining a function with two (function)variables in it.
    print(f"You have {cheese_count} cheeses!")                    # f string in this and next line.
    print(f"You have {boxes_of_crackers} boxes of crackers!")        
    print("Man that's enough for a party!.")           # simple string
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")         
cheese_and_crackers(20,30)                                  # giving input directly to the function just numbers


print("OR, we can use variables from our script:")                  
amount_of_crackers = 50                             # creating two (global) variables
amount_of_cheese = 10

cheese_and_crackers(amount_of_cheese,amount_of_crackers)        # using function with variable from the script


print("We can even do math inside too :")                  
cheese_and_crackers(10+20,5+6)                 # supports math inside 

print("And we can combine the two , variables and math:")
cheese_and_crackers(amount_of_cheese + 100 , amount_of_crackers + 120)     # depending on the variable defined we can perform maths with combination of variable and numbers.

