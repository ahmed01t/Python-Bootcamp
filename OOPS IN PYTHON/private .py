class customer:
    def __init__(self,number,password):
        self.number=number
        self.__password=password # make private bby adding underscore
    def __hello():
        print("welcome to our bank sir")
c1=customer(123455,0000)
print(c1.number)
print(c1.__password) # both will give error hello and this function 
print(c1.__hello())