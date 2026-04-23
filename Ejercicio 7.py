#Ejercicio 7
'''Crea una clase llamada Empleado con atributos nombre, salario y departamento.
Implementa un método que aumente el salario en un porcentaje dado y otro que muestre la información del empleado.'''

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
        
    def aumentar_salario (self, porcentaje):
        self.salario += self.salario * porcentaje/100
        
    def mostrar_informacion(self):
        return f"{self.nombre} - {self.departamento} - Salario {self.salario}"

# Ejemplo de uso
if __name__ == "__main__":
    empleado1 = Empleado("Naomi", 100000, "Marketing")
    empleado1.aumentar_salario(100)
    print(empleado1.mostrar_informacion())