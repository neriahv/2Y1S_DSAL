import random

garage = ["Innova", "Fortuner", "LC300"]

removeCar = random.randrange(0,2)

print("Garage : ", garage)
print("Randomly Picked Car : ", garage[removeCar])

newCar = input("New Car : ")

if removeCar == 0:
    remove1 = garage.pop(2)
    remove2 = garage.pop(1)
    garage.pop(removeCar)
    garage.insert(removeCar, newCar)
    garage.insert(1, remove2)
    garage.insert(2, remove1)

elif removeCar == 1:
    remove1 = garage.pop(2)
    garage.pop(removeCar)
    garage.insert(removeCar, newCar)
    garage.insert(2, remove1)

elif removeCar == 2:
    garage.pop(removeCar)
    garage.insert(2,newCar)

print("Garage : ", garage)