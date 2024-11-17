# esto será como una libreria de funciones que pueda utilizar en todo el código
## Función necesaria solo para limpiar pantalla, sin tener que definir la función en todos los archivos que los necesiten
import datetime
import os
import inspect

## función para limpiar pantalla
def cl():
    os.system('cls')
    
    
# función para esperar a que se ingrese una tecla.
def wait():
    input("Presione una tecla para continuar...")
    
def fecha_formato():
    while True:
        fecha = input("Ingrese la fecha en formato(DD/MM/YYYY): ")
        try:
        # comprueba si la fecha ingresada está en el formato correcto, de no ser así, reiniciará 
            fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        except:
            print("Formato de fecha incorrecto(Debe ingresar Día/Mes/año. Ejemplo: 24/08/2006)")
        else:
            return fecha
        

 # función recursiva para verificar que un input no esté vacío
def no_input(self, valor, mensaje):
    if not valor.strip():
        print("El valor no puede estar vacío. Inténtelo de nuevo.")
        # Obtener el nombre del atributo llamador
        frame = inspect.currentframe().f_back
        atributo = [name for name, val in frame.f_locals.items() if val is valor][0]
        # Solicitar nuevamente el input y llamar recursivamente
        nuevo_valor = input(mensaje)
        return self.no_input(nuevo_valor, mensaje)
    return valor