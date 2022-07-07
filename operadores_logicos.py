#conjuncion

print("Conjuncion (and)")

num_uno = int(input("escribe un numero mayor 2 o menor a 5: "))
if num_uno < 2 and num_uno > 5:
   print("el numero", num_uno ,"cumple con la condicion.\n")
else:
    print("el numero", num_uno,"no cumple con la condicion.\n")

#disyucion

print("disyuncion (or)")

palabra = input("para cumplir la condicion escribe 'si' o 'yes': ")
if palabra == "si" or palabra == "yes":
    print("la condicion se cumplio.\n")
else:
    print("la condicion no se cumplio.\n")

#negacion

print("negacion (not)")

num_uno = int(input("introduce un numero igual a 5: "))
if not num_uno == 5:
    print("\n el numero es diferente de cinco y si cumple la condicion.\n")
else:
    print("\n el numero es igual a cinco y no cumple la condicion.\n")