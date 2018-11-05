*****************
HTTP Introduction
*****************


HTTP Protocol
=============
* HTTP vs HTTPS
* Methods
* Statuses
* Headers
* URI vs URL
* HTTP/1.1 vs HTTP/2.0

HTTP Methods
------------
.. csv-table:: HTTP Methods
    :header-rows: 1
    :widths: 15, 25, 60

    "Method", "Function", "Description"
    "GET", "Read", "Requests using GET should only retrieve data and should have no other effect."
    "POST", "Create", "The POST method requests that the server accept the entity enclosed in the request as a new subordinate of the web resource identified by the URI."
    "PUT", "Update/Replace", "The PUT method requests that the enclosed entity be stored under the supplied URI."
    "PATCH", "Partial Update/Modify", "The PATCH method applies partial modifications to a resource."
    "DELETE", "Delete", "The DELETE method deletes the specified resource."
    "HEAD", "Show Headers", "The HEAD method asks for a response identical to that of a GET request, but without the response body."
    "CONNECT", "Connect", "The CONNECT method converts the request connection to a transparent TCP/IP tunnel, usually to facilitate SSL-encrypted communication (HTTPS) through an unencrypted HTTP proxy."
    "OPTIONS", "Show HTTP Methods", "The OPTIONS method returns the HTTP methods that the server supports for the specified URL."
    "TRACE", "Show Trace" "The TRACE method echoes the received request so that a client can see what (if any) changes or additions have been made by intermediate servers."

HTTP Statuses
-------------
.. csv-table:: HTTP Status Families
    :header-rows: 1
    :widths: 15, 85

    "Code", "Description"
    "1XX", "Informational"
    "2XX", "Successful"
    "3XX", "Redirection"
    "4XX", "Client Error"
    "5XX", "Server Error"

``1xx`` Informational response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table:: HTTP Statuses ``1xx`` Informational response
    :header-rows: 1
    :widths: 15, 85

    "Code", "Status", "Description"
    "100", "Continue", ""
    "101", "Switching Protocols", ""
    "102", "Processing (WebDAV)", ""
    "103", "Early Hints", ""

``2xx`` Success
^^^^^^^^^^^^^^^
.. csv-table:: HTTP Statuses ``2xx`` Success
    :header-rows: 1
    :widths: 15, 85

    "Code", "Status", "Description"
    "200", "OK", ""
    "201", "Created", ""
    "202", "Accepted", ""
    "203", "Non-Authoritative Information", ""
    "204", "No Content", ""
    "205", "Reset Content", ""
    "206", "Partial Content", ""
    "207", "Multi-Status (WebDAV)", ""
    "208", "Already Reported (WebDAV)", ""
    "209", "IM Used", ""

``3xx`` Redirection
^^^^^^^^^^^^^^^^^^^
.. csv-table:: HTTP Statuses ``3xx`` Redirection
    :header-rows: 1
    :widths: 15, 85

    "Code", "Status", "Description"
    "300", "Multiple Choices", ""
    "301", "Moved Permanently", ""
    "302", "Found (Previously "Moved temporarily")", ""
    "303", "See Other", ""
    "304", "Not Modified", ""
    "305", "Use Proxy", ""
    "306", "Switch Proxy", ""
    "307", "Temporary Redirect", ""
    "308", "Permanent Redirect", ""

``4xx`` Client errors
^^^^^^^^^^^^^^^^^^^^^
.. csv-table:: HTTP Statuses ``3xx`` Redirection
    :header-rows: 1
    :widths: 15, 85

    "Code", "Status", "Description"
    "400", "Bad Request", ""
    "401", "Unauthorized", ""
    "402", "Payment Required", ""
    "403", "Forbidden", ""
    "404", "Not Found", ""
    "405", "Method Not Allowed", ""
    "406", "Not Acceptable", ""
    "407", "Proxy Authentication Required", ""
    "408", "Request Timeout", ""
    "409", "Conflict", ""
    "410", "Gone", ""
    "411", "Length Required", ""
    "412", "Precondition Failed", ""
    "413", "Payload Too Large", ""
    "414", "URI Too Long", ""
    "415", "Unsupported Media Type", ""
    "416", "Range Not Satisfiable", ""
    "417", "Expectation Failed", ""
    "418", "I'm a teapot", "This code was defined in 1998 as one of the traditional IETF April Fools' jokes, in RFC 2324"
    "421", "Misdirected Request", ""
    "422", "Unprocessable Entity (WebDAV)", ""
    "423", "Locked (WebDAV)", ""
    "424", "Failed Dependency (WebDAV)", ""
    "426", "Upgrade Required", ""
    "428", "Precondition Required", ""
    "429", "Too Many Requests", ""
    "431", "Request Header Fields Too Large", ""
    "451", "Unavailable For Legal Reasons", ""

