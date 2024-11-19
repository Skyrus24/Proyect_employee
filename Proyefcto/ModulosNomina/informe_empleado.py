# En este modulo generamos el informe que se le entregara al empleado

def generar_informe_empleado(empleado_sal):
    #esta funcion es la que usaremos en el main y genera un informe detallado para un empleado
    datos_sal = empleado_sal.calcular_salario()
    informe_sal = f"""
    Recibo Detallado para el Empleado: {datos_sal['nombre_sal']}
    ---------------------------------------------------------
    Salario Bruto Total: {datos_sal['salarioBrutoTotal_sal']}
    Comisiones: {datos_sal['comisiones_sal']}
    Bono de Asistencia: {datos_sal['bonoAsistencia_sal']}
    Pago por horas Extras: {datos_sal['horasExtras_sal']}
    Pago por horas Nocturnas: {datos_sal['horasNocturnas_sal']}
    Deducción IPS: {datos_sal['deduccionIps_sal']}
    Deducción IRP: {datos_sal['deduccionIrp_sal']}
    Seguro Social: {datos_sal['seguroSocial_sal']}
    Préstamos: {datos_sal['prestamos_sal']}
    Adelantos: {datos_sal['adelantos_sal']}
    Salario Neto: {datos_sal['salarioNeto_sal']}
    """
    return informe_sal
