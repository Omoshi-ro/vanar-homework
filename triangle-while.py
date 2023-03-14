from os import system
system("CLS")
size = int(input("Enter the size of triangle: "))
n = 0
while n <=size:
    print("." * (size - n), "+" * (2 * n + 1))
    n +=1

print()