from os import system
system("CLS")

grades = {
   "Math"   : 9,
   "English": 8,
   "Anatomy": 7
}

grades["English"]     = 10
grades["Informatics"] = 10

for discipline, grade in grades.items():
    print(discipline +": " + str(grade))
print()