from xml.dom import InvalidCharacterErr


string = input("introduce una frase: ")
palabra = input("introduce la palabra que deasas eliminar: ")
substring = ""

indice = string.find(palabra)
substring = string[0 : indice] + string[indice +len(palabra) + 1 :]

print(f"cadena resultante: {substring}")