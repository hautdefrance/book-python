import numpy as np


def matrix_multiplication(A, B):
    """
    >>> import numpy as np

    >>> A = np.array([[1, 0], [0, 1]])
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    [[4, 1], [2, 2]]

    >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
    >>> B = np.matrix([[4,1], [2,2], [5,1], [2,3]])
    >>> matrix_multiplication(A, B)
    [[9, 2], [7, 3], [21, 8], [28, 8]]
    """
    A = np.matrix(A)
    B = np.matrix(B)

    return (A * B).tolist()
