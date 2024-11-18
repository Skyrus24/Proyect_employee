from moduloEmpleados.gestionEmpleados import Empleados
import utility.utility as utl

class Asistencia:
    def __init__(self, empleados: Empleados):
        self.empleados = empleados
        self.asistencias = {}  # Estructura: {idlegajo: [estado_del_dia, ...]}
        self.razones = {}  # Estructura: {idlegajo: {día: razón}}

    def inicializar_asistencias(self, dias_mes: int):
        """
        Inicializa las asistencias de todos los empleados a 0 (ausente) para los días del mes.
        """
        for empleado in self.empleados.employeeslist:
            self.asistencias[empleado.idlegajo] = [0] * dias_mes
            self.razones[empleado.idlegajo] = {}

    def registrar_asistencia(self):
        """
        Registra la asistencia de un empleado en un día específico.
        """
        utl.cl()
        try:
            idlegajo = int(input("Ingrese el número de legajo del empleado: "))
            dia = int(input("Ingrese el día del mes (1-31): ")) - 1  # Índice basado en 0
            if idlegajo in self.asistencias and 0 <= dia < len(self.asistencias[idlegajo]):
                print("Seleccione el estado:\n"
                      "0. Ausente\n"
                      "1. Presente\n"
                      "2. Llegada tarde\n"
                      "3. Permiso/licencia\n"
                      "4. Vacaciones/incapacidad")
                estado = int(input("Ingrese el estado (0-4): "))

                if estado in [3, 4]:
                    razon = input("Ingrese la razón para el estado seleccionado: ")
                    self.razones[idlegajo][dia] = razon

                self.asistencias[idlegajo][dia] = estado
                print("Asistencia registrada correctamente.")
            else:
                print("Número de legajo o día inválido.")
        except ValueError:
            print("Error: Debe ingresar valores numéricos válidos.")

    def consultar_asistencia(self):
        """
        Muestra la asistencia completa de un empleado.
        """
        utl.cl()
        try:
            idlegajo = int(input("Ingrese el número de legajo del empleado: "))
            if idlegajo in self.asistencias:
                print(f"Asistencias del empleado con legajo {idlegajo}:")
                for dia, estado in enumerate(self.asistencias[idlegajo], start=1):
                    estado_desc = ["Ausente", "Presente", "Llegada tarde", "Permiso/licencia", "Vacaciones/incapacidad"][estado]
                    razon = self.razones[idlegajo].get(dia - 1, "N/A")
                    print(f"Día {dia}: {estado_desc} (Razón: {razon if estado in [3, 4] else 'No aplica'})")
            else:
                print("Legajo no encontrado.")
        except ValueError:
            print("Error: Debe ingresar un número de legajo válido.")
    