``5xx`` Server errors
^^^^^^^^^^^^^^^^^^^^^
.. csv-table:: HTTP Statuses ``3xx`` Redirection
    :header-rows: 1
    :widths: 15, 85

    "Code", "Status", "Description"
    "500", "Internal Server Error", ""
    "501", "Not Implemented", ""
    "502", "Bad Gateway", ""
    "503", "Service Unavailable", ""
    "504", "Gateway Timeout", ""
    "505", "HTTP Version Not Supported", ""
    "506", "Variant Also Negotiates", ""
    "507", "Insufficient Storage (WebDAV)", ""
    "508", "Loop Detected (WebDAV)", ""
    "510", "Not Extended", ""
    "511", "Network Authentication Required", ""

HTTP Request Headers
--------------------
.. csv-table:: HTTP Request Headers
    :header-rows: 1
    :widths: 25, 75

    "Header", "Description"
    "Accept", ""
    "Accept-Charset", ""
    "Accept-Encoding", ""
    "Accept-Language", ""
    "Authorization", ""
    "Cache-Control", ""
    "Content-Length", ""
    "Content-Type", ""
    "Cookie", ""
    "Date", ""
    "Host", ""
    "Origin", ""
    "Pragma", ""
    "Referer", ""
    "User-Agent", ""
    "DNT", ""
    "X-Forwarded-For", ""
    "X-Csrf-Token", ""

HTTP Response Headers
--------------------
.. csv-table:: HTTP Response Headers
    :header-rows: 1
    :widths: 25, 75

    "Header", "Description"
    "Access-Control-Allow-Origin", ""
    "Access-Control-Allow-Methods", ""
    "Allow", ""
    "Cache-Control", ""
    "Content-Disposition", ""
    "Content-Encoding", ""
    "Content-Language", ""
    "Content-Length", ""
    "Content-Type", ""
    "Date", ""
    "ETag", ""
    "Expires", ""
    "Last-Modified", ""
    "Location", ""
    "Pragma", ""
    "Server", ""
    "Set-Cookie", ""
    "WWW-Authenticate", ""
    "X-Frame-Options", ""
    "Refresh", ""
    "Status", ""


``http`` Python stdlib
======================

HTTPStatus
----------
.. code-block:: python

    from http import HTTPStatus

    HTTPStatus.OK
    HTTPStatus.CREATED

.. code-block:: python

    from http import HTTPStatus

    HTTPStatus.OK
    HTTPStatus.OK == 200

    HTTPStatus.OK.value
    HTTPStatus.OK.phrase
    HTTPStatus.OK.description

    list(HTTPStatus)

