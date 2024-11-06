from datetime import datetime

class Contrato:
    # inicializa los legajos en 0
    legajo = 0


    def __init__(self):
        # Asigna un número de legajo
        self.idlegajo = Contrato.legajo
        Contrato.legajo += 1
        self.fecha = None
        self.puesto = str
        self.salario = int
        self.tipo_contrato = int
           
    def registro(self):
        try:
            self.fecha_format = 0
            self.fecha = input("Ingrese la fecha de contrato del trabajador(DD/MM/AAAA): ")
            self.fecha_format = datetime.strftime(self.fecha,"%d/%m/%Y")
            print(self.fecha_format)
        except:
            pass


if __name__ == "__main__":
    contrato = Contrato()
    contrato.registro()
    print(contrato.fecha_format)
    
    # contr = Contrato()
    # print(contr.idlegajo)
    