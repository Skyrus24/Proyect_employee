# Gestión de Empleados:Registro y actualización de información personal y laboral de los empleados. (nro Legajo, nombre, apellido, fecha nacimiento, dirección, barrio, ciudad, trabajos anteriores, puestos, años de trabajo)
import  gestion_empleados
from contrato import Contrato
from employees import Empleados as list_emp
class Empleado:
    # Construye los atributos
    def __init__(self):
        self.nombre = str
        self.apellido = str
        self.fecha_nac = None
        self.direc = str
        self.barrio = str
        self.ciudad = str
        self.ci = int
        self.trabajos_anteriores = []
        self.registro()

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


    # Registrar todos los datos del empleado
    def registro(self):
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
        
        # Añadir a la lista de 
        lista_empleados = list_emp()
        envio = self
        lista_empleados.añadir_emp(envio)



    # Registra para imprimir los datos cada que se requiera
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nFecha de nacimiento: {self.fecha_nac}, Dirección:{self.direc}\nBarrio: {self.barrio}\nCiudad:{self.ciudad}")
        print("")
        for trabajo in self.trabajos_anteriores:
            print(f"Trabajo anterior: {trabajo[0]}\nPuesto: {trabajo[1]}\nAños de trabajo: {trabajo[2]}")
        

if __name__ == "__main__":
    test = Empleado()
    test.imprimir_datos()
    
    


