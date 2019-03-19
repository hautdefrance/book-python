import json


class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

    def from_json(self):
        return ...


class CSVMixin:
    def to_csv(self):
        return ...

    def from_csv(self):
        return ...


class User(JSONMixin, CSVMixin):
    def __init__(self, first_name, last_name):
        ...







"""
Stwórz smoka w pozycji x=50, y=120 i nazwij go Wawelski
Ustaw nową pozycję na x=10, y=20
Przesuń smoka o 10 w lewo i 20 w dół
Przesuń smoka o 10 w lewo i 15 w prawo
Przesuń smoka o 15 w prawo i 5 w górę
Przesuń smoka o 5 w dół
Zadaj 10 obrażeń smokowi
Zadaj 5 obrażeń smokowi
Zadaj 3 obrażeń smokowi
Zadaj 2 obrażeń smokowi
Zadaj 15 obrażeń smokowi
Zadaj 25 obrażeń smokowi
Zadaj 75 obrażeń smokowi
"""
from random import randint


class Status:
    ALIVE = 1
    DEAD = 2


class Dragon:
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    HEALTH_MIN = 50
    HEALTH_MAX = 100
    GOLD_MIN = 1
    GOLD_MAX = 100
    TEXTURE_ALIVE = 'img/dragon/alive.png'
    TEXTURE_DEAD = 'img/dragon/dead.png'

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.status = Status.ALIVE
        self.texture = self.TEXTURE_ALIVE
        self.set_position(x, y)
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def get_position(self):
        return {
            'x': self.position_x,
            'y': self.position_y}

    def move(self, left=0, right=0, up=0, down=0):
        position = self.get_position()
        x = position['x'] + right - left
        y = position['y'] + down - up
        self.set_position(x, y)

    def attack(self):
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def is_alive(self):
        if self.status != Status.DEAD:
            return True
        else:
            return False

    def is_dead(self):
        if self.status == Status.DEAD:
            return True
        else:
            return False

    def update_status(self):
        if self.health <= 0:
            self.status = Status.DEAD

    def take_damage(self, damage):
        if self.is_dead():
            return None

        self.health -= damage
        self.update_status()

        if self.is_dead():
            self._make_dead()

    def _make_dead(self):
        self.health = 0
        self.texture = self.TEXTURE_DEAD

        drop = self._make_drop()
        gold = drop['gold']
        position = self.get_position()

        print(f'{self.name} is dead')
        print(f'Drop gold {gold}')
        print(f'Position {position}')

    def _make_drop(self):
        return {
            'gold': randint(self.GOLD_MIN, self.GOLD_MAX),
            'items': []
        }


wawelski = Dragon(name='Wawelski', x=50, y=120)

wawelski.set_position(x=10, y=20)

wawelski.move(left=10, down=20)
wawelski.move(left=10, right=15)
wawelski.move(right=15, up=5)
wawelski.move(down=5)

wawelski.take_damage(10)
wawelski.take_damage(5)
wawelski.take_damage(3)
wawelski.take_damage(2)
wawelski.take_damage(15)
wawelski.take_damage(25)
wawelski.take_damage(75)
