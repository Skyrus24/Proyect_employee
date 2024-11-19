# nomina.py
from empleadoNomina import Empleado

def calcular_nomina_empleado(ci_sal, nombre_sal, salarioPorHora_sal, horasTrabajadas_sal, productividad_sal, porcentajeComision_sal,
                             horasExtras_sal, horasNocturnas_sal, bonoAsistencia_sal, minimoHorasAsistencia_sal,
                             seguroSocial_sal, prestamos_sal, adelantos_sal):
    #Calculamos  la nómina de un empleado y retornamos los resultados
    empleado_sal = Empleado(
        ci_sal, nombre_sal, salarioPorHora_sal, horasTrabajadas_sal, productividad_sal,
        porcentajeComision_sal, horasExtras_sal, horasNocturnas_sal, bonoAsistencia_sal,
        minimoHorasAsistencia_sal, seguroSocial_sal, prestamos_sal, adelantos_sal
    )
    return empleado_sal.calcular_salario()
