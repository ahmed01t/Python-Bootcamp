class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"+",self.img,"i")
    def __add__(self,num2): # dunder function
        newReal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newReal,newimg)
num1=complex(1 ,5)
num1.show()
num2=complex(4,8)
num2.show()
num3=num1+num2
num3.show()