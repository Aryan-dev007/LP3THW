#Alter Before and After

class Parent(object):

    def altered(self):
        print("Parent Altered()")

class Child(Parent):

    def altered(self):
        print("Child Before Parent Altered()")

        super().altered()            #super(Child, self)

        print("Child After Parent altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()


