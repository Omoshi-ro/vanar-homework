from os import system
system("CLS")
class Laptop:
    def __init__(self, model, price, rate, description = "", year = ""):
        self.model       = model
        self.price       = price
        self.rate        = rate
        self.description = description
        self.year        = year

listOfLaptops = []
listOfLaptops.append(Laptop("Asus", 7000, 400, "very good laptop"))
listOfLaptops.append(Laptop("Apple", 5000, 300, "bad feedback"))
listOfLaptops.append(Laptop("Lenovo", 4000, 200, "gets hot very fast"))
listOfLaptops.append(Laptop("Acer", 4000, 200, description = "fancy"))
listOfLaptops.append(Laptop("HP", 4000, 200, year = "1989"))
choice = int(input(f"Enter number from 1 to {len(listOfLaptops)}: "))

while choice>len(listOfLaptops):
  choice = int(input(f"Please enter a correct number - 1 to {len(listOfLaptops)}: "))

neededLaptop = listOfLaptops[choice-1]
print(f"{neededLaptop.model} has the price {neededLaptop.price} and a monthly rate of {neededLaptop.rate}, has the description {neededLaptop.description}, and year {neededLaptop.year}")