from utility import utility as utl

class Empleados:
    def __init__(self):
        self.employeeslist = []

    def añadir_emp(self, entrada: object):
        self.employeeslist.append(entrada)
        return "Nuevo empleado añadido correctamente."
        

    def listar_emp(self):
        if self.employeeslist == []:
            print("ERROR: La nómina está vacía")
        else:  
            for emp in self.employeeslist:
                emp.imprimir_datos()
        
    def actualizar_emp(self):
        if self.employeeslist == []:
            print("La nómina de empleados está vacía.")
        else:
            found = False
            utl.cl()
            print("Actualización de datos del empleado.")
            ci = utl.pedir_ent("Ingrese CI del empleado a actualizar: ")
            for emp in self.employeeslist:
                if emp.ci == ci:
                    emp.actualizar_datos()
                    found = True
            if not found:
                print("Empleado no encontrado.")
            
    def eliminar_emp(self):
        if self.employeeslist == []:
            print("La nómina de empleados está vacía")
        else:
            found = False
            utl.cl()
            print("ELiminar un empleado.")
            ci = utl.pedir_ent("Ingrese CI del empleado a eliminar: ")
            index = 0
            for emp in self.employeeslist:
                if emp.ci == ci:
                    self.employeeslist.pop(index)       
                    found = True
                    print("Empleado eliminado")
                index += 1

            if not found:
                print("Empleado no encontrado")
                            
                        
                             
                