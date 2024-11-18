from menu_asistencia import ne
import utility.utility as utl
class SistemaAsistencia:
    def __init__(self):
        self.asistencias = {}

    def inicializar_asistencia(self):
        for emp in ne:
            id = getattr(emp, "idlegajo")
            day = utl.dias_del_mes()
        
        if id not in self.asistencias:
            self.asistencias[id] = {
                "estados": [0] * day,  # Inicializar días como ausente (0)
                "razones": {}  # Diccionario para razones de permisos y vacaciones
            }
        else:
            raise ValueError(f"El empleado con ID {id} ya tiene asistencia registrada.")

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
