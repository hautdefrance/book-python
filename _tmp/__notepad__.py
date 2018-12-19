from random import randint


class Status:
    ALIVE = 'alive'
    DEAD = 'dead'


class Dragon:
    TEXTURE_ALIVE = 'img/dragon/alive.png'
    TEXTURE_DEAD = 'img/dragon/dead.png'
    HP_MIN = 50
    HP_MAX = 100
    DMG_MIN = 5
    DMG_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.set_position(x, y)
        self.texture = self.TEXTURE_ALIVE
        self.hit_points = self._get_initial_hitpoints()
        self.gold = self._get_initial_gold()
        self.status = Status.ALIVE

    def _get_initial_gold(self):
        return randint(self.GOLD_MIN, self.GOLD_MAX)

    def _get_initial_hitpoints(self):
        return randint(self.HP_MIN, self.HP_MAX)

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def move(self, left=0, down=0, right=0, up=0):
        x = self.position_x + right - left
        y = self.position_y + down - up
        self.set_position(x, y)

    def make_damage(self):
        return randint(self.DMG_MIN, self.DMG_MAX)

    def _set_status(self):
        if self.hit_points > 0:
            self.status = Status.ALIVE
        else:
            self.status = Status.DEAD

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

    def _make_drop(self):
        print(f'Gold dropped {self.gold}')

    def _make_dead(self):
        print(f'{self.name} is dead')
        self.texture = self.TEXTURE_DEAD
        print(f'Position {self.position_x}, {self.position_y}')
        return self._make_drop()

    def take_damage(self, damage):
        self.hit_points -= damage
        self._set_status()

        if self.is_dead():
            return self._make_dead()

        if self.is_alive():
            print(f'{self.name} hit by {damage}, has now {self.hit_points} HP')


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
