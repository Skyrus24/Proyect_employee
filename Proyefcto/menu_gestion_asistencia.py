import utility.utility as utl

'''class Asistencia:
    def __init__(self, empleados):
        self.empleados = empleados
        self.asistencia = {}

    def inicializar_asistencia(self):
        dias = 30  # Por ejemplo, 30 días
        for emp in self.empleados.employeeslist:
            self.asistencia[emp.idlegajo] = [0] * dias
        print("Asistencia inicializada correctamente.")

    def registrar_asistencia(self):
        legajo = int(input("Ingrese el legajo del empleado: "))
        empleado = next((e for e in self.empleados.employeeslist if e.idlegajo == legajo), None)
        if empleado:
            dia = int(input("Ingrese el día (1-30): ")) - 1
            estado = int(input("Ingrese el estado (0 = ausente, 1 = presente): "))
            self.asistencia[legajo][dia] = estado
            print(f"Asistencia registrada para {empleado.nombre}.")
        else:
            print("Empleado no encontrado.")
'''

def menu_asistencia(asistencia):
    dayofmonth = utl.dias_del_mes()
    while True:
        print("\nMenú de Gestión de Asistencia")
        print("1- Inicializar Asistencia")
        print("2- Registrar Asistencia")
        print("3- Mostrar Asistencia")
        print("4- Salir")

        try:
            op = int(input("Ingrese su opción: "))
            if op == 1:
                asistencia.inicializar_asistencias(dayofmonth)
            elif op == 2:
                asistencia.registrar_asistencia()
            elif op == 3:
                for legajo, registro in asistencia.asistencia.items():
                    print(f"Legajo {legajo}: {registro}")
            elif op == 4:
                print("Saliendo del menú de asistencia.")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese una opción numérica.")
