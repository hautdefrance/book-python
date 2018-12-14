counter = dict()
numbers = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
           0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
           2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
           1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
           4, 8, 1, 9, 6, 3]

for digit in numbers:
    if digit not in counter:
        counter[digit] = 1
    else:
        counter[digit] += 1

counter.items()
# {
#   0: 7,
#   1: 7,
#   2: 2,
#   3: 3,
#   4: 8,
#   5: 4,
#   6: 4,
#   7: 4,
#   8: 6,
#   9: 5,
# }
