if __name__ == "__main__":

    class CuentaBancaria:

        def __init__(self, numero_cuenta: int, propietarios: str, balance: int):
            self.numero_cuenta = numero_cuenta
            self.propietarios = propietarios
            self.balance = balance

        def depositar(self, dinero: int):
            pass

        def retirar(self, dinero: int):
            pass

        def aplicar_cuota_manejo(self, porcentaje=0.02):
            pass

        def mostrar_detalles(self):
            print(f"Su numero de cuenta es: {self.numero_cuenta}")
            print(f"El propietario de esta cuenta es: {self.propietarios}")
            print(f"El balance que tiene en este momento: {self.balance}")
            print(f"Depositó: ")
            print(f"Retiró: ")
            print(f"Al aplicar el 2%: {self.aplicar_cuota_manejo}")

    cuenta_1 = CuentaBancaria(234563, "Juan Lopez", 400000)
