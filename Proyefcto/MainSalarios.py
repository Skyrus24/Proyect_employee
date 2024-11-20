#El main de salarios es donde todos los modulos se utilizan para mostrar un menu que
#permite saber y modificar los datos del empleado con respecto a su nomina salarial

#IMportamnos las funciones de los demas modulos
from SistemadeNominas import SistemaNomina
from informe_empleado import generar_informe_empleado
from RecursosHumanos import generar_informe_detallado_recursos_humanos

#Creamos el menu principal de creacion, modificacion y carga de datos
def menuprincipall():
    sistema_sal = SistemaNomina()
#Ingreso al usuario a un bucle infinito
    while True:
        print("\n=== Sistema de Nómina ===")
        print("1. Agregar nuevo empleado")
        print("2. Buscar y modificar datos de un empleado")
        print("3. Mostrar informe detallado del empleado")
        print("4. Mostrar informe de Recursos Humanos (IPS)")
        print("5. Salir")

        opcion_sal = input("Seleccione una opción: ")
        # Con la opcion uno ingresamos el empleado usando la funcion de SistemadeNominas.py
        if opcion_sal == "1":
            sistema_sal.ingresar_empleado()
        #Con la opcion 2 podemos  modificar los datos del empleado usando la funcion de SistemadeNominas,.py
        elif opcion_sal == "2":
            ci_buscado_sal = int(input("Ingrese el CI del empleado a modificar: "))
            empleado_sal = sistema_sal.buscar_por_ci(ci_buscado_sal)
            if empleado_sal:
                modificar_datos_empleado(empleado_sal)
                print("Datos del empleado actualizados con éxito.")
                #Este imput evita que el programa vuelva al menu despues de most    rar los datos
                input("\nPresione Enter para volver al menú...")
            else:
                print("Empleado no encontrado.")
                input("\nPresione Enter para volver al menú...")
        # COn la opcion 3 imprimimos el informe generado en la fuincion del modulo InformePagos.py
        elif opcion_sal == "3":
            ci_buscado_sal = int(input("Ingrese el CI del empleado para generar el informe: "))
            empleado_sal = sistema_sal.buscar_por_ci(ci_buscado_sal)
            if empleado_sal:
                print(generar_informe_empleado(empleado_sal))
                input("\nPresione Enter para volver al menú...")
            else:
                print("Empleado no encontrado.")
                input("\nPresione Enter para volver al menú...")
        #Con la opcion 4 imprimimos el informe a Recursos Humanos
        elif opcion_sal == "4":
            ci_buscado_sal = int(input("Ingrese el CI del empleado para el informe de Recursos Humanos: "))
            empleado_sal = sistema_sal.buscar_por_ci(ci_buscado_sal)
            if empleado_sal:
                print(generar_informe_detallado_recursos_humanos(empleado_sal))
                input("\nPresione Enter para volver al menú...")
            else:
                print("Empleado no encontrado.")
                input("\nPresione Enter para volver al menú...")

        elif opcion_sal == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para volver al menú...")

def modificar_datos_empleado(empleado_sal):

    #esta funcion nos permite modificar los datos de un empleado existente,
    #mantenemos el valor si el usuario no escribe nada

    print(f"\n=== Modificar datos de {empleado_sal.nombre_sal} ===")
    try:
        empleado_sal.nombre_sal = input(f"Nombre [{empleado_sal.nombre_sal}]: ") or empleado_sal.nombre_sal
        empleado_sal.salarioPorHora_sal = int(input(f"Salario por hora [{empleado_sal.salarioPorHora_sal}]: ") or empleado_sal.salarioPorHora_sal)
        empleado_sal.horasTrabajadas_sal = int(input(f"Horas trabajadas [{empleado_sal.horasTrabajadas_sal}]: ") or empleado_sal.horasTrabajadas_sal)
        empleado_sal.productividad_sal = int(input(f"Productividad/ventas del mes [{empleado_sal.productividad_sal}]: ") or empleado_sal.productividad_sal)
        empleado_sal.porcentajeComision_sal = float(input(f"Porcentaje de comisión (en %) [{empleado_sal.porcentajeComision_sal * 100}]: ") or (empleado_sal.porcentajeComision_sal * 100)) / 100
        empleado_sal.horasExtras_sal = int(input(f"Horas extras trabajadas [{empleado_sal.horasExtras_sal}]: ") or empleado_sal.horasExtras_sal)
        empleado_sal.horasNocturnas_sal = int(input(f"Horas nocturnas y festivas trabajadas [{empleado_sal.horasNocturnas_sal}]: ") or empleado_sal.horasNocturnas_sal)
        empleado_sal.bonoAsistencia_sal = int(input(f"Bono de asistencia [{empleado_sal.bonoAsistencia_sal}]: ") or empleado_sal.bonoAsistencia_sal)
        empleado_sal.minimoHorasAsistencia_sal = int(input(f"Mínimo de horas para el bono de asistencia [{empleado_sal.minimoHorasAsistencia_sal}]: ") or empleado_sal.minimoHorasAsistencia_sal)
        empleado_sal.seguroSocial_sal = int(input(f"Monto del seguro social [{empleado_sal.seguroSocial_sal}]: ") or empleado_sal.seguroSocial_sal)
        empleado_sal.prestamos_sal = int(input(f"Monto de préstamos [{empleado_sal.prestamos_sal}]: ") or empleado_sal.prestamos_sal)
        empleado_sal.adelantos_sal = int(input(f"Monto de adelantos [{empleado_sal.adelantos_sal}]: ") or empleado_sal.adelantos_sal)
    except ValueError:
        print("Error: Asegúrese de ingresar datos válidos.")
