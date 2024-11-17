# acá voy a gestionar todo el menú de asistencia
import utility.utility as u
import moduloAsistencia.gestionasistencia as gest_Asis
import moduloEmpleados.gestionEmpleados as gest_Empe
def menu_asis():
    u.cl()
    print("Menú Asistencia."
          "\n1- Registrar presencia"
          "\n2- Registrar permisos/licencias/vacaciones"
          "\n3- Atrás")
    opcion()
    
def opcion():
    while True:
        try:
            op = input("Ingrese una opción:")
            if op == 1:
                for emp in gest_Empe:
                    gest_Asis.presencia()
        except ValueError:
    