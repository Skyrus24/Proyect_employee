# esto será como una libreria de funciones que pueda utilizar en todo el código
## Función necesaria solo para limpiar pantalla, sin tener que definir la función en todos los archivos que los necesiten
import datetime
import os
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