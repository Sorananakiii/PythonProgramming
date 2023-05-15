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

# assign an object
a1 = Employee("aka", 20000, "cai")
a1.showdata()

# isinstance method
# check whether input create from Employee class or not
print(isinstance(a1, Employee))
# return class name that build em3
print(a1.__class__)