from random import randint


class Smok:

    def __init__(self, nazwa, pozycja_x=0, pozycja_y=0, tekstura='dragon.png'):
        self.nazwa = nazwa
        self.pozycja_x = pozycja_x
        self.pozycja_y = pozycja_y
        self.punkty_zycia = randint(50, 100)
        self.tekstura = tekstura
        self.zyje = True

    def _umrzyj(self):
        self.punkty_zycia = 0
        self.tekstura = 'dragon-dead.png'
        print(f'{self.nazwa} is dead')
        self.zyje = False
        print(f'Smok zwrocil {randint(1, 101)} zlota')

    def otrzymaj_obrazenia(self, sila_ciosu):
        if self.zyje:
            self.punkty_zycia -= sila_ciosu
            if self.punkty_zycia <= 0:
                self._umrzyj()
        else:
            print('Martwe smoki nie otrzymują obrażeń i nie dają złota')

    def oblicz_obrazenia(self):
        return randint(5, 21)

    def przesun(self, lewo=0, prawo=0, gora=0, dol=0):
        self.pozycja_x += prawo - lewo
        self.pozycja_y += dol - gora

    def ustaw_pozycje(self, x, y):
        self.pozycja_x = x
        self.pozycja_y = y


wawelski = Smok(nazwa='Wawelski', pozycja_x=50, pozycja_y=120)

wawelski.ustaw_pozycje(x=10, y=20)
wawelski.przesun(lewo=10, dol=20)
wawelski.przesun(lewo=10, prawo=15)
wawelski.przesun(prawo=15, gora=5)
wawelski.przesun(dol=5)

wawelski.otrzymaj_obrazenia(10)
wawelski.otrzymaj_obrazenia(5)
wawelski.otrzymaj_obrazenia(3)
wawelski.otrzymaj_obrazenia(2)
wawelski.otrzymaj_obrazenia(15)
wawelski.otrzymaj_obrazenia(25)
wawelski.otrzymaj_obrazenia(75)

