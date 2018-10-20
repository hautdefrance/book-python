a = (0, 1, 2, 3)
print(a)

b = list(a)
print(b)

b.insert(0, a)
print(b)
# [(0, 1, 2, 3), 0, 1, 2, 3]

c = set(b[0])
c.update(b[1:])
print(c)
# {0, 1, 2, 3}
