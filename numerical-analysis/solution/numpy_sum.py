import numpy as np


A = np.random.randint(10, 100, size=(16, 16)).astype(float)
B = A.transpose()
C = B[6:10, 6:10]
total = C.sum()

print(total)
