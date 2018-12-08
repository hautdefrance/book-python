
FILENAME = r'hosts.txt'
hosts = dict()


with open(FILENAME) as file:
    for line in file:
        if line.isspace():
            continue

        if line.startswith('#'):
            continue

        ip, *hostnames = line.split()

        if ip not in hosts:
            hosts[ip] = hostnames
        else:
            hosts[ip] += hostnames

print(hosts)





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
