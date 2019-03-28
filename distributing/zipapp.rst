***********************
Standalone Applications
***********************

.. _zipapp:


``zipapp``
==========
* Python has been able to execute zip files which contain a ``__main__.py`` file since version 2.6
* In order to be executed by Python, an application archive simply has to be a standard zip file containing a ``__main__.py`` file which will be run as the entry point for the application

Creating Standalone Applications
--------------------------------
#. Create your application in a directory "myapp" as normal
#. Create ``__main__.py`` file (this will be entrypoint)
#. Install (using pip) all of your application's dependencies:

    .. code-block:: console

        $ python -m pip install -r requirements.txt --target myapp

#. Package the application using:

    .. code-block:: console

        $ python -m zipapp -p "/usr/bin/env python3" myapp

About Standalone Applications
-----------------------------
* This will produce a standalone executable
* It can be shipped to users as a single file
* It can be run on any machine with the appropriate interpreter available
* On Unix, the ``myapp.pyz`` file is executable as it stands
* If you want you can rename the file to remove the ``.pyz`` extension
* On Windows, the ``myapp.pyz[w]`` file is executable by virtue of the fact that the Python interpreter registers the ``.pyz`` and ``.pyzw`` file extensions when installed

Run archive
-----------
.. code-block:: console

    $ python myapp.pyz
