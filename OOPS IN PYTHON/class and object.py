class employe:
    name="ahmed"
    salary=12334
    age=12
ahmed=employe()
print(ahmed.name,ahmed.salary)
class student:
    def __init__(self,fullname):
        self.name=fullname
s1=student("ahmed")
print(s1.name)
s2=student("ali")
print(s2.name)