class Empleados:
    def __init__(self):
        self.employeeslist = []

    def añadir_emp(self, entrada:object):
        self.employeeslist.append(entrada)
        return f"La nueva nómina de empleados es: {self.listar_emp()}"

    def listar_emp(self):
        for emp in self.employeeslist:
            print(emp)