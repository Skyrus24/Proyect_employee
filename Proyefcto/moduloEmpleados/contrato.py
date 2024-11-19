import utility.utility as utl
class Contrato:
    def __init__(self, objeto):
        # No sabía que existía esta función, sirve para obtener un atributo de un objeto enviado.
        self.nombre = getattr(objeto, "nombre")
        self.fecha = None
        self.puesto = str
        self.salario = int
        self.tipo_contrato = int
        self.ci = getattr(objeto, "ci")
        self.idlegajo = getattr(objeto, "idlegajo")
        self.registro()
    
    
    def registro(self):
        # Asignar la fecha de firma del contrato
        self.fecha = utl.fecha_formato("Ingrese la fecha del contrato(DD/MM/YYYY): ")
        
        # Define un puesto para el contrato
        self.puesto()
        
        # Definir tipo de contrato
        self.tipo_contrato()


    def puesto(self):
        # Definir puesto del trabajador
        while True:
            self.puesto = utl.pedir_str("Ingrese el puesto del trabajador: ")
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
                # En base a esta opción, se calculará las asistencias y el salario.
                if op == 1:
                    self.tipo_contrato = "Contrato Fijo"
                    self.def_sueldo(op)
                    break
                elif op == 2:
                    self.tipo_contrato = "Contrato Temporal"
                    self.def_sueldo(op)
                    break
                elif op == 3:
                    self.tipo_contrato = "Por horas"
                    self.def_sueldo(op)
                    break
                else:
                    print("ERROR: Valor ingresado inválido")
            except ValueError:
                print("Ingrese un valor correcto de tipo de contrato")
          
        
    def def_sueldo(self, op):
        # Establecer una variable del salario mínimo actual
        sueld_min = 2798309
        sueld_min_horas = sueld_min / 192 # Se divide ya que se trabajan 192 horas en promedio por mes.
        while True:
            try:
                if op == 1 or op == 2:
                    self.salario = int(input("Ingrese el salario del trabajador: "))
                    # Verificar que el salario ingresado no sea menor al salario mínimo
                    if self.salario < sueld_min:
                        print(f"ERROR: El salario no puede ser menor al salario minimo({sueld_min}).")
                    else:
                        break
                else:
                    sueld_horas = int(input("Ingrese el salario por horas del trabajador."))
                    if sueld_horas < sueld_min_horas:
                        print(f"ERROR: El salario por horas no debe ser menor a {sueld_min_horas}")
            except ValueError:
                print("ERROR: Debe ingresar solo el monto del salario.")
        
    def imprimir_cont(self):
        print(f"La fecha de inicio del contrato es: {self.fecha}\n"
              f"El número del legajo es: {self.idlegajo}\n"
              f"El puesto es: {self.puesto}\n"
              f"El salario es: {self.salario}\n"
              f"El tipo de contrato es: {self.tipo_contrato}\n")