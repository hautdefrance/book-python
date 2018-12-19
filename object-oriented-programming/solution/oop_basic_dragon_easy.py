from random import randint


class Status:
    DEAD = 'dead'
    ALIVE = 'alive'


class Dragon:
    HIT_POINTS_MAX = 100
    HIT_POINTS_MIN = 50
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100
    TEXTURE_LIVE = 'dragon.png'
    TEXTURE_DEAD = 'dragon-dead.png'

    def __init__(self, name, position_x=0, position_y=0, texture=TEXTURE_LIVE):
        self.name = name
        self.hit_points = randint(self.HIT_POINTS_MIN, self.HIT_POINTS_MAX)
        self.status = Status.ALIVE
        self.texture = texture
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.set_position(position_x, position_y)

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def move(self, left=0, right=0, up=0, down=0):
        self.set_position(
            x=self.position_x + right - left,
            y=self.position_y + down - up)

    def get_position(self):
        return self.position_x, self.position_y

    def make_damage(self):
        if self.is_dead():
            return None
        else:
            return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def _make_drop(self):
        print(f'Dropped {self.gold} gold')
        return self.gold

    def _make_dead(self):
        print(f'{self.name} is dead')
        self.texture = self.TEXTURE_DEAD
        print(f'Position: {self.get_position()}')
        return self._make_drop()

    def set_status(self):
        if self.hit_points <= 0:
            self.status = Status.DEAD
        else:
            self.status = Status.ALIVE

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

    def take_damage(self, damage):
        if self.is_dead():
            return None

        self.hit_points -= damage
        self.set_status()

        if self.is_alive():
            print(f'{self.name}, took DMG: {damage}, current HP: {self.hit_points}')
        else:
            self._make_dead()


def run():
    wawelski = Dragon(name='Wawelski', position_x=50, position_y=120)

    wawelski.set_position(x=10, y=20)
    wawelski.move(left=10, down=20)
    wawelski.move(left=10, right=15)
    wawelski.move(right=15, up=5)
    wawelski.move(down=5)

    wawelski.take_damage(10)
    wawelski.take_damage(5)
    wawelski.take_damage(3)
    wawelski.take_damage(2)
    wawelski.take_damage(25)
    wawelski.take_damage(30)
    wawelski.take_damage(75)


if __name__ == '__main__':
    run()
