import utility.utility as utl
# REspecto a la presencia y los estados.
# 1- Presente
# 2- Llegada tardía
# 3- Se paga medio salario
# 4- Caso especial, salario completo

# definiré una lista predeterminada con los meses de cada año
tamaño = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Revisará si el empleado está presente o no, si llego tarde y
def presencia(lista_Emp:list):
    try:
        for emp in lista_Emp:
            present = input("¿El empleado está presente?\n1- Sí\n2- No\nIngrese una opción: ")
            if present == 1:
                tard = input("¿El empleado llegó tarde?\n1- Sí\n2- No")
                if tard == "1":
                    estado = 2
                    retraso = int(input("Ingrese el tiempo de tardanza en minutos."))
                    return("Llegada tardía registrada correctamente"), retraso
                elif tard == "2":
                    estado = 1
                    return("Empleado presente registrado correctamente.")
                else:
                    print("Opción inválida, revise su opción e intente nuevamente.")
                    presencia()
            elif present == 2:
                estado = 0
            else:
                print("Opción ingresada inválida. Intente nuevamente.")
                presencia()
    except ValueError:
        print("ERROR: Valor ingresado inválido.")
        
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
        fecha_inicio = 
        fecha_final = int(input("Ingrese fecha de fin de las vacaciones"))
    elif op == 4:
        pass
    
    
def inicializar(lista_Emp):
    for emp in 


    