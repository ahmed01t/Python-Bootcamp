class animals:
    def __init__ (self,name):
        self.name=name

class pets(animals):
    pass
class dog(pets):
    @staticmethod
    def bark():
        pass