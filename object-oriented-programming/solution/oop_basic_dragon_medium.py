from enum import Enum
from oop_basic_dragon_easy import Dragon, Status


class Status(Status):
    FULL_HEALTH = 'Pełnia życia'
    LIGHT_WOUNDED = 'Lekko Ranny'
    SERIOUSLY_WOUNDED = 'Poważnie ranny'
    NEAR_DEAD = 'Na skraju śmierci'


class Config:
    BORDER_X_MAX = 1024
    BORDER_X_MIN = 0
    BORDER_Y_MAX = 768
    BORDER_Y_MIN = 0


class CharacterClass(Enum):
    WARRIOR = 'wojownik'


class Character(Dragon):

    def __init__(self, name, position_x=0, position_y=0):
        super().__init__(name, position_x, position_y)
        self.hit_points_full = self.hit_points
        self.status = Status.FULL_HEALTH

    def set_status(self):
        procent = self.hit_points / self.hit_points_full * 100

        if procent == 100:
            self.status = Status.FULL_HEALTH
        elif 75 <= procent < 100:
            self.status = Status.LIGHT_WOUNDED
        elif 25 <= procent < 75:
            self.status = Status.SERIOUSLY_WOUNDED
        elif 0 < procent < 25:
            self.status = Status.NEAR_DEAD
        else:
            self.status = Status.DEAD

    def _make_dead(self):
        self.texture = self.TEXTURE_DEAD
        self._make_drop()
        print(f'{self.name} is dead')
        print(f'Position: {self.get_position()}')

    def within_boundaries(self, value, min, max):
        if value > max:
            return max

        if value < min:
            return min

        return value

    def set_position(self, x, y):
        """
        >>> wawelski = MediumDragon(name='Red', position_x=0, position_y=0)
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
        self.position_x = self.within_boundaries(
            value=x,
            min=Config.BORDER_X_MIN,
            max=Config.BORDER_X_MAX)

        self.position_y = self.within_boundaries(
            value=y,
            min=Config.BORDER_Y_MIN,
            max=Config.BORDER_Y_MAX)


class MediumDragon(Character):
    LIFE_MIN = 100
    LIFE_MAX = 150


class Hero(Character):
    LIFE_MIN = 100
    LIFE_MAX = 150
    DMG_MIN = 1
    DMG_MAX = 15
    GOLD_MIN = 0
    GOLD_MAX = 0
    CHARACTER_CLASS = CharacterClass.WARRIOR


wawelski = MediumDragon(name='Wawelski')
jose = Hero(name='Jose Jimenez')

turn = 0

while wawelski.is_alive() and jose.is_alive():
    turn += 1
    print(f'\nTurn: {turn}')

    dmg = wawelski.make_damage()
    jose.take_damage(dmg)

    if jose.is_alive():
        dmg = jose.make_damage()
        wawelski.take_damage(dmg)

    if wawelski.is_dead():
        jose.gold += wawelski.gold
