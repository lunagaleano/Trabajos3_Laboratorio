#Ejercicio 5
'''Crea una clase llamada Estudiante que tenga atributos como nombre, edad y notas
(una lista de números). Implementa métodos para agregar una nota y calcular el promedio de las notas.'''

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []
        
    def agregar_nota (self, nota):
        self.notas.append (nota)
        
    def calcular_nota(self):
        if len (self.notas) == 0:
            return 0
        return sum (self.notas) / len (self.notas)

# Ejemplo de uso
if __name__ == "__main__":
    estudiante1 = Estudiante("Maria", 15)
    estudiante1.agregar_nota(7)
    estudiante1.agregar_nota(9)
    print ("Promedio: ", estudiante1.calcular_nota())