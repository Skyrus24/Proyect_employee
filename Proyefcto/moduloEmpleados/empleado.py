# Gestión de Empleados:Registro y actualización de información personal y laboral de los empleados. (nro Legajo, nombre, apellido, fecha nacimiento, dirección, barrio, ciudad, trabajos anteriores, puestos, años de empresa)
from moduloEmpleados.contrato import Contrato
from utility.utility import pedir_str
import utility.utility as utl
class Empleado:
    # inicializa los legajos en 0
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
        self.idlegajo = None
        self.trabajos_anteriores = []
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
        empresa = input("Ingrese su antigua empresa (0 para salir): ")
        if empresa == "0":
            empresa = ""
        else:
            puesto = utl.pedir_str("Ingrese su antiguo puesto: ")
            año = input("Ingrese sus años de empresa: ")
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
                self.nombre = input("Ingrese el nuevo nombre: ")
                print("¡Dato actualizado con éxito!")
                utl.wait()
            elif opcion == "2":
                utl.cl()
                self.apellido = input("Ingrese el nuevo apellido: ")
                print("¡Dato actualizado con éxito!")
                utl.wait()
            elif opcion == "3":
                utl.cl()
                self.fecha_nac = utl.fecha_formato()
                print("¡Dato actualizado con éxito!")
                utl.wait()
            elif opcion == "4":
                utl.cl()
                self.direc = input("Ingrese la nueva dirección: ")
                print("¡Dato actualizado con éxito!")
                utl.wait()
            elif opcion == "5":
                utl.cl()
                self.barrio = input("Ingrese el nuevo barrio: ")
                print("¡Dato actualizado con éxito!")
                utl.wait()
            elif opcion == "6":
                utl.cl()
                self.ciudad = input("Ingrese la nueva ciudad: ")
                print("¡Dato actualizado con éxito!")
                utl.wait()
            elif opcion == "7":
                utl.cl()
                self.ci = int(input("Ingrese la nueva cédula de identidad: "))
                print("¡Dato actualizado con éxito!")
                utl.wait()
            elif opcion == "0":
                print("Saliendo del menú de actualización.")
                utl.wait()
                break
                return False
            else:
                print("Opción inválida. Intente de nuevo.")
                
                


    # Registra para imprimir los datos cada que se requiera
    def imprimir_datos(self):
        print(f"Nombre(s): {self.nombre}\n"
              f"Apellido(s): {self.apellido}\n"
              f"Fecha de nacimiento: {self.fecha_nac}\n" 
              f"Dirección:{self.direc}\n"
              f"Barrio: {self.barrio}\n"
              f"Ciudad:{self.ciudad}\n")
        for empresa in self.trabajos_anteriores:
            print(f"Trabajo anterior: {empresa[0]}\n"
                  f"Puesto: {empresa[1]}\n"
                  f"Años de empresa: {empresa[2]}")
        
if __name__  == "__main__":
    emp = Empleado()