.. csv-table:: ``http.HTTPStatus``
    :header-rows: 1
    :widths: 15, 85

    "Code", "Description"
    "``100``", "``CONTINUE``"
    "``101``", "``SWITCHING_PROTOCOLS``"
    "``102``", "``PROCESSING``"
    "``200``", "``OK``"
    "``201``", "``CREATED``"
    "``202``", "``ACCEPTED``"
    "``203``", "``NON_AUTHORITATIVE_INFORMATION``"
    "``204``", "``NO_CONTENT``"
    "``205``", "``RESET_CONTENT``"
    "``206``", "``PARTIAL_CONTENT``"
    "``207``", "``MULTI_STATUS``"
    "``208``", "``ALREADY_REPORTED``"
    "``226``", "``IM_USED``"
    "``300``", "``MULTIPLE_CHOICES``"
    "``301``", "``MOVED_PERMANENTLY``"
    "``302``", "``FOUND``"
    "``303``", "``SEE_OTHER``"
    "``304``", "``NOT_MODIFIED``"
    "``305``", "``USE_PROXY``"
    "``307``", "``TEMPORARY_REDIRECT``"
    "``308``", "``PERMANENT_REDIRECT``"
    "``400``", "``BAD_REQUEST``"
    "``401``", "``UNAUTHORIZED``"
    "``402``", "``PAYMENT_REQUIRED``"
    "``403``", "``FORBIDDEN``"
    "``404``", "``NOT_FOUND``"
    "``405``", "``METHOD_NOT_ALLOWED``"
    "``406``", "``NOT_ACCEPTABLE``"
    "``407``", "``PROXY_AUTHENTICATION_REQUIRED``"
    "``408``", "``REQUEST_TIMEOUT``"
    "``409``", "``CONFLICT``"
    "``410``", "``GONE``"
    "``411``", "``LENGTH_REQUIRED``"
    "``412``", "``PRECONDITION_FAILED``"
    "``413``", "``REQUEST_ENTITY_TOO_LARGE``"
    "``414``", "``REQUEST_URI_TOO_LONG``"
    "``415``", "``UNSUPPORTED_MEDIA_TYPE``"
    "``416``", "``REQUEST_RANGE_NOT_SATISFIABLE``"
    "``417``", "``EXPECTATION_FAILED``"
    "``421``", "``MISDIRECTED_REQUEST``"
    "``422``", "``UNPROCESSABLE_ENTITY``"
    "``423``", "``LOCKED``"
    "``424``", "``FAILED_DEPENDENCY``"
    "``426``", "``UPGRADE_REQUIRED``"
    "``428``", "``PRECONDITION_REQUIRED``"
    "``429``", "``TOO_MANY_REQUESTS``"
    "``431``", "``REQUEST_HEADER_FIELDS_TOO_LARGE``"
    "``500``", "``INTERNAL_SERVER_ERROR``"
    "``501``", "``NOT_IMPLEMENTED``"
    "``502``", "``BAD_GATEWAY``"
    "``503``", "``SERVICE_UNAVAILABLE``"
    "``504``", "``GATEWAY_TIMEOUT``"
    "``505``", "``HTTP_VERSION_NOT_SUPPORTED``"
    "``506``", "``VARIANT_ALSO_NEGOTIATES``"
    "``507``", "``INSUFFICIENT_STORAGE``"
    "``508``", "``LOOP_DETECTED``"
    "``510``", "``NOT_EXTENDED``"
    "``511``", "``NETWORK_AUTHENTICATION_REQUIRED``"



``requests``
============

Request
-------
.. code-block:: python

    import requests

    requests.get('https://httpbin.org/get')                          # <Response [200]>
    requests.post('https://httpbin.org/post', data={'key':'value'})  # <Response [200]>
    requests.put('https://httpbin.org/put', data={'key':'value'})    # <Response [200]>
    requests.delete('https://httpbin.org/delete')                    # <Response [200]>
    requests.head('https://httpbin.org/get')                         # <Response [200]>
    requests.options('https://httpbin.org/get')                      # <Response [200]>

Response
--------
.. code-block:: python

    from http import HTTPStatus
    import requests


    response = requests.get('https://httpbin.org/get')
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = reponse.raw      # Raw Response Content
        data = reponse.content  # Binary Response Content
        data = response.text    # Response Content
        data = response.json()  # JSON Response Content

        print(data)

GET Requests
------------
* params

.. code-block:: python

    from http import HTTPStatus
    import requests


    response = requests.get('https://httpbin.org/get')
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)

.. code-block:: python

    from http import HTTPStatus
    import requests


    params = {'key1': 'value1', 'key2': 'value2'}

    response = requests.get('https://httpbin.org/get', params=params)
    # <Response [200]>

    print(response.url)
    # https://httpbin.org/get?key2=value2&key1=value1

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)

