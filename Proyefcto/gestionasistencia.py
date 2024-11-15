# REspecto a la presencia y los estados.
# 1- Presente
# 2- Llegada tardía
# 3- Se paga medio salario
# 4- Caso especial, salario completo
def presencia():
    present = input("¿El empleado está presente?\n1- Sí\n2- No\nIngrese una opción: ")
    if present == 1:
        tard = input("¿El empleado llegó tarde?\n1- Sí\n2- No")
        if tard == 1:
            estado = 2
            retraso = int(input("Ingrese el tiempo de tardanza en minutos."))
        elif tard == 2:
            estado = 1
        else:
            print("Opción inválida, revise su opción e intente nuevamente.")
    elif present == 2:
        estado = 0
    else:
        print("Opción ingresada inválida.")

# debido a la ambiguedad de las caractreristicas exigidas se tomará lo siguiente:
# 1- Las licencias y permisos serán remuneradas con medio jornal.
#
def permisos():
    op = int(input("¿Qué desea registrar?\n1- Licencias\n2- Permisos\n3- Vacaciones\n4- Incapacidades"))    
    if op == 1:
        razon = input("Ingrese la razón de su licencia.")
        estado = 3
    elif op == 2:
        razon = input("Ingrese la razón de su permiso.")
        estado = 3
    elif op == 3:
        fecha_inicio = int(input("Ingrese fecha de inicio de las vacaciones"))
        fecha_final = int(input("Ingrese fecha de fin de las vacaciones"))
            

    