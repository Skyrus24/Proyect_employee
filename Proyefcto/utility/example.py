## añadiré ejemplos que saco de stackoverflow y chatgpt para datos muy concretos
from datetime import datetime
import inspect

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


# ejemplo de chatgpt osbre como hacer asistencias 
class SistemaAsistencia:
    def __init__(self):
        self.asistencias = {}

    def inicializar_asistencia(self, id_empleado, dias_del_mes):
        if id_empleado not in self.asistencias:
            self.asistencias[id_empleado] = {
                "estados": [0] * dias_del_mes,  # Inicializar días como ausente (0)
                "razones": {}  # Diccionario para razones de permisos y vacaciones
            }
        else:
            raise ValueError(f"El empleado con ID {id_empleado} ya tiene asistencia registrada.")

    def registrar_asistencia(self, id_empleado, dia, estado, razon=None):
        if id_empleado in self.asistencias:
            if 1 <= dia <= len(self.asistencias[id_empleado]["estados"]):
                self.asistencias[id_empleado]["estados"][dia - 1] = estado
                if estado in {3, 4} and razon:
                    self.asistencias[id_empleado]["razones"][dia] = razon
            else:
                raise ValueError("El día especificado está fuera del rango permitido.")
        else:
            raise ValueError("El empleado no está registrado en el sistema de asistencias.")

    def obtener_asistencia(self, id_empleado):
        if id_empleado in self.asistencias:
            return self.asistencias[id_empleado]["estados"]
        else:
            raise ValueError("El empleado no está registrado en el sistema de asistencias.")

    def obtener_razones(self, id_empleado):
        if id_empleado in self.asistencias:
            return self.asistencias[id_empleado]["razones"]
        else:
            raise ValueError("El empleado no está registrado en el sistema de asistencias.")

