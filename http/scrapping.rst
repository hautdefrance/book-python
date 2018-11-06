**************
HTML Scrapping
**************


* BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
* Scrapy https://scrapy.org/

``BeautifulSoup``
=================

Install
-------
.. code-block:: console

    $ pip install beautifulsoup4

Basic Usage
-----------
.. code-block:: python

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

.. code-block:: python

    soup.title              # <title>The Dormouse's story</title>
    soup.title.name         # 'title'
    soup.title.string       # 'The Dormouse's story'
    soup.title.parent.name  # 'head'
    soup.p                  # <p class="title"><b>The Dormouse's story</b></p>
    soup.p['class']         # 'title'
    soup.a                  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    soup.find_all('a')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    soup.find(id="link3")
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

Iterating over items
--------------------
.. code-block:: python

    for link in soup.find_all('a'):
        print(link.get('href'))

    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

Getting Page Text
-----------------
.. code-block:: python

    soup.get_text()
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

* https://github.com/AstroTech/atlassian-python-api

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

Przykłady praktyczne
====================

Prosty serwer HTTP
------------------

.. code-block:: console

    $ python -m http.server 8000 --bind 127.0.0.1

.. code-block:: python

    import re
    from http.server import BaseHTTPRequestHandler
    from http.server import HTTPServer

    SERVER = ('localhost', 8080)


    class RequestHandler(BaseHTTPRequestHandler):
        def do_HEAD(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write('<html>')
            self.wfile.write('<body>Hello World!</body>')
            self.wfile.write('</html>')

        def do_POST(self):
            if re.search('/api/v1/*', self.path):
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)

                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write('<html>')
                self.wfile.write('<body>Hello World!</body>')
                self.wfile.write('</html>')


    try:
        print('Starting server {SERVER}, use <Ctrl-C> to stop')
        httpd = HTTPServer(SERVER, RequestHandler)
        httpd.serve_forever()

    except KeyboardInterrupt:
        print ('^C received, shutting down the web server...')
        httpd.socket.close()


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
