class Super:
    def __init__(self):
        self.supVal = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVal = 12

object = Sub()

print(object.subVal)
print(object.supVal)