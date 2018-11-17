import numpy as np


A = np.random.randint(low=10, high=101, size=(16, 16)).astype(float)
print(f'Matrix:\n{A}')

B = A.transpose()
print(f'Transposed:\n{B}')

inner = B[6:10, 6:10]
print(f'Inner:\n{inner}')

# total = sum(inner.flatten())
total = inner.sum()
print(f'Sum: {total}')
