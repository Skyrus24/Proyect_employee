import empleado
import gestion_empleados
def menu():
    print("¡Bienvenido al sistema!.\n"
            "1- Registrar un empleado.\n"
            "2- Actualizar datos de un empleado.\n"
            "3- Mantenimiento de historial laboral y salarial.\n"
            "4- Mantenimiento de contratos y tipos de empleados.\n"
            "5- Salir.\n")
   opcion()


def opcion():
        op = input("Ingrese su opción: ")
        # Op 1 = Registro
        if op == 1:
            emp = empleado.Empleado()
            emp.registro()#
            