.. code-block:: python

    from http import HTTPStatus
    import requests


    data = {'key1': 'value1', 'key2': ['value2', 'value3']}

    response = requests.get('https://httpbin.org/get', params=data)
    # <Response [200]>

    print(response.url)
    # https://httpbin.org/get?key1=value1&key2=value2&key2=value3

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)

POST Requests
-------------
.. code-block:: python

    from http import HTTPStatus
    import requests


    data = {'first_name': 'Jose', 'last_name': 'Jimenez'}

    response = requests.post('https://httpbin.org/post', data=data)
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        print('Created')

.. code-block:: python

    from http import HTTPStatus
    import requests


    data = {'key1': ['value1', 'value2']}

    response = requests.post('https://httpbin.org/post', data=data)
    # <Response [200]>

    print(response.text)
    # {
    #   ...
    #   "form": {
    #     "key1": [
    #       "value1",
    #       "value2"
    #     ]
    #   },
    #   ...
    # }

    if response.status_code == HTTPStatus.OK:
        print('Created')

POST Request with JSON
----------------------
.. code-block:: python

    import json
    from http import HTTPStatus
    import requests


    data = {
        'first_name': 'Jose',
        'last_name': 'Jimenez',
    }

    response = requests.post('https://httpbin.org/post', data=json.dumps(data))
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        print('Created')

.. code-block:: python

    import json
    from http import HTTPStatus
    import requests


    data = {
        'first_name': 'Jose',
        'last_name': 'Jimenez',
    }

    response = requests.post('https://httpbin.org/post', json=data)
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        print('Created')

DELETE Requests
---------------
.. code-block:: python

    import requests
    from http import HTTPStatus


    response = requests.post('https://api.github.com/delete')
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        print('Deleted')

Custom Headers
--------------
.. code-block:: python

    import requests
    from http import HTTPStatus


    url = 'https://api.github.com/some/endpoint'
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)

.. code-block:: python

    response.headers
    # {
    #     'content-encoding': 'gzip',
    #     'transfer-encoding': 'chunked',
    #     'connection': 'close',
    #     'server': 'nginx/1.0.4',
    #     'x-runtime': '148ms',
    #     'etag': '"e1ca502697e5c9317743dc078f67693f"',
    #     'content-type': 'application/json'
    # }

.. code-block:: python

    response.headers['Content-Type']
    # 'application/json'

    response.headers.get('content-type')
    # 'application/json'

Timeout
-------
.. code-block:: python

    import requests


    requests.get('https://github.com/', timeout=0.001)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)

Basic Auth
----------
.. code-block:: python

    import requests
    from http import HTTPStatus


    response = requests.get('https://api.github.com/users', auth=('login', 'password'))
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)

.. code-block:: python

    import requests
    from requests.auth import HTTPBasicAuth
    from http import HTTPStatus


    response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
    # <Response [200]>

    if response.status_code == HTTPStatus.OK:
        data = response.json()
        print(data)


Assignments
===========

REST API
--------
#. Używając biblioteki ``requests``
#. Zaciągnij informacje o repozytoriach użytkownika Django na https://github.com
#. W przeglądarce internetowej wygeneruj w swoim profilu token https://github.com/settings/tokens
#. Następnie z przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``django``.

    .. code-block:: python

        "name": "django",
        "full_name": "django/django",

        # wyszukaj "commits_url": ???

#. Przeglądnij to repozytorium i jego listę commitów.
#. Podaj datę i opis ostatniego commita
#. Znajdź numery ID ticketów (``Fixed #...``) z issue trackera, które zostały rozwiązane w ostatnim miesiącu

:About:
    * Filename: ``http_simple.py``
    * Lines of code to write: 35 lines
    * Estimated time of completion: 30 min

:The whys and wherefores:
    * Komunikacja HTTP (request, response)
    * Parsowanie odpowiedzi HTTP
    * Sprawdzanie stanu połączenia
    * Serializacja i parsowanie *JSON*
    * Korzystanie z API i dokumentacji
    * Regexpy
    * Używanie biblioteki standardowej i bibliotek zewnętrznych

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
