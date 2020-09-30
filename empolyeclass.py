class Employees:
    """Common base class for all employees"""
    empcount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employees.empcount += 1

    def displaycount(self):
        print("Total number of employees" + Employees.empcount)

    def displayemployees(self):
        print("Name:" ,  self.name , "Salary:" , self.salary)           # carefully read its syntax

"""This would create an object of employee class"""
emp1 = Employees("Zara" , 2000)
emp2 = Employees("Hello" , 98090)

emp1.displayemployees()
emp2.displayemployees()

print("Total employees count: ",Employees.empcount)