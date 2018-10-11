from matplotlib import pyplot as plt
import random


class ObiektGraficzny:
    def plot(self):
        raise NotImplementedError

class Punkt(ObiektGraficzny):
    def __init__(self, x ,y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Punkt({self._x}, {self._y})"

    def plot(self, color='black'):
        plt.plot(self._x, self._y, 'o', color=color)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @staticmethod
    def random_point(center_point, std):
        return Punkt(
            random.gauss(center_point.x, std),
            random.gauss(center_point.y, std))

    def oblicz_odleglosc_do(self, drugi_punkt):
        return ((self._x - drugi_punkt.x)**2 + (self._y - drugi_punkt.y)**2)**0.5

    @staticmethod
    def oblicz_odleglosc(punkt_A, punkt_B):
        return ((punkt_A.x - punkt_B.x)**2 + (punkt_A.y - punkt_B.y)**2)**0.5



if __name__ == '__main__':

    A = Punkt(0, 0)
    B = Punkt(2, 2)

    lista_A = []
    lista_B = []
    liczba_punktow = 100

    for i in range(liczba_punktow):
        lista_A.append(Punkt.random_point(A, 0.6))
        lista_B.append(Punkt.random_point(B, 0.2))


    A.plot()
    B.plot()


    for point_A, point_B in zip(lista_A, lista_B):
        point_A.plot(color='red')
        point_B.plot(color='blue')

    plt.show()
