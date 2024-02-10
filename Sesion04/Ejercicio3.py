class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print("Se ha depositado:", cantidad)
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print("Se ha retirado:", cantidad)
        else:
            print("No se puede retirar esa cantidad. Saldo insuficiente.")

    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(100)
print("Saldo actual:", cuenta.consultar_saldo())
cuenta.depositar(50)
print("Saldo actual:", cuenta.consultar_saldo())
cuenta.retirar(30)
print("Saldo actual:", cuenta.consultar_saldo())