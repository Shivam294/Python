class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("Woof!")

class Chihuahua(Dog):
    def __init__(self, name):
        Dog.__init__(self,name)
        self.size = "Small"

    def __str__(self) -> str:
        return super().__str__()

pet1 = Dog("Max")
pet2 = Dog("Daisy")
print(Dog.__name__)
print(type(pet1).__name__)
print("Module is", pet2.__module__)
print(Chihuahua.__str__)
for base in Chihuahua.__bases__:
    print("Superclass name is", base)