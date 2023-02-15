if __name__ == "__main__":

    class Rectangulo:

        def __init__(self, base: int, altura: int):
            self.base = base
            self.altura = altura

        def perimetro(self):
            suma = self.base + self.base + self.altura + self.altura
            print(f"El perimetro del rectangulo es: {suma}")


        def area_rectangulo (self):
            area = self.base * self.altura
            print(f"El area del rectangulo es: {area}")

        def es_cuadrado(self):
            print("Es cuadrado?")

            if self.base == self.altura:
                print(True)

            else:
                print(False)


    rectangulo_1 = Rectangulo( 2, 6)
    rectangulo_1.perimetro()
    rectangulo_1.area_rectangulo()
    rectangulo_1.es_cuadrado()

