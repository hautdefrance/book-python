from random import randint


class Smok:
    TEXTURE_ALIVE = 'dragon.png'
    TEXTURE_DEAD = 'dragon-dead.png'
    HP_INITIAL_MIN = 50
    HP_INITIAL_MAX = 100
    DMG_MIN = 5
    DMG_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100
    STATUS_DEAD = 'dead'
    STATUS_ALIVE = 'alive'

    def __init__(self, name, x=0, y=0, texture=TEXTURE_ALIVE):
        self.name = name
        self.texture = texture
        self.hit_points = randint(self.HP_INITIAL_MIN, self.HP_INITIAL_MAX)
        self.ustaw_pozycje(x, y)
        self.status = self.STATUS_ALIVE

    def zadaj_obrazenia(self):
        return randint(self.DMG_MIN, self.DMG_MAX)

    def przyjmij_obrazenia(self, ile_obrazen):
        if self.status == self.STATUS_DEAD:
            return

        self.hit_points -= ile_obrazen
        print(f'{self.name}: otrzymał {ile_obrazen}, pozostało {self.hit_points}')

        if self.hit_points <= 0:
            print(f'{self.name} is dead')
            gold = randint(self.GOLD_MIN, self.GOLD_MAX)
            print(f'Gold dropped {gold}')
            print(f'Pozycja {self.position_x}, {self.position_y}')
            self.texture = self.TEXTURE_DEAD
            self.status = self.STATUS_DEAD

    def ustaw_pozycje(self, x, y):
        self.position_x = x
        self.position_y = y

    def przesun(self, lewo=0, prawo=0, dol=0, gora=0):
        self.ustaw_pozycje(
            x=self.position_x + prawo - lewo,
            y=self.position_y + dol - gora)


wawelski = Smok(name='Wawelski', x=50, y=120)

wawelski.ustaw_pozycje(x=10, y=20)

wawelski.przesun(lewo=10, dol=20)
wawelski.przesun(lewo=10, prawo=15)
wawelski.przesun(prawo=15, gora=5)
wawelski.przesun(dol=5)

wawelski.przyjmij_obrazenia(10)
wawelski.przyjmij_obrazenia(5)
wawelski.przyjmij_obrazenia(3)
wawelski.przyjmij_obrazenia(2)
wawelski.przyjmij_obrazenia(15)
wawelski.przyjmij_obrazenia(25)
wawelski.przyjmij_obrazenia(75)

