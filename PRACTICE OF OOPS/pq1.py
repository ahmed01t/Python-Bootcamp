class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        result=3.14*(self.radius*self.radius)
        print(f"area is {result}")
    def perimeter(self):
        result2=2*3.14*self.radius
        print(f"perimeter is {result2}")
c1=circle(12)
c1.area()
c1.perimeter()