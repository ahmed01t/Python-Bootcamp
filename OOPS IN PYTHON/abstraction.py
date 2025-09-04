class car:
    def __init__(self):
        self.clutch=False
        self.acc=False
        self.race=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")
car1=car()
car1.start()
# hiding unecessary information outside the class is called abstraction
