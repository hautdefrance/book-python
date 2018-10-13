a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a)

b = list(a)
print(b)

b.insert(0, a)
print(b)
# [(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

c = set(b[0])
c.update(b[1:])
print(c)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
