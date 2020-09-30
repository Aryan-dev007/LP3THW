class Other(object):

    def override(self):
        print("Other override().")

    def implicit(self):
        print("Other implicit().")

    def altered(self):
        print("Other Altered()")

class Child(object):

    def __init__(self):
        self.other = Other()      # setting up an variable

    def implicit(self):
        self.other.implicit()      # calling that class's function

    def override(self):
        print("Child override().")

    def altered(self):
        print("Child, Before OTHER altered()")
        self.other.altered()            # calling that class's function.
        print("Child, After OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

