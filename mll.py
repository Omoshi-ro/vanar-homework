from os import system
system("CLS")
marks = [
    [
    [6, 8, 9, 9, 10], 
    [9, 9, 9, 9, 9],
    [7, 7, 7, 7, 8],
    ],
    [
    [9, 8, 8, 8, 9],
    [9, 5, 6, 2, 9],
    [1, 7, 7, 7, 6],
    ]
]
for gi in range(len(marks)):
    print("Group", gi + 1)
    print("------------------")
    print("Lesson:    1 2 3 4 5")
    for si in range(3):
        print(f"student {si+1}: {' '.join([str(marks[gi][si][li]) for li in range(5)])}")
        print()
# print()