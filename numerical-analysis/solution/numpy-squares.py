import numpy as np


np.random.seed(0)

A = np.random.randint(0, 1024, dtype=int, size=(50, 50))
squares = [2**x for x in range(0, 11)]

B = A[np.isin(A, squares)]
B = np.unique(B)
B = np.flip(B)

print(B)
