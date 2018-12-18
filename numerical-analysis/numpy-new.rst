*****
Numpy
*****


NumPy jest podstawowym pakiet (dodatkowym) w Pythonie do obliczeń naukowych. Integruje on niskopoziomowe biblioteki takie jak BLAS i LAPACK lub ATLAS. Podstawowe właściwości NumPy to :

    - potężny N-wymiarowy obiekt tablicy danych
    - rozbudowane funkcje
    - narzędzia do integracji z kodem napisanym w C/C++ i Fortranie
    - narzędzia do algebry liniowej, transformaty Fouriera czy generator liczb losowych

NumPy is the fundamental package for scientific computing with Python. It contains among other things:

    - a powerful N-dimensional array object
    - sophisticated (broadcasting) functions
    - tools for integrating C/C++ and Fortran code
    - useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

* http://www.numpy.org/

Import
======
.. code-block:: python

    import numpy as np


Data Structures
===============
* Skalar - jednowymiarowa
* Wektor - dwuwymiarowa
* Tensor - trójwymiarowa
* Tablica - czterowymiarowa
* Macierz - n-wymiarowa


Functions
=========
* ``np.abs()``
* ``np.sign()``
* ``np.sqrt()``
* ``np.log()``
* ``np.log10()``
* ``np.exp()``
* ``np.sin()``
* ``np.cos()``
* ``np.tan()``
* ``np.arcsin()``
* ``np.arccos()``
* ``np.arctan()``
* ``np.sinh()``
* ``np.cosh()``
* ``np.tanh()``
* ``np.arcsinh()``
* ``np.arccosh()``
* ``np.arctanh()``


Statistics
==========

Compute the median along the specified axis
-------------------------------------------
.. code-block:: python

    a = np.array([1, 4, 3, 8, 9, 2, 3], float)

    np.median(a)
    # 3.0

Estimate a covariance matrix, given data and weights
----------------------------------------------------
.. code-block:: python

    a = np.array([[1, 2, 1, 3], [5, 3, 1, 8]], float)

    np.cov(a)
    # array([[ 0.91666667, 2.08333333],
    #        [ 2.08333333, 8.91666667]])

    np.cov(a, ddof=0)
    # array([[0.6875, 1.5625],
    #       [1.5625, 6.6875]])


Pearson product-moment correlation coefficients
-----------------------------------------------
.. code-block:: python

    a = np.array([[1, 2, 1, 3], [5, 3, 1, 8]], float)

    np.corrcoef(a)
    # array([[ 1. , 0.72870505],
    #        [ 0.72870505, 1. ]])


Random numbers
==============
* Mersenne Twister algorithm for pseudorandom number generation

Seed the generator
------------------
.. code-block:: python

    np.random.seed(293423)

Random values in a given shape
------------------------------
* Random samples from a uniform distribution over ``[0, 1)``

.. code-block:: python

    np.random.rand(5)
    # array([ 0.40783762, 0.7550402 , 0.00919317, 0.01713451, 0.95299583])

    np.random.rand(2,3)
    # array([[ 0.50431753, 0.48272463, 0.45811345],
    #        [ 0.18209476, 0.48631022, 0.49590404]])

    np.random.rand(6).reshape((2,3))
    # array([[ 0.72915152, 0.59423848, 0.25644881],
    #        [ 0.75965311, 0.52151819, 0.60084796]])

Random floats in the half-open interval ``[0.0, 1.0)``
------------------------------------------------------
* Results are from the “continuous uniform” distribution over the stated interval

.. code-block:: python

    np.random.random()
    # 0.70110427435769551

Random integers from low (inclusive) to high (exclusive)
--------------------------------------------------------
.. code-block:: python

    np.random.randint(5, 10)
    # 9

Draw samples from a Poisson distribution
----------------------------------------
.. code-block:: python

    np.random.poisson(6.0)  # Poisson distribution with lambda = 6.0
    # 5

Draw random samples from a normal (Gaussian) distribution
---------------------------------------------------------
.. code-block:: python

    np.random.normal(1.5, 4.0)  # continuous normal (Gaussian) distribution with mean micro=1.5 and standard deviation sigma=4.0
    # 0.83636555041094318

    np.random.normal()  # micro=0.0, sigma=1.0
    # 0.27548716940682932

    np.random.normal(size=5)
    # array([-1.67215088, 0.65813053, -0.70150614, 0.91452499, 0.71440557])

Modify a sequence in-place by shuffling its contents
----------------------------------------------------
.. code-block:: python

    arr = range(10)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    np.random.shuffle(arr)
    # [4, 9, 5, 0, 2, 7, 6, 8, 1, 3]

