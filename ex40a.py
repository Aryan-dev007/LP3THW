class Mystuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"      # use of self.tangerine for setting tangerine instance variable

    def apple(self):
        print("I am Classy Apples!")

# Classes are like mini modules then there has to be concept similar to import but for classes.
# That concept is called "instantiate".
# When  you instantiate a class what you get is called an object.
# __init__ calls the function which you have created using 'def' to initialize your newly created empty object.
# 'self' is that empty object python made for me and can set values just like we would with a module ,dictionary or other object.


# three way to get things from things.

# class style
things = Mystuff()       # instantiate operation
things.apple()
print(things.tangerine)

# module style
mystuff.apples()

# dict style
mystuff['apples']      # refer to book for reference to mystuff
