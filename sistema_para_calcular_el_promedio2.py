print('sistema para calcular el promedio')

nombre = input("cual es tu nombre: ")

matematicas = int(input(nombre +", ¿cual es tu nota de matematicas?:\n"))
ingles = int(input(nombre + ", ¿cual es tu nota de ingles?:\n"))
ciencia = int(input(nombre +", ¿cual es tu nota de cienca?:\n"))
 
promedio = float((matematicas + ingles + ciencia) / 3)
promedio = (promedio)

if promedio >= 6:
   print('felicidades '  + nombre +  ', aprobaste con promedio de:', promedio)
   print('felicidades '  + nombre +  ', aprobaste con promedio de:', round(promedio,2))

else:
    print('lo sientimos'  + nombre +  'has reprobado con un promedio de:', promedio)
    print('lo sientimos'  + nombre + 'has reprobado con un promedio de:', round(promedio,1))

print("fin.")