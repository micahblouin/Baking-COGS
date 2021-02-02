name = input('Please enter the Ingredient Name: ')
purchPrice = input('Please enter the most recent Purchase Price: ')
purchUnit = input('Please enter the most recent Purchase Unit: ')
useUnit = input('Please enter the Usage Unit: ')
wstPrcnt = input('Please enter the Waste Percentage: ')


class Ingredient:
    def __init__(self, name, purchPrice, purchUnit, useUnit, wstPrcnt):
        self.name = name
        self.purchPrice = purchPrice
        self.purchUnit = purchUnit
        self.useUnit = useUnit
        self.wstPrcnt = wstPrcnt

# calculates cost as purchased per use

    def useRaw(self, use):
        return round(float(self.purchPrice) * float(use),2)


# calculates cost as purchased per use

    def useYield(self, use):
        return float(use) / (1 - float(self.wstPrcnt) / 100) * float(
            self.purchPrice)

Ingredient1 = Ingredient(name, purchPrice, purchUnit, useUnit, wstPrcnt)

print(f'$ {Ingredient1.useRaw(4)}')

#sugar = Ingredient('sugar', 0.65, 'lb', 'cup', 0)
#apple = Ingredient('apple', 1.18, 'lb', 'lb', 30)

#print(apple.useRaw(8))
#print(round(apple.useYield(8), 2))

"""
import gc

for obj in gc.get_objects():
    if isinstance(obj, Ingredient):
        print(obj.name)

"""
