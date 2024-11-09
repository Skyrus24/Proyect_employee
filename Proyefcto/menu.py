import empleado
import gestion_empleados


def menu_Princ():
    pass

    
def menu_gestion():
    print("¡Bienvenido al sistema!.\n"
            "1- Registrar un empleado.\n"
            "2- Actualizar datos de un empleado.\n"
            "3- Consultar datos de un empleado.\n"
            "4- Eliminar un empleado.\n"
            "5- Atrás.\n")
    opcion_gestion()


def opcion_gestion():
        op = int(input("Ingrese su opción: "))
        # Op 1 = Registro
        if op == 1:
            emp = empleado.Empleado()
            


if __name__ == "__main__":
    pass
            




