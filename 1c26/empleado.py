class EMPLEADO:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento