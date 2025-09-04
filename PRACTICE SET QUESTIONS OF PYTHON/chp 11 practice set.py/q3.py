class employee:
    salary=20000
    increment=20
    @property
    def salary_increment(self):
        return self.salary+self.salary*(self.increment/100)
    @salary_increment.setter
    def salary_increment(self,salary):
        self.increment=((salary/self.salary)-1)*100
e=employee()
print(e.salary_increment)
e.salary_increment=24000 
print(e.increment)