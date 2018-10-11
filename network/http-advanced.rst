******************
Programowanie HTTP
******************

Biblioteki standardowe
======================

``http``
--------

``urllib``
----------
.. literalinclude:: src/http-urllib.py
    :name: listing-http-urlib
    :language: python
    :caption: ściąganie danych z internetu, które trzeba rozpakować, Dane są w formacie TSV (tab separator values), można je rozpakować modułem CSV i podać jako ``delimiter='\t'``

Biblioteki zewnętrzne
=====================

``suds``
--------

``requests``
------------

.. code-block:: python

    import requests

    requests.put('http://httpbin.org/put', data = {'key':'value'})
    requests.delete('http://httpbin.org/delete')
    requests.head('http://httpbin.org/get')
    requests.options('http://httpbin.org/get')

.. code-block:: python

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('http://httpbin.org/get', params=payload)
    r.url
    # http://httpbin.org/get?key2=value2&key1=value1

    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    r = requests.get('http://httpbin.org/get', params=payload)
    r.url
    # http://httpbin.org/get?key1=value1&key2=value2&key2=value3


.. code-block:: python

    import requests

    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

    r.status_code              # 200
    r.headers['content-type']  # 'application/json; charset=utf8'
    r.encoding                 # 'utf-8'
    r.text                     # '{"type":"User"...'
    r.json()                   # {'private_gists': 419, 'total_private_repos': 77, ...}


.. code-block:: python

    url = 'https://api.github.com/some/endpoint'
    headers = {'user-agent': 'my-app/0.0.1'}

    r = requests.get(url, headers=headers)

.. code-block:: python

    payload = {'key1': 'value1', 'key2': 'value2'}

    r = requests.post("http://httpbin.org/post", data=payload)
    r.text
    # {
    #   ...
    #   "form": {
    #     "key2": "value2",
    #     "key1": "value1"
    #   },
    #   ...
    # }

.. code-block:: python

    r = requests.head('http://github.com', allow_redirects=True)

    r.url      # 'https://github.com/'
    r.history  # [<Response [301]>]

.. code-block:: python

    import json

    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}

    r = requests.post(url, data=json.dumps(payload))

.. code-block:: python

    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}

    r = requests.post(url, json=payload)

* http://docs.python-requests.org/en/master/user/quickstart/#json-response-content
* http://docs.python-requests.org/en/master/dev/contributing/#kenneth-reitz-s-code-style

Requests OAuth
--------------
http://requests-oauthlib.readthedocs.io/en/latest/index.html

.. code-block:: console

    pip install requests_oauthlib

.. literalinclude:: src/requests-oauthlib.py
    :name: listing-requests-oauthlib
    :language: python
    :caption: Requests OAuth

HTML Scrapping
==============
* BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
* Scrapy https://scrapy.org/

HTML Scrapping i ``BeautifulSoup``
----------------------------------

.. code-block:: console

    $ pip install beautifulsoup4

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


.. code-block:: python

    for link in soup.find_all('a'):
        print(link.get('href'))

    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

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


Standard WSGI
=============


Frameworki i technologie webowe
===============================

Google App Engine
-----------------

* https://cloud.google.com/appengine/

A powerful platform to build apps and scale automatically

- **Popular Languages** - Build your application in Node.js, Java, Ruby, C#, Go, Python, or PHP—or bring your own language runtime
- **Open & Flexible** - Custom runtimes allow you to bring any library and framework to App Engine by supplying a Docker container
- **Fully Managed** - A fully managed environment lets you focus on code while App Engine manages infrastructure concerns
- **Monitoring, Logging & Diagnostics** - Google Stackdriver gives you powerful application diagnostics to debug and monitor the health and performance of your app
- **Application Versioning** - Easily host different versions of your app, easily create development, test, staging, and production environments
- **Traffic Splitting** - Route incoming requests to different app versions, A/B test and do incremental feature rollouts
- **Services Ecosystem** - Tap a growing ecosystem of GCP services from your app including an excellent suite of cloud developer tools

``django``
----------

* https://www.djangoproject.com/
* https://github.com/django/django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

- **Ridiculously fast** - Django was designed to help developers take applications from concept to completion as quickly as possible.
- **Reassuringly secure** - Django takes security seriously and helps developers avoid many common security mistakes.
- **Exceedingly scalable** - Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

.. code-block:: console

    $ pip install django

``flask``
---------

