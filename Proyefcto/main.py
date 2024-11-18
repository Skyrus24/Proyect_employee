from moduloEmpleados.gestionEmpleados import Empleados
from menu_gestion_empleados import menu_gestion_empleados
from menu_gestion_asistencia import Asistencia, menu_asistencia
import utility.utility as utl

# Crear una instancia única del objeto Empleados
gestion_empleados = Empleados()

# Crear una instancia única de Asistencia
gestion_asistencia = Asistencia(gestion_empleados)

def menu_principal():
    while True:
        utl.cl()
        print("\nMenú Principal")
        print("1- Gestión de Empleados")
        print("2- Gestión de Asistencia")
        print("3- Salir")

        try:
            op = int(input("Ingrese su opción: "))
            if op == 1:
                menu_gestion_empleados(gestion_empleados)
            elif op == 2:
                menu_asistencia(gestion_asistencia)
            elif op == 3:
                print("Saliendo del sistema.")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese una opción numérica.")

if __name__ == "__main__":
    menu_principal()
