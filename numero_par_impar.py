print("****************************************************")
print("*programa que determina si un numero es par o impar*")
print("****************************************************")

numero = int(input("por favor introduce un numero entero: "))
if numero % 2 == 0:
    print("el numero", numero, "es par")
elif numero % 2 == 1:
    print("el numero", numero, "es impar")