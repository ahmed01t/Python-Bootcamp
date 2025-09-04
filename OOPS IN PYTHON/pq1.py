class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for value in self.marks:
            sum=sum+value
        print(f"hi{self.name}your average marks are:",sum/3)

s1=student("ahmed",[98,97,96])
s1.average()