class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def show(self):
        print(f" your role is{self.role} your salary is {self.salary} your department is {self.department}")
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineering","IT","70000")
e1=engineer("ahmed",20)
e1.show()