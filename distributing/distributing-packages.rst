*********************
Distributing Packages
*********************

.. _Instalacja i korzystanie z zewnętrznych bibliotek:

Instalacja i korzystanie z zewnętrznych bibliotek
=================================================

``pip search``
--------------

``pip install``
---------------

``pip install -r requirements.txt``
-----------------------------------

``requirements.txt`` a ``setup.py``
-----------------------------------


Importowanie modułów
====================
.. code-block:: python

    import module

.. code-block:: python

    from module import submodule
    from module.submodule import function as alias

.. code-block:: python

    from . import module
    from .. import module

    from .module import submodule
    from ..module import submodule


Modularyzacja
=============

Plik ``__init__.py``
--------------------
.. code-block:: python

    from backend.api_v2.models.click import Click
    from backend.api_v2.models.event import Event
    from backend.api_v2.models.survey import Survey
    from backend.api_v2.models.trial import Trial


    __all__ = ['Click', 'Event', 'Survey', 'Trial']


Linia ``if __name__ == '__main__'``
-----------------------------------

Importowanie względne ``from . import *``
-----------------------------------------

``__all__``
-----------

Konwencja nazewnicza - ``__main__.py``
--------------------------------------
* Python has been able to execute zip files which contain a ``__main__.py`` file since version 2.6
* In order to be executed by Python, an application archive simply has to be a standard zip file containing a ``__main__.py`` file which will be run as the entry point for the application

.. note:: Check :ref:`zipapp` for more information


Tworzenie paczek
================

``distutils`` i ``setuptools``
------------------------------

``wheel`` vs. ``egg``
---------------------

``setup.py``
------------

.. code-block:: python

    from setuptools import find_packages
    from setuptools import setup
    from os import path


    assert sys.version_info >= (3, 6), "Python 3.6+ required."


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Get the long description from the relevant file
    with open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as file:
        long_description = file.read()


    # Get the project requirements from requirements.txt file
    with open(path.join(BASE_DIR, 'requirements.txt'), encoding='utf-8') as file:
        requirements = file.read().splitlines()


    setup(
        name='HabitatOS',

        # Versions should comply with PEP440.  For a discussion on single-sourcing
        # the version across setup.py and the project code, see
        # https://packaging.python.org/en/latest/single_source_version.html
        version='0.5.0',

        description='Analog Habitat Operating System',
        long_description=long_description,

        # The project's main homepage.
        url='https://github.com/astromatt/HabitatOS',

        # Author details
        author='Matt Harasymczuk',
        author_email='habitatOS@astrotech.io',

        # Choose your license
        license='MIT',

        # See https://pypi.python.org/pypi?:action=list_classifiers
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 4 - Beta',

            # Indicate who your project is intended for
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'Topic :: System :: Operating System',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: MIT License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3.6',
        ],

        # What does your project relate to?
        keywords='space exploration analog analogue habitat operating system',

        # You can just specify the packages manually here if your project is
        # simple. Or you can use find_packages().
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

        # List run-time dependencies here.  These will be installed by pip when
        # your project is installed. For an analysis of "install_requires" vs pip's
        # requirements files see:
        # https://packaging.python.org/en/latest/requirements.html
        install_requires=requirements,

        # List additional groups of dependencies here (e.g. development
        # dependencies). You can install these using the following syntax,
        # for example:
        # $ pip install -e .[dev,test]
        extras_require={
            'dev': ['check-manifest'],
            'test': ['coverage', 'pep8'],
        },

        # If there are data files included in your packages that need to be
        # installed, specify them here.  If using Python 2.6 or less, then these
        # have to be included in MANIFEST.in as well.
        package_data={
            # 'sample': ['package_data.dat'],
        },

        # Although 'package_data' is the preferred approach, in some case you may
        # need to place data files outside of your packages. See:
        # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
        # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
        # data_files=[('my_data', ['data/data_file.txt'])],

        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and allow
        # pip to create the appropriate form of executable for the target platform.
        entry_points={
            'console_scripts': [
                'sample=sample:main',
            ],
        },
    )

``setup.cfg``
-------------
.. code-block:: ini

    [bdist_wheel]
    universal = 1

    [metadata]
    license_file = LICENSE

    [pycodestyle]
    max-line-length = 999
    exclude = */migrations/*
    ignore = E402,W391


``python setup.py sdist upload``
--------------------------------

Signing packages
----------------


Przyszłość paczkowania i dystrybucji
====================================
* https://www.youtube.com/watch?v=jOiAp3wtx18
* https://www.youtube.com/watch?v=Oc9khbXBes8
