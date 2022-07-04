print('sistema para calcular el promedio')

nombre = input("cual es tu nombre: ")

matematicas = int(input(nombre +"cual es tu nota de matematicas:"))
ingles = int(input(nombre + "cual es tu nota de ingles:"))
ciencia = int(input(nombre +"cual es tu nota de cienca:"))
 
promedio = float((matematicas + ingles + ciencia) / 3)
promedio = (promedio)

if promedio >= 6:
   print('felicidades' + nombre + 'aprobaste con promedio de: ', promedio)
   
   print("fin.")
