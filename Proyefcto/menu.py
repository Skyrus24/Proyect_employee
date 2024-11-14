from empleado import Empleado
from employees import Empleados
import utility as u
ne = Empleados()

def menu_Princ():
    pass


# menú que gestionará todo lo relacionado a la gestion de empleados
def menu_gestion():
    u.cl()
    print("Menú del empleado. ¿Qué desea hacer?.\n"
            "1- Registrar un empleado.\n"
            "2- Actualizar datos de un empleado.\n"
            "3- Consultar datos de un empleado.\n"
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
            
                
    except ValueError:
        pass