Multi-dimensional arrays are only shuffled along the first axis:

    .. code-block:: python

        arr = np.arange(9).reshape((3, 3))

        np.random.shuffle(arr)
        # array([[3, 4, 5],
        #       [6, 7, 8],
        #       [0, 1, 2]])

Polynomial mathematics
======================

Defining polynomial
-------------------
.. code-block:: text

    Ax^3 + Bx^2 + Cx^1 + D

.. code-block:: python

    np.poly([-1, 1, 1, 10])
    # array([ 1, -11, 9, 11, -10])

Roots of a polynomial
---------------------
.. code-block:: python

    np.roots([1, 4, -2, 3])
    # array([-4.57974010+0.j , 0.28987005+0.75566815j, 0.28987005-0.75566815j])

    np.roots([ 1, -11, 9, 11, -10])
    #array([10.+0.0000000e+00j, -1.+0.0000000e+00j,
    #       1.+9.6357437e-09j, 1.-9.6357437e-09j])

Antiderivative (indefinite integral) of a polynomial
----------------------------------------------------
.. code-block:: python

    np.polyint([1, 1, 1, 1])
    # array([ 0.25 , 0.33333333, 0.5 , 1. , 0. ])

Derivatives
-----------
.. code-block:: python

    np.polyder([1./4., 1./3., 1./2., 1., 0.])
    # array([ 1., 1., 1., 1.])

Evaluate a polynomial at specific values
----------------------------------------
.. code-block:: python

    np.polyval([1, -2, 0, 2], 4)
    # 34

Least squares polynomial fit
----------------------------
.. code-block:: python

    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [0, 2, 1, 3, 7, 10, 11, 19]

    np.polyfit(x, y, 2)
    # array([ 0.375 , -0.88690476, 1.05357143])

Polynomial Arithmetic
---------------------
* ``np.polyadd()``
* ``np.polysub()``
* ``np.polymul()``
* ``np.polydiv()``


Find the sum of two polynomials:
    .. code-block:: python

        np.polyadd([1, 2], [9, 5, 4])
        # array([9, 6, 6])


Arrays
======

Create array
------------
* From list:

    .. code-block:: python

        import numpy as np

        np.array([1, 2, 3])
        # [1, 2, 3]

        np.array([1, 4, 5, 8], float)
        # array([ 1., 4., 5., 8.])

        np.array([[1,2], [3,4]])
        # array([[1, 2],
        #        [3, 4]])

* Generate array:

    .. code-block:: python

        import numpy as np

        np.arange(3)
        # array([0, 1, 2])

        np.arange(3.0)
        # array([ 0.,  1.,  2.])

        np.arange(3, 7)
        # array([3, 4, 5, 6])

        np.arange(3, 7, step=2)
        # array([3, 5])

        np.arange(start=3, stop=7, step=2, dtype=float)
        # array([3., 5.])

Slice array
-----------
.. code-block:: python

    np.array([1, 4, 5, 8], float)
    # array([ 1., 4., 5., 8.])

    a[:2]
    # array([ 1., 4.])

    a[3]
    # 8.0

    a[0] = 5.
    # array([ 5., 4., 5., 8.])

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)
    # array([[ 1., 2., 3.], [ 4., 5., 6.]])

    a[0,0]  # 1.0
    a[0,1]  # 2.0

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    a[1,:]      # array([ 4., 5., 6.])
    a[:,2]      # array([ 3., 6.])
    a[-1:,-2:]  # array([[ 5., 6.]])

Array shape
-----------
.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    a.shape  # (2, 3)
    a.dtype  # dtype('float64')

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], int)

    a.astype(float)
    a.dtype  # dtype('float64')

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    len(a)  # 2

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    2 in a
    # True

    0 in a
    # False

.. code-block:: python

    a = np.array(range(10), float)
    # array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])

    a = a.reshape((5, 2))
    # array([[ 0., 1.],
    #        [ 2., 3.],
    #        [ 4., 5.],
    #        [ 6., 7.],
    #        [ 8., 9.]])

    a.shape
    # (5, 2)

.. code-block:: python

    a = np.array([1, 2, 3], float)

    b = a
    c = a.copy()

    a[0] = 0
    # array([0., 2., 3.])

    b
    # array([0., 2., 3.])

    c
    # array([1., 2., 3.])

.. code-block:: python

    a = np.array([1, 2, 3], float)

    a.tolist()
    # [1.0, 2.0, 3.0]

    list(a)
    # [1.0, 2.0, 3.0]

.. code-block:: python

    a = np.array([1, 2, 3], float)

    s = a.tostring()
    # '\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'

    np.fromstring(s)
    # array([ 1., 2., 3.])

