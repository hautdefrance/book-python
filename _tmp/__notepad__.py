a = '  Jana III Sobieskiego 1 apt 2'.replace('1', '').replace('2', '')
b = 'ul Jana III SobIESkiego 1/2'
c = '\tul. Jana trzeciego Sobieskiego 1/2'
d = 'ulicaJana III Sobieskiego 1/2'
e = 'UL. JA\tNA 3 SOBIES\tKIEGO 1/2'
f = 'UL. III SOBiesKIEGO 1/2'
g = 'ULICA JANA III SOBIESKIEGO 1 /2  '
h = 'ULICA. JANA III SOBI'
i = ' Jana 3 Sobieskiego 1/2 '
j = 'Jana III Sobieskiego 1 m. 2'
k = 'ul.Jana III Sob\n\nieskiego 1/2'


expected = 'Jana III Sobieskiego'
print(f'{a == expected}\t a: "{a}"')
print(f'{b == expected}\t b: "{b}"')
print(f'{c == expected}\t c: "{c}"')
print(f'{d == expected}\t d: "{d}"')
print(f'{e == expected}\t e: "{e}"')
print(f'{f == expected}\t f: "{f}"')
print(f'{g == expected}\t g: "{g}"')
print(f'{h == expected}\t h: "{h}"')
print(f'{i == expected}\t i: "{i}"')
print(f'{j == expected}\t j: "{j}"')
print(f'{k == expected}\t k: "{k}"')




# a = list(range(0, 3))
# b = list(range(3, 6))
# c = list(range(6, 9))
#
# wynik = [a, b, c]
#
#
# wynik = [list(range(x*3, x*3+3)) for x in range(3)]
#
#
#
# wiersz = wynik[0]
#     element = wiersz[0]
#     element = wiersz[1]
#     element = wiersz[2]
#
# wiersz = wynik[1]
#     element = wiersz[0]
#     element = wiersz[1]
#     element = wiersz[2]
#
# wiersz = wynik[2]
#     element = wiersz[0]
#     element = wiersz[1]
#     element = wiersz[2]
#
#
# for wiersz in wynik:
#
#     for element in wiersz:
#
#         if element % 2 != 0:
#             print(element)
#









# import pandas as pd
#
# FILENAME = r'iris.csv'
#
#
# pd.read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True, skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)
#
#
# pd.read_csv(FILENAME, encoding='utf-8', decimal=',',
#             quotechar='"', delimiter=',', lineterminator='\n')
#





# # def numbers():
# #     return [1, 2, 3, 4, 5, 6, 7]
# #
# #
# # a = numbers()
# #
# #
# #
# # def numbers():
# #     return [1, 2, 3, 4, 5, 6, 7]
# #
# #
# # a, b, *c = numbers()
# #
# # print(a)
# # print(b)
# # print(c)
#
#
#
# # def numbers():
# #     return [1, 2, 3, 4, 5, (6, 7)]
# #
# #
# # *a, b, c = numbers()
# #
# # print(a)
# # print(b)
# # print(c)
#
#
#
# def numbers():
#     return [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, (8,8), (9,9)],
#     ]
#
#
# a, b, c = numbers()
#
# print(a)
# print(b)
# print(c)
#
#
# d, e, f = c
#
# print(d)
# print(e)
# print(f)
#




#
# def celsius_to_fahrenheit(*degrees):
#     print(degrees)
#
#
# celsius_to_fahrenheit()
# # ()
#
# celsius_to_fahrenheit(1)
# # (1,)
#
# celsius_to_fahrenheit(1, 2, 3, 4, 5)
# # (1, 2, 3, 4, 5)

#
# def celsius_to_fahrenheit(**degrees):
#     print(degrees)
#
#
# celsius_to_fahrenheit()
# # {}
#
# celsius_to_fahrenheit(a=1)
# # {'a': 1}
#
# celsius_to_fahrenheit(a=1, b=2, c=3, d=4, e=5)
# # {}

#
# def my_function(x, y, z):
#     print(x, y, z)
#
#
# vector = {'y': 1, 'x': 0, 'z': 1}
#
# my_function(*vector)
# # y x z
#
# my_function(*vector.keys())
# # y x z
#
# my_function(*vector.values())
# # 1 0 1

#
# def sumuj(a, b, c=0):
#     print(locals())
#
# sumuj(1, 2)
# # {'a': 1, 'b': 2, 'c': 0}
#
#
#
#
# def sumuj(a, b, color='zielony', linia='ciagla'):
#     print(locals())
#
#
# parametry = {
#     'color': 'czerwony',
#     'linia': 'przerywana',
# }
#
# sumuj(1, 2, **parametry)
#
#
# sumuj(1, 2, **{
#     'color': 'czerwony',
#     'linia': 'przerywana',
# })
#
# sumuj(1, 2, color='czerwony', linia='przerywana')
#
#
# sumuj(1, 2, **dict(color='czerwony', linia='przerywana'))
#
#
# print()
# print('a')
# print('a', 'b')
# print('a', 'b', 'c', sep=' ', end='\n')
