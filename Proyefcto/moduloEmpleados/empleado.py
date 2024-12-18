# Gestión de Empleados:Registro y actualización de información personal y laboral de los empleados. (nro Legajo, nombre, apellido, fecha nacimiento, dirección, barrio, ciudad, trabajos anteriores, puestos, años de empresa)
from moduloEmpleados.contrato import Contrato
from utility.utility import pedir_alpha
import utility.utility as utl
class Empleado:
    # inicializa los legajos en 1
    legajo = 1
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
        self.idlegajo = None
        self.registro()


    def registro(self):
        # Registrar todos los datos del empleado
        utl.cl()
        print("Registro del trabajador.")
        self.nombre = utl.pedir_str("Ingrese nombre del trabajador: ")
        self.apellido = utl.pedir_str("Ingrese apellido del trabajador: ")
        self.ci = utl.pedir_ent("Ingrese cédula de identidad del trabajador: ")
        self.fecha_nac = utl.fecha_formato("Ingrese la fecha de nacimiento(DD/MM/YYYY): ")
        self.direc = utl.pedir_alpha("Ingrese dirección del trabajador: ")
        self.barrio = utl.pedir_alpha("Ingrese barrio del trabajador: ")
        self.ciudad = utl.pedir_alpha("Ingrese ciudad del trabajador: ")

        # Asigna un número de legajo y automáticamente suma +1
        self.idlegajo = Empleado.legajo
        Empleado.legajo += 1

        # Llama a la función de registrar trabajos
        self.regist_trabajos()
        
        # Ejecuta una instancia del objeto contrato, para almacenarse en empleado.
        cont = Contrato(self)

        

    # Registra trabajos anteriores del empleado
    def regist_trabajos(self):
        empresa = utl.pedir_alpha("Ingrese su antigua empresa (0 para salir): ")
        if empresa == "0":
            empresa = ""
        else:
            puesto = utl.pedir_str("Ingrese su antiguo puesto: ")
            año = utl.pedir_ent("Ingrese sus años de empresa: ")
            trabajos_ant = [empresa,puesto,año]
            self.trabajos_anteriores.append(trabajos_ant)
            self.regist_trabajos()

    
    def actualizar_datos(self):
        while True:
            utl.cl()
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
                utl.cl()
                print(f"Nombre actual: {self.nombre}.")
                self.nombre = utl.pedir_str("Ingrese el nuevo nombre: ")
                print("¡Dato actualizado con éxito!")
            elif opcion == "2":
                utl.cl()
                print(f"Apellido actual: {self.apellido}.")
                self.apellido = utl.pedir_str("Ingrese el nuevo apellido: ")
                print("¡Dato actualizado con éxito!")
            elif opcion == "3":
                utl.cl()
                print(f"Fecha actual: {self.fecha_nac}.")
                self.fecha_nac = utl.fecha_formato("Ingrese la nueva fecha de nacimiento: ")
                print("¡Dato actualizado con éxito!")
            elif opcion == "4":
                utl.cl()
                print(f"Dirección actual: {self.direc}.")
                self.direc = utl.pedir_alpha("Ingrese la nueva dirección: ")
                print("¡Dato actualizado con éxito!")
            elif opcion == "5":
                utl.cl()
                print(f"Barrio actual: {self.barrio}.")     
                self.barrio = utl.pedir_alpha("Ingrese el nuevo barrio: ")
                print("¡Dato actualizado con éxito!")
            elif opcion == "6":
                utl.cl()
                print(f"Ciudad actual: {self.ciudad}.")
                self.ciudad = utl.pedir_alpha("Ingrese la nueva ciudad: ")
                print("¡Dato actualizado con éxito!")
            elif opcion == "7":
                utl.cl()
                print(f"Cédula actual: {self.ci}.")
                self.ci = utl.pedir_ent("Ingrese la nueva cédula de identidad: ")
                print("¡Dato actualizado con éxito!")
            elif opcion == "0":
                print("Saliendo del menú de actualización.")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                
                


    # Registra para imprimir los datos cada que se requiera
    def imprimir_datos(self):
        utl.cl()
        print("Datos del empleado: \n"
              f"Nombre(s): {self.nombre}\n"
              f"Apellido(s): {self.apellido}\n"
              f"Fecha de nacimiento: {self.fecha_nac}\n" 
              f"Dirección:{self.direc}\n"
              f"Barrio: {self.barrio}\n"
              f"Ciudad:{self.ciudad}\n"
              f"Cédula de identidad:{self.ci}")
        for empresa in self.trabajos_anteriores:
            print(f"Trabajo anterior: {empresa[0]}\n"
                  f"Puesto: {empresa[1]}\n"
                  f"Años de empresa: {empresa[2]}\n")
        
if __name__  == "__main__":
    emp = Empleado()