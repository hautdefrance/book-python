***********
HTTP Simple
***********

``requests``
------------
.. code-block:: python

    import requests
    from http import HTTPStatus

    result = requests.get('https://api.github.com/users')

    if result.status == HTTPStatus.OK:
        dane = result.json()
        print(dane)

.. code-block:: python

    import requests
    from http import HTTPStatus

    result = requests.get('https://api.github.com/users', auth=('login', 'haslo'))

    if result.status == HTTPStatus.OK:
        for user in result.json()
            print(user['login'])

.. code-block:: python

    import requests
    from http import HTTPStatus

    data = {
        'first_name': 'Jose',
        'last_name': 'Jimenez',
    }

    result = requests.post('https://api.github.com/users', data=data)

    if result.status == HTTPStatus.CREATED:
        print('Created')
