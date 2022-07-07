print("Introduce dos numeros a comparar: \n")

num_uno = int(input("introduce el primer numero: "))
num_dos = int(input("introduce el segundo numero: "))

print("\n Los numeros a comprar son:", num_uno, "y", num_dos,"\n")

if num_uno == num_dos:
    print("es igual...")

if num_uno != num_dos:
    print("es diferente...")

if num_uno < num_dos:
    print("son menor...")

if num_uno > num_dos:
    print("es mayor...")

if num_uno <= num_dos:
    print("es menor o igual...")

if num_uno >= num_dos:
    print("es mayor igual...")