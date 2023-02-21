from os import system
system("CLS")
start_n = int(input("Enter the starting number: "))
end_n   = int(input("Enter the ending number: "))

if start_n < end_n:
    n = start_n
    while n <= end_n:
        print(n)
        n += 1
else:
    n = start_n
    while n >= end_n:
        print(n)
        n -= 1