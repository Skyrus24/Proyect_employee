import datetime
import empleado
class Contrato:
    # inicializa los legajos en 0
    legajo = 0


    def __init__(self, objeto):
        
        self.nombre = getattr(objeto, "nombre")
        self.fecha = None
        self.puesto = str
        self.salario = int
        self.tipo_contrato = int
        self.ci = getattr(objeto, "ci")
        self.registro()
    
    
    def fecha_contrato(self):
        self.fecha = input("Ingrese la fecha de contrato del empleado(DD/MM/YYYY): ")
        # comprueba si la fecha ingresada está en el formato correcto, de no ser así, reiniciará 
        try:
            self.fecha = datetime.datetime.strptime(self.fecha, "%d/%m/%Y").date()
        except:
            print("Formato de fecha incorrecto(Debe ingresar Día/Mes/año. Ejemplo: 24/08/2006)")
            self.fecha_contrato()

    # función recursiva para verificar que un input no esté vacío
    def no_input(self, x):
        while True:
            if x.strip() == "":
                print("La entrada no puede estar vacía")
                self.no_input()
            else:
                break
        
            
            
    
    def registro(self):
        self.fecha_contrato()
        
        # Asigna un número de legajo y automáticamente suma +1
        self.idlegajo = Contrato.legajo
        Contrato.legajo += 1
        
        self.puesto = input("Ingrese el puesto del trabajador: ")
        self.no_input(self.puesto)
        
        self.

        
        
        

if __name__ == "__main__":    
    contrato = Contrato()
    contrato.registro()
    

    
    # contr = Contrato()
    # print(contr.idlegajo)
    