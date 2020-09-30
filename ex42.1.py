# Animal is-a object (yes,sort of confusing) look at the extra credit.
class Animal(object):
    pass

## Dog is-a Animal.
class Dog(Animal):

    def __init__(self,name,voice):
        #Dog has-a name.
        self.name = name
        self.voice = voice
    def name():
        print(self.name)

    def voice():
        print(self.voice)


# Cat is a Animal.
class Cat(Animal):

    def __init__(self,name,voice):
        #Cat has-a name.
        self.name = name
        self.voice =voice

    def name():
        print(name)

    def voice():
        print(voice)


#Person is a object
class Person(object):

    def __init__(self,name,pet):
        # Person has-a name.
        self.name = name
        self.pet = pet # Person has-a pet.

# Employee is a person.
class Employee(Person):

    def __init__(self,name,pet):
        # Employee has-a name and salary.

        super(Employee, self).__init__(name,pet)


    def salary(x):
        print("Enter you daily wage.")
        x = int(input()) * 30 + 150          # 150 minimum wage scheme per day
        print("Your salary is --->",x)

class Fish(object):            #Fish is-a object.
    def __init__(self,weight):
        self.weight = weight
        self.water = None
class Salmon(Fish):    #Salmon is-a Fish.
    def __init__(self,weight):

        super(Salmon,self).__init__(weight)

    def fins(a):
        print("Fins are sharp.")

class Halibut(Fish):  #Halibut is-a fish.
    def __init__(self,weight):

        super(Halibut,self).__init__(weight)

    def fins(a):
        print("Fins are not that sharp.")


r = {"cats":[ 'satan', "pog" ] , "dogs":["rover","blackie"]}
rover = Dog(r["dogs"][1].capitalize(),"woof!") # Rover is-a dog.
dogv = rover.voice
dogn = rover.name
print(dogn)
print(dogv)

satan = Cat(r["cats"][1],"meowdarchod")  # Satan is-a cat.
catn = satan.name
catv = satan.voice
print(catn)
print(catv)

mary = Person("Mary","satan") # Mary is-a Person.

mary.pet = satan  # From mary get attribute pet set it to satan // satan is pet cat of mary.
print("Mary has pet ---> ",catn)

frank = Employee("Frank","elephant")#Frank is an instance of Employee.
frank.salary()

fpet = frank.pet # From frank(instance of employee) get attribute pet set it to rover.
print("Frank's pet is ",fpet)

flipper = Fish(23) # flipper is an instance of fish / alternatively property of fish.
flipper.water = "salty and fresh water."
print("Fish lives in",flipper.water)
print("Fish I got has weight = ",flipper.weight)


crouse = Salmon(42) # crouse is an instance of Salmon / alternatively property
crouse.water = "Fresh water."
# crouse.weight = 34 in this line I am re-assigning weight.
print("Weight of Salmon I got is ",crouse.weight)
print("Salmon lives in {}".format(crouse.water))
crouse.fins()

bt = Halibut(24)
bt.water = "Salty"
print("Halibut has weight of ",bt.weight)
print("Halibut lives in  ",bt.water)
bt.fins()

class Relation(Animal,Fish,Person):
    def __init__(self,voice,weight,name):
        super(Relation).__init__(voice)

rel = Relation("woof",43,"pope")
print(rel.voice)
