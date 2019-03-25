import random
from pprint import pprint

random.seed(0)
matrix = []
total = 0


for x in range(0, 16):
    matrix.append([])

    for y in range(0, 16):
        losowa = random.randint(0, 9)
        matrix[x].append(losowa)

        if 6 <= x < 10 and 6 <= y < 10:
            total += matrix[x][y]


pprint(matrix)
pprint(total)
