from os import system
system("CLS")
parking_places= 7
free_place    = 2
print("#" * parking_places * 5)
for place_index in range(1, parking_places +1):
    if place_index - 1 == free_place:
        print("|   |", end="")
    else:
        print("| X |", end="")
print("\n","#" * parking_places * 5, sep="")
# sep = argumentul sep este folosit pentru a separa diferite valori.
# Implicit, separatorul este un singur spațiu. 
# Parametrul sep este utilizat premordial pentru a transforma spațiul dintr-un string într-o valoare atribuită de către programator.
# sep a fost introdus in Python în versiunea 3.x
# sep și end in Python au o fucție similară venind să schimbe conținutul a funcției ”print” și felul cum este tipărită pe consolă.  