class Flower:
    stem = 'green'
    def __init__(self, petals = True, thorns = False):
        self.petals = petals
        self.thorns = thorns
        
flower = Flower(False)
flower.__leaves = True # type: ignore
print(flower.__dict__)