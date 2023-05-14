from employee import Employee

class Developer(Employee):
    __departmentName = "developer"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self._exp = experience
        self._skill = skill
        
    def _showdata(self):
        super()._showdata()
        print(f"EXPERIENCE : {str(self._exp)}")
        print(f"SKILL : {self._skill}")
        print()
        
    def __str__(self):
        return super().__str__() + ", EXPERIENCE {}, SKILL {}".format(self._exp, self._skill)