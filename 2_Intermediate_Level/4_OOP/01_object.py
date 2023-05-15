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

a2 = Employee("abc", 500000, "cai_ocr")
a2.salary = 0
a2.showdata()