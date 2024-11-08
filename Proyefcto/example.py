## añadiré ejemplos que saco de stackoverflow y chatgpt para datos muy concretos
from datetime import datetime

fecha_str = "2024-11-07"  # ejemplo de cadena de fecha
formato = "%Y-%m-%d"      # formato de la cadena de fecha

fecha_objeto = datetime.strptime(fecha_str, formato)
print(fecha_objeto)
