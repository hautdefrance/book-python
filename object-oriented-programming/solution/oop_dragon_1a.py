from dataclasses import dataclass
from random import randint


class Status:
    ALIVE = 'alive'
    DEAD = 'dead'


@dataclass(frozen=True)
class Position:
    x: int = 0
    y: int = 0


class Movable:
    def set_position_coordinates(self, x: int, y: int) -> None:
        self.set_position(Position(x, y))

    def set_position(self, position: Position = Position()) -> None:
        self.position = position

    def move(self, left: int = 0, down: int = 0, up: int = 0, right: int = 0) -> None:
        x = self.position.x + right - left
        y = self.position.y + down - up
        self.set_position_coordinates(x, y)


class Dragon(Movable):
    TEXTURE_ALIVE = 'img/dragon/alive.png'
    TEXTURE_DEAD = 'img/dragon/dead.png'
    HEALTH_MIN = 50
    HEALTH_MAX = 100
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100

    class IsDead(Exception):
        pass

    def __init__(self, name: str, position: Position = Position()):
        self.name = name
        self.texture = self.TEXTURE_ALIVE
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.update_status()
        self.set_position(position)

    def make_damage(self):
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def is_dead(self):
        if self.status == Status.DEAD:
            return True
        else:
            return False

    def update_status(self):
        if self.health <= 0:
            self.status = Status.DEAD
        else:
            self.status = Status.ALIVE

    def is_alive(self):
        return not self.is_dead()

    def _get_drop(self):
        return {
            'gold': self.gold}

    def _make_dead(self):
        self.texture = self.TEXTURE_DEAD
        return self._get_drop()

    def take_damage(self, damage):
        if self.is_dead():
            raise Dragon.IsDead

        self.health -= damage
        self.update_status()

        if self.is_alive():
            print(f'{self.name}, DMG taken: {damage}, HP left: {self.health}')
        else:
            return self._make_dead()


wawelski = Dragon(name='Wawelski')
wawelski.set_position_coordinates(x=50, y=120)
wawelski.set_position_coordinates(x=10, y=20)

# wawelski.move_left(10)
# wawelski.move(LEFT, 10)
# wawelski.move(DOWN, 20)
# wawelski.move('left', 10)
# wawelski.move(x=-10)
# wawelski.left(10)
wawelski.move(left=10, down=20)
wawelski.move(left=10, right=15)
wawelski.move(right=15, up=5)
wawelski.move(down=5)

# wawelski.get_attacked
# wawelski.get_damage
# wawelski.damage_taken
# wawelski.get_injured
# wawelski.hit_me
# wawelski.hit
# wawelski.attack
# wawelski.try_kill

try:
    wawelski.take_damage(10)
    wawelski.take_damage(5)
    wawelski.take_damage(3)
    wawelski.take_damage(2)
    wawelski.take_damage(15)
    wawelski.take_damage(25)
    wawelski.take_damage(75)
except wawelski.IsDead:
    print(f'{wawelski.name} is dead')
    print(f'Position {wawelski.position}')
    print(f'Gold: {wawelski.gold}')
