# Neriah Faith L. Villapana
# DSAL / CS-202
# July 10, 2024

mylist = [ ]
while True:
        nickname = input ("Nickname: ")
        if nickname.isdigit():
                print("Incorrect data type. Please try again.")
                input("Nickname: ")
        
        age = input ("Age: ")
        if type(age) != int:
                print("Incorrect data type. Please try again.")
                input("Age: ")

        loc = input ("Location: ")
        if loc.isdigit():
                print("Incorrect data type. Please try again.")
                input("Location: ")

        break

