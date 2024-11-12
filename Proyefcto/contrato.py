import datetime
class Contrato:
    # inicializa los legajos en 0
    legajo = 0


    def __init__(self, objeto):
        # No sabía que existía esta función, sirve para obtener un atributo de un objeto enviado.
        self.nombre = getattr(objeto, "nombre")
        self.fecha = None
        self.puesto = str
        self.salario = int
        self.tipo_contrato = int
        self.ci = getattr(objeto, "ci")
        self.registro()
    
    
    def registro(self):
        # Asignar la fecha de firma del contrato
        self.fecha_contrato()
        
        # Asigna un número de legajo y automáticamente suma +1
        self.idlegajo = Contrato.legajo
        Contrato.legajo += 1
        
        # Define un puesto para el contrato
        self.puesto()
        
        # Definir tipo de contrato
        self.tipo_contrato()
    
    
    def fecha_contrato(self):
        self.fecha = input("Ingrese la fecha de contrato del empleado(DD/MM/YYYY): ")
        try:
        # comprueba si la fecha ingresada está en el formato correcto, de no ser así, reiniciará 
            self.fecha = datetime.datetime.strptime(self.fecha, "%d/%m/%Y").date()
        except:
            print("Formato de fecha incorrecto(Debe ingresar Día/Mes/año. Ejemplo: 24/08/2006)")
            self.fecha_contrato()


    def puesto(self):
        # Definir puesto del trabajador
        while True:
            self.puesto = input("Ingrese el puesto del trabajador: ")
            # Verificar que no esté vacío
            if self.puesto == "":
                print("El puesto no puede ser vacio")
            else:
                break


    
    
    def tipo_contrato(self):
        while True:
            try:
                print("Ingrese su tipo de contrato:\n1- Fijo\n2- Temporal\n3- Por horas")
                op = int(input("Ingrese su opción: "))
                # En base a esta opción, se calculará las asistencias y el sueldo.
                if op == 1:
                    self.tipo_contrato = "Contrato Fijo"
                    self.sueldo(op)
                    break
                elif op == 2:
                    self.tipo_contrato = "Contrato Temporal"
                    self.sueldo(op)
                    break
                elif op == 3:
                    self.tipo_contrato = "Por horas"
                    self.sueldo(op)
                    break
                else:
                    print("ERROR: Valor ingresado inválido")
            except ValueError:
                print("Ingrese un valor correcto de tipo de contrato")
          
        
    def sueldo(self, op):
        # Establecer una variable del sueldo mínimo actual
        sueld_min = 2798309
        sueld_min_horas = sueld_min / 192 # Se divide ya que se trabajan 192 horas en promedio por mes.
        while True:
            try:
                if op == 1 or op == 2:
                    self.sueldo = int(input("Ingrese el sueldo del trabajador: "))
                    # Verificar que el sueldo ingresado no sea menor al sueldo mínimo
                    if self.sueldo < sueld_min:
                        print(f"ERROR: El sueldo no puede ser menor al sueldo minimo({sueld_min}).")
                    else:
                        break
                else:
                    sueld_horas = int(input("Ingrese el sueldo por horas del trabajador."))
                    if sueld_horas < sueld_min_horas:
                        print(f"ERROR: El sueldo por horas no debe ser menor a {sueld_min_horas}")
            except ValueError:
                print("ERROR: Debe ingresar solo el monto del sueldo.")
        
