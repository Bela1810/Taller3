if __name__ == "__main__":

    class CuentaBancaria:

        PORCENTAJE = 0.02

        def __init__(self, numero_cuenta: int, propietarios: str, balance: int):
            self.numero_cuenta = numero_cuenta
            self.propietarios = propietarios
            self.balance = balance

        def depositar(self, dinero: int):
            self.balance += dinero

        def retirar(self, dinero: int):
            self.balance -= dinero

        def aplicar_cuota_manejo(self):
            cuota= self.balance * self.PORCENTAJE
            return cuota

        def mostrar_detalles(self):
            print(f"Su numero de cuenta es: {self.numero_cuenta}")
            print(f"El propietario de esta cuenta es: {self.propietarios}")
            print(f"El balance que tiene en este momento: {self.balance}")


    cuenta_1 = CuentaBancaria(234563, "Juan Lopez", 400000)
    cuenta_1.mostrar_detalles()
