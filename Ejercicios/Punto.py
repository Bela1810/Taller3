if __name__ == "__main__":

    import math

    class Punto:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def mostrar(self):
            print(f"El punto en x es: {self.x}")
            print(f"El punto en y es: {self.y}")
            print((f"Sus coordenadas ({self.x},{self.y})"))

        def mover(self, mover_x, mover_y):
            self.x += mover_x
            self.y += mover_y
            print(f"({mover_x},{mover_y})")

        def calcular_distancia(self, otro_punto_x, otro_punto_y):
            distancia_x = self.x + otro_punto_x
            distancia_y = self.y + otro_punto_y
            print(math.sqrt((distancia_x**2+distancia_y**2)))

    punto_1 = Punto(3, 6)
    punto_1.mostrar()
    punto_1.mover(2, 4)
    punto_1.calcular_distancia(4, 2)










