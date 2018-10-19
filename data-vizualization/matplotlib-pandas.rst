*****************
Matplotlib Pandas
*****************


Visualizing data
================

Hist
----
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv'
    data = pd.read_csv(url)

    data.hist()
    data.show()

.. figure:: img/matplotlib-pd-hist.png
    :scale: 100%
    :align: center

    Vizualization using hist

Density
-------
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv'
    data = pd.read_csv(url)

    data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
    data.show()

.. figure:: img/matplotlib-pd-density.png
    :scale: 100%
    :align: center

    Vizualization using density

Box
---
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv'
    data = pd.read_csv(url)

    data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
    data.show()

.. figure:: img/matplotlib-pd-box.png
    :scale: 100%
    :align: center

    Vizualization using density

Scatter matrix
--------------
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd
    from pandas.plotting import scatter_matrix

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv'
    data = pd.read_csv(url)

    scatter_matrix(data)
    plt.show()

.. figure:: img/matplotlib-pd-scatter-matrix.png
    :scale: 100%
    :align: center

    Vizualization using density