Array modification
------------------
.. code-block:: python

    a = np.array([1, 2, 3], float)
    # array([ 1., 2., 3.])

    a.fill(0)
    # array([ 0., 0., 0.])

.. code-block:: python

    a = np.array(range(6), float).reshape((2, 3))
    # array([[ 0., 1., 2.],
    #        [ 3., 4., 5.]])

    a.transpose()
    # array([[ 0., 3.],
    #        [ 1., 4.],
    #        [ 2., 5.]])

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)
    # array([[ 1., 2., 3.],
    #        [ 4., 5., 6.]])

    a.flatten()
    # array([ 1., 2., 3., 4., 5., 6.])

.. code-block:: python

    a = np.array(range(6), float).reshape((2, 3, 1))
    # array([[[0.],
    #         [1.],
    #         [2.]],
    #
    #        [[3.],
    #         [4.],
    #         [5.]]])

Concatenation
-------------
.. code-block:: python

    a = np.array([1,2], float)
    b = np.array([3,4,5,6], float)
    c = np.array([7,8,9], float)

    np.concatenate((a, b, c))
    # array([1., 2., 3., 4., 5., 6., 7., 8., 9.])

.. code-block:: python

    a = np.array([[1, 2], [3, 4]], float)
    b = np.array([[5, 6], [7,8]], float)

    np.concatenate((a,b))
    # array([[ 1., 2.],
    #        [ 3., 4.],
    #        [ 5., 6.],
    #        [ 7., 8.]])

    np.concatenate((a,b), axis=0)
    # array([[ 1., 2.],
    #        [ 3., 4.],
    #        [ 5., 6.],
    #        [ 7., 8.]])

    np.concatenate((a,b), axis=1)
    # array([[ 1., 2., 5., 6.],
    #        [ 3., 4., 7., 8.]])

.. code-block:: python

    a = np.array([1, 2, 3], float)
    # array([1., 2., 3.])

    a[:,np.newaxis]
    # array([[ 1.],
    #        [ 2.],
    #        [ 3.]])

    a[:,np.newaxis].shape
    # (3,1)

    b[np.newaxis,:]
    # array([[ 1., 2., 3.]])

    b[np.newaxis,:].shape
    # (1,3)

.. code-block:: python

    n1 = np.array([1,2,3])
    n2 = np.array([[1,2],[3,4]])

    f'Wymiar: n1: {n1.ndim}, n2: {n2.ndim}'
    # Wymiar: n1: 1, n2: 2

    f'Kształt: n1: {n1.shape}, n2: {n2.shape}'
    # Kształt: n1: (3,), n2: (2, 2)

    f'Rozmiar: n1: {n1.size}, n2: {n2.size}'
    # Rozmiar: n1: 3, n2: 4

    f'Typ: n1: {n1.dtype}, n2: {n2.dtype}'
    # Typ: n1: int32, n2: int32

    f'Rozmiar elementu (w bajtach): n1: {n1.itemsize}, n2: {n2.itemsize}'
    # Rozmiar elementu (w bajtach): n1: 4, n2: 4

    f'Wskaźnik do danych: n1: {n1.data}, n2: {n2.data}'
    # Wskaźnik do danych: n1: <memory at 0x000001B93EC75348>, n2: <memory at 0x000001B93EC5BB40>


W przeciwieństwie do kolekcji, tablice mogą mieć tylko jeden typ elementu, choć może być złożony
https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html

.. code-block:: python

    for v in [1, 1., 1j]:
       a = np.array([v])
       print('Tablica: {}, typ: {}'.format(a, a.dtype))

    # Można też wymusić typ przy tworzeniu tablicy
    a = np.array([1], dtype=str)

    f'Tablica: {a}, typ: {a.dtype}'
    # Tablica: [1], typ: int32
    # Tablica: [1.], typ: float64
    # Tablica: [0.+1.j], typ: complex128
    # Tablica: ['1'], typ: <U1

.. code-block:: python

    np.arange(1,10)
    # [1 2 3 4 5 6 7 8 9]

    np.zeros((2,3))
    # [[0. 0. 0.]
    #  [0. 0. 0.]]

    np.ones((3,2))
    # [[1. 1.]
    #  [1. 1.]
    #  [1. 1.]]

    np.empty((2,7))  # Bez inicjalizacji
    # [[1.01855798e-312 1.18831764e-312 1.01855798e-312 9.54898106e-313
    #   1.06099790e-312 1.03977794e-312 1.23075756e-312]
    # [1.20953760e-312 1.06099790e-312 9.76118064e-313 1.01855798e-312
    #  1.01855798e-312 1.16709769e-312 4.44659081e-322]]

    np.random.rand(2,2)
    # [[0.6468727  0.76909227]
    #  [0.89730518 0.13993221]]

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    np.zeros_like(a)
    # array([[ 0., 0., 0.],
    #        [ 0., 0., 0.]])

    np.ones_like(a)
    # array([[ 1., 1., 1.],
    #        [ 1., 1., 1.]])

    np.identity(4, dtype=float)
    # array([[ 1., 0., 0., 0.],
    #        [ 0., 1., 0., 0.],
    #        [ 0., 0., 1., 0.],
    #        [ 0., 0., 0., 1.]])

