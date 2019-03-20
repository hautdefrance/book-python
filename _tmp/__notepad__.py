from itertools import cycle
#
DATA = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Mark', 'last_name': 'Watney'},
    {'first_name': 'Иван'},
    {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
    {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
]
#
# fieldnames = set(key for record in DATA for key in record.keys())
#
# print(fieldnames)



def get_species(species):
    for record in DATA:
        if record[4] == species:
            yield record

data = get_species('setosa')

cycle(data)



# a = 'Jose Jimenez'
# b = 'Jose Jimenez'
#
# print(id(a))
# # 4649319408, 4450998960
# print(id(b))
# # 4649320304, 4450998960
# print(a is b)
# # False, True
# print(a == b)
# # True, True





# from dataclasses import dataclass
# from datetime import datetime, timezone
# from typing import Optional
# from unittest import TestCase
#
#
# @dataclass
# class User:
#     first_name: str
#     last_name: str
#     date_of_birth: Optional[datetime] = None
#     permission: list = ()
#
#     def __post_init__(self):
#         self.permission = list(self.permission)
#
#         if self.date_of_birth and self.date_of_birth.tzinfo != timezone.utc:
#             raise ValueError
#
#     def add_permission(self, permission):
#         self.permission.append(permission)
#
#     def remove_permission(self, permission):
#         self.permission.remove(permission)
#
#     def __str__(self):
#         return f'User(first_name="{self.first_name}", last_name="{self.last_name}")'
#
#
# class UserTest(TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         pass
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         pass
#
#     def setUp(self) -> None:
#         now = datetime.now(tz=timezone.utc)
#         self.user = User(first_name='Jan', last_name='Twardowski', date_of_birth=now)
#
#     def tearDown(self) -> None:
#         pass
#
#     def test_create_user(self):
#         user = User(first_name='Jan', last_name='Twardowski')
#         self.assertEqual(user.first_name, 'Jan')
#         self.assertEqual(user.last_name, 'Twardowski')
#
#     def test_permission_add(self):
#         self.user.add_permission('read')
#         self.assertIn('read', self.user.permission)
#
#     def test_permission_remove(self):
#         self.user.add_permission('read')
#         self.user.remove_permission('read')
#         self.assertNotIn('read', self.user.permission)
#
#     def test_date_of_birth_in_utc(self):
#         self.assertEqual(self.user.date_of_birth.tzinfo, timezone.utc)
#
#     def test_date_of_birth_not_in_utc(self):
#         with self.assertRaises(ValueError):
#             now = datetime.now()
#             user = User(first_name='Jan', last_name='Twardowski', date_of_birth=now)
#             self.assertEqual(user.date_of_birth.tzinfo, timezone.utc)
#
#     def test_str(self):
#         self.assertEqual(str(self.user), 'User(first_name="Jan", last_name="Twardowski")')

# import warnings
#
# administrators = (DeprecationWarning)
#
#
# class RemovedInVersion20(DeprecationWarning):
#     pass
#
#
# def sumuj(a, b):
#     warnings.warn('Use ``sum`` function', RemovedInVersion20)
#     return a + b
#
# def sum(a, b):
#     return a + b
#
#
# sumuj(1, 2)
# sum(1, 2)
