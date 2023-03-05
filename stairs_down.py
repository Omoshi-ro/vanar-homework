from os import system
system("CLS")
n = int(input("Enter the number of stairs: "))
for steps in range(n, 0, -1):
    print(" " * (steps - 1) * 2 + "--")