class Empleados:
    def __init__(self):
        self.employeeslist = []

    def añadiremp(self, entrada):
        self.employeeslist.append(entrada)

    def listaremp(self):
        for emp in self.employeeslist:
            print(emp)