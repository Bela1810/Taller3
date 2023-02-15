if __name__ == "__main__":
    import math


    class Punto:
        def _init_(self, x, y):
            self.x = x
            self.y = y

        def getx(self):
            return self.x

        def gety(self):
            return self.y

        def mostrar(self):
            print(f"X: {str(self.getx())} \nY: {str(self.gety())}")

        def mover(self, mover_x, mover_y):
            self.x += mover_x
            self.y += mover_y

        def calcular_distancia(self):
            math.sqrt()


    P = punto(5, 6)
    P.mostrar()
    P.mover(1, 3)

