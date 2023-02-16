if __name__ == "__main__":

    from Ejercicios import Punto

    import math

    PI = math.pi

    class Circulo:
        def __init__(self, centro, radio):
            self.centro = centro
            self.radio = radio

        def area_circulo(self):
            area = PI * self.radio ** 2
            print(f"El area del circulo es: {area}")

        def perimetro_circulo(self):
            perimetro= 2 * PI * self.radio
            print(f"El perimetro del circulo es: {perimetro}")

        def pertenece_circulo(self, nuevo_punto):
            diferencia_x = self.centro.x - nuevo_punto.x
            diferencia_y= self.centro.y - nuevo_punto.y

            pitagoras= (diferencia_x **2 + diferencia_y**2)**1/2

            if pitagoras <= self.radio:
                print("El punto pertenece al circulo")

            else:
                print("El punto no pertenece al circulo")


    circulo_1 = Circulo(4, 6)
    circulo_1.area_circulo()
    circulo_1.perimetro_circulo()

# si un punto pertenece al círculo o no.