* http://flask.pocoo.org/

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!

.. code-block:: console

    $ pip install Flask

.. code-block:: console

    $ python hello.py
     * Running on http://localhost:5000/

.. code-block:: console

    $ export FLASK_APP=hello.py
    $ python -m flask run --host=0.0.0.0
     * Running on http://0.0.0.0:5000/

.. literalinclude:: src/http-flask-simple.py
    :name: listing-http-flask-simple
    :language: python
    :caption: Simple usage of Flask

.. literalinclude:: src/http-flask-template.py
    :name: listing-http-flask-template
    :language: python
    :caption: Flask using templates and data from user

``webapp2``
-----------

* https://webapp2.readthedocs.io/en/latest/
* https://github.com/GoogleCloudPlatform/webapp2

webapp2 is a lightweight Python web framework compatible with Google App Engine’s webapp.

- **webapp2 is a simple** - it follows the simplicity of webapp, but improves it in some ways: it adds better URI routing and exception handling, a full featured response object and a more flexible dispatching mechanism.
- **webapp2 also offers the package webapp2_extras** - with several optional utilities: sessions, localization, internationalization, domain and subdomain routing, secure cookies and others.
- **webapp2 can also be used outside of Google App Engine**, independently of the App Engine SDK.

.. code-block:: yaml

    application: helloworld
    version: 1
    runtime: python27
    api_version: 1
    threadsafe: true

    handlers:
    - url: /.*
      script: main.app

.. code-block:: python

    import webapp2

    class HelloWebapp2(webapp2.RequestHandler):
        def get(self):
            self.response.write('Hello, webapp2!')

    app = webapp2.WSGIApplication([
        ('/', HelloWebapp2),
    ], debug=True)

``tornado``
-----------

* http://www.tornadoweb.org/en/stable/
* https://github.com/tornadoweb/tornado

Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

.. code-block:: python

    import tornado.ioloop
    import tornado.web

    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("Hello, world")

    def make_app():
        return tornado.web.Application([
            (r"/", MainHandler),
        ])

    if __name__ == "__main__":
        app = make_app()
        app.listen(8888)
        tornado.ioloop.IOLoop.current().start()

Formatowanie JSON
-----------------

.. code-block:: console

    $ echo '{"json": "obj"}' | python -m json.tool
    {
        "json": "obj"
    }
    $ echo '{1.2:3.4}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

.. code-block:: console

    $ curl https://api.github.com/repos/django/django/commits |python -m json.tool

Alternatywy:

- https://stedolan.github.io/jq/

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


Wersjonowanie API
=================
.. code-block:: text

    Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding:gzip, deflate, sdch
    Accept-Language:en-US,en;q=0.8,pl;q=0.6


Assignments
===========

REST API
--------
#. Używając biblioteki standardowej w Pythonie zaciągnij informacje o repozytoriach użytkownika Django na https://github.com
#. w przeglądarce internetowej wygeneruj w swoim profilu token https://github.com/settings/tokens
#. Następnie z przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``django``.

    .. code-block:: python

        "name": "django",
        "full_name": "django/django",

        # wyszukaj "commits_url": ???

#. Przeglądnij to repozytorium i jego listę commitów.
#. Podaj datę i opis ostatniego commita
#. Znajdź numery ID ticketów (``Fixed #...``) z issue trackera, które zostały rozwiązane w ostatnim miesiącu
#. Spróbuj skorzystać zamiast biblioteki standardowej z pakietu ``requests``

:Hints:
    .. code-block:: rest

        https://api.github.com/

        GET /orgs/django/repos
        GET /repos/django/django/commits

    .. code-block:: console

        $ curl https://api.github.com/orgs/django/repos
        $ curl https://api.github.com/repos/django/django/commits

    .. code-block:: python

        auth = b'username:token'
        key = base64.b64encode(auth).decode("ascii")
        headers={
            'Authorization': 'Basic {key}',
            'User-Agent': 'Python HTTP',
        }

        # ...

        body = resp.read().decode()
        data = json.loads(body)

:The whys and wherefores:
    * Komunikacja HTTP (request, response)
    * Parsowanie odpowiedzi HTTP
    * Sprawdzanie stanu połączenia
    * Serializacja i parsowanie *JSON*
    * Korzystanie z API i dokumentacji
    * Regexpy
    * Używanie biblioteki standardowej i bibliotek zewnętrznych
