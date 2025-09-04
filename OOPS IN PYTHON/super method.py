class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class toyota_car(Car):
    def __init__(self,name,type):
        super().__init__(type)# super method if we dont pass type to parent class and wanted to print it it will generate error
        self.name=name
        super().start()
car1=toyota_car("prius","electric")
print(car1.type)