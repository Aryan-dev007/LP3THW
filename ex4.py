cars = 100
# cars is now a variable with value assigned to it
space_in_a_car = 4
#it is also now a variable with value assigned to it
drivers = 30
#same as above 
passengers = 90
#same as above
cars_not_driven = cars - drivers
# deriving a variable by mathematical exp of other variable it is nothing but 100-30
cars_driven = drivers
# assignment of a variable 
carpool_capacity = cars_driven * space_in_a_car
# same what is said in line number 10
average_passengers_per_car = passengers / cars_driven
# same what is said in line number 10


print("There are",cars,"cars available.")          #in all the line we  are doing nothing
print("There are only",drivers,"drivers available.")  #putting the values of the variable
print("There will be",cars_not_driven,"empty cars today.") # value for cars not driven 
print("We can transport",carpool_capacity,"people today.") # value for carpool capacity
print("We have",passengers,"to carpool today.")  # value for the passengers
print("We need to put about",average_passengers_per_car,"in each car.") # value for the average passengers capacity


# Error that is given in the book 
# it shows car_pool_capacity is not defined this is because
# in code carpool_capacity it is written like this also i noticed one more thing that
# For average passenger per car we have a different formula


#from the more study drill section 
# space in car was previously 4.0 and now it is 4 it makes changes in the number of people we can transport
# making it 120 instead of 120.0