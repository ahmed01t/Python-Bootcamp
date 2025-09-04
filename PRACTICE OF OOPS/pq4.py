class calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
            print(f"square is {self.num*self.num}")
    def cube(self):
            print(f"cube is {self.num*self.num*self.num}")
    def root(self):
            print(f"square root is {self.num**1/2}")
a=calculator(12)
a.square()
a.cube()
a.root()