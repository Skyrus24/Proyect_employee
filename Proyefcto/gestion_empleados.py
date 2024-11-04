import empleado

class HistorialSalarial:
    def __init__(self):
        self.historial = []  # Almacenar el historial laboral y salarial

    def agregar_registro(self, fecha, puesto, salario, tipo_contrato):
        registro = {
            'fecha': fecha,
            'puesto': puesto,
            'salario': salario,
            'tipo_contrato': tipo_contrato
        }
        self.historial.append(registro)

    def imprimir_historial(self):
        for registro in self.historial:
            print(f"Fecha: {registro['fecha']}, Puesto: {registro['puesto']}, "
                  f"Salario: {registro['salario']}, Tipo de contrato: {registro['tipo_contrato']}")


class GestionHistorico:
    def __init__(self):
        self.historials = {}  # Almacena los historiales de empleados por id de legajo

    def agregar_historial(self, empleado, fecha, puesto, salario, tipo_contrato):
        if empleado.idlegajo not in self.historials:
            self.historials[empleado.idlegajo] = HistorialSalarial()
        self.historials[empleado.idlegajo].agregar_registro(fecha, puesto, salario, tipo_contrato)

    def imprimir_historial(self, empleado):
        if empleado.idlegajo in self.historials:
            print(f"Historial de {empleado.nombre} {empleado.apellido}:")
            self.historials[empleado.idlegajo].imprimir_historial()
        else:
            print(f"No hay historial registrado para {empleado.nombre} {empleado.apellido}.")

