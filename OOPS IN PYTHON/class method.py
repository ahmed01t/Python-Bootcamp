class person:
    name="anonymus"
    #def__init__(self,name):
    #self.__class__.name="ahmed" (one mthod is this for changing in class name)
    #  class method
    @classmethod
    def changename(cls,name):
        cls.name=name
p1=person()
p1.changename("ahmed")
print(p1.name)
print(person.name)