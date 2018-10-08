from enum import Enum
from random import randint


class Status(Enum):
    ALIVE = 'alive'
    DEAD = 'dead'


class Dragon:
    BASE_HIT_POINTS = randint(50, 100)
    BASE_DAMAGE = randint(5, 20)
    TEXTURE = 'dragon.png'

    def __init__(self, name, position_x=0, position_y=0, texture=TEXTURE):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.texture = texture
        self.hit_points = self.BASE_HIT_POINTS
        self.status = Status.ALIVE

    def move(self, left: int = 0, down: int = 0, right: int = 0, up: int = 0) -> None:
        self.set_position(
            x=self.position_x + right - left,
            y=self.position_y + down - up
        )

    def set_position(self, x: int, y: int) -> None:
        self.position_x = x
        self.position_y = y

    def get_position(self):
        return self.position_x, self.position_y

    def is_dead(self):
        if self.status == Status.DEAD:
            return True
        else:
            return False

    def make_damage(self):
        return self.BASE_DAMAGE

    def take_damage(self, damage):
        if self.is_dead():
            return None

        self.hit_points -= damage

        if self.hit_points <= 0:
            self._make_dead()

    def _make_dead(self):
        print('Dragon is dead')
        self.texture = 'dragon-dead.png'
        self.status = Status.DEAD
        print('Gold: ', randint(1, 100))
        print('Position: ', self.get_position())


    # Do not modify anything below!
if __name__ == '__main__':
    wawelski = Dragon(name='Wawelski', position_x=50, position_y=120)

    wawelski.set_position(x=10, y=20)
    wawelski.move(left=10, down=20)
    wawelski.move(left=10, right=15)
    wawelski.move(right=15, up=5)
    wawelski.move(down=5)

    wawelski.take_damage(10)
    wawelski.take_damage(50)
    wawelski.take_damage(35)
    wawelski.take_damage(20)
    wawelski.take_damage(25)
