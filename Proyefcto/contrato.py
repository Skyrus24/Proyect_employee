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
            self.fecha = input("Ingrese la fecha de contrato del trabajador(DD/MM/AAAA): ")
            fecha_format = datetime.strptime( self.fecha,"%d / %m / %Y")
            print(self.fecha)
        except:
            pass


if __name__ == "__main__":
    contrato = Contrato()
    contrato.registro()
    print(contrato.fecha)
    
    # contr = Contrato()
    # print(contr.idlegajo)
    