#Ejercicio 3
'''Crea una clase llamada CuentaBancaria que tenga atributos como titular,
saldo y numero_cuenta. Implementa métodos para depositar y retirar dinero,
asegurándote de que el saldo no se vuelva negativo.'''

class CuentaBancaria:
    def __init__(self, titular, saldo, numero_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta
        
    def depositar(self, monto):
        self.saldo += monto
        
    def retirar(self, monto):
        if self.saldo - monto >= 0:
            self.saldo -= monto
        else:
            print ("Fondos insuficiente")

    def mostrar_informacion(self):
        return f"Saldo Actual: {self.saldo}"

# Ejemplo de uso
if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Karina", 190, "1825")
    cuenta1.depositar (299)
    cuenta1.retirar (30)
    print(cuenta1.mostrar_informacion())