if __name__ == "__main__":

    import math

    pi = math.pi

    class Circulo:
        def __init__(self, centro, radio):
            self.centro = centro
            self.radio = radio

        def area_circulo(self):
            area = pi * self.radio ** 2
            print(f"El area del circulo es: {area}")

        def perimetro_circulo(self):
            perimetro= 2 * pi * self.radio
            print(f"El perimetro del circulo es: {perimetro}")

        def pertenece_circulo(self):
            pass

circulo_1 = Circulo( 4, 6 )
circulo_1.area_circulo()
circulo_1.perimetro_circulo()

# si un punto pertenece al círculo o no.