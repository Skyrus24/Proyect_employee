# Calculo de nomina
# La definicion de las funciones usaran este_formato
# Las variables utilizaran camelCase
class CalculoNomina:
    def calcular_salario():

    # Primeramente voy a pedir al usuario todos los datos necesarios para
    # un calculo de nomina dirigido a individuo, con la posibilidad de cambiar cada aspecto variablle del salario

    # Como el sistema se basa en calcular el salario por horas trabajadas, vamos a pedir esos datos primero en primera instancia
      salarioPorHora = int(input("Ingrese el salario fijo por hora: "))
      horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
      
          ## abel: yo solicitaré estos datos previamente, por lo tanto te los enviaré después

    # Uno de los requisitos es que el programa admita la posibilidad de que el individuo
    # tenga comision y calcular el porcentaje de ganancia en base a su productividad
      productividad = int(input("Ingrese la productividad/ventas del mes: "))

    # El porcentaje de comision sera una variable que el usuario podra ingresar,pero tambien podria hacer un sistema de comision que cambie en base al porcentaje
    # alcanzado en base a objetivo
      porcentajeComision = int(input("Ingrese el porcentaje de comisión (en %): ")) / 100

    # El calculo de horas nocturnas y festivas voy a basarlo en el doble del salario normal, asi que solo pedire la cantidad de horas
      horasExtras = int(input("Ingrese las horas extras trabajadas: "))
      horasNocturnas = int(input("Ingrese las horas nocturnas y festivas trabajadas: "))

    # Otro requiisto es un apartado de bonos, como no esta espécificado voy a hacer que el bono sea de asistencia
      bonoAsistencia = int(input("Ingrese el bono de asistencia: "))

    # El bono de asistencia sera calculado bajo una condicion de horas minimas trabajadas
      minimoHorasAsistencia = int(input("Ingrese el mínimo de horas para el bono: "))

    # Voy a pedir ahora los datos necesarios para las deducciones

    # Las deducciones de ips e irp seran constantes
      ips = 0.09  # 9%
      irp = 0.10  # 10%

    # Los demas datos de deduccion seran variables
      seguroSocial = int(input("Ingrese el monto del seguro social: "))
      prestamos = int(input("Ingrese el monto de préstamos: "))
      adelantos = int(input("Ingrese el monto de adelantos: "))

    # Ahora realizamos los calculos necesarios
      salarioBruto = (salarioPorHora * horasTrabajadas)
      comisiones = productividad * porcentajeComision

      if horasTrabajadas >= minimoHorasAsistencia:
          salarioBruto += bonoAsistencia

      salarioBruto += (horasExtras * salarioPorHora)  # Sumando poago por horas extras
      salarioBruto += (horasNocturnas * salarioPorHora * 2)  # Sumando pago por horas nocturnas y festivas

    # Sumar todo para obtener el salario bruto final
      salarioBrutoTotal = salarioBruto + comisiones

    # Calculamos todas las deducciones
      deduccionIps = salarioBrutoTotal * ips
      deduccionIrp = (salarioBrutoTotal - deduccionIps) * irp
      totalDeducciones = deduccionIps + deduccionIrp + seguroSocial + prestamos + adelantos

    # Calculamos el salario neto, restandole al salario bruto total todas las deducciones
      salarioNeto = salarioBrutoTotal - totalDeducciones

    # Guardamos todos los datos para poder imprimirlos en pantalla para los informes
      return {
          'salarioBrutoTotal': salarioBrutoTotal,
          'comisiones': comisiones,
          'bonoAsistencia': bonoAsistencia if horasTrabajadas >= minimoHorasAsistencia else 0,
          'horasExtras': horasExtras * salarioPorHora,
          'horasNocturnas': horasNocturnas * salarioPorHora * 2,
          'deduccionIps': deduccionIps,
          'deduccionIrp': deduccionIrp,
          'seguroSocial': seguroSocial,
          'prestamos': prestamos,
          'adelantos': adelantos,
          'salarioNeto': salarioNeto
      }

    # Creo la funcion que va a imprimir los dtos de manera ordenada al usuario, en base a los datos que previamente ingreso
    def imprimir_recibo_empleado(datos):
        print("\nRecibo Detallado para el Empleado:")
        print(f"Comisiones: {datos['comisiones']}")
        print(f"Bono de Asistencia: {datos['bonoAsistencia']}")
        print(f"Pago por horas Extras: {datos['horasExtras']}")
        print(f"Pago por horas Nocturnas: {datos['horasNocturnas']}")
        print(f"Deducción IPS: {datos['deduccionIps']}")
        print(f"Deducción IRP: {datos['deduccionIrp']}")
        print(f"Seguro Social: {datos['seguroSocial']}")
        print(f"Préstamos: {datos['prestamos']}")
        print(f"Adelantos: {datos['adelantos']}")
        print(f"Salario Bruto Total: {datos['salarioBrutoTotal']}")
        print(f"Salario Neto: {datos['salarioNeto']}")

    def imprimir_generacion_rrhh(datos):
        print("\nInforme Detallado para RRHH")
        print(f"Monto total a ser pagado de {empleado} es: {datos['salarioBrutoTotal']}")
        print(f"Descuento de ips a")
    # Llamamos a la funcion de calculo de salarios
    datos = calcular_salario()

    # Si queremos los datos, llamamos a la funcion de imprimir los datos en pantalla
    imprimir_recibo_empleado(datos)





## si te digo que tengo que cambiar absolutamente todo tu código porque vos pedís todo en inputs, y yo ya pido todos los datos por tanto tenemos que interconectar:/