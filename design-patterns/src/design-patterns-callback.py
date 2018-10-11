from http import HTTPStatus
import requests


def noop(*arg, **kwargs):
    pass


def http_request(url, on_success=noop, on_error=noop):
    result = requests.get(url)
    if result.status_code == HTTPStatus.OK:
        on_success(result)
    else:
        on_error(result)


def success(result):
    print('Success')


def error(result):
    print('Error')


http_request(
    url='http://python.astrotech.io',
    on_success=success,
    on_error=error,
)
