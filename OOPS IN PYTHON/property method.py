class stuednt:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    @property
    def percentage(self):
        return (self.phy+self.chem+self.maths)/3
s1=stuednt(98,88,99)
print(f"{s1.percentage:.2f}%")
s1.phy=55
print(f"{s1.percentage:.2f}%")