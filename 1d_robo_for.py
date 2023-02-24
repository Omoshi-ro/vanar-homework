# remake 1d robo game -> for loop
from os import system
robox  = 5
roboHP = 100
roboBT = 100
roboH  = 10
coinx  = 1
bombx  = 7
bombz  = 2
length = 20
option = " "
#game loop
while True:
#Draw Map 
    system("CLS")
    print("\n")

    for x in range(1, length + 1):
        if x == robox:
            print("R", end=" ")
        elif x == bombx:
            print("B", end =" ")
        elif x == bombz:
            print("B2", end =" ")
        elif x == roboH:
            print("H", end =" ")
        elif x == coinx:
            print("$", end=" ")
        else:
            print(".", end=" ")

    print("\nHP: ", roboHP)
    print("BT: ", roboBT, "%")
    print("Coin: ", coinx)
    print("\n")
# Map #
# Read input
    option = input(">>>>> ")
# decide
    if option == "a" and robox > 1:
        robox -= 1
        roboBT -= 1
    if option == "b" and robox < length:
        robox += 1
        roboBT -=1
#check if bomb
    if robox == bombx or robox == bombz:
        roboHP -= 20
        bombx +=2
        bombz -=1
    if roboHP <= 0:
        system("CLS")
        print("You are dead!")
        break
    if robox == roboH:
        roboHP += 10
        roboBT += 1
    if roboBT == 0:
        system("CLS")
        print("No more battery, you lost the game!")
        break
    if robox == coinx:
        coinx +=2
        if coinx >=12:
            system("CLS")
            print("Congratulations! You passed the game.")
            break
    elif option == "x":
        system("CLS")
        print("Thank you for playing! ")
        break


