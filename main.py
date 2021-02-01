class Ingredient:
    def __init__(self, name, purchPrice, purchUnit, useUnit, wstPrcnt):
        self.name = name
        self.purchPrice = purchPrice
        self.purchUnit = purchUnit
        self.useUnit = useUnit
        self.wstPrcnt = wstPrcnt

# calculates cost as purchased per use

    def useRaw(self, use):
        return float(self.purchPrice) * float(use)


# calculates cost as purchased per use

    def useYield(self, use):
        return float(use) / (1 - float(self.wstPrcnt) / 100) * float(
            self.purchPrice)

sugar = Ingredient('sugar', 0.65, 'lb', 'cup', 0)
apple = Ingredient('apple', 1.18, 'lb', 'lb', 30)

print(apple.useRaw(8))
print(round(apple.useYield(8), 2))
"""
import gc

for obj in gc.get_objects():
    if isinstance(obj, Ingredient):
        print(obj.name)

"""
