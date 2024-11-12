from empleado import Empleado
from employees import Empleados
import os

ne = Empleados()

def menu_Princ():
    pass

    
def menu_gestion():
    cl()
    print("Menú del empleado. ¿Qué desea hacer?.\n"
            "1- Registrar un empleado.\n"
            "2- Actualizar datos de un empleado.\n"
            "3- Consultar datos de un empleado.\n"
            "4- Eliminar un empleado.\n"
            "5- Atrás.\n")
    opcion_gestion()


def opcion_gestion():
        op = int(input("Ingrese su opción: "))
        # Opción 1: Registro
        if op == 1:
            emp = Empleado()
            

def cl():
    os.system('cls')
    
    
if __name__ == "__main__":
    pass
            




