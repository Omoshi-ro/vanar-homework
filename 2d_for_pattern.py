rx = 5
ry = 5
print()

for y in range(1,11):
     
    for x in range(1,11):
        if x == rx and y == rx:
            print("R", end=" ")
        elif x == rx and y == ry - 1:
            print("+", end=" ")
        elif x == rx and y == ry + 1:
            print("+", end=" ")
        elif x == rx - 1 and y == ry:
            print("+", end=" ")
        elif x == rx + 1 and y == ry:
            print("+", end=" ")
        elif x == rx - 1 and y == ry - 1:
            print("+", end=" ")
        elif x == rx + 1 and y == ry + 1:
            print("+", end=" ")
        elif x == rx + 1 and y == ry - 1:
            print("+", end=" ")
        elif x == rx - 1 and y == ry + 1:
            print("+", end=" ")
        else:    
            print(".", end = " ")
    print()
print()