from os import system
system("CLS")
big_ship = int(input("Enter an number: (1 till 10) "))

for x in range(1,11):
    if big_ship == x:
      print("W", end="")
    elif x == big_ship -1:
      print("w", end="")
    elif x == big_ship +1:
      print("w", end="")
    else:
      print( "~", end="")