# esto será como una libreria de funciones que pueda utilizar en todo el código
## Función necesaria solo para limpiar pantalla, sin tener que definir la función en todos los archivos que los necesiten
import datetime
import os
import inspect
import re   




## función para limpiar pantalla
def cl():
    os.system('cls')
    
    
# función para esperar a que se ingrese una tecla.
def wait():
    input("Presione una tecla para continuar...")
    
def fecha_formato(mensaje):
    while True:
        fecha = input(mensaje)
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




 # función para determinar cantidas de días de un mes def dias_del_mes(mes):
def dias_del_mes():
    # Grupos de meses según su cantidad de días
    dias_31 = [1, 3, 5, 7, 8, 10, 12]  # Meses con 31 días
    dias_30 = [4, 6, 9, 11]            # Meses con 30 días
    while True:
        try:
            mes = int(input("Ingrese número del mes(Por ejemplo, 1 para enero): "))
            if mes in dias_31:
                return 31
            elif mes in dias_30:
                return 30
            elif mes == 2:
                return 28
            else:
                print("Mes inválido")
        except ValueError:
            print("ERROR: Debes ingresar un NÚMERO para el mes.")

## función para que solo se pueda ingresar enteros
def pedir_ent(mensaje):
    while True:
        try:
            integer = int(input(mensaje))
        except ValueError:
            print("ERROR: Debe ingresar un entero")
        else:
            return integer


# Función que solo permita ingresar determinados tipos de caracteres
def pedir_alpha(mensaje):
    patron = r"^[a-zA-ZáéíóúüñàèùçĀāšžÇ'(),.\-/ ]+$"  # Definición del patrón
    while True:
        try:
            special = input(mensaje)  # Solicitar entrada al usuario
            if not re.match(patron, special):  # Verificar si no coincide con el patrón
                raise ValueError("El dato ingresado solo puede contener letras y los siguientes caracteres especiales: ( ), . , - , /")
            return special  # Si la entrada es válida, retornarla
        except ValueError as e:
            print(e)  # Mostrar el mensaje de error y volver a pedir la entrada
        
        
# código original con errores
'''def pedir_str(mensaje):
    while True:
        string = input(mensaje)
        if string.isalpha():
            return string
        else:
            print("ERROR: Debe ingresar solo carácteres válidos(No se permiten números).")'''
            
def pedir_str(mensaje):
    while True:
        string = input(mensaje)
        # Usamos .isalpha() para verificar si solo tiene letras (sin números o caracteres especiales).
        # Aceptamos letras con acentos y caracteres especiales como ñ, é, etc.
        if all(c.isalpha() or c in "áéíóúüñàèùç" for c in string):  
            return string
        else:
            print("ERROR: Debe ingresar solo caracteres válidos (No se permiten números ni caracteres especiales).")

            
            
            
if __name__ == "__main__":
    print(f"El día tiene {dias_del_mes()} días")