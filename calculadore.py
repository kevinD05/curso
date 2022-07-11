from pickletools import int4
from tkinter import ROUND


print("calculadora con una sola variable \n")

print("****************")
print("menu de opciones")
print("****************")

print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. division entera")
print("6. exponente")
print("7. modulo o resto \n")

numero = int(input("introduce la opcion deseada: "))

if numero == 1:
    print("elgiste suma \n")
    numero = int(input("introduce el primer numero: "))
    numero += int(input("introduce el segundo numero: "))
    print("el resultado de la suma es:", numero)

elif numero == 2:
     print("elgiste resta \n")
     numero = int(input("introduce el primer numero: "))
     numero -= int(input("introduce el segundo numero: "))
     print("el resultado de la resta es:", numero)


elif numero == 3:
    print("elgiste multiplicacion \n")
    numero = int(input("introduce el primer numero: "))
    numero *= int(input("introduce el segundo numero: "))
    print("el resultado de la multiplicacion es:", numero)

elif numero == 4:
    print("elgiste divicion \n")
    numero = float(input("introduce el primer numero: "))
    numero /= float(input("introduce el segundo numero: "))
    print("el resultado de la divicion entera es:", round(numero, 2))

elif numero == 5:
    print("elgiste divicion entera \n")
    numero = int(input("introduce el primer numero: "))
    numero //= int(input("introduce el segundo numero: "))
    print("el resultado de la divicion entera es:", numero)

elif numero == 6:
    print("elgiste exponente \n")
    numero = int(input("introduce el primer numero: "))
    numero **= int(input("introduce el segundo numero: "))
    print("el resultado del exponente es:", numero)

elif numero == 7:
    print("elgiste modulo o resto \n")
    numero = int(input("introduce el primer numero: "))
    numero %= int(input("introduce el segundo numero: "))
    print("el resultado del modulo o resto es:", numero)

else:
    print("la opcion elegida no existe, vuelva a intetar.")