Array slicing
-------------
.. code-block:: python

    n1 = np.array([1,2,3])
    n2 = np.array([[1,2],[3,4]])

    n1[1], n2[1][1]
    # 2 4

    n2[1,1]
    # 4

    n2[1,:]
    # [3 4]

    n2[:,1]
    # [2 4]

    n2[1,:1]
    # [3]

.. code-block:: python

    a = np.random.randint(100,size=(2,3))
    # [[38  5 91]
    #  [26 33 65]]

    2*a
    # [[ 76  10 182]
    #  [ 52  66 130]]

    a**2
    # [[1444   25 8281]
    #  [ 676 1089 4225]]

    a*a
    # [[1444   25 8281]
    #  [ 676 1089 4225]]

Array math operations
---------------------
.. code-block:: python

    a = np.array([1,2,3], float)
    b = np.array([5,2,6], float)

    a + b
    # array([6., 4., 9.])

    a - b
    # array([-4., 0., -3.])

    a * b
    # array([5., 4., 18.])

    b / a
    # array([5., 1., 2.])

    a % b
    # array([1., 0., 3.])

    b**a
    # array([5., 4., 216.])

.. code-block:: python

    a = np.array([[1,2], [3,4]], float)
    b = np.array([[2,0], [1,3]], float)

    a * b
    # array([[2., 0.], [3., 12.]])

.. warning:: For two-dimensional arrays, multiplication ``*`` remains elementwise and does not correspond to matrix multiplication.

Array Multiplication
--------------------
.. code-block:: text

    a = np.array([[1, 0], [0, 1]])
    b = np.array([[4, 1], [2, 2]])

    a @ b
    # [[4, 1], [2, 2]]

.. code-block:: python

    a = np.array([1,2,3], float)
    b = np.array([4,5], float)

    a + b
    # ValueError: shape mismatch: objects cannot be broadcast to a single shape

.. code-block:: python

    a = np.array([[1, 2], [3, 4], [5, 6]], float)
    # array([[ 1., 2.],
    #  [ 3., 4.],
    #  [ 5., 6.]])

    b = np.array([-1, 3], float)
    # array([-1., 3.])

    a + b
    # array([[ 0., 5.],
    #  [ 2., 7.],
    #  [ 4., 9.]])

.. code-block:: python

    a = np.zeros((2,2), float)
    # array([[ 0., 0.],
    #        [ 0., 0.]])

    b = np.array([-1., 3.], float)
    # array([-1., 3.])

    a + b
    # array([[-1., 3.],
    #        [-1., 3.]])

    a + b[np.newaxis,:]
    # array([[-1., 3.],
    #        [-1., 3.]])

    a + b[:,np.newaxis]
    # array([[-1., -1.],
    #        [ 3., 3.]])

.. code-block:: python

    a = np.array([1.1, 1.5, 1.9], float)

    np.sqrt(a)
    # array([ 1., 2., 3.])

    np.floor(a)
    # array([ 1., 1., 1.])

    np.ceil(a)
    # array([ 2., 2., 2.])

    np.rint(a)
    # array([ 1., 2., 2.])

.. code-block:: python

    np.pi
    # 3.1415926535897931

    np.e
    # 2.7182818284590451

    np.nan
    # NaN

    np.inf
    # inf

Array iteration
---------------
.. code-block:: python

    >>> a = np.array([1, 4, 5], int)

    for x in a:
        print x

    # 1
    # 4
    # 5

.. code-block:: python

    a = np.array([[1, 2], [3, 4], [5, 6]], float)

    for x in a:
        print x

    # [ 1. 2.]
    # [ 3. 4.]
    # [ 5. 6.]

Array operations
----------------
.. code-block:: python

    a = np.array([2, 4, 3], float)

    a.sum()
    # 9.0

    a.prod()
    # 24.0

.. code-block:: python

    a = np.array([2, 1, 9], float)

    a.mean()
    # 4.0

    a.var()
    # 12.666666666666666

    a.std()
    # 3.5590260840104371

    a.min()
    # 1.0

    a.max()
    # 9.0

    a.argmin()  # index of an ``a.min()`` element in array
    # 1

    a.argmax()  # index of an ``a.max()`` element in array
    # 2

