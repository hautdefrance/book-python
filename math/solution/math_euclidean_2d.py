import math


def euclidean_distance(A, B):
    """
    >>> A = (1, 0)
    >>> B = (0, 1)
    >>> euclidean_distance(A, B)
    1.4142135623730951

    >>> euclidean_distance((0,0), (1,0))
    1.0

    >>> euclidean_distance((0,0), (1,1))
    1.4142135623730951

    >>> euclidean_distance((0,1), (1,1))
    1.0

    >>> euclidean_distance((0,10), (1,1))
    9.055385138137417
    """

    x1 = A[0]
    x2 = B[0]

    y1 = A[1]
    y2 = B[1]

    part_x = (x2-x1) ** 2
    part_y = (y2-y1) ** 2

    return math.sqrt(part_x + part_y)

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return math.sqrt(pow(B[1]-A[1],2)+pow(B[0]-A[0],2))
