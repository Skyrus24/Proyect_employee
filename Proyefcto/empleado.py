# Gestión de Empleados:Registro y actualización de información personal y laboral de los empleados. (nro Legajo, nombre, apellido, fecha nacimiento, dirección, barrio, ciudad, trabajos anteriores, puestos, años de trabajo)
import  gestion_empleados as ge
class Empleado:
    # Construye los atributos
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.fecha_nac = None
        self.direc = None
        self.barrio = None
        self.ciudad = None
        self.trabajos_anteriores = []


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
        self.fecha_nac = input("Ingrese fecha de nacimiento del trabajador(DD/MM/AA): ")
        self.direc = input("Ingrese dirección del trabajador: ")
        self.barrio = input("Ingrese barrio del trabajador: ")
        self.ciudad = input("Ingrese ciudad del trabajador: ")
        self.regist_trabajos()
        self.contrato()



    # Registra para imprimir los datos cada que se requiera
    def imprimir_datos(self):
        print(f"Nro legajo:{self.idlegajo}, Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha de nacimiento: {self.fecha_nac}, Dirección:{self.direc}, Barrio: {self.barrio}, Ciudad:{self.ciudad}")
        for trabajo in self.trabajos_anteriores:
            print(f"Trabajo anterior: {trabajo[0]}\nPuesto: {trabajo[1]}\nAños de trabajo: {trabajo[2]}")


    def contrato(self):


if __name__ == "__main__":
    test = Empleado()
    test.registro()
    test.imprimir_datos()
