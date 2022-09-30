from unicodedata import name

class Drink:
  name = ""
  price = 0

  def __init__(self, name, price):
    self.name = name
    self.price = price

drinks = dict()
drinks["D0001"] = Drink("コーヒー", 350)
drinks["D0002"] = Drink("紅茶", 400)
drinks["D0003"] = Drink("ほうじ茶", 300)

print(drinks.get("D0001").name)

for key in drinks.keys():
  print(key)

for drink in drinks.values():
  print(drink.name)
  print(drink.price)

foodMap = dict()
foodMap["F0001"] = "Apple"
foodMap["F0002"] = "Peach"
foodMap["F0003"] = "Grape"

selectFood = foodMap["F0002"]
print(selectFood)

for food in foodMap.values():
  print(food)
