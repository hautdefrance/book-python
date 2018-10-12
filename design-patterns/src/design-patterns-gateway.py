import datetime
import json
import logging
import os
import requests

log = logging.getLogger(__name__)


class HTTPGateway:
    def __init__(self, username=None, password=None, cache_expiry_days=30, cache_directory='.'):
        self.username = username
        self.password = password
        self.cache_expiry_days = cache_expiry_days
        self.cache_directory = cache_directory

    @staticmethod
    def _get_cache_name_from_url(url):
        return url.replace('/', '-').replace(':', '-')

    def _fetch_from_url(self, url):
        connection = requests.get(url, auth=(self.username, self.password))

        if connection.status_code != 200:
            log.error(f'Cannot fetch from URL: {url}')
            raise ConnectionError
        else:
            log.debug(f'Fetched from {url}')
            return connection.text

    def _fetch_from_cache(self, url):
        cache_name = self._get_cache_name_from_url(url)
        path = os.path.join(self.cache_directory, cache_name)

        with open(path) as file:
            log.debug(f'Reading from cache file {path}')
            return file.read()

    def _set_cache(self, url, data):
        cache_name = self._get_cache_name_from_url(url)
        path = os.path.join(self.cache_directory, cache_name)

        with open(path, 'w') as file:
            log.debug(f'Writing to cache file {path}')
            file.write(data)

    def _cache_invalid(self, url):
        def last_modification(filepath, since):
            modification_timestamp = os.path.getmtime(filepath)
            modification_datetime = datetime.datetime.fromtimestamp(modification_timestamp)
            now = datetime.datetime.now()
            return (now - modification_datetime).days < since

        cache_name = self._get_cache_name_from_url(url)
        path = os.path.join(self.cache_directory, cache_name)

        if os.path.isfile(path) and last_modification(path, since=self.cache_expiry_days):
            return False
        else:
            return True

    def get(self, url):
        if self._cache_invalid(url):
            log.info(f'Will read from URL {url}')
            data = self._fetch_from_url(url)
            self._set_cache(url, data)
        else:
            log.info(f'Will read from cache')
            data = self._fetch_from_cache(url)

        return json.loads(data)


http = HTTPGateway(
    username='username',
    password='password',
    cache_directory='tmp',
    cache_expiry_days=10,
)

# pobranie i ustawienie cache
html1 = http.get('http://python.astrotech.io')

# wczytanie z cache, bez komunikacji z internetem
html2 = http.get('http://python.astrotech.io')
