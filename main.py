from pprint import pprint

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

print(f'New Ingredient Added! \n')
pprint(vars(Ingredient1))
