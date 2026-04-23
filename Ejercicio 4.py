#Ejercicio 4
'''Crea una clase llamada Libro con atributos titulo, autor y año_publicacion.
Implementa un método que devuelva una descripción del libro y otro que verifique
si el libro es considerado un clásico (publicado hace más de 50 años).'''

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        
    def descripción(self):
        return f"{self.titulo} - {self.autor} ({self.año_publicacion})"
        
    def clasico(self):
        return 2026 - self.año_publicacion > 50

# Ejemplo de uso
if __name__ == "__main__":
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
    print(libro1.descripción())
    print("¿ES clasico?: ", libro1.clasico())