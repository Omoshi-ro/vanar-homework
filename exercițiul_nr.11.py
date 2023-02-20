from os import system
system("CLS")

big_ship = int(input("Enter an number: (1 till 10) "))
for x in range(1,11):
    if x == big_ship:
      print( "wWw", end="" )
    else:
      print( "~", end="" )
