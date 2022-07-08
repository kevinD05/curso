print("* programa para determinar el numero mayor entre tres*")

num_uno = int(input("introduce el primer numero: "))
num_dos = int(input("introduce el segundo numero: "))
num_tres = int(input("introduce el tercer numero: "))

if num_uno > num_dos and num_uno > num_tres:
    print("el numero", num_uno, "Es el numero mas grande de los tres.")
else:
    if num_dos > num_tres:
        print("el numero", num_dos, "Es el numero mas grande de los tres.")
    else:
        print("es el numero", num_tres, "es el numero mas grende de los tres.")