**************
HTML Scrapping
**************


* BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
* Scrapy https://scrapy.org/

``BeautifulSoup``
=================

Example usage
-------------
* https://github.com/AstroMatt/thesis-masters-aerospace/blob/master/src/worldspaceflight-astronaut-bios.py

Install
-------
.. code-block:: console

    $ pip install beautifulsoup4

Parser
------
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| Parser               | Typical usage                              | Advantages                     | Disadvantages            |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| Python's html.parser | ``BeautifulSoup(markup, "html.parser")``   | * Batteries included           | * Not very tolerant      |
|                      |                                            | * Decent speed                 |   (before Python 2.7.3   |
|                      |                                            | * tolerant (as of Python 2.7.3 |   or 3.2.2)              |
|                      |                                            |   and 3.2.)                    |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| lxml's HTML parser   | ``BeautifulSoup(markup, "lxml")``          | * Very fast                    | * External C dependency  |
|                      |                                            | * Tolerant                     |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| lxml's XML parser    | ``BeautifulSoup(markup, "lxml-xml")``      | * Very fast                    | * External C dependency  |
|                      | ``BeautifulSoup(markup, "xml")``           | * The only currently supported |                          |
|                      |                                            |   XML parser                   |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+
| html5lib             | ``BeautifulSoup(markup, "html5lib")``      | * Extremely tolerant           | * Very slow              |
|                      |                                            | * Parses pages the same way a  | * External Python        |
|                      |                                            |   web browser does             |   dependency             |
|                      |                                            | * Creates valid HTML5          |                          |
+----------------------+--------------------------------------------+--------------------------------+--------------------------+

Open
----
.. code-block:: python

    from bs4 import BeautifulSoup

    with open("index.html") as file:
        html = BeautifulSoup(file, 'html.parser')

    html.find(id='menubox').decompose()

Basic Usage
-----------
.. code-block:: python

    from bs4 import BeautifulSoup


    html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>

        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>

        <p class="story">...</p>
    """

    html = BeautifulSoup(html_doc, 'html.parser')

    print(html.prettify())
    # <html>
    #  <head>
    #   <title>
    #    The Dormouse's story
    #   </title>
    #  </head>
    #  <body>
    #   <p class="title">
    #    <b>
    #     The Dormouse's story
    #    </b>
    #   </p>
    #   <p class="story">
    #    Once upon a time there were three little sisters; and their names were
    #    <a class="sister" href="http://example.com/elsie" id="link1">
    #     Elsie
    #    </a>
    #    ,
    #    <a class="sister" href="http://example.com/lacie" id="link2">
    #     Lacie
    #    </a>
    #    and
    #    <a class="sister" href="http://example.com/tillie" id="link2">
    #     Tillie
    #    </a>
    #    ; and they lived at the bottom of a well.
    #   </p>
    #   <p class="story">
    #    ...
    #   </p>
    #  </body>
    # </html>

.. code-block:: python

    html.title              # <title>The Dormouse's story</title>
    html.title.name         # 'title'
    html.title.string       # 'The Dormouse's story'
    html.title.parent.name  # 'head'
    html.p                  # <p class="title"><b>The Dormouse's story</b></p>
    html.p['class']         # 'title'
    html.a                  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    html.find_all('a')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    html.find(id="link3")
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

Iterating over items
--------------------
.. code-block:: python

    for link in html.find_all('a'):
        print(link.get('href'))

    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

Getting Page Text
-----------------
.. code-block:: python

    html.get_text()
    # The Dormouse's story
    #
    # The Dormouse's story
    #
    # Once upon a time there were three little sisters; and their names were
    # Elsie,
    # Lacie and
    # Tillie;
    # and they lived at the bottom of a well.
    #
    # ...



Utils
=====

``atlassian-python-api``
------------------------

* https://github.com/atlassian-api/atlassian-python-api

.. code-block:: python

    from atlassian import Confluence
    from atlassian import Jira


    jira = Jira(
        url='http://localhost:8080',
        username='admin',
        password='admin')

    confluence = Confluence(
        url='http://localhost:8090',
        username='admin',
        password='admin')


    JQL = 'project = DEMO AND status NOT IN (Closed, Resolved) ORDER BY issuekey'
    data = jira.jql(JQL)

    status = confluence.create_page(
        space='DEMO',
        title='This is the title',
        body=f'This is the body. You can use <strong>HTML tags</strong>!<div>{data}</div>')

    print(status)


Template
========

``Jinja2``
----------

.. code-block:: html

    <title>{% block title %}{% endblock %}</title>
    <ul>
    {% for user in users %}
      <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
    </ul>



Assignments
===========

EVA
---
#. Na podstawie podanych URL:

    * https://www.worldspaceflight.com/bios/eva/eva.php
    * https://www.worldspaceflight.com/bios/eva/eva2.php
    * https://www.worldspaceflight.com/bios/eva/eva3.php
    * https://www.worldspaceflight.com/bios/eva/eva4.php

#. Scrappuj stronę wykorzystując ``beautifulsoup4``
#. Przygotuj plik CSV z danymi dotyczącymi spacerów kosmicznych
#. Spróbuj to samo zrobić za pomocą ``pandas.read_html()``
