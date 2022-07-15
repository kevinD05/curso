string = input("introduce un string: ")

print(f"\nTodas las letras son minisculas?: {string.islower () }")
string = string.lower()
print(f"string en minusculas: {string}")

print(f"\nTodas las letras estan en mayusculas?: {string.isupper () }")
print(f"string en mayusculas: {string.upper () }")
print(f"string original: {string}")