a = (0, 1, 2, 3)
b = [2, 3, 4, 5]

c = set()
c.update(a[::2], b[::2])

print(c)
# {0, 2, 4}
