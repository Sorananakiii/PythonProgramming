class Employee:
        
    _minSalary = 15000
    _maxSalary = 500000 
    companyName = "GG"
    # Constructor
    def __init__(self, name ,salary, department):
        # public attribute
        self.__name = name
        self.__salary = salary
        self._department = department
        
    def _showdata(self):
        print(f"NAME : {self.__name}")
        print(f"SALARY : {self.__salary}")
        print(f"DEPARTMENT : {self._department}")
        
    def _getIncome(self, bonus=0):
        return self.__salary * 12 + bonus
    
    def __str__(self):
        return "Name {}, Department {}, Salary {}, Annual_Income {}".format(self.__name, 
                                                                              self._department, 
                                                                              self.__salary,
                                                                              self._getIncome())