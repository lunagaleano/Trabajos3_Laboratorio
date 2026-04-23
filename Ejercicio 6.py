#Ejercicio 6
'''Crea una clase llamada Rectángulo que tenga atributos base y altura.
Implementa métodos para calcular el área y el perímetro del rectángulo.'''

class Rectángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area (self):
        return self.base * self.altura
        
    def perimetro(self):
        return 2 * (self.base + self.altura)

# Ejemplo de uso
if __name__ == "__main__":
    rectangulo1 = Rectángulo(9, 24)
    print ("Area: ", rectangulo1.area())
    print ("Perimetro: ", rectangulo1.perimetro())