import datetime
class Contrato:
    # inicializa los legajos en 0
    legajo = 0


    def __init__(self, nombre, ci):
        # Asigna un número de legajo
        self.idlegajo = Contrato.legajo
        Contrato.legajo += 1
        self.nombre = nombre
        self.fecha = None
        self.puesto = str
        self.salario = int
        self.tipo_contrato = int
        self.ci = ci
    
    
    def fechalegajo(self):
        while True:
            self.fecha = input("Ingrese la fecha de contrato del empleado(DD/MM/YYYY): ")
            # comprueba si la fecha ingresada está en el formato correcto, de no ser así, reiniciará
            try:
                self.fecha = datetime.datetime.strptime(self.fecha, "%d/%m/%Y").date()
                print(self.fecha)
                break
            except:
                print("Formato de fecha incorrecto(Debe ingresar Día/Mes/año. Ejemplo: 24/08/2006)")

    
    def registro(self):
        self.fechalegajo()
        

if __name__ == "__main__":
    contrato = Contrato("abel", 65)
    contrato.registro()

    
    # contr = Contrato()
    # print(contr.idlegajo)
    