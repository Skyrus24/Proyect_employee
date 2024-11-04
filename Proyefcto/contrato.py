class Contrato:
    # inicializa los legajos en 0
    idlegajo = 0


    def __init__(self):
        # Asigna un número de legajo
        Contrato.idlegajo += 1
        self.idlegajo = Contrato.idlegajo