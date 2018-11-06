import random
from matplotlib import pyplot as plt


def random_point(center, std=0.2):
    if not isinstance(std, (tuple, list)):
        std = (std, std)

    x = random.gauss(center[0], std[0])
    y = random.gauss(center[1], std[1])

    return x, y


def distance(A, B):
    """
    Wylicz odległość między punktami A i B.

    Argumenty:
        A: punkt w przestrzeni wielowymiarowej zdefiniowany następująco:
            [x, y, z, ...]
        B: punkt w przestrzeni wielowymiarowej zdefiniowany następująco:
            [x, y, z, ...]

    Zwraca:
        Odległość euklidesową między punktami A i B.

    >>> distance((0,0), (1,0))
    1.0

    >>> distance((0,0), (1,1))
    1.4142135623730951
    """
    suma = 0
    for a, b in zip(A, B):
        suma += (b - a) ** 2

    return suma ** 0.5


def plot_list_of_points(list_of_points, color='black'):
    """
    Wyrysowuje listę punktów na aktualnie aktywnym wykresie.

    Argumenty:
        list_of_points: lista punktów, zgodnie z konwencją:
            [[x1, y1], [x2, y2], [x3, y3], ...]
        color: kolor jakim mają być punkty narysowane. Domyślnie czarny.
    """
    plt.plot([p[0] for p in list_of_points],
             [p[1] for p in list_of_points],
             'o',
             color=color,
             alpha=0.3)


A = [0,3]
B = [2,4]
ODCHYLENIE_STANDARDOWE_A = 0.8
ODCHYLENIE_STANDARDOWE_B = 1.0

p1 = [random_point(A, ODCHYLENIE_STANDARDOWE_A)
          for _ in range(0,500)]

p2 = [random_point(B, ODCHYLENIE_STANDARDOWE_B)
          for _ in range(0,500)]

plot_list_of_points(p1, 'red')
plot_list_of_points(p2, 'blue')
plt.axis('equal')
plt.show()

punkty_po_klasyfikacji_A = []
punkty_po_klasyfikacji_B = []


for p in p1 + p2:
    if distance(A, p) < distance(B, p):
        punkty_po_klasyfikacji_A.append(p)
    else:
        punkty_po_klasyfikacji_B.append(p)


plot_list_of_points(punkty_po_klasyfikacji_A, 'red')
plot_list_of_points(punkty_po_klasyfikacji_B, 'blue')
plt.axis('equal')
plt.show()

## Zobacz co się stanie jak wywołasz:
# help(random_points)
# Python automatycznie stworzył dokumentację do modułu na podstawie komentarzy!
