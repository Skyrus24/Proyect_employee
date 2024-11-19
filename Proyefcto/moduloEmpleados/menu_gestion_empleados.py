import utility.utility as utl
from moduloEmpleados.empleado import Empleado
def menu_gestion_empleados(empleados):
    while True:
        utl.cl() 
        print("\nMenú de Gestión de Empleados")
        print("1- Agregar Empleado")
        print("2- Mostrar Empleados")
        print("3- Actualizar datos de un empleado")
        print("4- Eliminar un empleado")
        print("5- Salir")

        try:
            op = int(input("Ingrese su opción: "))
            if op == 1:
                emp = Empleado()
                empleados.añadir_emp(emp)  # Modifica directamente el objeto Empleados
                utl.wait()
            elif op == 2:
                empleados.listar_emp()  # Consulta directamente el objeto Empleados
                utl.wait()
            elif op == 3:
                empleados.actualizar_emp()
                utl.wait()
            elif op == 4:
                empleados.eliminar_emp()
                utl.wait()
            elif op == 5:
                print("Saliendo del menú de empleados.")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese una opción numérica.")
