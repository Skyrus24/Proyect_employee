from MainSalarios import menuprincipall
from moduloEmpleados.gestionEmpleados import Empleados
from moduloEmpleados.menu_gestion_empleados import menu_gestion_empleados
from moduloAsistencia.asistencia import Asistencia
from menu_gestion_asistencia import menu_asistencia
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
        print("3- Gestión de Salarios")
        print("4- Salir")

        try:
            op = int(input("Ingrese su opción: "))
            if op == 1:
                menu_gestion_empleados(gestion_empleados)
            elif op == 2:
                menu_asistencia(gestion_asistencia)
            elif op == 3:
                menuprincipall()
            elif op == 4:
                print("Saliendo del sistema.")
                break
            else:
                print("Opción inválida.")
                utl.wait()
        except ValueError:
            print("Ingrese una opción numérica.")
            utl.wait()

if __name__ == "__main__":
    menu_principal()
