## añadiré ejemplos que saco de stackoverflow y chatgpt para datos muy concretos
from datetime import datetime

fecha_str = "2024-11-07"  # ejemplo de cadena de fecha
formato = "%Y-%m-%d"      # formato de la cadena de fecha

fecha_objeto = datetime.strptime(fecha_str, formato)
print(fecha_objeto)




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