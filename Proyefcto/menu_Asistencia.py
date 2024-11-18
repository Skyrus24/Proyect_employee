from moduloEmpleados.gestionEmpleados import Empleados
import utility.utility as utl

class Asistencia:
    def __init__(self, empleados: Empleados):
        self.empleados = empleados
        self.asistencia = {}  # Diccionario para almacenar asistencias por legajo

    def inicializar_asistencia(self):
        dias = utl.dias_del_mes()
        for emp in self.empleados.employeeslist:
            self.asistencia[emp.idlegajo] = [0] * dias
        print("Asistencia inicializada correctamente para todos los empleados.")
        utl.wait()

    def registrar_asistencia(self):
        legajo = self.seleccionar_empleado()
        if legajo is not None:
            dia = self.seleccionar_dia()
            estado = self.seleccionar_estado()
            if estado in [3, 4]:
                razon = input("Ingrese la razón del estado (permiso/vacaciones/incapacidad): ").strip()
                self.asistencia[legajo][dia] = (estado, razon)
            else:
                self.asistencia[legajo][dia] = estado
            print(f"Estado del día {dia + 1} actualizado correctamente.")
            utl.wait()

    def mostrar_asistencia(self):
        for legajo, registro in self.asistencia.items():
            empleado = next((emp for emp in self.empleados.employeeslist if emp.idlegajo == legajo), None)
            if empleado:
                print(f"\nEmpleado: {empleado.nombre} {empleado.apellido} (Legajo: {legajo})")
                for dia, estado in enumerate(registro):
                    if isinstance(estado, tuple):
                        print(f"Día {dia + 1}: {estado[0]} - {estado[1]}")
                    else:
                        print(f"Día {dia + 1}: {estado}")
        utl.wait()

    def seleccionar_empleado(self):
        while True:
            try:
                legajo = int(input("Ingrese el número de legajo del empleado: "))
                if any(emp.idlegajo == legajo for emp in self.empleados.employeeslist):
                    return legajo
                print("Legajo no encontrado.")
            except ValueError:
                print("Debe ingresar un número válido.")

    def seleccionar_dia(self):
        while True:
            try:
                dia = int(input("Ingrese el día del mes (1-31): "))
                if 1 <= dia <= 31:
                    return dia - 1
                print("Día inválido. Debe estar entre 1 y 31.")
            except ValueError:
                print("Debe ingresar un número válido.")

    def seleccionar_estado(self):
        while True:
            try:
                print("Seleccione el estado:\n0 = Ausente\n1 = Presente\n2 = Llegada tarde\n3 = Permiso/licencia\n4 = Vacaciones/incapacidad")
                estado = int(input("Ingrese el estado: "))
                if estado in [0, 1, 2, 3, 4]:
                    return estado
                print("Estado inválido.")
            except ValueError:
                print("Debe ingresar un número válido.")

def menu_asistencia(asistencia: Asistencia):
    while True:
        utl.cl()
        print("Menú de Gestión de Asistencia")
        print("1- Inicializar Asistencia")
        print("2- Registrar Asistencia")
        print("3- Mostrar Asistencia")
        print("4- Salir")

        try:
            op = int(input("Ingrese su opción: "))
            if op == 1:
                asistencia.inicializar_asistencia()
            elif op == 2:
                asistencia.registrar_asistencia()
            elif op == 3:
                asistencia.mostrar_asistencia()
            elif op == 4:
                print("Saliendo del menú de asistencia.")
                utl.wait()
                break
            else:
                print("Opción inválida.")
                utl.wait()
        except ValueError:
            print("Ingrese una opción numérica.")
            utl.wait()
