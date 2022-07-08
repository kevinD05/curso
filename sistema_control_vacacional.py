print("***************************************")
print("* Sistema de control vacacional rappi *")
print("*************************************** \n")

nombre_empleado = input("por favor introduce el nombre del empleado: ")
clave_despartameto  = int(input("por favor introduce la clave del departemanto: "))
antiguedad_empleado = float(input("por favor introduce los años laborales del empleado: "))

if clave_despartameto == 1:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, "tiene derecho a 6 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
         print("el empleado", nombre_empleado,"tiene derecho a 14 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
         print("el empleado", nombre_empleado, "tiene derecho a 16 dias de vacaciones.")
    else:
        print("el empleado", nombre_empleado, "aun no tiene derecho a vacaciones.")

elif clave_despartameto == 2:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, "tiene derecho a 7 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
         print("el empleado", nombre_empleado,"tiene derecho a 15 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
         print("el empleado", nombre_empleado, "tiene derecho a 22 dias de vacaciones.")
    else:
        print("el empleado", nombre_empleado, "aun no tiene derecho a vacaciones.")


elif clave_despartameto == 3:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("El empleado", nombre_empleado, "tiene derecho a 10 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
         print("el empleado", nombre_empleado,"tiene derecho a 20 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
         print("el empleado", nombre_empleado, "tiene derecho a 30 dias de vacaciones.")
    else:
        print("el empleado", nombre_empleado, "aun no tiene derecho a vacaciones.")

else:
    print("la clave de departamento no existe, vuelve a intentarlo.")
