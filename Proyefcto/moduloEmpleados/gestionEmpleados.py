import utility.utility as utl

class Empleados:
    def __init__(self):
        self.employeeslist = []

    def añadir_emp(self, entrada:object):
        self.employeeslist.append(entrada)
        return "Nuevo empleado añadido correctamente."
        

    def listar_emp(self):
        for emp in self.employeeslist:
            print(emp)
    
    def actualizar_emp(self):
        if self.employeeslist == []:
            print("La nómina de empleados está vacía.")
        else:
            while True:
                try:
                    found = False
                    while found == False:
                        utl.cl()
                        ci = int(input("Ingrese CI del empleado a actualizar: "))
                        for emp in self.employeeslist:
                            if emp.ci == ci:
                                emp.actualizar_datos()
                                found = True
                        if found == False:
                            print("Empleado no encontrado.")
                            
                except ValueError:
                    print("ERROR: Debe ingresar un CI válido")
                    
    def eliminar_emp(self):
        if self.employeeslist == []:
            print("La nómina de empleados está vacía")
        else:
            while True:
                try:
                    found = False
                    while found != True:
                        utl.cl()
                        ci = int(input("Ingrese CI del empleado a eliminar: "))
                        index = 0
                        for emp in self.employeeslist:
                            if emp.ci == ci:
                                self.employeeslist.pop(index)       
                                found = True
                                return("Empleado eliminado")
                            index += 1

                        if not found:
                            print("Empleado no encontrado")
                except ValueError:
                    print("ERROR: Debe ingresar un valor válido")

                            
                        
                             
                