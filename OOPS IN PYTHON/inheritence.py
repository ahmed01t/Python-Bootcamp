class Car:
    colour="black"
    @staticmethod
    def start():
        print("start the car")
    def stop():
        print("stop the car")
class toyota(Car):
    def __init__(self,name):
        self.name=name
car1=toyota("fortuner")
car2=toyota("legender")
print(car1.start())
print(car1.colour)