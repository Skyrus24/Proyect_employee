from moduloEmpleados.empleado import Empleado
from moduloEmpleados.gestionEmpleados import Empleados
import utility.utility as u
ne = Empleados()
# menú que gestionará todo lo relacionado a la gestion de empleados
def menu_gestion():
    u.cl()
    print("Menú del empleado. ¿Qué desea hacer?.\n"
            "1- Registrar un empleado.\n"
            "2- Actualizar datos de un empleado.\n"
            "3- Listar nómina de empleados.\n"
            "4- Eliminar un empleado.\n"
            "5- Atrás.\n")
    opcion_gestion()


# parte lógica del menú de gestión de empleados
def opcion_gestion():
    try:
        op = int(input("Ingrese su opción: "))
        
        if op == 1:
            # Opción 1: Registrar empleado
            emp = Empleado()
            ne.añadir_emp(emp)
            
        elif op == 2:
            # Opción 2: Actualizar datos de un empleado
            ne.actualizar_emp()
        elif op == 3:
            # Opción 3: Listar empleados
            ne.listar_emp()
        elif op == 4:
            # Opción 4: Eliminar un empleado.
            ne.eliminar_emp()
        elif op ==5:
            # acá irá la llamada al menú principal
            pass
        else:
            print("Opción inválida")
            opcion_gestion()
                
    except ValueError:
        print("Ingrese una opción numérica")
        opcion_gestion()

