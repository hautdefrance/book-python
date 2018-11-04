from random import randint
from oop_basic_dragon_easy import Dragon, Status


BORDER_X_MAX = 1024
BORDER_X_MIN = 0
BORDER_Y_MAX = 768
BORDER_Y_MIN = 0


class SuperDragon(Dragon):
    def set_position(self, x: int, y: int) -> None:
        """
        >>> wawelski = SuperDragon(name='Red', position_x=0, position_y=0)
        >>> wawelski.move(right=1)
        >>> wawelski.get_position()
        (1, 0)
        >>> wawelski.move(down=1)
        >>> wawelski.get_position()
        (1, 1)
        >>> wawelski.move(left=2)
        >>> wawelski.get_position()
        (0, 1)
        >>> wawelski.move(up=2)
        >>> wawelski.get_position()
        (0, 0)
        """
        x = max(x, BORDER_X_MIN)
        x = min(x, BORDER_X_MAX)

        y = max(y, BORDER_X_MIN)
        y = min(y, BORDER_Y_MAX)

        self.position_x = x
        self.position_y = y

    def make_damage(self):
        if self.is_alive():
            return super().make_damage()
        else:
            return 0


class Hero:
    def _set_initial_hitpoints(self):
        randint(100, 150)

    def __init__(self, name):
        self.name = name
        self.hit_points = self._set_initial_hitpoints()

    def make_damage(self):
        if self.is_dead():
            return 0
        else:
            return randint(1, 15)

    def is_alive(self):
        if self.status == Status.ALIVE:
            return True
        else:
            return False

    def take_damage(self, damage):
        if self.is_dead():
            return None

        self.hit_points -= damage

        if self.hit_points <= 0:
            self.make_dead()

    def make_dead(self):
        print('Dragon is dead')
        self.texture = 'dragon-dead.png'
        self.status = Status.DEAD
        print('Gold: ', randint(1, 100))
        print('Position: ', self.get_position())



if __name__ == '__main__':
    jose = Hero(name='Jose Jimenez')
    wawelski = SuperDragon(name='Wawelski')

    while jose.is_alive() and wawelski.is_alive():
        dmg = jose.make_damage()
        wawelski.take_damage(dmg)

        dmg = wawelski.make_damage()
        jose.take_damage(dmg)
