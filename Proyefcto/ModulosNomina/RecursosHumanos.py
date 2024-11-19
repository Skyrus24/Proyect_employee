# En este mpodulo generamos el informe para recursos humanos

from InformePagos import generar_informe_empleado

def generar_informe_detallado_recursos_humanos(empleado_sal):
# esta funcion es la que genera un informe detallado para el departamento de recursos humanos

    # Información del empleado
    nombre_sal = empleado_sal.nombre_sal
    ci_sal = empleado_sal.ci_sal
    horas_trabajadas_sal = empleado_sal.horasTrabajadas_sal

    # Descuentos
    seguro_social_sal = empleado_sal.seguroSocial_sal
    prestamos_sal = empleado_sal.prestamos_sal
    adelantos_sal = empleado_sal.adelantos_sal
    total_descuentos = seguro_social_sal + prestamos_sal + adelantos_sal

    # Beneficios
    horas_extras_sal = empleado_sal.horasExtras_sal
    horas_nocturnas_sal = empleado_sal.horasNocturnas_sal
    bono_asistencia_sal = empleado_sal.bonoAsistencia_sal
    comisiones_sal = empleado_sal.productividad_sal * empleado_sal.porcentajeComision_sal
    total_beneficios = horas_extras_sal + horas_nocturnas_sal + bono_asistencia_sal + comisiones_sal

    # Cálculo de salario neto
    salario_base_sal = empleado_sal.salarioPorHora_sal * horas_trabajadas_sal
    salario_neto_sal = salario_base_sal + total_beneficios - total_descuentos

    informe_sal = (
        f"--- Informe Detallado de Recursos Humanos ---\n"
        f"Nombre: {nombre_sal}\n"
        f"CI: {ci_sal}\n"
        f"Total horas trabajadas: {horas_trabajadas_sal}\n\n"
        f"** Descuentos **\n"
        f"Seguro Social: {seguro_social_sal}\n"
        f"Préstamos: {prestamos_sal}\n"
        f"Adelantos: {adelantos_sal}\n"
        f"Total descuentos: {total_descuentos}\n\n"
        f"** Beneficios **\n"
        f"Horas extras: {horas_extras_sal}\n"
        f"Horas nocturnas: {horas_nocturnas_sal}\n"
        f"Bono de asistencia: {bono_asistencia_sal}\n"
        f"Comisiones: {comisiones_sal}\n"
        f"Total beneficios: {total_beneficios}\n\n"
        f"** Cálculo del salario **\n"
        f"Salario base (horas trabajadas): {salario_base_sal}\n"
        f"Salario neto: {salario_neto_sal}\n"
    )

    return informe_sal

