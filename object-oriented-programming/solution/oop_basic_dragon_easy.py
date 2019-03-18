from random import randint


class Status:
    DEAD = 'dead'
    ALIVE = 'alive'


class Dragon:
    TEXTURE_ALIVE = 'img/dragon/alive.png'
    TEXTURE_DEAD = 'img/dragon/dead.png'
    HIT_POINTS_MIN = 50
    HIT_POINTS_MAX = 100
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100

    def __init__(self, name, position_x=0, position_y=0):
        self.name = name
        self.texture = self.TEXTURE_ALIVE
        self.status = Status.ALIVE
        self.hit_points = self._get_initial_hit_points()
        self.gold = self._get_initial_gold()
        self.set_position(position_x, position_y)

    def _get_initial_gold(self):
        return randint(self.GOLD_MIN, self.GOLD_MAX)

    def _get_initial_hit_points(self):
        return randint(self.HIT_POINTS_MIN, self.HIT_POINTS_MAX)

    def get_position(self):
        return {
            'x': self.position_x,
            'y': self.position_y}

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def move(self, left=0, right=0, up=0, down=0):
        position = self.get_position()
        x = position['x'] + right - left
        y = position['y'] + down - up
        self.set_position(x, y)


        self.set_position(
            x=self.position_x + right - left,
            y=self.position_y + down - up)

    def make_damage(self):
        if self.is_alive():
            return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

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
        if not isinstance(damage, (int, float)):
            raise ValueError('Damage must be int or float')

        if self.is_dead():
            return

        self.hit_points -= damage
        self.set_status()

        if self.is_alive():
            print(f'{self.name}, DAMAGE: {damage}, HIT POINTS: {self.hit_points}')
        else:
            return self._make_dead()

    def _get_drop(self):
        return {
            'position': self.get_position(),
            'gold': self.gold,
        }

    def _make_dead(self):
        self.set_status()
        self.texture = self.TEXTURE_DEAD

        drop = self._get_drop()
        gold = drop['gold']
        position = drop['position']

        print(f'{self.name} is dead')
        print(f'Gold dropped: {gold}')
        print(f'Position {position}')

        return drop


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
