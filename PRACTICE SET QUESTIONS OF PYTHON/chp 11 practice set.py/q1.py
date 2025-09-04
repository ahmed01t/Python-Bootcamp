class two_d:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"{self.i},{self.j}")
class three_d(two_d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"{self.i},{self.j},{self.k}")
a=two_d(1,2)
b=three_d(5,6,4)
a.show()
b.show()