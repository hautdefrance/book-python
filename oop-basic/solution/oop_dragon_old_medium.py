import random
from oop_dragon_easy import Dragon
from oop_dragon_easy import STATUS_ALIVE, STATUS_DEAD


BORDER_LEFT = 0
BORDER_RIGHT = 1024
BORDER_TOP = 0
BORDER_BOTTOM = 768


class DragonMedium(Dragon):

    def make_damage(self):
        if self.status != STATUS_DEAD:
            return random.randint(5, 20)

    def move(self, left=0, down=0, up=0, right=0):
        """
        >>> DragonMedium(name='Wawelski').move(right=10)
        >>> DragonMedium(name='Wawelski').move(down=10)
        >>> DragonMedium(name='Wawelski', position_x=20, position_y=20).move(left=10)
        >>> DragonMedium(name='Wawelski', position_x=20, position_y=20).move(up=10)
        >>> DragonMedium(name='Wawelski').move(right=BORDER_RIGHT+1)
        Traceback (most recent call last):
            ...
        ValueError: New position is out of borders
        >>> DragonMedium(name='Wawelski').move(down=BORDER_BOTTOM+1)
        Traceback (most recent call last):
            ...
        ValueError: New position is out of borders
        >>> DragonMedium(name='Wawelski').move(left=10)
        Traceback (most recent call last):
            ...
        ValueError: New position is out of borders
        >>> DragonMedium(name='Wawelski').move(up=10)
        Traceback (most recent call last):
            ...
        ValueError: New position is out of borders
        """
        new_x = self.position_x + right - left
        new_y = self.position_y + down - up

        if BORDER_LEFT <= new_x <= BORDER_RIGHT:
            self.position_x = new_x
        else:
            raise ValueError(f'New position is out of borders')

        if BORDER_TOP <= new_y <= BORDER_BOTTOM:
            self.position_y = new_y
        else:
            raise ValueError(f'New position is out of borders')


class Hero:
    def __init__(self, name):
        self.name = name
        self.hit_points = random.randint(100, 150)
        self.status = STATUS_ALIVE

    def make_damage(self):
        if self.status != STATUS_DEAD:
            return random.randint(1, 15)

    def take_damage(self, damage=0):
        if self.status != STATUS_DEAD:
            self.hit_points -= damage
            print(f'Hero damage taken: {damage}, HP left: {self.hit_points}')

        if self.hit_points <= 0:
            self.status = STATUS_DEAD


if __name__ == '__main__':
    wawelski = DragonMedium(name='Wawelski')
    jose = Hero(name='José Jiménez')
    turn = 0

    print(f'Wawelski: {wawelski.hit_points}')
    print(f'Hero: {jose.hit_points}')

    # wawelski.move(right=1, down=1)
    # wawelski.move(left=2, up=2)
    # print(wawelski.get_position())

    while True:
        turn += 1
        print(f'\nTurn: {turn}')

        if wawelski.status == STATUS_DEAD:
            print('Hero won!')
            break

        if jose.status == STATUS_DEAD:
            print('Dragon won!')
            break

        damage = jose.make_damage()
        wawelski.take_damage(damage)

        damage = wawelski.make_damage()
        jose.take_damage(damage)
