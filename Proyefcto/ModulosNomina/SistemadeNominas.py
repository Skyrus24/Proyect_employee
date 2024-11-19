#Este modulo recauda los datos individuales para los calculos de nomina necesarios

from NominadePagos import calcular_nomina_empleado
from empleadoNomina import Empleado
from InformePagos import generar_informe_empleado
from RecursosHumanos import generar_informe_detallado_recursos_humanos

class SistemaNomina:
    def __init__(self):
        self.empleados_sal = []

    def agregar_empleado(self, empleado_sal):
        #Agrega un empleado a la lista, con append lo llevamos al final
        self.empleados_sal.append(empleado_sal)

    def buscar_por_ci(self, ci_sal):
        #Con el atributo ci buscamos el empleado por numero de ci
        for empleado_sal in self.empleados_sal:
            if empleado_sal.ci_sal == ci_sal:
                return empleado_sal
        return None

    def ingresar_empleado(self):
        print("Ingrese los datos del empleado:")
        try:
            ci_sal = int(input("CI: "))
            nombre_sal = input("Nombre: ")
            salarioPorHora_sal = int(input("Salario por hora: "))
            horasTrabajadas_sal = int(input("Horas trabajadas: "))
            productividad_sal = int(input("Productividad/ventas del mes: "))
            porcentajeComision_sal = int(input("Porcentaje de comisión (en %): ")) / 100
            horasExtras_sal = int(input("Horas extras trabajadas: "))
            horasNocturnas_sal = int(input("Horas nocturnas y festivas trabajadas: "))
            bonoAsistencia_sal = int(input("Bono de asistencia: "))
            minimoHorasAsistencia_sal = int(input("Mínimo de horas para el bono de asistencia: "))
            seguroSocial_sal = int(input("Monto del seguro social: "))
            prestamos_sal = int(input("Monto de préstamos: "))
            adelantos_sal = int(input("Monto de adelantos: "))

            empleado_sal = Empleado(
                ci_sal, nombre_sal, salarioPorHora_sal, horasTrabajadas_sal, productividad_sal,
                porcentajeComision_sal, horasExtras_sal, horasNocturnas_sal, bonoAsistencia_sal,
                minimoHorasAsistencia_sal, seguroSocial_sal, prestamos_sal, adelantos_sal
            )
            self.agregar_empleado(empleado_sal)
            print("\nEmpleado ingresado con éxito.\n")
        except ValueError:
            print("Error: Asegúrese de ingresar solo números donde se indique.\n")

    def imprimir_recibo_empleado(self, empleado_sal):
        informe_sal = generar_informe_empleado(empleado_sal)
        print(informe_sal)

    def imprimir_informe_ips_empresa(self, empleado_sal):
        informe_sal = generar_informe_detallado_recursos_humanos(empleado_sal)
        print(informe_sal)

