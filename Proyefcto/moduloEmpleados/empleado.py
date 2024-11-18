# Gestión de Empleados:Registro y actualización de información personal y laboral de los empleados. (nro Legajo, nombre, apellido, fecha nacimiento, dirección, barrio, ciudad, trabajos anteriores, puestos, años de trabajo)
from contrato import Contrato
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
        self.nombre = input("Ingrese nombre del trabajador: ")
        self.apellido = input("Ingrese apellido del trabajador: ")
        self.ci = int(input("Ingrese cédula de indentidad del trabajador: "))
        self.fecha_nac = utl.fecha_formato()
        self.direc = input("Ingrese dirección del trabajador: ")
        self.barrio = input("Ingrese barrio del trabajador: ")
        self.ciudad = input("Ingrese ciudad del trabajador: ")
        
         # Asigna un número de legajo y automáticamente suma +1
        self.idlegajo = Empleado.legajo
        Empleado.legajo += 1
        
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
        for trabajo in self.trabajos_anteriores:
            print(f"Trabajo anterior: {trabajo[0]}\n"
                  f"Puesto: {trabajo[1]}\n"
                  f"Años de trabajo: {trabajo[2]}")
        
if __name__  == "__main__":
    emp = Empleado()