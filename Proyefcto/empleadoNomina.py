# empleadoNomina.py
# Clase de Empleado Dirigido al calculo de pago de Nomina Salarial

class Empleado:
    def __init__(self, ci_sal, nombre_sal, salarioPorHora_sal, horasTrabajadas_sal, productividad_sal, porcentajeComision_sal, horasExtras_sal, horasNocturnas_sal, bonoAsistencia_sal, minimoHorasAsistencia_sal, seguroSocial_sal, prestamos_sal, adelantos_sal):
        # Constructor de la clase Empleado
        self.ci_sal = ci_sal
        self.nombre_sal = nombre_sal
        self.salarioPorHora_sal = salarioPorHora_sal
        self.horasTrabajadas_sal = horasTrabajadas_sal
        self.productividad_sal = productividad_sal
        self.porcentajeComision_sal = porcentajeComision_sal
        self.horasExtras_sal = horasExtras_sal
        self.horasNocturnas_sal = horasNocturnas_sal
        self.bonoAsistencia_sal = bonoAsistencia_sal
        self.minimoHorasAsistencia_sal = minimoHorasAsistencia_sal
        self.seguroSocial_sal = seguroSocial_sal
        self.prestamos_sal = prestamos_sal
        self.adelantos_sal = adelantos_sal

    def calcular_salario(self):
        """Método para calcular el salario del empleado."""
        salarioBruto_sal = (self.salarioPorHora_sal * self.horasTrabajadas_sal)
        comisiones_sal = self.productividad_sal * self.porcentajeComision_sal

        # Bonificación por asistencia si se cumplen las horas mínimas
        if self.horasTrabajadas_sal >= self.minimoHorasAsistencia_sal:
            salarioBruto_sal += self.bonoAsistencia_sal

        # Horas extras y nocturnas
        salarioBruto_sal += (self.horasExtras_sal * self.salarioPorHora_sal)  # Pago por horas extras
        salarioBruto_sal += (self.horasNocturnas_sal * self.salarioPorHora_sal * 2)  # Pago por horas nocturnas y festivas

        # Salario bruto total con comisiones
        salarioBrutoTotal_sal = salarioBruto_sal + comisiones_sal

        # Cálculo de deducciones
        ips_sal = 0.09  # 9% de deducción por IPS
        irp_sal = 0.10  # 10% de deducción por IRP
        deduccionIps_sal = salarioBrutoTotal_sal * ips_sal
        deduccionIrp_sal = (salarioBrutoTotal_sal - deduccionIps_sal) * irp_sal
        totalDeducciones_sal = deduccionIps_sal + deduccionIrp_sal + self.seguroSocial_sal + self.prestamos_sal + self.adelantos_sal

        # Salario neto después de deducciones
        salarioNeto_sal = salarioBrutoTotal_sal - totalDeducciones_sal

        # Retornamos los datos calculados en un diccionario
        return {
            'nombre_sal': self.nombre_sal,
            'salarioBrutoTotal_sal': salarioBrutoTotal_sal,
            'comisiones_sal': comisiones_sal,
            'bonoAsistencia_sal': self.bonoAsistencia_sal if self.horasTrabajadas_sal >= self.minimoHorasAsistencia_sal else 0,
            'horasExtras_sal': self.horasExtras_sal * self.salarioPorHora_sal,
            'horasNocturnas_sal': self.horasNocturnas_sal * self.salarioPorHora_sal * 2,
            'deduccionIps_sal': deduccionIps_sal,
            'deduccionIrp_sal': deduccionIrp_sal,
            'seguroSocial_sal': self.seguroSocial_sal,
            'prestamos_sal': self.prestamos_sal,
            'adelantos_sal': self.adelantos_sal,
            'salarioNeto_sal': salarioNeto_sal
        }
