first_name = input("nombre: ")
last_name = input("apellido: ")
full_name = f"{first_name} {last_name}"

print()
print(f"El formato del metodo title () se ha aplicado?: {full_name.istitle () }")
print(f"Aplicando el metodo titl (): {full_name.istitle () }")
print(f"Volvemos a imprimir el nombre: {full_name}")

print()
full_name = full_name.title ()
print(f"El formato del metodo title () se ha aplicado?: {full_name.istitle () }")
print(f"se ha  aplicado el metodo  title () de manera permanente: {full_name}")