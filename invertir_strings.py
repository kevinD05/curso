string = input("introduce un string para invertirlo: ")
string_reserved = ""

for character in string: 
    string_reserved = character + string_reserved  
    
print(f"string invertido: {string_reserved}")