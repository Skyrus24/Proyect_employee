import datetime
import inspect
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


    def puesto(self):
        while True:
            self.puesto = input("Ingrese el puesto del trabajador: ")
            if self.puesto == "":
                print("El puesto no puede ser vacio")
            else:
                break


    def sueldo(self):
        sueld_min = 2798309
        while True:
            try:
                self.sueldo = int(input("Ingrese el sueldo del trabajador: "))
                if self.sueldo < sueld_min:
                    print("ERROR: El sueldo no puede ser menor al sueldo minimo.")
                else:
                    break
            except ValueError:
                print("ERROR: Debe ingresar solo el monto del sueldo")
    
    
    def registro(self):
        # Asignar la fecha de firma del contrato
        self.fecha_contrato()
        
        # Asigna un número de legajo y automáticamente suma +1
        self.idlegajo = Contrato.legajo
        Contrato.legajo += 1
        
        # Define un puesto para el contrato
        self.puesto()
        
        # Define un sueldo
        self.sueldo()
        
        
        

        
        
        

if __name__ == "__main__":    
    contrato = Contrato()
    contrato.registro()
    

    
    # contr = Contrato()
    # print(contr.idlegajo)
    