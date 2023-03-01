from os import system
from time import sleep
from random import randint
# robot coords
rx     = 5
# bullet cords / -1 - not active
bx     = -1
by     = -1
# target coords
tx     = 5
ty     = 3
score  = 0
option = ""
while option != "x":
    # map
    system("CLS")
    for y in range(1,11):
        for x in range(1,11):
            if x == rx and y == 10:
                print("R", end=" ")
            elif x == bx and y == by:
                print("^", end=" ")
            elif x == tx and y == ty:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()
    print(f"Score: {score}")
    sleep(0.2)
    #bullet
    if by != - 1:
        by -= 1
        if bx == tx and by == ty:
           print("Hit!")
           ty = randint(1,7)
           tx = randint(1,10)
           by = - 1
           score += 1
        continue   
    option = input(">>> ")
    if option == "a":
        if rx > 1:
            rx -= 1
    if option == "d":
        if rx <10:
            rx += 1
    if option == " ":
        if by == -1:
            bx = rx
            by = 10 - 1