.. code-block:: python

    a = np.array([[0, 2], [3, -1], [3, 5]], float)

    a.mean(axis=0)
    # array([ 2., 2.])

    a.mean(axis=1)
    # array([ 1., 1., 4.])

    a.min(axis=1)
    # array([ 0., -1., 3.])

    a.max(axis=0)
    # array([ 3., 5.])

.. code-block:: python

    a = np.array([6, 2, 5, -1, 0], float)

    sorted(a)
    # [-1.0, 0.0, 2.0, 5.0, 6.0]

    a.sort()
    # array([-1., 0., 2., 5., 6.])

.. code-block:: python

    a = np.array([6, 2, 5, -1, 0], float)

    a.clip(0, 5)
    # array([ 5., 2., 5., 0., 0.])

.. code-block:: python

    a = np.array([1, 1, 4, 5, 5, 5, 7], float)

    np.unique(a)
    # array([ 1., 4., 5., 7.])

.. code-block:: python

    a = np.array([[1, 2], [3, 4]], float)

    a.diagonal()
    # array([ 1., 4.])

Array arithmetic
----------------
.. code-block:: python

    a = np.array([[1,2], [3,4]], float)
    b = np.array([[2,0], [1,3]], float)

    a * b
    # array([[2., 0.], [3., 12.]])

.. code-block:: python

    a = np.array([1,2,3], float)
    b = np.array([4,5], float)

    a + b
    # ValueError: shape mismatch: objects cannot be broadcast to a single shape

.. code-block:: python

    a = np.array([[1, 2], [3, 4], [5, 6]], float)
    b = np.array([-1, 3], float)

    a
    # array([[ 1., 2.],
    #        [ 3., 4.],
    #        [ 5., 6.]])

    b
    # array([-1., 3.])

    a + b
    # array([[ 0., 5.],
    #        [ 2., 7.],
    #        [ 4., 9.]])

.. code-block:: python

    a = np.zeros((2,2), float)
    # array([[ 0., 0.],
    #        [ 0., 0.]])

    b = np.array([-1., 3.], float)
    # array([-1., 3.])

    a + b
    # array([[-1., 3.],
    #        [-1., 3.]])

    a + b[np.newaxis,:]
    # array([[-1., 3.],
    #        [-1., 3.]])

    a + b[:,np.newaxis]
    # array([[-1., -1.],
    #        [ 3., 3.]])

Comparison operators and value testing
--------------------------------------
.. code-block:: python

    a = np.array([1, 3, 0], float)
    b = np.array([0, 3, 2], float)

    a > b
    # array([ True, False, False], dtype=bool)

    a == b
    # array([False, True, False], dtype=bool)

    a <= b
    # array([False, True, True], dtype=bool)

    c = a > b
    # array([ True, False, False], dtype=bool)

.. code-block:: python

    a = np.array([1, 3, 0], float)
    a > 2
    # array([False, True, False], dtype=bool)

.. code-block:: python

    c = np.array([ True, False, False], bool)

    any(c)
    # True

    all(c)
    # False

.. code-block:: python

    a = np.array([1, 3, 0], float)

    np.logical_and(a > 0, a < 3)
    # array([ True, False, False], dtype=bool)

.. code-block:: python

    a = np.array([True, False, True], bool)

    np.logical_not(a)
    # array([False, True, False], dtype=bool)

.. code-block:: python

    a = np.array([True, False, True], bool)
    b = np.array([False, True, False], bool)

    np.logical_or(a, b)
    # array([ True, True, False], dtype=bool)

Where
^^^^^
* Single argument where ``where(boolarray)``:

    .. code-block:: python

        a = np.array([1, 3, 0], float)

        np.where(a != 0)
        # array([0, 1])  # indexes of elements


        b = np.array([1, 0, 3, 4, 0], float)
        np.where(b != 0)
        # array([0, 2, 3])

* Multiple argument where ``where(boolarray, truearray, falsearray)``:

    .. code-block:: python

        a = np.array([1, 3, 0], float)

        np.where(a != 0, a, None)  # for element ``a != 0`` return such element, otherwise ``None``
        # array([1.0, 3.0, None], dtype=object)

    .. code-block:: python

        a = np.array([1, 3, 0], float)

        np.where(a != 0, 1 / a, a)
        # array([ 1. , 0.33333333, 0. ])

    .. code-block:: python

        a = np.array([1, 3, 0], float)

        np.where(a != 0, 1 / a, a)
        # array([ 1. , 0.33333333, 0. ])

        np.where(a > 0, 3, 2)
        # array([3, 3, 2])

        a = np.array([1, -3, 3, 0], float)
        np.logical_and(a > 0, a % 3 == 0)
        # array([False, False, False, False])

