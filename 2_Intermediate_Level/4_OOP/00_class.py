# class is prototype of object, to create an object we need to build a class of its structure
# object is build from class with Attribute/Data member and behavior/Method
# - Attribute/Data member, what class is
# - behavior/Method, what class can do

# define a class
class Employee:
        
    # Constructor
    def __init__(self, name ,salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        
    def showdata(self):
        print(f"NAME : {self.name}")
        print(f"SALARY : {self.salary}")
        print(f"DEPARTMENT : {self.department}")