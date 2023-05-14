from employee import Employee

class Accounting(Employee):
    __departmentName = "accouting"
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self._age = age
    
    def _showdata(self):
        super()._showdata()
        print(f"AGE : {str(self._age)}")
        print()

    def __str__(self):
        return super().__str__() + ", AGE {}".format(self._age)