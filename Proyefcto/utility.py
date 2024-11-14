# esto será como una libreria de funciones que pueda utilizar en todo el código
## Función necesaria solo para limpiar pantalla, sin tener que definir la función en todos los archivos que los necesiten

import os
def cl():
    os.system('cls')
    
    
# función para esperar a que se ingrese una tecla.
def wait():
    input("Presione una tecla para continuar...")