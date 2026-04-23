#Ejercicio 2
'''Crea una clase llamada Persona con atributos nombre, edad y sexo.
Implementa un método que permita cambiar la edad de la persona y otro que
muestre la información de la persona.'''

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        
    def cambiar_edad(self, edad_nueva):
        self.edad = edad_nueva

    def mostrar_informacion(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"

# Ejemplo de uso
if __name__ == "__main__":
    persona1 = Persona("Karina", 25, "Femenino")
    persona1.cambiar_edad (27)
    print(persona1.mostrar_informacion())