Nonzero
^^^^^^^
.. code-block:: python

    a = np.array([[0, 1], [3, 0]], float)
    a.nonzero()
    # (array([0, 1]), array([1, 0]))

IsFinite and IsNaN
^^^^^^^^^^^^^^^^^^
.. code-block:: python

    a = np.array([1, np.NaN, np.Inf], float)
    # array([ 1., NaN, Inf])

    np.isnan(a)
    # array([False, True, False], dtype=bool)

    np.isfinite(a)
    # array([True, False, False], dtype=bool)

Array item selection and manipulation
-------------------------------------
.. code-block:: python

    a = np.array([[6, 4], [5, 9]], float)

    a >= 6
    # array([[ True, False],
    #        [False, True]], dtype=bool)

    a[a >= 6]
    # array([ 6., 9.])

.. code-block:: python

    a = np.array([[6, 4], [5, 9]], float)

    sel = (a >= 6)
    a[sel]
    # array([ 6., 9.])

    a[np.logical_and(a > 5, a < 9)]
    # array([ 6.])

.. code-block:: python

    a = np.array([2, 4, 6, 8], float)
    b = np.array([0, 0, 1, 3, 2, 1], int)

    a[b]
    # array([ 2., 2., 4., 8., 6., 4.])

.. code-block:: python

    a = np.array([2, 4, 6, 8], float)

    a[[0, 0, 1, 3, 2, 1]]
    # array([ 2., 2., 4., 8., 6., 4.])

.. code-block:: python

    a = np.array([[1, 4], [9, 16]], float)
    b = np.array([0, 0, 1, 1, 0], int)
    c = np.array([0, 1, 1, 1, 1], int)

    a[b,c]
    # array([ 1., 4., 16., 16., 4.])

.. code-block:: python

    a = np.array([2, 4, 6, 8], float)
    b = np.array([0, 0, 1, 3, 2, 1], int)

    a.take(b)
    # array([ 2., 2., 4., 8., 6., 4.])

.. code-block:: python

    a = np.array([[0, 1], [2, 3]], float)
    b = np.array([0, 0, 1], int)

    a.take(b, axis=0)
    # array([[ 0., 1.],
    #        [ 0., 1.],
    #        [ 2., 3.]])

    a.take(b, axis=1)
    # array([[ 0., 0., 1.],
    #        [ 2., 2., 3.]])

.. code-block:: python

    a = np.array([0, 1, 2, 3, 4, 5], float)
    b = np.array([9, 8, 7], float)

    a.put([0, 3], b)
    # array([ 9., 1., 2., 8., 4., 5.])

.. code-block:: python

    a = np.array([0, 1, 2, 3, 4, 5], float)

    a.put([0, 3], 5)
    # array([ 5., 1., 2., 5., 4., 5.])


Vector and matrix mathematics
=============================
.. code-block:: python

    a = np.array([1, 2, 3], float)
    b = np.array([0, 1, 1], float)

    np.dot(a, b)
    # 5.0

.. code-block:: python

    a = np.array([[0, 1], [2, 3]], float)
    b = np.array([2, 3], float)
    c = np.array([[1, 1], [4, 0]], float)

    a
    # array([[ 0., 1.],
    #        [ 2., 3.]])

    np.dot(b, a)
    # array([ 6., 11.])

    np.dot(a, b)
    # array([ 3., 13.])

    np.dot(a, c)
    # array([[ 4., 0.],
    #        [ 14., 2.]])

    np.dot(c, a)
    # array([[ 2., 4.],
    #        [ 0., 4.]])

.. code-block:: python

    a = np.array([1, 4, 0], float)
    b = np.array([2, 2, 1], float)

    np.outer(a, b)
    # array([[ 2., 2., 1.],
    #        [ 8., 8., 4.],
    #        [ 0., 0., 0.]])

    np.inner(a, b)
    # 10.0

    np.cross(a, b)
    # array([ 4., -1., -6.])

.. code-block:: python

    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    np.linalg.det(a)
    # -53.999999999999993

.. code-block:: python

    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    vals, vecs = np.linalg.eig(a)

    vals
    # array([ 9. , 2.44948974, -2.44948974])

    vecs
    # array([[-0.3538921 , -0.56786837, 0.27843404],
    #        [-0.88473024, 0.44024287, -0.89787873],
    #        [-0.30333608, 0.69549388, 0.34101066]])

