# Gestión de Empleados:Registro y actualización de información personal y laboral de los empleados. (nro Legajo, nombre, apellido, fecha nacimiento, dirección, barrio, ciudad, trabajos anteriores, puestos, años de trabajo)
from contrato import Contrato
import datetime

class Empleado:
    # Construye los atributos
    def __init__(self):
        # Inicializa los datos del empleado
        self.nombre = str
        self.apellido = str
        self.fecha_nac = None
        self.direc = str
        self.barrio = str
        self.ciudad = str
        self.ci = int
        self.trabajos_anteriores = []
        self.registro()


    def ingresar_fecha(self, mensaje):
        while True:
            fecha = input(mensaje)
            try:
                return datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            except ValueError:
                print("Formato de fecha incorrecto. Debe ingresar Día/Mes/Año. Ejemplo: 24/08/2006")

    def registro(self):
        # Registrar todos los datos del empleado
        self.nombre = input("Ingrese nombre del trabajador: ")
        self.apellido = input("Ingrese apellido del trabajador: ")
        self.ci = int(input("Ingrese cédula de indentidad del trabajador: "))
        self.fecha_nac = input("Ingrese fecha de nacimiento del trabajador(DD/MM/AA): ")
        self.direc = input("Ingrese dirección del trabajador: ")
        self.barrio = input("Ingrese barrio del trabajador: ")
        self.ciudad = input("Ingrese ciudad del trabajador: ")
        
        # Llama a la función de registrar trabajos 
        self.regist_trabajos()
        
        # Ejecuta una instancia del objeto contrato, para almacenarse en empleado.
        cont = Contrato(self)
        

    # Registra trabajos anteriores del empleado
    def regist_trabajos(self):
        trabajo = input("Ingrese su antiguo trabajo (0 para salir): ")
        if trabajo == "0":
            trabajo = ""
        else:
            puesto = input("Ingrese su antiguo puesto: ")
            año = input("Ingrese sus años de trabajo: ")
            trabajos_ant = [trabajo,puesto,año]
            self.trabajos_anteriores.append(trabajos_ant)
            self.regist_trabajos()

    
    def actualizar_datos(self):
        while True:
            print("\nSeleccione el dato que desea actualizar:")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Fecha de nacimiento")
            print("4. Dirección")
            print("5. Barrio")
            print("6. Ciudad")
            print("7. Cédula de identidad")
            print("0. Salir")

            opcion = input("Ingrese el número de la opción: ")

            if opcion == "1":
                self.nombre = input("Ingrese el nuevo nombre: ")
            elif opcion == "2":
                self.apellido = input("Ingrese el nuevo apellido: ")
            elif opcion == "3":
                self.fecha_nac = self.ingresar_fecha("Ingrese la nueva fecha de nacimiento (DD/MM/YYYY): ")
            elif opcion == "4":
                self.direc = input("Ingrese la nueva dirección: ")
            elif opcion == "5":
                self.barrio = input("Ingrese el nuevo barrio: ")
            elif opcion == "6":
                self.ciudad = input("Ingrese la nueva ciudad: ")
            elif opcion == "7":
                self.ci = int(input("Ingrese la nueva cédula de identidad: "))
            elif opcion == "0":
                print("Saliendo del menú de actualización.")
                break
            else:
                print("Opción inválida. Intente de nuevo.")


    # Registra para imprimir los datos cada que se requiera
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nFecha de nacimiento: {self.fecha_nac}, Dirección:{self.direc}\nBarrio: {self.barrio}\nCiudad:{self.ciudad}")
        print("")
        for trabajo in self.trabajos_anteriores:
            print(f"Trabajo anterior: {trabajo[0]}\nPuesto: {trabajo[1]}\nAños de trabajo: {trabajo[2]}")
        
