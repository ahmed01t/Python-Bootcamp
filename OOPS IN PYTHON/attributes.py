class student:
    college_name="gcu"
    name="anonymous"# class attribute
    def __init__(self,name,salary):
        self.name=name#object attribute
        self.salary=salary
    def welcome(self):
        print("welcome student ",self.name)
s1=student("hamza",1234567)
print(s1.name)
s1.welcome()
