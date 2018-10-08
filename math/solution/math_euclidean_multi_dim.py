import math


def euclidean_distance_n_dimensions(A, B):
    """
    >>> euclidean_distance_n_dimensions((0,0,0), (0,0,0))
    0.0

    >>> euclidean_distance_n_dimensions((0,0,0), (1,1,1))
    1.7320508075688772

    >>> euclidean_distance_n_dimensions((0,1,0,1), (1,1,0,0))
    1.4142135623730951

    >>> euclidean_distance_n_dimensions((0,0,1,0,1), (1,1,0,0,1))
    1.7320508075688772

    >>> euclidean_distance_n_dimensions((0,0,1,0,1), (1,1))
    Traceback (most recent call last):
        ...
    ValueError: Punkty muszą być w przestrzeni tylu-samo wymiarowej
    """
    if len(A) != len(B):
        raise ValueError('Punkty muszą być w przestrzeni tylu-samo wymiarowej')

    pod_pierwiastkiem = 0

    for i, _ in enumerate(A):
        pod_pierwiastkiem += (B[i]-A[i]) ** 2

    return math.sqrt(pod_pierwiastkiem)
