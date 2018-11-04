from enum import Enum


class Color(Enum):
    RED = 'Roscosmos'
    BLUE = 'NASA'


class Moon:
    def __init__(self, explorer):
        self.color = Color(explorer)


moon = Moon(explorer='NASA')


if moon.color is Color.BLUE:
    print("That's one small step for [a] man, one giant leap for mankind.")

elif moon.color is Color.RED:
    print('Красная Луна, товарищ!')
