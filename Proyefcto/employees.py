class Empleados:
    def __init__(self):
        self.employeeslist = []

    def añadir_emp(self, entrada):
        self.employeeslist.append(entrada)

    def listar_emp(self):
        for emp in self.employeeslist:
            print(emp)