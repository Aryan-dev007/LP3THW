name = 'Aryan'
age  = 20 # I just need to comment
height = 68 # inches
weight = 87 #kg
eyes = 'Black'
teeth = 'White'
hair = 'Brown'
weight_conv = weight * 2.2 # converting to pounds
height_conv = height * 12  # converting to inches


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on coffee.")
# this line is tricky , try to get it exactly right
total = age + height + weight
print(f"If I add my {age} , {height} and {weight} I get {total}")
print(f"Weight in pounds {weight_conv} lbs")
print(f"Height in inches {height_conv} inches ")
