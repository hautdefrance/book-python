class Osoba:
    imie = 'statycznie'

    def __init__(self, nazwisko='dynamicznie'):
        self.nazwisko = nazwisko


def say_hello():
    print('hello')


def say_ehlo():
    print('ehlo')


o1 = Osoba()
o1.data_urodzenia = 'dynamicznie w locie'
o1.hello = say_hello
o1.imie = 'moge to zmienic'

Osoba.adres = 'pole klasy modyfikowane dynamicznie'
Osoba.hello = say_ehlo
Osoba.imie = 'jeszcze inne imie'

o2 = Osoba()
o2.data_urodzenia = 'dynamicznie w locie'


o1.hello()  # hello
o2.hello()  # ehlo