.. code-block:: python

    a = np.array([[4, 2, 0], [9, 3, 7], [1, 2, 1]], float)
    # array([[ 4., 2., 0.],
    #        [ 9., 3., 7.],
    #        [ 1., 2., 1.]])

    b = np.linalg.inv(a)
    # array([[ 0.14814815, 0.07407407, -0.25925926],
    #        [ 0.2037037 , -0.14814815, 0.51851852],
    #        [-0.27777778, 0.11111111, 0.11111111]])

    np.dot(a, b)
    # array([[ 1.00000000e+00, 5.55111512e-17, 2.22044605e-16],
    #        [ 0.00000000e+00, 1.00000000e+00, 5.55111512e-16],
    #        [ 1.11022302e-16, 0.00000000e+00, 1.00000000e+00]])

.. code-block:: python

    a = np.array([[1, 3, 4], [5, 2, 3]], float)

    U, s, Vh = np.linalg.svd(a)

    U
    # array([[-0.6113829 , -0.79133492],
    #        [-0.79133492, 0.6113829 ]])

    s
    # array([ 7.46791327, 2.86884495])

.. code-block:: python

    Vh
    # array([[-0.61169129, -0.45753324, -0.64536587],
    #        [ 0.78971838, -0.40129005, -0.46401635],
    #        [-0.046676 , -0.79349205, 0.60678804]])


Matrix
======
Numpy ma również typ macierzy matrix. Jest on bardzo podobny do tablicy ale podstawowe operacje wykonywane są w sposób macierzowy a nie tablicowy.

.. code-block:: python

    a = np.matrix([[1,2], [3,4]])
    b = np.matrix([[5,6], [7,8]])

    a * b
    # [[19 22]
    #  [43 50]]

    a ** 2
    # [[ 7 10]
    #  [15 22]]

    a * 2
    # [[2 4]
    #  [6 8]]

.. code-block:: python

    d = np.diag([3,4])
    # [[3 0]
    #  [0 4]]

    d * m
    # [[ 3  6]
    #  [12 16]]

Niemniej, tablice można używać podobnie, ale do mnożenia trzeba wykorzystywać funkcje dot:

.. code-block:: python

    a = np.array([[1,2], [3,4]])
    b = np.array([[5,6], [7,8]])

    a * b
    # [[ 5 12]
    #  [21 32]]

    a.dot(b)
    # [[19 22]
    #  [43 50]]

    a ** 2
    #  [[ 1  4]
    #   [ 9 16]]

    a * 2
    # [[2 4]
    #  [6 8]]

Dodatkowo, operacje algebry liniowej można wykonywać zarówno na tablicach jak i macierzach, np:

.. code-block:: python

    print('det(m) = {}'.format(np.linalg.det(m)))
    print('det(a) = {}'.format(np.linalg.det(a)))

Linear Algebra
==============
.. csv-table:: Linear algebra basics
    :header-rows: 1

    "Function", "Description"
    "norm", "Vector or matrix norm"
    "inv", "Inverse of a square matrix"
    "solve", "Solve a linear system of equations"
    "det", "Determinant of a square matrix"
    "slogdet", "Logarithm of the determinant of a square matrix"
    "lstsq", "Solve linear least-squares problem"
    "pinv", "Pseudo-inverse (Moore-Penrose) calculated using a singular value decomposition"
    "matrix_power", "Integer power of a square matrix"
    "matrix_rank", "Calculate matrix rank using an SVD-based method"

.. csv-table:: Eigenvalues and decompositions
    :header-rows: 1

    "Function", "Description"
    "eig", "Eigenvalues and vectors of a square matrix"
    "eigh", "Eigenvalues and eigenvectors of a Hermitian matrix"
    "eigvals", "Eigenvalues of a square matrix"
    "eigvalsh", "Eigenvalues of a Hermitian matrix"
    "qr", "QR decomposition of a matrix"
    "svd", "Singular value decomposition of a matrix"
    "cholesky", "Cholesky decomposition of a matrix"

.. csv-table:: Tensor operations
    :header-rows: 1

    "Function", "Description"
    "tensorsolve", "Solve a linear tensor equation"
    "tensorinv", "Calculate an inverse of a tensor"

.. csv-table:: Exceptions
    :header-rows: 1

    "Function", "Description"
    "LinAlgError", "Indicates a failed linear algebra operation"


Assignments
===========
* http://www.labri.fr/perso/nrougier/teaching/numpy.100/
* https://github.com/rougier/numpy-100

Matrix multiplication
---------------------
* Filename: ``numpy-matrix-mul.py``
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min

#. Używając ``numpy`` oraz operatora ``@`` oraz ``*``
#. Czym się różnią?

.. code-block:: python

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
        pass

Sum of inner matrix
-------------------
* Filename: ``numpy-sum.py``
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min

