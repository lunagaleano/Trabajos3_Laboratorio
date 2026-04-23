#Ejercicio 8
'''Crea una clase llamada Producto que tenga atributos nombre, precio y stock.
Implementa métodos para aumentar y disminuir el stock, asegurándote de que no se pueda tener un stock negativo.'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def aumentar_stock (self, cantidad):
        self.stock += cantidad
        
    def diminuir_stock (self, cantidad):
        if self.stock - cantidad >= 0:
            self.stock -= cantidad
        else:
            print ("Stock insuficiente")

# Ejemplo de uso
if __name__ == "__main__":
    producto1 = Producto("Harina", 150, 50)
    producto1.diminuir_stock(5)
    print("Stock: ", producto1.stock)