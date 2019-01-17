********************
Zastosowanie naukowe
********************


Scipy
=====

SciPy (pronounced "Sigh Pie") is open-source software for mathematics, science, and engineering. It includes modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing, ODE solvers, and more. It is also the name of a very popular conference on scientific programming with Python.

The SciPy library depends on NumPy, which provides convenient and fast N-dimensional array manipulation. The SciPy library is built to work with NumPy arrays, and provides many user-friendly and efficient numerical routines such as routines for numerical integration and optimization. Together, they run on all popular operating systems, are quick to install, and are free of charge. NumPy and SciPy are easy to use, but powerful enough to be depended upon by some of the world's leading scientists and engineers. If you need to manipulate numbers on a computer and display or publish the results.

SciPy builds on the NumPy array object and is part of the NumPy stack which includes tools like Matplotlib, pandas and SymPy, and an expanding set of scientific computing libraries. This NumPy stack has similar users to other applications such as MATLAB, GNU Octave, and Scilab. The NumPy stack is also sometimes referred to as the SciPy stack.

* https://www.scipy.org/
* https://github.com/scipy/scipy

.. code-block:: python

    import scipy
    
    help(scipy)
    # Help on package scipy:
    # NAME
    #  scipy
    # FILE
    #  c:\python25\lib\site-packages\scipy\__init__.py
    # DESCRIPTION
    #  SciPy --- A scientific computing package for Python
    #  ===================================================
    #  Documentation is available in the docstrings and
    #  online at http://docs.scipy.org.
    #  Contents
    #  --------
    #  SciPy imports all the functions from the NumPy namespace, and in
    #  addition provides:
    #  Available subpackages
    #  ---------------------
    #  odr --- Orthogonal Distance Regression [*]
    #  misc --- Various utilities that don't have another home.
    #  sparse.linalg.eigen.arpack --- Eigenvalue solver using iterative methods. [*]
    #  fftpack --- Discrete Fourier Transform algorithms [*]
    #  io --- Data input and output [*]
    #  sparse.linalg.eigen.lobpcg --- Locally Optimal Block Preconditioned Conjugate Gradient Method (LOBPCG) [*]
    #  special --- Airy Functions [*]
    #  lib.blas --- Wrappers to BLAS library [*]
    #  sparse.linalg.eigen --- Sparse Eigenvalue Solvers [*]
    #  stats --- Statistical Functions [*]
    #  lib --- Python wrappers to external libraries [*]
    #  lib.lapack --- Wrappers to LAPACK library [*]
    #  maxentropy --- Routines for fitting maximum entropy models [*]
    #  integrate --- Integration routines [*]
    #  ndimage --- n-dimensional image package [*]
    #  linalg --- Linear algebra routines [*]
    #  spatial --- Spatial data structures and algorithms [*]
    #  interpolate --- Interpolation Tools [*]
    #  sparse.linalg --- Sparse Linear Algebra [*]
    #  sparse.linalg.dsolve.umfpack --- :Interface to the UMFPACK library: [*]
    #  sparse.linalg.dsolve --- Linear Solvers [*]
    #  optimize --- Optimization Tools [*]
    #  cluster --- Vector Quantization / Kmeans [*]
    #  signal --- Signal Processing Tools [*]
    #  sparse --- Sparse Matrices [*]

    # [*] - using a package requires explicit import (see pkgload)
    
.. code-block:: python

    import scipy
    import scipy.interpolate

.. csv-table:: Scipy
    :header-rows: 1
    :file: data/scipy.csv
