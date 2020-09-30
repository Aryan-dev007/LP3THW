# Animal is-a object (yes,sort of confusing) look at the extra credit.
class Animal(object):
    pass

## Dog is-a Animal.
class Dog(Animal):

    def __init__(self,name):
        #Dog has-a name.
        self.name = name
    

# Cat is a Animal.
class Cat(Animal):

    def __init__(self,name):
        #Cat has-a name.
        self.name = name

#Person is a object
class Person(object):

    def __init__(self,name):
        # Person has-a name.
        self.name = name
        self.pet = None  # Person has-a pet.

# Employee is a person.
class Employee(Person):

    def __init__(self,name,salary):
        # Employee has-a name and salary.

        super(Employee, self).__init__(name)

        self.salary = salary
        # Employee has a salary.
class Fish(object):            #Fish is-a object.
    pass     

class Salmon(Fish):    #Salmon is-a Fish.
    pass

class Halibut(Fish):  #Halibut is-a fish.
    pass


rover = Dog("Rover")  # Rover is-a dog.

satan = Cat("Satan")  # Satan is-a cat.

mary = Person("Mary") # Mary is-a Person.

mary.pet = satan  # From mary get attribute pet set it to satan // satan is pet cat of mary.

frank = Employee("Frank",120000) #Frank is an instance of Employee.

frank.pet = rover  # From frank(instance of employee) get attribute pet set it to rover.

flipper = Fish() # flipper is an instance of fish / alternatively property of fish.

crouse = Salmon() # crouse is an instance of Salmon / alternatively property

harry = Halibut()  # harry is an instance of Halibut/ harry is property (name) of the fish.

