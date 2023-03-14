from os import system
system("CLS")
print()
w = int(input("width: "))
h = int(input("height: "))

for r in range(h):
    for s in range(w):
        if r == 0 or r == h - 1:
            print("--", end= "")
        elif s == 0:
            print("| ", end= "")
        elif s == w - 1:
            print(" |", end= "")
        elif s == w // 2:
            print("|", end="")
        elif r == h // 2:
            print("--", end="")
        else:
            print("  ", end = "")
    print()
print()