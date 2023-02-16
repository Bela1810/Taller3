if __name__ == "__main__":

    import math

    class Punto:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def mostrar(self):
            print(f"El punto en x es: {self.x}")
            print(f"El punto en y es: {self.y}")
            print((f"Coordenadas ({self.x},{self.y}"))

        def mover(self, mover_x, mover_y):
            self.x += mover_x
            self.y += mover_y

        def calcular_distancia(self):
            pass



        ##A la clase del punto anterior, defínale los siguientes métodos:

#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.



