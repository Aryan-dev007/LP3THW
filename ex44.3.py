class Parent(object):

    def override(self):
        print("Parent override()")

    def implicit(self):
        print("Parent Implicit()")     # This will be inherit1.

    def altered(self):
        print("Parent altered()")

class Child(Parent):

    def override(self):                      # overrides the funtion in on line 3
        print("Child override()")

    def altered(self):
        print("Child, Before Parent altered()")

        super(Child, self).altered()  # will bring Parent() altered function

        print("Child After Parent altered()")


dad = Parent()
son = Child()


dad.implicit()
son.implicit()         #inherit 1 occurs here

dad.override()            #Parent override()
son.override()             # Child override()

dad.altered()          #Parent altered()  #child before parent altered --> child after parent altered
son.altered()          # Parent altered()

