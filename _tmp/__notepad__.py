



# https://www.ventusky.com/krakow


# from random import randint
#
# STATUS_DEAD = 'dead'
#
#
# class Dragon:
#     GOLD_MIN = 1
#     GOLD_MAX = 100
#     HIT_POINTS_MIN = 50
#     HIT_POINTS_MAX = 100
#     TEXTURE_ALIVE = 'img/dragon/alive.png'
#     TEXTURE_DEAD = 'img/dragon/dead.png'
#
#     def __init__(self, name, x=0, y=0):
#         self.name = name
#         self.texture = self.TEXTURE_ALIVE
#         self.hit_points = randint(self.HIT_POINTS_MIN, self.HIT_POINTS_MAX)
#         self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
#         self.set_position(x, y)
#
#     def set_position(self, x, y):
#         self.position_x = x
#         self.position_y = y
#
#     def get_position(self):
#         return self.position_x, self.position_y
#
#     def move(self, left=0, right=0, up=0, down=0):
#         x, y = self.get_position()
#         x += right - left
#         y += down - up
#         self.set_position(x, y)
#
#     def make_damage(self):
#         return randint(5, 20)
#
#     def take_damage(self, damage):
#         if self.is_dead():
#             return None
#
#         self.hit_points -= damage
#
#         if self.hit_points <= 0:
#             return self._make_dead()
#
#     def is_dead(self):
#         if self.hit_points <= 0:
#             return True
#         else:
#             return False
#
#     def _make_dead(self):
#         self.status = STATUS_DEAD
#         self.texture = self.TEXTURE_DEAD
#         print(f'{self.name} is {self.status}')
#         print(f'Position {self.get_position()}')
#         return self._make_drop()
#
#     def _make_drop(self):
#         print(f'Gold dropped {self.gold}')
#
#
# wawelski = Dragon(name='Wawelski', x=50, y=120)
#
# wawelski.set_position(x=10, y=20)
# wawelski.move(left=10, down=20)
# wawelski.move(left=10, right=15)
# wawelski.move(right=15, up=5)
# wawelski.move(down=5)
#
# wawelski.take_damage(10)
# wawelski.take_damage(5)
# wawelski.take_damage(3)
# wawelski.take_damage(2)
# wawelski.take_damage(15)
# wawelski.take_damage(25)
# wawelski.take_damage(75)
#
#
#
#




# """
# Stwórz smoka w pozycji x=50, y=120 i nazwij go Wawelski
# Ustaw nową pozycję na x=10, y=20
# Przesuń smoka o 10 w lewo i 20 w dół
# Przesuń smoka o 10 w lewo i 15 w prawo
# Przesuń smoka o 15 w prawo i 5 w górę
# Przesuń smoka o 5 w dół
# Zadaj 10 obrażeń smokowi
# Zadaj 5 obrażeń smokowi
# Zadaj 3 obrażeń smokowi
# Zadaj 2 obrażeń smokowi
# Zadaj 15 obrażeń smokowi
# Zadaj 25 obrażeń smokowi
# Zadaj 75 obrażeń smokowi
# """
# from random import randint
#
#
# class Dragon:
#     TEXTURE_ALIVE = 'img/dragon/alive.png'
#     TEXTURE_DEAD = 'img/dragon/dead.png'
#     STATUS_DEAD = 'dead'
#     HP_MIN = 50
#     HP_MAX = 100
#     DAMAGE_MIN = 5
#     DAMAGE_MAX = 20
#     GOLD_MIN = 1
#     GOLD_MAX = 100
#
#     def __init__(self, name, position_x, position_y):
#         self.name = name
#         self.texture = self.TEXTURE_ALIVE
#         self.hit_points = self._get_initial_hit_points()
#         self.gold = self._get_initial_gold()
#         self.set_position(position_x, position_y)
#
#     def _get_initial_gold(self):
#         return randint(self.GOLD_MIN, self.GOLD_MAX)
#
#     def _get_initial_hit_points(self):
#         return randint(self.HP_MIN, self.HP_MAX)
#
#     def set_position(self, x, y):
#         self.position_x = x
#         self.position_y = y
#
#     def move(self, left=0, down=0, right=0, up=0):
#         self.set_position(
#             x=self.position_x + right - left,
#             y=self.position_y + down - up
#         )
#
#     def make_damage(self):
#         return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)
#
#     def is_dead(self):
#         if self.hit_points <= 0:
#             return True
#         else:
#             return False
#
#     def is_alive(self):
#         return not self.is_dead()
#
#     def take_damage(self, damage):
#         if not isinstance(damage, (int, float)):
#             raise ValueError('Damage must be int or float')
#
#         if self.is_dead():
#             return
#
#         self.hit_points -= damage
#
#         if self.is_alive():
#             print(f'{self.name}, DAMAGE: {damage}, HIT POINTS: {self.hit_points}')
#         else:
#             return self._make_dead()
#
#     def get_position(self):
#         return {
#             'x': self.position_x,
#             'y': self.position_y}
#
#     def _get_drop(self):
#         return {
#             'position': self.get_position(),
#             'gold': self.gold,
#         }
#
#     def _make_dead(self):
#         self.texture = self.TEXTURE_DEAD
#         self.status = self.STATUS_DEAD
#
#         drop = self._get_drop()
#         gold = drop['gold']
#         position = self.get_position()
#
#         print(f'{self.name} is dead')
#         print(f'Gold dropped: {gold}')
#         print(f'Position {position}')
#
#         return drop
#
#
# wawelski = Dragon(name='Wawelski', position_x=50, position_y=120)
#
# wawelski.set_position(x=10, y=20)
#
# wawelski.move(left=10, down=20)
# wawelski.move(left=10, right=15)
# wawelski.move(right=15, up=5)
# wawelski.move(down=5)
#
# wawelski.take_damage(10)
# wawelski.take_damage(5)
# wawelski.take_damage(3)
# wawelski.take_damage(2)
# wawelski.take_damage(15)
# wawelski.take_damage(25)
# wawelski.take_damage(75)
