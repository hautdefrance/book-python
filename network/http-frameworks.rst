***************
HTTP Frameworks
***************


Google App Engine
=================

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
==========

* https://www.djangoproject.com/
* https://github.com/django/django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

- **Ridiculously fast** - Django was designed to help developers take applications from concept to completion as quickly as possible.
- **Reassuringly secure** - Django takes security seriously and helps developers avoid many common security mistakes.
- **Exceedingly scalable** - Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

.. code-block:: console

    $ pip install django

``flask``
=========

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
===========

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
===========

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
