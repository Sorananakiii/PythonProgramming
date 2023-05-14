from employee import Employee

class Sale(Employee):
    __departmentName = "sale"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.area = area
        
    def _showdata(self):
        super()._showdata()
        print(f"AREA : {self.area}")
        print()
        
    def __str__(self):
        return super().__str__() + ", AREA {}".format(self.area)