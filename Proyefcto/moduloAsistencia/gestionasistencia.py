import utility.utility as utl

class gest_Asistencia:
    def __init__(self):
        self.razones = {}
        utl.dias_del_mes()
    

    def registrarAsistencia(self):
        while True:
            try:
                utl.cl()
                op = int(input("¿El empleado estuvo presente?\n1- Si\n2-No"))
                if op == 1:
                    subop = int(input("¿El empleado llegó tarde?\n1- Si\n2-No"))
                    if subop == 1:
                        while True:
                            try:
                                tardanza = int(input("Ingrese tiempo de tardanza en minutos"))
                            except ValueError:
                                print("ERROR: Debes ingresar un tiempo valido")
            except ValueError:
                pass
                
    
    def registrarOtros(self):
        pass
    
    
    
