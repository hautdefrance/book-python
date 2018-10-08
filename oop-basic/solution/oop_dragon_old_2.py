import random


BORDER_LEFT = 0
BORDER_RIGHT = 1024
BORDER_TOP = 0
BORDER_BOTTOM = 768


class Character:
    STATUS_ALIVE = 'alive'
    STATUS_DEAD = 'dead'

    def __init__(self, position_x=0, position_y=0,):
        self.position_x = position_x
        self.position_y = position_y
        self.status = self.STATUS_ALIVE

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def get_position(self):
        return self.position_x, self.position_y

    def move(self, left=0, right=0, down=0, up=0):
        """
        >>> Character(position_x=0, position_y=0).move(right=1)
        >>> Character(position_x=0, position_y=0).move(down=1, right=1)
        >>> Character(position_x=0, position_y=0).move(left=1)
        Traceback (most recent call last):
            ...
        IndexError: Position out of borders
        >>> Character(position_x=0, position_y=0).move(up=1)
        Traceback (most recent call last):
            ...
        IndexError: Position out of borders
        >>> Character(position_x=0, position_y=0).move(left=1, up=1)
        Traceback (most recent call last):
            ...
        IndexError: Position out of borders
        >>> Character(position_x=1024, position_y=768).move(down=1)
        Traceback (most recent call last):
            ...
        IndexError: Position out of borders
        >>> Character(position_x=1024, position_y=768).move(right=1)
        Traceback (most recent call last):
            ...
        IndexError: Position out of borders
        >>> Character(position_x=1024, position_y=768).move(up=1)
        >>> Character(position_x=1024, position_y=768).move(left=1)
        """
        new_x = self.position_x + right - left
        new_y = self.position_y + down - up

        if BORDER_LEFT <= new_x <= BORDER_RIGHT:
            self.position_x = new_x
        else:
            raise IndexError('Position out of borders')

        if BORDER_TOP <= new_y <= BORDER_BOTTOM:
            self.position_y = new_y
        else:
            raise IndexError('Position out of borders')

    def take_damage(self, damage):
        final_hp = self.hit_points - damage

        if final_hp < 0:
            final_hp = 0

        print(f'{self.name:15} HP: {self.hit_points:3}, hit: {damage:2}, final HP: {final_hp}')

        if final_hp > 0:
            self.hit_points = final_hp
        elif self.is_alive():
            self.make_dead()

    def is_alive(self):
        return not self.is_dead()

    def is_dead(self):
        if self.status == self.STATUS_DEAD:
            return True
        else:
            return False


class Dragon(Character):
    def __init__(self, name,  texture='dragon.png'):
        self.name = name
        self.hit_points = random.randint(50, 100)
        self.texture = texture
        super().__init__()

    def make_damage(self):
        return random.randint(5, 20)

    def make_dead(self):
        self.status = self.STATUS_DEAD
        self.texture = 'dragon-dead.png'
        print('Dragon is dead')
        print('Dropped gold: ', random.randint(1, 100))
        print('Position: ', self.get_position())


class Hero(Character):
    def __init__(self, name):
        self.name = name
        self.hit_points = random.randint(100, 150)
        super().__init__()

    def make_damage(self):
        return random.randint(1, 15)

    def make_dead(self):
        self.status = self.STATUS_DEAD
        print(f'{self.name} is dead')


jose = Hero(name='José Jiménez')
wawelski = Dragon(name='Wawelski')


while True:  # Main game loop

    dmg = jose.make_damage()
    wawelski.take_damage(dmg)

    if wawelski.is_dead():
        break

    dmg = wawelski.make_damage()
    jose.take_damage(dmg)

    if jose.is_dead():
        break

    print()