#. Wygeneruj macierz (16x16) randomowych intów o wartościach od 10 do 100
#. Przekonwertuj macierz na typ float
#. Transponuj ją
#. Policz sumę środkowych (4x4) elementów macierzy
#. Wyświetl wartość (skalar) sumy, a nie nie wektor

Szukanie liczby
---------------
#. Mamy liczbę trzycyfrową.
#. Jeżeli od liczny dziesiątek odejmiemy liczbę jedności otrzymamy 6.
#. Jeżeli do liczby dziesiątek dodamy liczbę jedności otrzymamy 10.
#. Znajdź wszystkie liczby trzycyfrowe spełniające ten warunek
#. Znajdź liczby trzycyfrowe podzielne przez 3

:Hints:
    - Ax=B
    - x=A−1B

.. code-block:: python

    liczba_dziesiatek - liczba_jednosci = 6
    liczba_dziesiatek + liczba_jednosci = 10

    liczba_dziesiatek = liczba_jednosci + 6
    liczba_dziesiatek + liczba_jednosci = 10

    liczba_dziesiatek = liczba_jednosci + 6
    (liczba_jednosci + 6) + liczba_jednosci 10

    liczba_dziesiatek = liczba_jednosci + 6
    2 * liczba_jednosci + 6 = 10

    liczba_dziesiatek = liczba_jednosci + 6
    liczba_jednosci = 8 / 2

    liczba_dziesiatek = 2 + 6
    liczba_jednosci = 2

    liczba_dziesiatek = 8
    liczba_jednosci = 2

.. code-block:: python

    x1 - x2 = 6
    x1 + x2 = 10

    x1 = 6 + x2
    6 + x2 + x2 = 10

    2 * x2 = 4
    x2 = 2
    x1 = 8


    import numpy as np

    A = np.matrix([[1, -1], [1, 1]])
    # matrix([[ 1, -1],
    #        [ 1,  1]])

    B = np.matrix([6, 10]).T  # Transpose matrix
    # matrix([[ 6],
    #        [10]])

    x = A**(-1) * B
    # matrix([[8.],
    #        [2.]])

    A*x == B
    # matrix([[ True],
    #        [ True]])

    res1 = np.arange(1, 10)*100 + 10*x[0,0] + 1*x[1,0]
    # array([182., 282., 382., 482., 582., 682., 782., 882., 982.])

    res1[res1 % 3 == 0]
    # array([282., 582., 882.])

    m = res1 % 3 == 0
    # array([False,  True, False, False,  True, False, False,  True, False])

    res1[m]
    # array([282., 582., 882.])

    res2 = res1[m]
    # array([282., 582., 882.])


Assgnments
==========


Euclidean distance 2D
---------------------
* Filename: ``math_euclidean_2d.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min

#. Dany jest ``np.array`` przechowujący wektor
#. Dane są dwa punkty :math:`A` i :math:`B` o podanych koordynatach ``tuple``
#. Punkty :math:`A` i :math:`B` są dwuwymiarowe ``(x, y)``
#. Oblicz odległość między nimi
#. Wykorzystaj algorytm Euklidesa
#. Funkcja musi przechodzić ``doctest`` :numref:`listing-numpy-euclidean-distance-2D`

.. code-block:: python
    :name: listing-numpy-euclidean-distance-2D
    :caption: Euclidean distance 2D

    def euclidean_distance_2D(A, B):
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
        return

.. figure:: ../machine-learning/img/k-nearest-neighbors-euclidean-distance.png
    :scale: 100%
    :align: center

    Wyliczanie odległości w celu oszacowania przynależności do zbioru. Zwróć uwagę, że bez względu na ilość wymiarów wzór się niewiele różni.


Euclidean distance multi dimensions
-----------------------------------
* Filename: ``math_euclidean_multi_dim.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min

#. Dane są dwa punkty :math:`A` i :math:`B` o podanych koordynatach ``tuple``
#. Punkty :math:`A` i :math:`B` są na :math:`N`-wymiarowej przestrzeni ``(x, y, ...)``
#. Punkty :math:`A` i :math:`B` muszą być równo-wymiarowe
#. Funkcja musi przechodzić ``doctest`` :numref:`listing-numpy-euclidean-distance-n-dimensions`

.. code-block:: python
    :name: listing-numpy-euclidean-distance-n-dimensions
    :caption: Euclidean distance N-dimension

    def euclidean_distance_n_dimensions(A, B):
        """
        >>> A = (0,1,0,1)
        >>> B = (1,1,0,0)
        >>> euclidean_distance_n_dimensions(A, B)
        1.4142135623730951

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
        return
